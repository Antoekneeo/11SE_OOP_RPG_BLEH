"""
Enhanced console utilities for the RPG game.

This module provides simple but effective console utilities with colors
and better user feedback.
"""

import os
import sys
from typing import List, Any

# Simple ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen() -> None:
    """Clear the console screen with a simple animation."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Colors.BLUE}{'=' * 60}{Colors.END}\n")

def press_enter(prompt: str = "Press Enter to continue...") -> None:
    """Prompt the user to press Enter with an optional custom message."""
    input(f"\n{Colors.CYAN}{prompt}{Colors.END} ")

def print_border(char: str = '-', length: int = 80) -> None:
    """Print a border line for visual separation.
    
    Args:
        char: Character to use for the border
        length: Length of the border
    """
    print(f"{Colors.BLUE}{char * length}{Colors.END}")

def print_header(text: str) -> None:
    """Print a styled header."""
    border = f"{'=' * (len(text) + 4)}"
    print(f"\n{Colors.BLUE}{border}")
    print(f"  {text.upper()}  ")
    print(f"{border}{Colors.END}\n")

def print_success(message: str) -> None:
    """Print a success message."""
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")

def print_error(message: str) -> None:
    """Print an error message."""
    print(f"{Colors.RED}✗ {message}{Colors.END}")

def get_user_choice(prompt: str, valid_choices: List[Any]) -> str:
    """
    Get a valid choice from the user with better feedback.
    
    Args:
        prompt: The prompt to display
        valid_choices: List of valid choices (case-insensitive)
        
    Returns:
        The user's valid choice (lowercase)
    """
    valid_choices_lower = [str(c).lower() for c in valid_choices]
    
    while True:
        choice = input(f"{Colors.CYAN}{prompt} {Colors.END}").strip().lower()
        if choice in valid_choices_lower:
            return choice
        print_error(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")

def show_menu(options: List[str], title: str = "Menu") -> int:
    """
    Display a simple numbered menu and get user's choice.
    
    Args:
        options: List of menu options
        title: Optional menu title
        
    Returns:
        Index of the selected option (0-based)
    """
    print_header(title)
    for i, option in enumerate(options, 1):
        print(f"{Colors.YELLOW}{i}.{Colors.END} {option}")
    print()
    
    while True:
        try:
            choice = int(input(f"{Colors.CYAN}Enter your choice (1-{len(options)}): {Colors.END}"))
            if 1 <= choice <= len(options):
                return choice - 1
            print_error(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print_error("Please enter a valid number")
