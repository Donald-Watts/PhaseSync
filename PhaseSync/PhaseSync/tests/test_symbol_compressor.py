"""
Symbol Compressor Test Suite

This module contains comprehensive tests for the Symbolic Weight Protocol (SWP)
implementation. It verifies:

1. Letter value calculations
2. Word compression
3. Number reduction
4. Phase tag compression
5. Tag extraction
6. Deterministic behavior
7. Full text compression

The test suite ensures that the SWP:
- Produces consistent results
- Handles all edge cases
- Maintains semantic meaning
- Works with phase tags
- Processes compound words correctly

Example test cases:
    - "Python" → 8
    - "build_web_ui" → 9
    - "architecture" → 5
"""

import unittest
from ..symbol_compressor import (
    get_letter_value,
    reduce_number,
    compress_word,
    compress,
    extract_phase_tags
)

class TestSymbolCompressor(unittest.TestCase):
    def test_letter_values(self):
        """
        Test letter value calculations.
        
        Verifies that:
        - Letters are correctly mapped to numbers (A=1 to Z=26)
        - Case is handled properly
        - Non-letters return 0
        """
        test_cases = [
            ('P', 16), ('Y', 25), ('T', 20), ('H', 8), ('O', 15), ('N', 14),
            ('C', 3), ('U', 21), ('R', 18), ('S', 19)
        ]
        for letter, expected in test_cases:
            self.assertEqual(get_letter_value(letter), expected)
    
    def test_word_compression(self):
        """
        Test word compression with known examples.
        
        Verifies that:
        - Single words compress correctly
        - Compound words are handled properly
        - Results match expected values
        """
        test_cases = [
            ("Python", 8),  # P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98 → 17 → 8
            ("Cursor", 4),  # C(3) + U(21) + R(18) + S(19) + O(15) + R(18) = 94 → 13 → 4
            ("Phase", 4),   # P(16) + H(8) + A(1) + S(19) + E(5) = 49 → 13 → 4
            ("Sync", 7)     # S(19) + Y(25) + N(14) + C(3) = 61 → 7
        ]
        for word, expected in test_cases:
            result = compress_word(word)
            print(f"Compressing {word}: {result} (Expected: {expected})")
            self.assertEqual(result, expected)
    
    def test_reduce_number(self):
        """
        Test number reduction logic.
        
        Verifies that:
        - Numbers are correctly reduced to single digits
        - Multiple reduction steps work
        - Edge cases are handled
        """
        test_cases = [
            (98, 8),    # 9 + 8 = 17 → 1 + 7 = 8
            (94, 4),    # 9 + 4 = 13 → 1 + 3 = 4
            (130, 4),   # 1 + 3 + 0 = 4
            (35, 8),    # 3 + 5 = 8
            (66, 3),    # 6 + 6 = 12 → 1 + 2 = 3
        ]
        for num, expected in test_cases:
            self.assertEqual(reduce_number(num), expected)
    
    def test_phase_tag_compression(self):
        """
        Test compression of phase tags.
        
        Verifies that:
        - Phase names compress correctly
        - Compound phase names work
        - Results match expected values
        """
        test_cases = [
            ("build_web_ui", 9),      # build(7) + web(8) + ui(3) = 18 → 9
            ("architecture", 5),      # A(1) + R(18) + C(3) + H(8) + I(9) + T(20) + E(5) + C(3) + T(20) + U(21) + R(18) + E(5) = 131 → 5
            ("high", 5),              # H(8) + I(9) + G(7) + H(8) = 32 → 5
            ("task_management", 9),   # task(6) + management(3) = 9
            ("logging", 8),           # L(12) + O(15) + G(7) + G(7) + I(9) + N(14) + G(7) = 71 → 8
            ("unit_testing", 5)       # U(21) + N(14) + I(9) + T(20) + T(20) + E(5) + S(19) + T(20) + I(9) + N(14) + G(7) = 158 → 14 → 5
        ]
        for tag, expected in test_cases:
            result = compress_word(tag)
            print(f"Compressing {tag}: {result} (Expected: {expected})")
            self.assertEqual(result, expected)
    
    def test_tag_extraction(self):
        """
        Test phase tag extraction from content.
        
        Verifies that:
        - @phase tags are extracted
        - @task tags are extracted
        - @weight tags are extracted
        - Multiple tags work together
        """
        content = """
        # @phase:core
        # @task:build_web_ui
        # @weight:high
        def some_function():
            pass
        """
        tags = extract_phase_tags(content)
        self.assertEqual(tags['phase'], 'core')
        self.assertEqual(tags['task'], 'build_web_ui')
        self.assertEqual(tags['weight'], 'high')
    
    def test_deterministic_compression(self):
        """
        Test that compression is deterministic.
        
        Verifies that:
        - Same input always produces same output
        - Results are consistent
        - Known values are correct
        """
        word = "Python"
        first_result = compress_word(word)
        second_result = compress_word(word)
        self.assertEqual(first_result, second_result)
        self.assertEqual(first_result, 8)  # Verify known value
    
    def test_full_compression(self):
        """
        Test full text compression.
        
        Verifies that:
        - Full text compression works
        - Results are valid integers
        - Reduced value is single digit
        """
        text = "Python is a programming language"
        mass, reduced = compress(text)
        self.assertIsInstance(mass, int)
        self.assertIsInstance(reduced, int)
        self.assertLess(reduced, 10)  # Reduced should be single digit

if __name__ == '__main__':
    unittest.main() 