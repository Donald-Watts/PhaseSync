#!/usr/bin/env python3
"""Weight analysis script for PhaseSync."""

import sys
import json
from typing import Dict, List, Union

# Character mapping for SWP
CHAR_MAP = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def compress_text(text: str) -> List[int]:
    """Convert text to numeric values using SWP."""
    return [CHAR_MAP.get(c.upper(), 0) for c in text if c.isalpha()]

def reduce_sum(numbers: List[int]) -> int:
    """Reduce a list of numbers to a single digit through iterative addition."""
    total = sum(numbers)
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

def calculate_weight(text: str) -> Dict[str, Union[str, List[int], int]]:
    """Calculate weight using the Symbolic Weight Protocol."""
    compressed = compress_text(text)
    reduced = reduce_sum(compressed)
    total = sum(compressed)
    
    return {
        "label": text,
        "compressed": compressed,
        "reduced": reduced,
        "sum": total
    }

def analyze_file(file_path: str) -> Dict[str, Union[str, List[int], int]]:
    """Analyze a file and return its weight analysis."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return calculate_weight(content)
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }

def main():
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print(json.dumps({
            "error": "Invalid number of arguments",
            "success": False
        }))
        sys.exit(1)

    file_path = sys.argv[1]
    result = analyze_file(file_path)
    print(json.dumps(result))

if __name__ == "__main__":
    main() 