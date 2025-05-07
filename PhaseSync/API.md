# PhaseSync API Reference

This document provides detailed information about the PhaseSync API, including all available functions, classes, and their usage.

## Core Modules

### symbol_compressor.py

The main module containing core compression functionality.

#### Functions

##### `compress_word(word: str, custom_map: Optional[Dict[str, int]] = None) -> int`

Compress a word into its symbolic weight.

```python
from PhaseSync.symbol_compressor import compress_word

# Basic usage
weight = compress_word("Python")  # Returns 8

# With custom mapping
weight = compress_word("Python", custom_map={"P": 10})  # Returns 9
```

Parameters:
- `word` (str): The word to compress
- `custom_map` (Optional[Dict[str, int]]): Custom letter-to-number mapping

Returns:
- `int`: The compressed weight (1-9)

##### `analyze_phase(phase: Optional[str] = None, weight: Optional[int] = None) -> Union[Dict[str, Any], List[str]]`

Analyze a development phase or find phases by weight.

```python
from PhaseSync.symbol_compressor import analyze_phase

# Analyze phase
info = analyze_phase("Core Feature Development")
# Returns: {'weight': 8, 'description': 'Main functionality implementation'}

# Find phases by weight
phases = analyze_phase(weight=8)
# Returns: ['Foundation and Definition', 'Core Feature Development', 'Finalization and Product']
```

Parameters:
- `phase` (Optional[str]): The phase to analyze
- `weight` (Optional[int]): The weight to find phases for

Returns:
- `Union[Dict[str, Any], List[str]]`: Phase information or list of phases

##### `extract_phase_tags(code: str) -> Dict[str, str]`

Extract phase tags from code.

```python
from PhaseSync.symbol_compressor import extract_phase_tags

tags = extract_phase_tags("""
# @phase:core
# @task:build_web_ui
# @weight:high
def build_ui():
    pass
""")
# Returns: {'phase': 'core', 'task': 'build_web_ui', 'weight': 'high'}
```

Parameters:
- `code` (str): The code to extract tags from

Returns:
- `Dict[str, str]`: Dictionary of extracted tags

##### `analyze_project_phases(project_path: str) -> Dict[str, Any]`

Analyze phases in a project.

```python
from PhaseSync.symbol_compressor import analyze_project_phases

phases = analyze_project_phases("path/to/project")
# Returns: Dictionary of phases and their weights
```

Parameters:
- `project_path` (str): Path to the project directory

Returns:
- `Dict[str, Any]`: Project phase analysis

##### `analyze_code_review(code_path: str) -> Dict[str, Any]`

Analyze code for review.

```python
from PhaseSync.symbol_compressor import analyze_code_review

review = analyze_code_review("path/to/code")
# Returns: Phase information and recommendations
```

Parameters:
- `code_path` (str): Path to the code file

Returns:
- `Dict[str, Any]`: Code review analysis

### visualizer.py

Module for visualization and reporting.

#### Functions

##### `visualize_compression(word: str) -> str`

Generate compression visualization.

```python
from PhaseSync.visualizer import visualize_compression

viz = visualize_compression("Python")
print(viz)
# Output:
# Python:
# P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
# 9 + 8 = 17
# 1 + 7 = 8
```

Parameters:
- `word` (str): The word to visualize

Returns:
- `str`: Visualization text

##### `generate_phase_report(phase: str) -> str`

Generate phase report.

```python
from PhaseSync.visualizer import generate_phase_report

report = generate_phase_report("Core Feature Development")
print(report)
# Output: Detailed phase analysis
```

Parameters:
- `phase` (str): The phase to report on

Returns:
- `str`: Phase report text

##### `create_visualization(word: str, output_path: Optional[str] = None) -> None`

Create visualization file.

```python
from PhaseSync.visualizer import create_visualization

create_visualization("Python", "output.png")
```

Parameters:
- `word` (str): The word to visualize
- `output_path` (Optional[str]): Path to save visualization

Returns:
- `None`

## Classes

### SymbolMap

Class for managing symbol mappings.

```python
from PhaseSync.symbol_compressor import SymbolMap

# Create map
symbol_map = SymbolMap()

# Load from file
symbol_map.load("path/to/map.json")

# Save to file
symbol_map.save("path/to/map.json")

# Get mapping
mapping = symbol_map.get_mapping()

# Update mapping
symbol_map.update_mapping({"P": 10})
```

#### Methods

##### `load(path: str) -> None`

Load mapping from file.

Parameters:
- `path` (str): Path to mapping file

##### `save(path: str) -> None`

Save mapping to file.

Parameters:
- `path` (str): Path to save mapping

##### `get_mapping() -> Dict[str, int]`

Get current mapping.

Returns:
- `Dict[str, int]`: Current mapping

##### `update_mapping(mapping: Dict[str, int]) -> None`

Update mapping.

Parameters:
- `mapping` (Dict[str, int]): New mapping

### PhaseAnalyzer

Class for phase analysis.

```python
from PhaseSync.symbol_compressor import PhaseAnalyzer

# Create analyzer
analyzer = PhaseAnalyzer()

# Analyze phase
info = analyzer.analyze("Core Feature Development")

# Get phases by weight
phases = analyzer.get_phases_by_weight(8)
```

#### Methods

##### `analyze(phase: str) -> Dict[str, Any]`

Analyze phase.

Parameters:
- `phase` (str): Phase to analyze

Returns:
- `Dict[str, Any]`: Phase information

##### `get_phases_by_weight(weight: int) -> List[str]`

Get phases by weight.

Parameters:
- `weight` (int): Weight to find phases for

Returns:
- `List[str]`: List of phases

## Error Handling

### Exceptions

#### `PhaseSyncError`

Base exception for PhaseSync.

```python
from PhaseSync.symbol_compressor import PhaseSyncError

try:
    compress_word("")
except PhaseSyncError as e:
    print(f"Error: {e}")
```

#### `InvalidInputError`

Raised for invalid input.

```python
from PhaseSync.symbol_compressor import InvalidInputError

try:
    compress_word("")
except InvalidInputError as e:
    print(f"Invalid input: {e}")
```

#### `FileNotFoundError`

Raised when file not found.

```python
from PhaseSync.symbol_compressor import FileNotFoundError

try:
    analyze_project_phases("nonexistent")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

## Configuration

### Default Settings

```python
DEFAULT_SETTINGS = {
    "verbose": False,
    "debug": False,
    "output_format": "text",
    "custom_map": None
}
```

### Custom Configuration

```python
from PhaseSync.symbol_compressor import configure

configure({
    "verbose": True,
    "debug": True,
    "output_format": "json",
    "custom_map": {"P": 10}
})
```

## Type Hints

All functions and classes use Python type hints for better IDE support and code clarity.

```python
from typing import Dict, List, Optional, Union, Any

def compress_word(word: str, custom_map: Optional[Dict[str, int]] = None) -> int:
    pass
```

## Constants

### Phase Weights

```python
PHASE_WEIGHTS = {
    "Foundation and Definition": 8,
    "Blueprint and Canonical Structure": 2,
    "Scaffolding and Schema Definition": 6,
    "Core Feature Development": 8,
    "Intelligence Learning Test Suites": 7,
    "User Interface and Orchestration": 9,
    "Finalization and Product": 8
}
```

### Tag Types

```python
TAG_TYPES = {
    "phase": str,
    "task": str,
    "weight": str
}
``` 