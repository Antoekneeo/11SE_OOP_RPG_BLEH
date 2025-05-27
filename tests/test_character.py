"""
Tests for the Character class.
"""

import pytest
import sys
import io
from unittest.mock import patch, Mock
from character import Character
from boss import Boss
from weapon import Weapon
from game_logger import GameLogger


class TestCharacter:
    """Test cases for the Character class."""

    def test_character_creation(self):
        """Test character creation with default values."""
        char = Character("Test", 100, 10)
        assert char.name == "Test"
        assert char.health == 100
        assert char.damage == 10
        assert char.weapon is None

    def test_character_with_weapon(self, sample_weapon):
        """Test character creation with a weapon."""
        char = Character("Warrior", 120, 15, "Sword", 5)
        assert char.weapon is not None
        assert char.weapon.name == "Sword"
        assert char.weapon.damage_bonus == 5

    def test_health_property(self, sample_character):
        """Test health property getter and setter."""
        sample_character.health = 50
        assert sample_character.health == 50
        
        # Test health can't go below 0
        sample_character.health = -10
        assert sample_character.health == 0

    def test_take_damage(self, sample_character):
        """Test taking damage."""
        # Test normal damage
        sample_character.take_damage(20)
        assert sample_character.health == 80  # 100 - 20
        
        # Test health doesn't go below 0
        sample_character.take_damage(200)
        assert sample_character.health == 0
        
        # Reset health for next test
        sample_character.health = 100
        
        # Test with negative damage (should be treated as 0)
        sample_character.take_damage(-10)
        assert sample_character.health == 100  # No change

    def test_is_alive(self, sample_character):
        """Test is_alive property."""
        # Test when alive
        sample_character.health = 100
        assert sample_character.is_alive is True
        
        # Test when dead
        sample_character.health = 0
        assert sample_character.is_alive is False
        
        # Test with negative health
        sample_character.health = -10
        assert sample_character.is_alive is False
        
    def test_display(self, capsys, sample_character):
        """Test display method output."""
        # Setup - use the sample_character from fixture which already has a weapon
        
        # Execute
        sample_character.display()
        captured = capsys.readouterr()
        output = captured.out
        
        # Verify
        assert "Name: Test Hero" in output
        assert "Health: 100" in output
        assert "Damage: 10" in output
        assert "Test Weapon (+5 Damage)" in output
        
    def test_attack_with_logger(self, sample_character, sample_boss):
        """Test attack method with logger."""
        # Setup - use the sample_character from fixture with a different weapon
        sample_character.weapon = Weapon("Sword", 5)
        logger = GameLogger()
        
        # Save original health for damage calculation
        original_health = sample_boss.health
        
        # Redirect stdout to capture logger output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            # Execute
            damage = sample_character.attack(sample_boss, logger)
            output = sys.stdout.getvalue()
            
            # Verify
            expected_damage = 15  # 10 base + 5 weapon
            assert damage == expected_damage
            assert "COMBAT LOG" in output
            assert "Test Hero" in output  # Should match fixture name
            assert "Test Boss" in output
            assert str(expected_damage) in output
        finally:
            sys.stdout = old_stdout

    def test_attack_with_weapon(self, sample_character, sample_boss, mocker):
        """Test attack method with weapon."""
        # Setup - use the sample_character from fixture
        sample_character.weapon = Weapon("Sword", 5)
        logger = Mock()
        
        # Mock take_damage to track actual damage
        original_health = sample_boss.health
        sample_boss.take_damage = Mock(side_effect=lambda x: setattr(sample_boss, '_health', max(0, sample_boss.health - x)))
        
        # Execute
        damage = sample_character.attack(sample_boss, logger)
        
        # Verify
        expected_damage = 15  # 10 base + 5 weapon
        sample_boss.take_damage.assert_called_once_with(expected_damage)
        logger.log_combat.assert_called_once_with(
            attacker="Test Hero",
            defender=sample_boss.name,
            damage=expected_damage,
            is_critical=False
        )
        assert damage == expected_damage
        
    def test_attack_without_weapon(self, sample_character, sample_boss, mocker):
        """Test attack method without weapon."""
        # Setup - use the sample_character from fixture
        sample_character.weapon = None
        logger = Mock()
        
        # Mock take_damage to track actual damage
        original_health = sample_boss.health
        sample_boss.take_damage = Mock(side_effect=lambda x: setattr(sample_boss, '_health', max(0, sample_boss.health - x)))
        
        # Execute
        damage = sample_character.attack(sample_boss, logger)
        
        # Verify
        expected_damage = 10  # Just base damage
        sample_boss.take_damage.assert_called_once_with(expected_damage)
        logger.log_combat.assert_called_once_with(
            attacker="Test Hero",
            defender=sample_boss.name,
            damage=expected_damage,
            is_critical=False
        )
        assert damage == expected_damage
