#!/usr/bin/env python3
"""
Main entry point for the RPG game.

This module initializes and runs the game.
"""

from game import Game

def main() -> None:
    """Initialize and run the game."""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
