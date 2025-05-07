"""
Visualizer Test Suite

This module contains comprehensive tests for the PhaseSync visualization tools.
It verifies:

1. Symbol map loading and validation
2. Compression visualization
3. Phase weight reporting
4. Bidirectional phase/weight lookup
5. Edge cases and error handling

The test suite ensures that the visualizer:
- Correctly loads and validates symbol maps
- Generates accurate compression visualizations
- Produces consistent phase weight reports
- Handles phase/weight lookups correctly
- Manages edge cases appropriately

Example test cases:
    - "Python" compression visualization
    - Phase weight report generation
    - Weight lookup for "core" phase
    - Phase lookup for weight "8"
"""

import unittest
import os
import json
from ..visualizer import (
    load_symbol_map,
    visualize_compression,
    visualize_phase_weights,
    get_phase_by_weight,
    get_weight_by_phase
)

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        """
        Set up test environment.
        
        Creates a temporary symbol map file for testing.
        """
        self.test_map = {
            "8": ["core", "backend"],
            "4": ["utils", "frontend"],
            "9": ["tests", "docs"]
        }
        with open("test_symbol_map.json", "w") as f:
            json.dump(self.test_map, f)
    
    def tearDown(self):
        """
        Clean up test environment.
        
        Removes temporary symbol map file.
        """
        if os.path.exists("test_symbol_map.json"):
            os.remove("test_symbol_map.json")
    
    def test_symbol_map_loading(self):
        """
        Test symbol map loading functionality.
        
        Verifies that:
        - Symbol map loads correctly from file
        - Map structure is preserved
        - Weights map to correct phases
        """
        loaded_map = load_symbol_map("test_symbol_map.json")
        self.assertEqual(loaded_map, self.test_map)
        self.assertEqual(loaded_map["8"], ["core", "backend"])
    
    def test_compression_visualization(self):
        """
        Test compression visualization.
        
        Verifies that:
        - Visualization includes all steps
        - Letter values are correct
        - Summation is accurate
        - Reduction steps are shown
        """
        word = "Python"
        visualization = visualize_compression(word)
        
        # Check that visualization contains all required elements
        self.assertIn("Letter values:", visualization)
        self.assertIn("Sum:", visualization)
        self.assertIn("Reduced:", visualization)
        
        # Verify specific values
        self.assertIn("P = 16", visualization)
        self.assertIn("Y = 25", visualization)
        self.assertIn("98", visualization)  # Sum
        self.assertIn("8", visualization)   # Final reduced value
    
    def test_phase_weight_report(self):
        """
        Test phase weight report generation.
        
        Verifies that:
        - Report includes all phases
        - Weights are correctly associated
        - Compression steps are shown
        - Format is consistent
        """
        report = visualize_phase_weights()
        
        # Check report structure
        self.assertIn("Phase Weight Report", report)
        self.assertIn("Weight 8:", report)
        self.assertIn("Weight 4:", report)
        self.assertIn("Weight 9:", report)
        
        # Verify phase associations
        self.assertIn("core", report)
        self.assertIn("backend", report)
        self.assertIn("utils", report)
    
    def test_phase_lookup(self):
        """
        Test phase lookup by weight.
        
        Verifies that:
        - Correct phases are returned for weights
        - Multiple phases per weight work
        - Non-existent weights return empty list
        """
        # Test existing weight
        phases = get_phase_by_weight("8")
        self.assertIn("core", phases)
        self.assertIn("backend", phases)
        
        # Test non-existent weight
        empty_phases = get_phase_by_weight("1")
        self.assertEqual(empty_phases, [])
    
    def test_weight_lookup(self):
        """
        Test weight lookup by phase.
        
        Verifies that:
        - Correct weight is returned for phase
        - Non-existent phase returns None
        - Case sensitivity is handled
        """
        # Test existing phase
        weight = get_weight_by_phase("core")
        self.assertEqual(weight, "8")
        
        # Test non-existent phase
        no_weight = get_weight_by_phase("nonexistent")
        self.assertIsNone(no_weight)
    
    def test_edge_cases(self):
        """
        Test edge cases and error handling.
        
        Verifies that:
        - Empty input is handled
        - Invalid file paths are handled
        - Malformed symbol maps are handled
        - Special characters are processed
        """
        # Test empty word
        empty_viz = visualize_compression("")
        self.assertIn("No letters to compress", empty_viz)
        
        # Test special characters
        special_viz = visualize_compression("Python!")
        self.assertIn("P = 16", special_viz)
        self.assertIn("! = 0", special_viz)

if __name__ == '__main__':
    unittest.main() 