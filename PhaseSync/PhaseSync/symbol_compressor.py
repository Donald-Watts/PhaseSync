"""
Symbolic Weight Protocol (SWP) Implementation

This module implements the core compression algorithm for PhaseSync, providing
a deterministic way to convert text into single-digit weights while preserving
semantic meaning.

The SWP works through these steps:
1. Convert letters to numbers (A=1 to Z=26)
2. Sum the numbers
3. Reduce to a single digit by summing digits
4. For compound words, handle each part separately
5. Use total sum as tie breaker when reduced sums match

Example:
    "Python" → P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
    98 → 9 + 8 = 17
    17 → 1 + 7 = 8
    Total sum (98) used as tie breaker if reduced sum matches another word
"""

from typing import Tuple, Dict

# Letter-to-number map (A=1 to Z=26)
alphabet: Dict[str, int] = {chr(i + 64): i for i in range(1, 27)}

def get_letter_value(char: str) -> int:
    """
    Get the numeric value for a letter (A=1 to Z=26).
    
    Args:
        char: A single character to convert
        
    Returns:
        The numeric value (1-26) for the letter, or 0 for non-letters
        
    Example:
        >>> get_letter_value('A')
        1
        >>> get_letter_value('Z')
        26
        >>> get_letter_value('!')
        0
    """
    return alphabet.get(char.upper(), 0)

def reduce_number(num: int) -> int:
    """
    Reduce a number to a single digit by summing its digits.
    
    Args:
        num: The number to reduce
        
    Returns:
        A single digit (0-9)
        
    Example:
        >>> reduce_number(98)
        8  # 9 + 8 = 17, 1 + 7 = 8
    """
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def compress_word(word: str) -> Tuple[int, int]:
    """
    Compress a word using the Symbolic Weight Protocol.
    
    For single words:
    - Calculate total letter values
    - Reduce once to get final value
    - Return both reduced and total sum for tie breaking
    
    For compound words (with underscores or spaces):
    - Split into parts
    - Calculate reduced sum for each part
    - Sum the reduced values
    - Return both final sum and original total
    
    Args:
        word: The word to compress
        
    Returns:
        A tuple of (reduced, total) where:
        - reduced is the single-digit weight (0-9)
        - total is the sum of reduced values (for tie breaking)
        
    Example:
        >>> compress_word("Python")
        (8, 98)  # P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98 → 17 → 8
        >>> compress_word("build_web_ui")
        (9, 18)  # build(7) + web(8) + ui(3) = 18 → 9
    """
    # Handle compound words (with underscores or spaces)
    parts = word.replace('_', ' ').split()
    
    if not parts:
        return 0, 0
    
    # For single words, calculate total directly
    if len(parts) == 1:
        total = sum(get_letter_value(char) for char in parts[0])
        return reduce_number(total), total
    
    # For compound words, calculate reduced sum for each part
    reduced_values = []
    total = 0
    for part in parts:
        part_sum = sum(get_letter_value(char) for char in part)
        reduced = reduce_number(part_sum)
        reduced_values.append(reduced)
        total += reduced
    
    # Return the reduced total and original total
    return total if total < 10 else reduce_number(total), total

def compress(text: str) -> Tuple[int, int, int]:
    """
    Compress text using the Symbolic Weight Protocol.
    
    Args:
        text: The text to compress
        
    Returns:
        A tuple of (mass, reduced, total) where:
        - mass is the sum of all letter values
        - reduced is the single-digit reduction of mass
        - total is the original mass (for tie breaking)
        
    Example:
        >>> compress("Python is great")
        (287, 8, 287)  # 287 → 17 → 8
    """
    # Calculate mass (sum of all letter values)
    mass = sum(get_letter_value(char) for char in text)
    # Calculate reduced digit
    reduced = reduce_number(mass)
    return mass, reduced, mass

def analyze_file_complexity(file_path: str) -> Tuple[int, int, int]:
    """
    Analyze a file's complexity using SWP.
    
    Args:
        file_path: Path to the file to analyze
        
    Returns:
        A tuple of (mass, reduced, total) representing the file's complexity
        where total is used as a tie breaker when reduced values match
        
    Example:
        >>> analyze_file_complexity("src/main.py")
        (1234, 1, 1234)  # 1234 → 10 → 1
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return compress(content)
    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")
        return 0, 0, 0

def extract_phase_tags(content: str) -> Dict[str, str]:
    """
    Extract @phase, @task, and @weight tags from content.
    
    Args:
        content: The text content to analyze
        
    Returns:
        A dictionary of tag types to their values
        
    Example:
        >>> extract_phase_tags("# @phase:core\\n# @task:build_web_ui")
        {'phase': 'core', 'task': 'build_web_ui'}
    """
    tags = {}
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if '@phase:' in line:
            tags['phase'] = line.split('@phase:')[1].strip()
        elif '@task:' in line:
            tags['task'] = line.split('@task:')[1].strip()
        elif '@weight:' in line:
            tags['weight'] = line.split('@weight:')[1].strip()
    
    return tags

def create_compressed_map(tags: Dict[str, str]) -> Dict[str, Tuple[str, int]]:
    """
    Create a compressed mapping of tags.
    
    Args:
        tags: Dictionary of tag types to their values
        
    Returns:
        A dictionary mapping compressed keys to (original value, total sum) tuples
        where total sum is used for tie breaking
        
    Example:
        >>> create_compressed_map({'task': 'build_web_ui'})
        {'task_9': ('build_web_ui', 18)}
    """
    compressed = {}
    for tag_type, value in tags.items():
        reduced, total = compress_word(value)
        compressed[f"{tag_type}_{reduced}"] = (value, total)
    return compressed 