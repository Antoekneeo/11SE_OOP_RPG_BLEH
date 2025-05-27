"""
Pytest configuration and fixtures for testing the RPG game.
"""
import pytest
from character import Character
from boss import Boss
from weapon import Weapon

@pytest.fixture
def sample_weapon():
    """Create a sample weapon for testing."""
    return Weapon("Test Sword", 5)

@pytest.fixture
def sample_character():
    """Create a sample character for testing."""
    return Character("Test Hero", 100, 10, "Test Weapon", 5)

@pytest.fixture
def sample_boss():
    """Create a sample boss for testing."""
    return Boss("Test Boss", 150, 15)

@pytest.fixture
def game_instance():
    """Create a game instance for testing."""
    from game import Game
    game = Game()
    return game
