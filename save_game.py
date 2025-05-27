"""
Save and load game functionality.

This module provides functions to save the game state to a file and load it back.
"""

import json
import os
from typing import Dict, Any, Optional
from pathlib import Path

# Default save file location
SAVE_DIR = os.path.join(str(Path.home()), "rpg_saves")
SAVE_FILE = os.path.join(SAVE_DIR, "save.json")

def ensure_save_dir() -> None:
    """Ensure the save directory exists."""
    os.makedirs(SAVE_DIR, exist_ok=True)

def save_game(game_state: Dict[str, Any]) -> bool:
    """
    Save the game state to a file.
    
    Args:
        game_state: Dictionary containing the game state to save
        
    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        ensure_save_dir()
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(game_state, f, indent=2)
        return True
    except (IOError, OSError, json.JSONDecodeError) as e:
        print(f"Error saving game: {e}")
        return False

def load_game() -> Optional[Dict[str, Any]]:
    """
    Load the game state from a file.
    
    Returns:
        Optional[Dict[str, Any]]: The loaded game state, or None if loading failed
    """
    try:
        if not os.path.exists(SAVE_FILE):
            return None
            
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, OSError, json.JSONDecodeError) as e:
        print(f"Error loading game: {e}")
        return None

def delete_save() -> bool:
    """
    Delete the save file if it exists.
    
    Returns:
        bool: True if file was deleted or didn't exist, False if an error occurred
    """
    try:
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
        return True
    except OSError as e:
        print(f"Error deleting save file: {e}")
        return False
