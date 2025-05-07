# PhaseSync Quick Start Guide

This guide will help you get started with PhaseSync quickly. We'll cover basic usage, common scenarios, and best practices.

## Installation

1. **Clone and Setup**
   ```bash
   # Clone the repository
   git clone https://github.com/Donald-Watts/PhaseSync.git
   cd PhaseSync

   # Create virtual environment
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   # Install
   pip install -e .
   ```

2. **Verify Installation**
   ```bash
   phasesync --version
   ```

## Basic Usage

### 1. Word Compression

```python
from PhaseSync.symbol_compressor import compress_word

# Basic compression
weight = compress_word("Python")  # Returns 8

# Compound words
weight = compress_word("Web Development")  # Returns 7

# Multiple words
weights = [compress_word(word) for word in ["Python", "Django", "Flask"]]
# Returns [8, 7, 6]
```

### 2. Phase Analysis

```python
from PhaseSync.symbol_compressor import analyze_phase

# Get phase information
phase_info = analyze_phase("Core Feature Development")
print(phase_info)
# Output: {'weight': 8, 'description': 'Main functionality implementation'}

# Find phases by weight
phases = analyze_phase(weight=8)
print(phases)
# Output: ['Foundation and Definition', 'Core Feature Development', 'Finalization and Product']
```

### 3. Phase Tagging

```python
# In your code files:
# @phase:core
# @task:build_web_ui
# @weight:high

from PhaseSync.symbol_compressor import extract_phase_tags

# Extract tags from code
code = """
# @phase:core
# @task:build_web_ui
# @weight:high
def build_ui():
    pass
"""

tags = extract_phase_tags(code)
print(tags)
# Output: {'phase': 'core', 'task': 'build_web_ui', 'weight': 'high'}
```

### 4. Visualization

```python
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
```

## Common Scenarios

### 1. Project Phase Analysis

```python
from PhaseSync.symbol_compressor import analyze_project_phases

# Analyze project phases
project_phases = analyze_project_phases("path/to/project")
print(project_phases)
# Output: Dictionary of phases and their weights
```

### 2. Code Review Integration

```python
from PhaseSync.symbol_compressor import analyze_code_review

# Analyze code review
review_info = analyze_code_review("path/to/code")
print(review_info)
# Output: Phase information and recommendations
```

### 3. Development Workflow

```python
# 1. Start new feature
phasesync analyze "Core Feature Development"
# Output: Weight: 8, Description: Main functionality implementation

# 2. Add phase tags to code
# @phase:core
# @task:new_feature
# @weight:high

# 3. Track progress
phasesync visualize --phase "Core Feature Development"
```

## Best Practices

1. **Consistent Phase Tagging**
   - Use standard phase tags
   - Include task descriptions
   - Set appropriate weights

2. **Regular Analysis**
   - Analyze phases regularly
   - Track phase weights
   - Monitor progress

3. **Documentation**
   - Document phase decisions
   - Keep phase tags updated
   - Maintain phase history

4. **Integration**
   - Use in CI/CD pipelines
   - Integrate with project management
   - Automate phase tracking

## Troubleshooting

### Common Issues

1. **Installation Problems**
   ```bash
   # Check Python version
   python --version  # Should be 3.8+

   # Verify installation
   pip list | grep PhaseSync
   ```

2. **Import Errors**
   ```python
   # Check import
   from PhaseSync.symbol_compressor import compress_word
   ```

3. **CLI Issues**
   ```bash
   # Check CLI installation
   which phasesync

   # Verify PATH
   echo $PATH
   ```

### Getting Help

```bash
# Show help
phasesync --help

# Command help
phasesync <command> --help

# Debug mode
phasesync --debug <command>
```

## Next Steps

1. **Explore Documentation**
   - Read full documentation
   - Check examples
   - Review API reference

2. **Try Examples**
   - Run sample code
   - Experiment with features
   - Test different scenarios

3. **Join Community**
   - Check GitHub issues
   - Join discussions
   - Contribute code

4. **Advanced Usage**
   - Custom mappings
   - Integration patterns
   - Automation scripts

## Resources

- [Full Documentation](README.md)
- [API Reference](API.md)
- [CLI Documentation](CLI.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md) 