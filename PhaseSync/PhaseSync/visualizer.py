"""
PhaseSync Visualization Module

This module provides tools for visualizing and analyzing the Symbolic Weight Protocol (SWP)
compression process. It includes functions for:

1. Step-by-step compression visualization
2. Phase weight reporting
3. Bidirectional phase/weight lookup
4. Symbol map management

The visualizer helps developers and AI tools understand:
- How words are compressed to weights
- Which phases share the same weight
- The semantic relationships between phases
- The mathematical process of compression

Example:
    >>> visualize_compression("Python")
    Python:
    P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
    9 + 8 = 17
    1 + 7 = 8
"""

import json
from typing import Dict, List, Tuple
from .symbol_compressor import compress_word, get_letter_value

def load_symbol_map() -> Dict[str, List[str]]:
    """
    Load the symbol map from JSON.
    
    The symbol map contains the mapping between weights and phase names,
    allowing for bidirectional lookup and semantic analysis.
    
    Returns:
        A dictionary mapping weights to lists of phase names
        
    Example:
        >>> load_symbol_map()
        {
            "8": ["Foundation and Definition", "Core Feature Development"],
            "2": ["Blueprint and Canonical Structure"]
        }
    """
    try:
        with open('PhaseSync/symbol_map.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading symbol map: {e}")
        return {}

def visualize_compression(word: str) -> str:
    """
    Create a visual representation of the compression process.
    
    Shows each step of the SWP algorithm:
    1. Letter-to-number conversion
    2. Sum calculation
    3. Number reduction steps
    
    Args:
        word: The word to visualize
        
    Returns:
        A multi-line string showing the compression steps
        
    Example:
        >>> print(visualize_compression("Python"))
        Python:
        P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
        9 + 8 = 17
        1 + 7 = 8
    """
    # Calculate letter values
    letter_values = [(char.upper(), get_letter_value(char)) for char in word]
    total = sum(value for _, value in letter_values)
    
    # Build visualization
    lines = [f"{word}:"]
    
    # Show letter values
    letter_parts = [f"{char}({value})" for char, value in letter_values]
    lines.append(" + ".join(letter_parts) + f" = {total}")
    
    # Show reduction steps
    current = total
    while current >= 10:
        digits = [int(d) for d in str(current)]
        next_num = sum(digits)
        lines.append(f"{' + '.join(map(str, digits))} = {next_num}")
        current = next_num
    
    return "\n".join(lines)

def visualize_phase_weights() -> str:
    """
    Create a visualization of all phase weights.
    
    Generates a comprehensive report showing:
    - All weights and their phases
    - Compression process for each phase
    - Semantic relationships between phases
    
    Returns:
        A multi-line string containing the phase weight report
        
    Example:
        >>> print(visualize_phase_weights())
        Phase Weights:
        
        Weight 8:
          • Foundation and Definition
            F(6) + O(15) + U(21) + ... = 287 → 17 → 8
    """
    symbol_map = load_symbol_map()
    lines = ["Phase Weights:"]
    
    for weight, phases in sorted(symbol_map.items()):
        lines.append(f"\nWeight {weight}:")
        for phase in phases:
            lines.append(f"  • {phase}")
            # Show compression process
            lines.append(f"    {visualize_compression(phase)}")
    
    return "\n".join(lines)

def get_phase_by_weight(weight: str) -> List[str]:
    """
    Get all phases associated with a weight.
    
    Args:
        weight: The weight to look up (0-9)
        
    Returns:
        A list of phase names with the given weight
        
    Example:
        >>> get_phase_by_weight("8")
        ["Foundation and Definition", "Core Feature Development"]
    """
    symbol_map = load_symbol_map()
    return symbol_map.get(weight, [])

def get_weight_by_phase(phase: str) -> str:
    """
    Get the weight for a given phase.
    
    Args:
        phase: The phase name to look up
        
    Returns:
        The weight (0-9) for the phase, or "0" if not found
        
    Example:
        >>> get_weight_by_phase("Foundation and Definition")
        "8"
    """
    symbol_map = load_symbol_map()
    for weight, phases in symbol_map.items():
        if phase in phases:
            return weight
    return "0"  # Default weight if not found 