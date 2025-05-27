"""
Tests for the Weapon class.
"""
from weapon import Weapon

class TestWeapon:
    """Test cases for the Weapon class."""

    def test_weapon_creation(self):
        """Test weapon creation with valid parameters."""
        weapon = Weapon("Sword", 5)
        assert weapon.name == "Sword"
        assert weapon.damage_bonus == 5
        
    def test_weapon_creation_with_zero_damage(self):
        """Test weapon creation with zero damage bonus."""
        weapon = Weapon("Stick", 0)
        assert weapon.name == "Stick"
        assert weapon.damage_bonus == 0
        
    def test_weapon_creation_with_negative_damage(self):
        """Test weapon creation with negative damage bonus."""
        weapon = Weapon("Broken Sword", -2)
        assert weapon.name == "Broken Sword"
        assert weapon.damage_bonus == -2  # Negative damage is allowed
        
    def test_weapon_string_representation(self):
        """Test the string representation of a weapon."""
        weapon = Weapon("Axe", 7)
        assert str(weapon) == "Axe (+7 damage)"
        
    def test_weapon_equality(self):
        """Test weapon equality based on name and damage bonus."""
        weapon1 = Weapon("Sword", 5)
        weapon2 = Weapon("Sword", 5)
        weapon3 = Weapon("Axe", 5)
        weapon4 = Weapon("Sword", 7)
        
        assert weapon1 == weapon2
        assert weapon1 != weapon3
        assert weapon1 != weapon4
