"""
Game logging functionality for the RPG game.

This module provides the GameLogger class for handling game events logging,
such as combat actions.
"""

import datetime
from typing import Any


class GameLogger:
    """
    Handles logging of game events.
    
    This class demonstrates association relationship with the Game class.
    """
    
    def __init__(self, log_to_console: bool = True) -> None:
        """
        Initialize the GameLogger.
        
        Args:
            log_to_console: Whether to output logs to the console
        """
        self.log_to_console = log_to_console
        
    def log_combat(self, attacker: Any, defender: Any, damage: int) -> None:
        """
        Log a combat event.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            damage: The amount of damage dealt
            
        Returns:
            None
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] COMBAT LOG: {attacker.name} attacked {defender.name} for {damage} damage"
        if self.log_to_console:
            print(log_message)
        # Future enhancement: could log to file, database, etc.
