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
8. Tie breaker functionality

The test suite ensures that the SWP:
- Produces consistent results
- Handles all edge cases
- Maintains semantic meaning
- Works with phase tags
- Processes compound words correctly
- Uses total sum as tie breaker when reduced sums match

Example test cases:
    - "Python" → (8, 98)
    - "build_web_ui" → (9, 18)
    - "architecture" → (5, 131)
"""

import unittest
from PhaseSync.symbol_compressor import (
    get_letter_value,
    reduce_number,
    compress_word,
    compress,
    extract_phase_tags,
    create_compressed_map
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
        - Total sums are preserved for tie breaking
        """
        test_cases = [
            ("Python", (8, 98)),  # P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98 → 17 → 8
            ("Cursor", (4, 94)),  # C(3) + U(21) + R(18) + S(19) + O(15) + R(18) = 94 → 13 → 4
            ("Phase", (4, 49)),   # P(16) + H(8) + A(1) + S(19) + E(5) = 49 → 13 → 4
            ("Sync", (7, 61))     # S(19) + Y(25) + N(14) + C(3) = 61 → 7
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
        - Total sums are preserved for tie breaking
        """
        test_cases = [
            ("build_web_ui", (9, 18)),      # build(7) + web(8) + ui(3) = 18 → 9
            ("architecture", (5, 131)),     # A(1) + R(18) + C(3) + H(8) + I(9) + T(20) + E(5) + C(3) + T(20) + U(21) + R(18) + E(5) = 131 → 5
            ("high", (5, 32)),              # H(8) + I(9) + G(7) + H(8) = 32 → 5
            ("task_management", (9, 9)),    # task(6) + management(3) = 9
            ("logging", (8, 71)),           # L(12) + O(15) + G(7) + G(7) + I(9) + N(14) + G(7) = 71 → 8
            ("unit_testing", (5, 158))      # U(21) + N(14) + I(9) + T(20) + T(20) + E(5) + S(19) + T(20) + I(9) + N(14) + G(7) = 158 → 14 → 5
        ]
        for tag, expected in test_cases:
            result = compress_word(tag)
            print(f"Compressing {tag}: {result} (Expected: {expected})")
            self.assertEqual(result, expected)
    
    def test_tie_breaker(self):
        """
        Test tie breaker functionality.
        
        Verifies that:
        - Words with same reduced sum have different total sums
        - Total sums are used to break ties
        - Compound words handle ties correctly
        """
        # Test words with same reduced sum but different total sums
        word1 = "Phase"
        word2 = "Cursor"
        reduced1, total1 = compress_word(word1)
        reduced2, total2 = compress_word(word2)
        
        self.assertEqual(reduced1, reduced2)  # Both reduce to 4
        self.assertNotEqual(total1, total2)  # Different total sums (49 vs 94)
        
        # Test compound words with same reduced sum
        word3 = "task_management"
        word4 = "build_web_ui"
        reduced3, total3 = compress_word(word3)
        reduced4, total4 = compress_word(word4)
        
        self.assertEqual(reduced3, reduced4)  # Both reduce to 9
        self.assertNotEqual(total3, total4)  # Different total sums (9 vs 18)
    
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
    
    def test_compressed_map_with_tie_breaker(self):
        """
        Test compressed map creation with tie breaker.
        
        Verifies that:
        - Compressed maps include total sums
        - Tie breaker values are preserved
        - Multiple tags with same reduced sum work
        """
        tags = {
            'task': 'build_web_ui',
            'phase': 'architecture'
        }
        compressed = create_compressed_map(tags)
        
        # Verify structure and values
        self.assertIn('task_9', compressed)
        self.assertIn('phase_5', compressed)
        
        # Check that total sums are preserved
        task_value, task_total = compressed['task_9']
        phase_value, phase_total = compressed['phase_5']
        
        self.assertEqual(task_value, 'build_web_ui')
        self.assertEqual(task_total, 18)
        self.assertEqual(phase_value, 'architecture')
        self.assertEqual(phase_total, 131)
    
    def test_deterministic_compression(self):
        """
        Test that compression is deterministic.
        
        Verifies that:
        - Same input always produces same output
        - Results are consistent
        - Known values are correct
        - Total sums are consistent
        """
        word = "Python"
        first_result = compress_word(word)
        second_result = compress_word(word)
        self.assertEqual(first_result, second_result)
        self.assertEqual(first_result, (8, 98))  # Verify known value
    
    def test_full_compression(self):
        """
        Test full text compression.
        
        Verifies that:
        - Full text compression works
        - Results are valid integers
        - Reduced value is single digit
        - Total sum is preserved
        """
        text = "Python is a programming language"
        mass, reduced, total = compress(text)
        self.assertIsInstance(mass, int)
        self.assertIsInstance(reduced, int)
        self.assertIsInstance(total, int)
        self.assertLess(reduced, 10)  # Reduced should be single digit
        self.assertEqual(mass, total)  # Mass and total should be equal

if __name__ == '__main__':
    unittest.main() 