"""
Tests for the Game class.
"""
import pytest
import os
import json
from pathlib import Path
from rpg_game.game import Game
from rpg_game.character import Character
from rpg_game.boss import Boss

class TestGame:
    """Test cases for the Game class."""
    
    def test_game_initialization(self):
        """Test game initialization."""
        game = Game()
        assert game.player is None
        assert game.bosses == []
        assert hasattr(game, 'logger')
        assert hasattr(game, 'save_dir')
        assert game.save_dir.name == 'rpg_saves'
    
    def test_setup_game(self, mocker):
        """Test game setup with player creation."""
        game = Game()
        mocker.patch('builtins.input', return_value='1')  # Simulate weapon choice
        
        game.setup_game("TestHero")
        
        assert game.player is not None
        assert game.player.name == "TestHero"
        assert game.player.health > 0
        assert game.player.weapon is not None
        assert len(game.bosses) > 0
    
    def test_combat_player_wins(self, mocker):
        """Test combat where player wins."""
        game = Game()
        player = Character("Player", 100, 20)
        boss = Boss("Weak Boss", 1, 1)  # Very weak boss
        
        # Mock random to control damage
        mocker.patch('random.randint', return_value=0)
        
        # Mock input to choose attack
        mocker.patch('builtins.input', return_value='1')
        
        # Player should win in one hit
        result = game.combat(player, boss)
        assert result is True
    
    def test_combat_player_loses(self, mocker):
        """Test combat where player loses."""
        game = Game()
        player = Character("Player", 1, 1)  # Very weak player
        boss = Boss("Strong Boss", 100, 100)  # Very strong boss
        
        # Mock random to control damage
        mocker.patch('random.randint', return_value=0)
        
        # Mock input to choose attack
        mocker.patch('builtins.input', return_value='1')
        
        # Player should lose in one hit
        result = game.combat(player, boss)
        assert result is False
    
    def test_save_and_load_game(self, tmp_path, mocker):
        """Test saving and loading a game."""
        # Create a temporary directory for saves
        mocker.patch('pathlib.Path.home', return_value=tmp_path)
        
        game = Game()
        
        # Setup a simple game state
        game.player = Character("TestHero", 100, 10, "Sword", 5)
        game.bosses = [Boss("TestBoss", 50, 5)]
        
        # Save the game
        save_success = game.save_current_game()
        assert save_success is True
        
        # Create a new game instance to test loading
        loaded_game = Game()
        load_success = loaded_game.load_game()
        
        # Verify load was successful
        assert load_success is True
        assert loaded_game.player is not None
        assert loaded_game.player.name == "TestHero"
        assert loaded_game.player.health == 100
        assert len(loaded_game.bosses) == 1
        assert loaded_game.bosses[0].name == "TestBoss"
