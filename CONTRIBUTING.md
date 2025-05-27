# Contributing to RPG Lesson

Thank you for your interest in contributing to the RPG Lesson project! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up your development environment (see [README.md](README.md) for instructions)
4. Create a new branch for your changes
5. Make your changes following the project's coding standards
6. Write tests for your changes
7. Run the test suite to ensure all tests pass
8. Submit a pull request

## Development Workflow

### Branch Naming

Use the following prefixes for branch names:
- `feature/` - New features or enhancements
- `bugfix/` - Bug fixes
- `docs/` - Documentation improvements
- `refactor/` - Code refactoring
- `test/` - Test additions or improvements

Example: `feature/add-new-weapon` or `bugfix/fix-save-game`

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep the first line under 50 characters
- Include a blank line between the subject and the body
- Reference issues and pull requests liberally

Example:
```
Add save game functionality

- Implement save_game function in save_game.py
- Add tests for save/load functionality
- Update documentation

Closes #42
```

### Pull Requests

1. Update the [CHANGELOG.md](CHANGELOG.md) with your changes
2. Ensure your code passes all tests
3. Document any new features or changes in the relevant documentation
4. Request a code review from a project maintainer

## Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **mypy** for static type checking
- **pylint** for code quality

Run the following commands before committing:

```bash
black .
isort .
mypy src/
pylint src/
```

## Testing

All contributions should include appropriate tests. The project uses `pytest` for testing.

To run the test suite:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=rpg_game
```

## Reporting Issues

When reporting issues, please include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any relevant error messages
- Your Python version and operating system

## Feature Requests

For feature requests, please:
1. Check if the feature has already been requested
2. Describe the feature in detail
3. Explain why this feature would be valuable
4. Include any relevant examples or use cases

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
