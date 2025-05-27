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

def get_user_choice(prompt: str, valid_choices: list) -> str:
    """
    Get a valid choice from the user.
    
    Args:
        prompt: The prompt to display to the user
        valid_choices: List of valid choices
        
    Returns:
        The user's valid choice
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")
