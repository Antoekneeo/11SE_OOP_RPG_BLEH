"""
Boss class for the RPG game.

This module defines the Boss class which represents boss enemies in the game.
Bosses are special types of characters with enhanced abilities.
"""

import random
from typing import Any, Optional
from character import Character
from weapon import Weapon


class Boss(Character):
    """A boss enemy in the game."""
    
    def __init__(self, name: str, health: int, damage: int):
        """
        Initialize a new boss.
        
        Args:
            name: The name of the boss
            health: The boss's health points
            damage: The boss's base damage
        """
        super().__init__(name, health, damage)
        self.weapon = Weapon("Boss Weapon", 5)  # Bosses always have a weapon
    
    def attack(self, enemy: Any, logger: Optional[Any] = None) -> int:
        """
        Attack an enemy character with a chance for a special attack.
        
        Args:
            enemy: The enemy character to attack
            logger: Optional logger for combat messages
            
        Returns:
            int: The amount of damage dealt
        """
        # Bosses have a 25% chance to do a special attack
        special_attack = random.random() < 0.25
        
        damage = self.damage
        if self.weapon:
            damage += self.weapon.damage_bonus
        
        if special_attack:
            # Special attack does 1.5x damage
            damage = int(damage * 1.5)
        
        # Store initial health for damage calculation
        initial_health = enemy.health
        enemy.take_damage(damage)
        actual_damage = initial_health - enemy.health
        
        if logger:
            logger.log_combat(attacker=self.name,
                           defender=enemy.name,
                           damage=actual_damage,
                           is_critical=special_attack)
            
        return actual_damage
    
    def take_damage(self, amount: int) -> None:
        """
        Reduce the boss's health by the given amount.
        
        Args:
            amount: Amount of damage to take
        """
        self.health -= amount
        
        # Check if boss is defeated
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
