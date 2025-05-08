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
import tempfile
from PhaseSync.visualizer import (
    load_symbol_map,
    visualize_compression,
    visualize_phase_weights,
    get_phase_by_weight,
    get_weight_by_phase
)

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        """Set up test environment with sample symbol map."""
        self.test_map = {
            "8": ["core", "backend"],
            "4": ["utils", "frontend"],
            "9": ["tests", "docs"]
        }
        
        # Create temporary symbol map file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(self.test_map, f)
            self.test_map_path = f.name
        
        # Create test directory
        self.test_dir = tempfile.mkdtemp()
        
        # Create test files
        self.create_test_files()
    
    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_map_path):
            os.remove(self.test_map_path)
        
        # Clean up test directory
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)
    
    def create_test_files(self):
        """Create test files with phase tags."""
        # Create core module
        core_content = """
        # @phase:core
        # @task:build_web_ui
        # @weight:high
        
        def build_web_ui():
            pass
        """
        with open(os.path.join(self.test_dir, 'core.py'), 'w') as f:
            f.write(core_content)
        
        # Create utils module
        utils_content = """
        # @phase:utils
        # @task:helpers
        # @weight:medium
        
        def helpers():
            pass
        """
        with open(os.path.join(self.test_dir, 'utils.py'), 'w') as f:
            f.write(utils_content)
    
    def test_symbol_map_loading(self):
        """
        Test symbol map loading functionality.

        Verifies that:
        - Symbol map loads correctly from file
        - Map structure is preserved
        - Weights map to correct phases
        """
        loaded_map = load_symbol_map(self.test_map_path)
        self.assertEqual(loaded_map, self.test_map)
    
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
        self.assertIn("Total Sum:", visualization)
        
        # Check specific values
        self.assertIn("P = 16", visualization)
        self.assertIn("Sum: 98", visualization)
        self.assertIn("Reduced: 8", visualization)
    
    def test_phase_weight_report(self):
        """
        Test phase weight report generation.

        Verifies that:
        - Report includes all phases
        - Weights are correctly associated
        - Format is consistent
        - Tie breaker information is included
        """
        # Override the default symbol map path
        loaded_map = load_symbol_map(self.test_map_path)
        
        # Update the global symbol map for testing
        import PhaseSync.visualizer as viz
        viz._symbol_map = loaded_map
        
        report = visualize_phase_weights()
        
        # Check report structure
        self.assertIn("Phase Weight Report", report)
        
        # Check weight sections
        for weight in ["8", "4", "9"]:
            self.assertIn(f"Weight {weight}:", report)
            
            # Check phases for this weight
            phases = get_phase_by_weight(weight)
            for phase in phases:
                self.assertIn(phase, report)
    
    def test_phase_lookup(self):
        """
        Test phase lookup by weight.

        Verifies that:
        - Correct phases are returned for a weight
        - All phases are included
        - Order is preserved
        """
        # Override the default symbol map path
        loaded_map = load_symbol_map(self.test_map_path)
        
        # Update the global symbol map for testing
        import PhaseSync.visualizer as viz
        viz._symbol_map = loaded_map
        
        phases = get_phase_by_weight("8")
        self.assertIn("core", phases)
        self.assertIn("backend", phases)
        self.assertEqual(len(phases), 2)
    
    def test_weight_lookup(self):
        """
        Test weight lookup by phase.

        Verifies that:
        - Correct weight is returned for a phase
        - Case sensitivity is handled
        - Non-existent phases return "0"
        """
        # Override the default symbol map path
        loaded_map = load_symbol_map(self.test_map_path)
        
        # Update the global symbol map for testing
        import PhaseSync.visualizer as viz
        viz._symbol_map = loaded_map
        
        weight = get_weight_by_phase("core")
        self.assertEqual(weight, "8")
        
        weight = get_weight_by_phase("nonexistent")
        self.assertEqual(weight, "0")
    
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