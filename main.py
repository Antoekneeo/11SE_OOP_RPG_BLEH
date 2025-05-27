#!/usr/bin/env python3
"""
Main entry point for the RPG game.

This module initializes and runs the game.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from rpg_game.game import Game

def main() -> None:
    """Initialize and run the game."""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
