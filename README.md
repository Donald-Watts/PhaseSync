PhaseSync
PhaseSync is a powerful tool for managing and tracking codebases using the Symbolic Weight Protocol (SWP). It provides a deterministic way to convert text into single-digit weights while preserving semantic meaning, making it easier for both AI and human developers to understand and navigate codebases.

Features
Symbolic Weight Protocol (SWP)
Converts text into single-digit weights (0-9)
Preserves semantic meaning through deterministic compression
Handles compound words and phrases
Uses total sum as tie breaker when reduced sums match
Phase Management
Automatic phase detection and tagging
Weight-based phase organization
Bidirectional phase/weight lookup
Visual phase weight reporting
Codebase Analysis
File complexity analysis
Phase tag extraction
Symbolic weight calculation
Tie breaker resolution
Installation
pip install phasesync
Quick Start
Initialize PhaseSync in your project:
phasesync init
Add phase tags to your files:
# @phase:core
# @task:build_web_ui
# @weight:high
def some_function():
    pass
Analyze your project:
phasesync analyze
How It Works
Symbolic Weight Protocol
The SWP works through these steps:

Convert letters to numbers (A=1 to Z=26)
Sum the numbers
Reduce to a single digit by summing digits
For compound words, handle each part separately
Use total sum as tie breaker when reduced sums match
Example:

"Python" → P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
98 → 9 + 8 = 17
17 → 1 + 7 = 8
Total sum (98) used as tie breaker if reduced sum matches another word
Tie Breaker System
When two phases have the same reduced sum, PhaseSync uses the total sum as a tie breaker:

Higher total sum indicates more significant phase
Provides definitive guidance for phase ordering
Helps resolve ambiguous weight matches
Example:

Weight 8:
  • Foundation and Definition (Total: 287)
  • Core Feature Development (Total: 198)
In this case, "Foundation and Definition" is considered more significant due to its higher total sum.

Usage
Command Line Interface
# Initialize project
phasesync init

# Analyze project
phasesync analyze

# Generate phase report
phasesync report

# Visualize phase weights
phasesync visualize
Python API
from phasesync import compress_word, analyze_file_complexity

# Compress a word
reduced, total = compress_word("Python")
print(f"Reduced: {reduced}, Total: {total}")

# Analyze file complexity
mass, reduced, total = analyze_file_complexity("src/main.py")
print(f"Mass: {mass}, Reduced: {reduced}, Total: {total}")
Testing
Run the test suite:

python -m unittest discover tests
The test suite verifies:

Letter value calculations
Word compression
Number reduction
Phase tag compression
Tag extraction
Deterministic behavior
Full text compression
Tie breaker functionality
Contributing
Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request


License
Apache License 2.0

This release represents a significant step forward in semantic phase management and AI collaboration. We invite the community to try PhaseSync and contribute to its growth.

For support, open issues on GitHub or reach out to the author.
