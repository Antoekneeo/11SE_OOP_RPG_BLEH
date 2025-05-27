"""
Game constants and configuration.

This module contains all the constant values used throughout the game.
Centralizing these values makes the game easier to balance and maintain.
"""
from typing import Dict, Tuple, List, Final

# Game settings
GAME_TITLE: Final[str] = "RPG Adventure"
VERSION: Final[str] = "1.0.0"
SEPARATOR_LENGTH: Final[int] = 30
SAVE_FILE_EXTENSION: Final[str] = ".sav"

# Player constants
PLAYER_INITIAL_HEALTH: Final[int] = 110
PLAYER_INITIAL_DAMAGE: Final[int] = 10
PLAYER_STARTING_WEAPON: Final[str] = "Rock"

# Boss constants
class BossConfig:
    GOBLIN_KING = {
        "name": "Goblin King",
        "health": 50,
        "damage": 8,
        "special_attack_chance": 0.3,
        "special_attack_multiplier": 1.5,
    }
    
    DARK_SORCERER = {
        "name": "Dark Sorcerer",
        "health": 60,
        "damage": 9,
        "special_attack_chance": 0.4,
        "special_attack_multiplier": 1.7,
    }

# Weapon constants
class WeaponConfig:
    ROCK = {
        "name": "Rock",
        "damage": 2,
        "description": "A simple rock. Basic but reliable.",
    }
    
    PAPER = {
        "name": "Paper",
        "damage": 3,
        "description": "A sheet of paper. Surprisingly effective.",
    }
    
    SCISSORS = {
        "name": "Scissors",
        "damage": 4,
        "description": "Sharp scissors. Handle with care!",
    }

# Game messages
class Messages:
    WELCOME = "Welcome to {game_title} v{version}!"
    GAME_OVER = "Game Over! Thanks for playing!"
    BOSS_DEFEATED = "You defeated the {boss_name}!"
    PLAYER_DEFEATED = "You were defeated by {boss_name}!"
    INVALID_CHOICE = "Invalid choice. Please try again."
    SAVE_SUCCESS = "Game saved successfully!"
    LOAD_SUCCESS = "Game loaded successfully!"
    NO_SAVE_FOUND = "No saved game found."

# UI constants
class UIConstants:
    MENU_OPTIONS = [
        "New Game",
        "Load Game",
        "How to Play",
        "Quit"
    ]
    
    GAME_OPTIONS = [
        "Fight",
        "Use Item",
        "Run Away",
        "Save Game",
        "Quit to Menu"
    ]

# Combat constants
class CombatConstants:
    CRITICAL_HIT_CHANCE: Final[float] = 0.1
    CRITICAL_HIT_MULTIPLIER: Final[float] = 2.0
    DODGE_CHANCE: Final[float] = 0.15
    MIN_DAMAGE_MULTIPLIER: Final[float] = 0.8
    MAX_DAMAGE_MULTIPLIER: Final[float] = 1.2

# File paths
class Paths:
    SAVES_DIR: Final[str] = "saves"
    LOGS_DIR: Final[str] = "logs"
    ASSETS_DIR: Final[str] = "assets"

# Type aliases
Position = Tuple[int, int]
HealthPoints = int
DamagePoints = int
WeaponName = str
BossName = str
