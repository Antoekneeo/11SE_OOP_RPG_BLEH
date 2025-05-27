"""
Boss class for the RPG game.

This module defines the Boss class which represents boss enemies in the game.
Bosses are special types of characters with enhanced abilities.
"""

from typing import Any, Optional
from character import Character


class Boss(Character):
    """
    Represents a boss enemy in the game.
    
    This class demonstrates inheritance by extending the Character class.
    """
    
    def __init__(self, name: str, health: int, damage: int) -> None:
        """
        Initialize a new boss.
        
        Args:
            name: The boss's name
            health: The boss's health points
            damage: The boss's base damage
        """
        # Call the parent class's __init__ with weapon details
        super().__init__(name, health, damage, "Boss Weapon", 5)
    
    def attack(self, enemy: Any, logger: Optional[Any] = None) -> int:
        """
        Attack an enemy with a special boss attack.
        
        Overrides the parent class's attack method to add a special attack.
        
        Args:
            enemy: The enemy character to attack
            logger: Optional GameLogger instance for logging combat
            
        Returns:
            The total damage dealt (base damage + weapon bonus + special damage)
        """
        # Call the parent class's attack method
        total_damage = super().attack(enemy, logger)
        
        # Boss special attack: additional damage
        additional_damage = 1
        enemy.health -= additional_damage
        
        print(f"{self.name} uses a special attack! (+{additional_damage} Damage)")
        
        # Log the special attack if a logger is provided
        if logger:
            logger.log_combat(self, enemy, additional_damage)
            
        return total_damage + additional_damage
