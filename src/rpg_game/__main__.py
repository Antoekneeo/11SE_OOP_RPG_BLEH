#!/usr/bin/env python3
"""
Main entry point for the RPG game package.

This module allows the package to be run directly with `python -m rpg_game`.
"""

from rpg_game.game import Game

def main() -> None:
    """Initialize and run the game."""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
