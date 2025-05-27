"""
Tests for the Boss class.
"""
import pytest
import random
from unittest.mock import patch, Mock
from rpg_game.boss import Boss
from rpg_game.character import Character
from rpg_game.weapon import Weapon
from rpg_game.game_logger import GameLogger

@pytest.fixture
def sample_boss():
    return Boss("Test Boss", 200, 15)

@pytest.fixture
def sample_character():
    return Character("Test Character", 100, 10)

class TestBoss:
    """Test cases for the Boss class."""

    def test_boss_initialization(self, sample_boss):
        """Test boss initialization."""
        assert sample_boss.name == "Test Boss"
        assert sample_boss.health == 200
        assert sample_boss.damage == 15
        assert sample_boss.weapon is not None
        assert sample_boss.weapon.name == "Boss Weapon"
        assert sample_boss.weapon.damage_bonus == 5  # Boss weapon bonus

    @patch('random.random')
    def test_attack_normal(self, mock_random, sample_boss, sample_character):
        """Test normal boss attack."""
        # Setup
        mock_random.return_value = 0.8  # Not a special attack (0.8 > 0.25)
        logger = Mock()
        
        # Mock take_damage to track actual damage
        original_health = sample_character.health
        sample_character.take_damage = Mock(side_effect=lambda x: setattr(sample_character, '_health', max(0, sample_character.health - x)))
        
        # Execute
        damage = sample_boss.attack(sample_character, logger)
        
        # Verify
        expected_damage = 20  # 15 base + 5 weapon
        sample_character.take_damage.assert_called_once_with(expected_damage)
        logger.log_combat.assert_called_once_with(
            attacker=sample_boss.name,
            defender=sample_character.name,
            damage=expected_damage,
            is_critical=False
        )
        assert damage == expected_damage

    @patch('random.random')
    def test_boss_attack_special(self, mock_random):
        """Test boss special attack."""
        # Mock random.random to trigger special attack (0.1 < 0.25)
        mock_random.return_value = 0.1
        
        boss = Boss("Dragon", 200, 20)
        enemy = Character("Hero", 100, 10)
        logger = Mock()
        
        # Mock take_damage to track actual damage
        original_health = enemy.health
        enemy.take_damage = Mock(side_effect=lambda x: setattr(enemy, '_health', max(0, enemy.health - x)))
    
        # Execute
        damage = boss.attack(enemy, logger)
    
        # Verify
        expected_damage = 37  # (20 base + 5 weapon) * 1.5 = 37.5 -> 37 (int)
        enemy.take_damage.assert_called_once_with(expected_damage)
        logger.log_combat.assert_called_once_with(
            attacker="Dragon",
            defender="Hero",
            damage=expected_damage,
            is_critical=True
        )
        assert damage == expected_damage
    
    @patch('random.random')
    def test_boss_attack_with_logger(self, mock_random):
        """Test boss attack with logger."""
        # Mock random.random to trigger special attack
        mock_random.return_value = 0.1
    
        boss = Boss("Dragon", 200, 20)
        enemy = Character("Hero", 100, 10)
        logger = GameLogger()
    
        # Redirect stdout to capture logger output
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
    
        try:
            damage = boss.attack(enemy, logger)
            output = sys.stdout.getvalue()
            
            # Verify the output contains expected strings
            assert "Dragon" in output
            assert "Hero" in output
            assert "37" in output  # Expected damage for special attack
            assert "CRITICAL" in output
        finally:
            sys.stdout = old_stdout
    
    def test_boss_take_damage(self):
        """Test boss taking damage."""
        boss = Boss("Dragon", 200, 20)
        boss.take_damage(50)
        assert boss.health == 150
        
        # Test health doesn't go below 0
        boss.take_damage(200)
        assert boss.health == 0

    def test_boss_is_alive(self):
        """Test is_alive property."""
        boss = Boss("Dragon", 200, 20)
        assert boss.is_alive is True
        boss.health = 0
        assert boss.is_alive is False
    
    def test_display(self, capsys, sample_boss):
        """Test display method output."""
        # Setup
        sample_boss.weapon = Weapon("Boss Weapon", 5)
        
        # Execute
        sample_boss.display()
        captured = capsys.readouterr()
        output = captured.out
        
        # Verify
        assert "Name: Test Boss" in output
        assert "Health: 200" in output
        assert "Damage: 15" in output
        assert "Boss Weapon" in output
        assert "+5" in output
        assert "Boss Weapon" in captured.out
