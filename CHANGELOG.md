# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- **Testing Infrastructure**:
  - Fixed test cases in `test_character.py` to match fixture names and behavior
  - Updated `test_boss.py` to correctly test special attacks and damage calculations
  - Fixed error handling in `test_save_game.py` for file operations
  - Improved test coverage and reliability

### Changed
- **Code Quality**:
  - Updated `delete_save` function in `save_game.py` to properly handle file operations
  - Improved error handling in game components
  - Enhanced test assertions for better failure messages
  - Simplified project structure for educational use
  - Updated documentation to emphasize educational focus
  - Enhanced code organization with logical separation of concerns

### Added
- **Testing Infrastructure**:
  - Comprehensive test suite using pytest
  - Test coverage reporting
  - Test fixtures for common test objects
  - Unit tests for all major components:
    - `Character` class
    - `Boss` class
    - `Weapon` class
    - `Game` class
    - `save_game` module
  - Test configuration with `pytest.ini`
  - Development dependencies in `requirements-dev.txt`
  - Documentation for running tests in README.md
  - Test directory structure following Python best practices
  - Mocking for isolated testing
  - Test coverage reporting
  - CI/CD integration ready

- **Save/Load System**:
  - New `save_game.py` module for handling game state persistence
  - JSON-based save file format for game state storage
  - Automatic save directory creation
  - Save game validation and error handling
  - Main menu with New Game/Load Game options
  - In-game save functionality during boss battles
  - Option to save and quit the game
  - Automatic save cleanup when starting a new game after completion
  - Detailed error messages for save/load operations
- Comprehensive type hints throughout the codebase
- Detailed docstrings for all classes and methods
- New modular file structure:
  - `console_utils.py`: Utility functions for console operations
  - `game_logger.py`: Game logging functionality
  - `weapon.py`: Weapon class implementation
  - `character.py`: Base Character class
  - `boss.py`: Boss class that inherits from Character
  - `game.py`: Main Game class
  - `main.py`: Entry point
  - `save_game.py`: Game state persistence functionality
- Improved error handling and input validation
- Better code organization following OOP principles

### Changed
- Refactored single-file implementation into modular structure
- Replaced direct attribute access with properties where appropriate
- Improved method and variable naming for clarity
- Enhanced combat system with better logging
- Updated documentation to reflect new structure

### Fixed
- Potential issues with circular imports
- Inconsistent health management
- Improved error messages for better user experience

## [2025-05-23]

### Added
- Forked from [Mr-Zamora/11SE_OOP_RPG](https://github.com/Mr-Zamora/11SE_OOP_RPG.git)
- Initial project setup and structure
- Basic README with project information
- CHANGELOG.md for tracking changes
- Refactored single-file implementation into multi-file structure
- Added `constants.py` for centralized configuration management
- Implemented type hints throughout the codebase
- Added comprehensive docstrings to all classes and methods

### Changed
- Improved code style to follow PEP 8 guidelines
- Refactored string formatting for better readability
- Updated ROADMAP.md to reflect new project structure

### Fixed
- Fixed long lines to comply with PEP 8 (88 character limit)
- Eliminated magic numbers and hardcoded strings

## [2025-05-26] - Major Restructuring

### Milestone: Multi-File RPG Implementation
This update represents a significant milestone in the project's evolution, transforming the codebase from a single-file implementation to a well-organised, modular multi-file structure. This new structure better demonstrates professional software design while maintaining educational clarity.

### Added
- Created dedicated files for each major component:
  - `game.py` - Core game logic and flow management
  - `character.py` - Character and Boss class implementations
  - `weapon.py` - Weapon system implementation
  - `constants.py` - Game configuration and constants
  - `utils/logger.py` - Logging functionality
  - `utils/console.py` - Console interface utilities
- Implemented a clean entry point via `main.py`

### Changed
- Transformed from single-file to multi-file architecture while preserving OOP principles
- Simplified project structure by removing unnecessary package architecture
- Removed `__init__.py` files to make the project a standard Python project
- Modified import statements to work without package structure
- Renamed `PROJECT_RULES.md` to `RULES.md` for better consistency
- Updated documentation to emphasise educational focus
- Enhanced code organisation with logical separation of concerns

### Removed
- Deleted `setup.py` and package installation files
- Removed `run_game.py` in favour of using `rpg_game/main.py` directly
- Eliminated unnecessary complexity that could distract from learning objectives

### Commit Reference
- Commit [0ff49c9](https://github.com/Mr-Zamora/11SE_OOP_RPG/commit/0ff49c9) - "refactor: simplify project structure for educational use"
- Commit [884340c](https://github.com/Mr-Zamora/11SE_OOP_RPG/commit/884340c) - "chore: remove __pycache__ directories and add .gitignore"

### Maintenance
- Removed Python bytecode files (`__pycache__` directories) from version control
- Added comprehensive `.gitignore` file to prevent tracking of generated files
- Improved repository cleanliness and adherence to Python project standards

## [Unreleased]

### Planned
- Add unit tests with 80%+ coverage
- Implement error handling with specific exceptions
- Add inventory system for characters
- Expand character types (Sidekick, Villain classes)
- Enhance combat system
