# Error Handling Standards for PhaseSync
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

This document defines the error handling standards for all code in the PhaseSync project. Consistent error handling improves reliability, debuggability, and user experience.



## Python Error Handling

- Use custom exception classes for project-specific errors (e.g., `class SWPError(Exception): ...`).
- Always provide meaningful error messages.
- Use try/except blocks to handle expected errors gracefully.
- Log errors using the standard `logging` module.
- Avoid catching broad exceptions (e.g., `except Exception:`) unless necessary.
- Propagate errors up the stack when appropriate.
- Never suppress errors silently.
- Document all custom exceptions and error codes.



## TypeScript/Node.js Error Handling

- Use custom error classes for project-specific errors (e.g., `class SWPError extends Error { ... }`).
- Always provide meaningful error messages.
- Use try/catch blocks to handle expected errors gracefully.
- Log errors using a standard logger or `console.error` for development.
- Avoid catching broad errors unless necessary.
- Propagate errors up the stack when appropriate.
- Never suppress errors silently.
- Document all custom errors and error codes.



## General Guidelines

- Provide clear, actionable feedback to users when errors occur.
- Use error codes or types for programmatic error handling.
- Ensure all errors are logged for debugging and auditing.
- Keep error handling logic consistent across the codebase.
- Update documentation when new error types or codes are introduced.



## References

- See `coding-standards.md`, `Project_rules.md`, and `PHASE_SYNC_SPEC.md` for additional standards.



## Next Steps

- Update this document as error handling standards evolve.
- Ensure all contributors follow these guidelines. 