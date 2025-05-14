# Coding Standards for PhaseSync
#
# @phase: Blueprint and Canonical Structure
# @weight: Raw sum: 353, Reduced sum (digital root): 2
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## Overview

This document defines the coding standards for all code in the PhaseSync project. All contributors must follow these guidelines to ensure code quality, maintainability, and consistency.



## Python Standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) for style and formatting.
- Use type hints for all functions and methods.
- Include comprehensive docstrings for all public classes, methods, and functions.
- Use snake_case for variable and function names.
- Use PascalCase for class names.
- Limit lines to 88 characters (Black default).
- Use [Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/) for code formatting.
- Run static analysis with `ruff`, `mypy`, and `bandit`.
- Handle errors with custom exceptions where appropriate.
- Avoid hardcoded credentials and sensitive data.



## TypeScript/Node.js Standards

- Follow [ESLint](https://eslint.org/) and [Prettier](https://prettier.io/) rules for formatting and linting.
- Use camelCase for variables and functions.
- Use PascalCase for class and interface names.
- Include JSDoc comments for all public classes, methods, and functions.
- Use explicit types wherever possible.
- Limit lines to 100 characters.
- Prefer `const` and `let` over `var`.
- Handle errors with try/catch and custom error classes.
- Avoid hardcoded credentials and sensitive data.



## General Guidelines

- Write clear, maintainable, and well-documented code.
- Keep functions and classes small and focused.
- Use meaningful names for all identifiers.
- Document all parameters and return values.
- Keep documentation and code in sync.
- Review and test all code before committing.



## References

- See `Project_rules.md` and `PHASE_SYNC_SPEC.md` for additional standards and requirements.



## Next Steps

- Update this document as standards evolve.
- Ensure all contributors are familiar with and follow these guidelines. 