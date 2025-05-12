# Contributing to PhaseSync

Thank you for your interest in contributing to PhaseSync! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read it before contributing.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. If not, create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce the bug
   - Expected behavior
   - Actual behavior
   - Environment details (OS, Python version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue with:
   - A clear, descriptive title
   - Detailed description of the feature
   - Use cases and benefits
   - Any implementation ideas you have

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature/fix
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation if needed
7. Submit a pull request

### Development Setup

1. Clone the repository:
 
   git clone https://github.com/Donald-Watts/PhaseSync.git
   cd PhaseSync
 

2. Create a virtual environment:
   
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
 

3. Install development dependencies:
 
   pip install -e ".[dev]"
 
4. Run tests:
 
   python -m unittest discover PhaseSync/tests


### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions and classes
- Keep functions small and focused
- Write meaningful commit messages

### Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Maintain or improve test coverage
- Test edge cases and error conditions

### Documentation

- Update README.md if needed
- Add docstrings to new functions/classes
- Update examples if behavior changes
- Keep documentation in sync with code

## License

By contributing to PhaseSync, you agree that your contributions will be licensed under the project's Apache 2.0 License.

## Questions?

Feel free to open an issue or contact the maintainers at limited.adls@gmail.com. 