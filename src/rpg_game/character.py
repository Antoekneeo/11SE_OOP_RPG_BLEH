"""
Character class for the RPG game.

This module defines the base Character class that represents playable
and non-playable characters in the game.
"""

from typing import Optional, Any
from rpg_game.weapon import Weapon


class Character:
    """
    Represents a character in the game.
    
    This is the base class for all character types in the game.
    """
    
    def __init__(self, name: str, health: int, damage: int, 
                 weapon_name: Optional[str] = None, weapon_damage: int = 0) -> None:
        """
        Initialize a new character.
        
        Args:
            name: The character's name
            health: The character's health points
            damage: The character's base damage
            weapon_name: Optional name of the character's weapon
            weapon_damage: Damage bonus from the weapon
        """
        self.name = name
        self._health = health  # Private attribute (by convention)
        self.damage = damage
        # Create the weapon inside the Character constructor (strong composition)
        self.weapon = Weapon(weapon_name, weapon_damage) if weapon_name else None
    
    @property
    def health(self) -> int:
        """Get the character's current health."""
        return self._health
    
    @health.setter
    def health(self, value: int) -> None:
        """
        Set the character's health, ensuring it doesn't go below 0.
        
        Args:
            value: The new health value
        """
        self._health = max(0, value)
    
    def get_health(self) -> int:
        """
        Get the character's current health.
        
        Returns:
            The character's current health points
        """
        return self.health
    
    @property
    def is_alive(self) -> bool:
        """Check if the character is alive."""
        return self.health > 0
    
    def take_damage(self, amount: int) -> None:
        """
        Reduce the character's health by the given amount.
        
        Args:
            amount: Amount of damage to take (negative values will be treated as 0)
        """
        if amount > 0:
            self.health -= amount
    
    def attack(self, enemy: Any, logger: Optional[Any] = None) -> int:
        """
        Attack an enemy character.

        Args:
            enemy: The enemy character to attack
            logger: Optional logger for combat messages

        Returns:
            int: The amount of damage dealt
        """
        damage = self.damage
        if self.weapon:
            damage += self.weapon.damage_bonus

        # Store initial health for damage calculation
        initial_health = enemy.health
        enemy.take_damage(damage)
        actual_damage = initial_health - enemy.health

        if logger:
            logger.log_combat(attacker=self.name, 
                           defender=enemy.name, 
                           damage=actual_damage,
                           is_critical=False)

        return actual_damage
    
    def display(self) -> None:
        """Display the character's information."""
        weapon_name = self.weapon.name if self.weapon else 'No Weapon'
        weapon_damage = self.weapon.damage_bonus if self.weapon else 0
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Weapon: {weapon_name} (+{weapon_damage} Damage)")
