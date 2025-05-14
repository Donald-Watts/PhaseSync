# Naming Conventions for PhaseSync
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

This document defines the naming conventions for all code and files in the PhaseSync project. Consistent naming improves readability, maintainability, and collaboration.



## Python Naming Conventions

- **Files & Modules:** Use `snake_case` (e.g., `symbol_compressor.py`)
- **Packages:** Use `snake_case` (e.g., `phasesync`)
- **Classes:** Use `PascalCase` (e.g., `PhaseSyncEngine`)
- **Functions & Methods:** Use `snake_case` (e.g., `calculate_weight`)
- **Variables:** Use `snake_case` (e.g., `symbol_map`)
- **Constants:** Use `UPPER_SNAKE_CASE` (e.g., `CHAR_MAP`)
- **Test Files:** Prefix with `test_` (e.g., `test_compressor.py`)



## TypeScript/Node.js Naming Conventions

- **Files:** Use `kebab-case` or `camelCase` (e.g., `extension.ts`, `weightAnalysis.ts`)
- **Directories:** Use `kebab-case` (e.g., `src/`, `test/`)
- **Classes & Interfaces:** Use `PascalCase` (e.g., `SWPBridge`)
- **Functions & Methods:** Use `camelCase` (e.g., `calculateWeight`)
- **Variables:** Use `camelCase` (e.g., `weightResult`)
- **Constants:** Use `UPPER_SNAKE_CASE` (e.g., `DEFAULT_PHASE`)
- **Test Files:** Suffix with `.test.ts` or `.spec.ts` (e.g., `weightAnalysis.test.ts`)



## General Guidelines

- Use descriptive, meaningful names for all identifiers.
- Avoid abbreviations unless they are well-known.
- Be consistent with naming across the codebase.
- Update names if the purpose or usage changes significantly.



## References

- See `coding-standards.md`, `Project_rules.md`, and `PHASE_SYNC_SPEC.md` for additional standards.



## Next Steps

- Update this document as naming conventions evolve.
- Ensure all contributors follow these conventions. 