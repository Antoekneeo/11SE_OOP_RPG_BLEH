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
            name: The name of the weapon
            damage_bonus: The damage bonus this weapon provides
        """
        self.name = name
        self.damage_bonus = damage_bonus
