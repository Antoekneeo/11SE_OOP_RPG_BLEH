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
        
    def log_combat(self, attacker: str, defender: str, damage: int, is_critical: bool = False) -> None:
        """
        Log a combat message.
        
        Args:
            attacker: Name of the attacker
            defender: Name of the defender
            damage: Amount of damage dealt
            is_critical: Whether the attack was a critical hit
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        crit_msg = " (CRITICAL!)" if is_critical else ""
        log_message = f"[{timestamp}] COMBAT LOG: {attacker} attacks {defender} for {damage} damage{crit_msg}"
        if self.log_to_console:
            print(log_message)
        # Future enhancement: could log to file, database, etc.
