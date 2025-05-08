"""
PhaseSync Visualization Module

This module provides tools for visualizing and analyzing the Symbolic Weight Protocol (SWP)
compression process. It includes functions for:

1. Step-by-step compression visualization
2. Phase weight reporting
3. Bidirectional phase/weight lookup
4. Symbol map management
5. Tie breaker visualization

The visualizer helps developers and AI tools understand:
- How words are compressed to weights
- Which phases share the same weight
- The semantic relationships between phases
- The mathematical process of compression
- How tie breakers are used when reduced sums match

Example:
    >>> visualize_compression("Python")
    Python:
    P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
    9 + 8 = 17
    1 + 7 = 8
    Total Sum: 98 (used as tie breaker)
"""

import json
from typing import Dict, List, Tuple
from .symbol_compressor import compress_word, get_letter_value

# Global symbol map for caching
_symbol_map: Dict[str, List[str]] = {}

def load_symbol_map(file_path: str = 'symbol_map.json') -> Dict[str, List[str]]:
    """
    Load the symbol map from JSON.
    
    The symbol map contains the mapping between weights and phase names,
    allowing for bidirectional lookup and semantic analysis.
    
    Args:
        file_path: Path to the symbol map JSON file
        
    Returns:
        A dictionary mapping weights to lists of phase names
        
    Example:
        >>> load_symbol_map()
        {
            "8": ["core", "backend"],
            "4": ["utils", "frontend"],
            "9": ["tests", "docs"]
        }
    """
    try:
        with open(file_path, 'r') as f:
            raw_map = json.load(f)
            # Convert to simple format for testing
            new_map = {}
            for weight, phases in raw_map.items():
                if isinstance(phases[0], list):
                    new_map[weight] = [phase[0] for phase in phases]
                else:
                    new_map[weight] = phases
            return new_map
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
    4. Total sum for tie breaking
    
    Args:
        word: The word to visualize
        
    Returns:
        A multi-line string showing the compression steps
        
    Example:
        >>> print(visualize_compression("Python"))
        Python:
        Letter values:
        P = 16, Y = 25, T = 20, H = 8, O = 15, N = 14
        Sum: 98
        Reduced: 8 (9 + 8 = 17, 1 + 7 = 8)
        Total Sum: 98 (used as tie breaker)
    """
    if not word:
        return "No letters to compress"
        
    # Calculate letter values
    letter_values = [(char.upper(), get_letter_value(char)) for char in word]
    total = sum(value for _, value in letter_values)
    
    # Build visualization
    lines = [f"{word}:", "Letter values:"]
    
    # Show letter values
    letter_parts = [f"{char} = {value}" for char, value in letter_values]
    lines.append(", ".join(letter_parts))
    
    # Show sum
    lines.append(f"Sum: {total}")
    
    # Show reduction steps
    current = total
    reduction_steps = []
    while current >= 10:
        digits = [int(d) for d in str(current)]
        next_num = sum(digits)
        reduction_steps.append(f"{' + '.join(map(str, digits))} = {next_num}")
        current = next_num
    
    if reduction_steps:
        lines.append(f"Reduced: {current} ({', '.join(reduction_steps)})")
    else:
        lines.append(f"Reduced: {current}")
    
    # Add total sum for tie breaking
    lines.append(f"Total Sum: {total} (used as tie breaker)")
    
    return "\n".join(lines)

def visualize_phase_weights() -> str:
    """
    Create a visualization of all phase weights.
    
    Generates a comprehensive report showing:
    - All weights and their phases
    - Compression process for each phase
    - Semantic relationships between phases
    - Tie breaker information when weights match
    
    Returns:
        A multi-line string containing the phase weight report
        
    Example:
        >>> print(visualize_phase_weights())
        Phase Weight Report:
        
        Weight 8:
          • Foundation and Definition (Total: 287)
            F(6) + O(15) + U(21) + ... = 287 → 17 → 8
          • Core Feature Development (Total: 198)
            C(3) + O(15) + R(18) + ... = 198 → 18 → 8
    """
    if not _symbol_map:
        _symbol_map.update(load_symbol_map())
    
    lines = ["Phase Weight Report:"]
    
    for weight, phases in sorted(_symbol_map.items()):
        lines.append(f"\nWeight {weight}:")
        for phase in phases:
            reduced, total = compress_word(phase)
            lines.append(f"  • {phase} (Total: {total})")
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
        ["core", "backend"]
    """
    if not _symbol_map:
        _symbol_map.update(load_symbol_map())
    return _symbol_map.get(weight, [])

def get_weight_by_phase(phase: str) -> str:
    """
    Get the weight for a given phase.
    
    Args:
        phase: The phase name to look up
        
    Returns:
        The weight for the phase, or "0" if not found
        
    Example:
        >>> get_weight_by_phase("core")
        "8"
    """
    if not _symbol_map:
        _symbol_map.update(load_symbol_map())
    for weight, phases in _symbol_map.items():
        if phase in phases:
            return weight
    return "0" 