"""
Weapon class for the RPG game.

This module defines the Weapon class which represents weapons that characters can use.
"""

from typing import Optional


class Weapon:
    """
    Represents a weapon in the game.
    
    This class is used in composition with the Character class.
    """
    
    def __init__(self, name: str, damage_bonus: int) -> None:
        """
        Initialize a new weapon.
        
        Args:
            name: The weapon's name
            damage_bonus: The damage bonus this weapon provides
        """
        self.name = name
        self.damage_bonus = damage_bonus
    
    def __str__(self) -> str:
        """
        Return a string representation of the weapon.
        
        Returns:
            str: A string in the format "Name (+X damage)"
        """
        return f"{self.name} (+{self.damage_bonus} damage)"
    
    def __eq__(self, other: object) -> bool:
        """
        Check if this weapon is equal to another weapon.
        
        Args:
            other: The other object to compare with
            
        Returns:
            bool: True if weapons have the same name and damage bonus, False otherwise
        """
        if not isinstance(other, Weapon):
            return False
        return (self.name == other.name and 
                self.damage_bonus == other.damage_bonus)
