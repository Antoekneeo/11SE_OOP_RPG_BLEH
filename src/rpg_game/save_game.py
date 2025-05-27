"""
Save and load game functionality.

This module provides functions to save the game state to a file and load it back.
"""

import json
import os
from typing import Dict, Any, Optional, Callable
from pathlib import Path

# Default save file location
_SAVE_DIR = os.path.join(str(Path.home()), "rpg_saves")
_SAVE_FILE = os.path.join(_SAVE_DIR, "save.json")

# Allow tests to override these values
_get_save_dir = lambda: _SAVE_DIR
_get_save_file = lambda: _SAVE_FILE

def set_save_paths(save_dir: str, save_file: str) -> None:
    """
    Set custom save directory and file paths.
    
    Args:
        save_dir: Path to the save directory
        save_file: Path to the save file
    """
    global _SAVE_DIR, _SAVE_FILE
    _SAVE_DIR = save_dir
    _SAVE_FILE = save_file

def ensure_save_dir() -> None:
    """Ensure the save directory exists."""
    os.makedirs(_get_save_dir(), exist_ok=True)

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
        save_file = _get_save_file()
        with open(save_file, 'w', encoding='utf-8') as f:
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
        save_file = _get_save_file()
        if not os.path.exists(save_file):
            return None
            
        with open(save_file, 'r', encoding='utf-8') as f:
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
        save_file = _get_save_file()
        if os.path.exists(save_file):
            os.remove(save_file)
        return True
    except OSError as e:
        print(f"Error deleting save file: {e}")
        return False
