# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
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
