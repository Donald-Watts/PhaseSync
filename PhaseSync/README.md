# PhaseSync

A semantic compression tool for development phases and AI collaboration.

## Overview

PhaseSync implements the Symbolic Weight Protocol (SWP), a system that compresses development phases into single-digit weights while preserving semantic meaning. This enables:

- Consistent phase identification across projects
- Token-efficient AI communication
- Semantic phase mapping
- Visual compression analysis

## Quick Start

1. **Installation**
   # Clone the repository
   git clone https://github.com/Donald-Watts/PhaseSync.git
   cd PhaseSync

   # Create and activate virtual environment
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Install the package
   pip install -e .

2. **Basic Usage**
   from PhaseSync.symbol_compressor import compress_word, analyze_phase

   # Compress a single word
   weight = compress_word("Python")  # Returns 8

   # Analyze a development phase
   phase_info = analyze_phase("Core Feature Development")
   print(phase_info)
   # Output: {'weight': 8, 'description': 'Main functionality implementation'}


3. **CLI Usage**
   # Compress a word
   phasesync compress "Python"

   # Analyze a phase
   phasesync analyze "Core Feature Development"

   # Visualize compression
   phasesync visualize "Python"


## Core Components

### Symbol Compressor
The heart of PhaseSync, implementing the SWP algorithm:
- Letter-to-number mapping (A=1 to Z=26)
- Number reduction to single digits
- Compound word handling
- Phase tag extraction

### Symbol Map
JSON-based storage of phase-to-weight mappings:
{
    "8": ["Foundation and Definition", "Core Feature Development", "Finalization and Product"],
    "2": ["Blueprint and Canonical Structure"],
    "6": ["Scaffolding and Schema Definition"],
    "7": ["Intelligence Learning Test Suites"],
    "9": ["User Interface and Orchestration"]
}


### Visualizer
Tools for analyzing and displaying compression:
- Step-by-step compression visualization
- Phase weight reporting
- Bidirectional phase/weight lookup

## Detailed Usage

### 1. Word Compression
from PhaseSync.symbol_compressor import compress_word

# Basic compression
weight = compress_word("Python")  # Returns 8

# Compound words
weight = compress_word("Web Development")  # Returns 7

# With custom mapping
weight = compress_word("Python", custom_map={"P": 10})  # Returns 9


### 2. Phase Analysis
from PhaseSync.symbol_compressor import analyze_phase

# Analyze a phase
phase_info = analyze_phase("Core Feature Development")
print(phase_info)
# Output: {'weight': 8, 'description': 'Main functionality implementation'}

# Get all phases for a weight
phases = analyze_phase(weight=8)
print(phases)
# Output: ['Foundation and Definition', 'Core Feature Development', 'Finalization and Product']


### 3. Phase Tagging
# In your code files:
# @phase:core
# @task:build_web_ui
# @weight:high

# Extract tags from code
from PhaseSync.symbol_compressor import extract_phase_tags

tags = extract_phase_tags("""
# @phase:core
# @task:build_web_ui
# @weight:high
def build_ui():
    pass
""")
print(tags)
# Output: {'phase': 'core', 'task': 'build_web_ui', 'weight': 'high'}


### 4. Visualization
from PhaseSync.visualizer import visualize_compression, generate_phase_report

# Show compression steps
print(visualize_compression("Python"))
# Output:
# Python:
# P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
# 9 + 8 = 17
# 1 + 7 = 8

# Generate phase report
report = generate_phase_report("Core Feature Development")
print(report)
# Output: Detailed phase analysis with weight and related phases


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
# Run all tests
python -m unittest discover PhaseSync/tests

# Run with coverage
pytest --cov=PhaseSync


## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

Apache License 2.0 - See [LICENSE](LICENSE) file for details 