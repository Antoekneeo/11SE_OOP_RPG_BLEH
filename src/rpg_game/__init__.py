"""
RPG Game Package

This package contains the implementation of a simple RPG game
demonstrating object-oriented programming principles.
"""
from typing import List, Any, TypeVar, Type

# Import key classes to make them available at package level
from .character import Character
from .boss import Boss
from .weapon import Weapon
from .game import Game
from .game_logger import GameLogger
from .console_utils import clear_screen, press_enter, print_border, get_user_choice
from . import save_game as save_game_module
from .save_game import save_game, load_game, delete_save
from . import constants

# Version of the package
__version__ = "1.0.0"

# Type variable for generic type hints
T = TypeVar('T')

# Define public API
__all__: List[str] = [
    # Core classes
    'Character',
    'Boss',
    'Weapon',
    'Game',
    'GameLogger',
    
    # Utility functions
    'clear_screen',
    'press_enter',
    'print_border',
    'get_user_choice',
    'save_game',
    'load_game',
    'delete_save',
    
    # Constants
    'constants',
    
    # Version
    '__version__',
]

def __dir__() -> List[str]:
    """Return a list of all public items in the package."""
    return __all__

def __getattr__(name: str) -> Any:
    """Allow lazy loading of modules to improve import time."""
    if name == 'constants':
        from . import constants as _constants
        return _constants
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
