# PhaseSync

A semantic compression tool for development phases and AI collaboration.

## Overview

PhaseSync implements the Symbolic Weight Protocol (SWP), a system that compresses development phases into single-digit weights while preserving semantic meaning. This enables:

- Consistent phase identification across projects
- Token-efficient AI communication
- Semantic phase mapping
- Visual compression analysis

## Installation

```bash
pip install -e .
```

## Core Components

### Symbol Compressor
The heart of PhaseSync, implementing the SWP algorithm:
- Letter-to-number mapping (A=1 to Z=26)
- Number reduction to single digits
- Compound word handling
- Phase tag extraction

### Symbol Map
JSON-based storage of phase-to-weight mappings:
```json
{
    "8": ["Foundation and Definition", "Core Feature Development", "Finalization and Product"],
    "2": ["Blueprint and Canonical Structure"],
    "6": ["Scaffolding and Schema Definition"],
    "7": ["Intelligence Learning Test Suites"],
    "9": ["User Interface and Orchestration"]
}
```

### Visualizer
Tools for analyzing and displaying compression:
- Step-by-step compression visualization
- Phase weight reporting
- Bidirectional phase/weight lookup

## Usage

### Basic Compression
```python
from PhaseSync.symbol_compressor import compress_word

# Compress a single word
weight = compress_word("Python")  # Returns 8
```

### Phase Tagging
```python
# In your code files:
# @phase:core
# @task:build_web_ui
# @weight:high
```

### Visualization
```python
from PhaseSync.visualizer import visualize_compression

# Show compression steps
print(visualize_compression("Python"))
# Output:
# Python:
# P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
# 9 + 8 = 17
# 1 + 7 = 8
```

## Development Phases

PhaseSync recognizes these key development phases:

1. **Foundation and Definition** (8)
   - Project setup
   - Core architecture
   - Initial documentation

2. **Blueprint and Canonical Structure** (2)
   - System design
   - Architecture planning
   - Component mapping

3. **Scaffolding and Schema Definition** (6)
   - Base structure
   - Data models
   - API definitions

4. **Core Feature Development** (8)
   - Main functionality
   - Business logic
   - Core algorithms

5. **Intelligence Learning Test Suites** (7)
   - Unit tests
   - Integration tests
   - AI training data

6. **User Interface and Orchestration** (9)
   - UI components
   - User flows
   - System integration

7. **Finalization and Product** (8)
   - Bug fixes
   - Performance optimization
   - Final documentation

## Testing

Run the test suite:
```bash
python -m unittest discover PhaseSync/tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - See LICENSE file for details 