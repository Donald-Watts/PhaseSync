# PhaseSync CLI Documentation

The PhaseSync command-line interface provides easy access to all core functionality. This document details all available commands and their usage.

## Installation

After installing PhaseSync, the CLI tool is available as `phasesync`:

# Verify installation
phasesync --version


## Available Commands

### 1. Compress

Compress words or phrases into their symbolic weights.


# Basic compression
phasesync compress "Python"

# Compress multiple words
phasesync compress "Web Development" "Python"

# Verbose output
phasesync compress -v "Python"

# Custom mapping file
phasesync compress -m custom_map.json "Python"


Options:
- `-v, --verbose`: Show detailed compression steps
- `-m, --map`: Use custom symbol mapping file
- `-o, --output`: Save output to file

### 2. Analyze

Analyze development phases and their weights.


# Analyze a phase
phasesync analyze "Core Feature Development"

# List all phases for a weight
phasesync analyze --weight 8

# Show phase details
phasesync analyze -d "Core Feature Development"

# Export analysis
phasesync analyze -o report.json "Core Feature Development"


Options:
- `-w, --weight`: Filter by weight
- `-d, --details`: Show detailed phase information
- `-o, --output`: Save analysis to file
- `-f, --format`: Output format (json, yaml, text)

### 3. Visualize

Generate visual representations of compression and phase analysis.


# Visualize word compression
phasesync visualize "Python"

# Generate phase report
phasesync visualize --phase "Core Feature Development"

# Save visualization
phasesync visualize -o output.png "Python"

# Interactive mode
phasesync visualize -i "Python"


Options:
- `-p, --phase`: Visualize phase instead of word
- `-o, --output`: Save visualization to file
- `-i, --interactive`: Launch interactive visualization
- `-f, --format`: Output format (png, svg, html)

### 4. Extract

Extract phase tags from code files.


# Extract from single file
phasesync extract path/to/file.py

# Extract from directory
phasesync extract path/to/directory

# Show detailed tags
phasesync extract -d path/to/file.py

# Export tags
phasesync extract -o tags.json path/to/file.py


Options:
- `-d, --details`: Show detailed tag information
- `-o, --output`: Save tags to file
- `-r, --recursive`: Process directories recursively
- `-f, --format`: Output format (json, yaml, text)

## Global Options

These options are available for all commands:


# Show help
phasesync --help
phasesync <command> --help

# Verbose output
phasesync --verbose <command>

# Debug mode
phasesync --debug <command>

# Version
phasesync --version


## Examples

### Basic Usage


# Compress a word
phasesync compress "Python"
# Output: 8

# Analyze a phase
phasesync analyze "Core Feature Development"
# Output: Weight: 8, Description: Main functionality implementation

# Visualize compression
phasesync visualize "Python"
# Output: Step-by-step compression visualization

# Extract tags
phasesync extract src/main.py
# Output: {'phase': 'core', 'task': 'build_web_ui', 'weight': 'high'}


### Advanced Usage


# Compress with custom mapping
phasesync compress -m custom_map.json "Python"

# Generate detailed phase report
phasesync analyze -d "Core Feature Development" -o report.json

# Create interactive visualization
phasesync visualize -i "Python" -o output.html

# Extract tags from entire project
phasesync extract -r -o project_tags.json .


## Error Handling

The CLI provides clear error messages and exit codes:

- `0`: Success
- `1`: General error
- `2`: Invalid input
- `3`: File not found
- `4`: Permission denied

## Configuration

You can configure the CLI behavior using a configuration file at `~/.phasesync/config.yaml`:


defaults:
  verbose: false
  debug: false
  output_format: text

compression:
  custom_map: ~/.phasesync/maps/default.json

visualization:
  theme: light
  format: png
  interactive: false

extraction:
  recursive: true
  include_patterns:
    - "*.py"
    - "*.js"
    - "*.ts"


## Troubleshooting

Common issues and solutions:

1. **Command not found**
   - Ensure PhaseSync is installed: `pip install -e .`
   - Check PATH: `which phasesync`

2. **Permission denied**
   - Check file permissions
   - Use `sudo` if necessary

3. **Invalid input**
   - Check command syntax: `phasesync --help`
   - Verify input format

4. **File not found**
   - Check file path
   - Ensure file exists
   - Verify permissions

For more help, run:

phasesync --help
phasesync <command> --help
 