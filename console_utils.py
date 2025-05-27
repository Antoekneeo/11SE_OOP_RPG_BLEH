"""
Console utility functions for the RPG game.

This module provides utility functions for console operations like clearing the screen
and handling user input.
"""

import os

def clear_screen() -> None:
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter() -> None:
    """Prompt the user to press Enter to continue."""
    input("\nPress Enter to continue...\n")

def print_border() -> None:
    """Print a border line for visual separation."""
    print("-" * 80)
