"""
PhaseSync Integration Test Suite

This module contains integration tests that verify PhaseSync's functionality
in real-world scenarios, with a focus on the tie breaker system.

The test suite verifies:
1. End-to-end phase analysis
2. Tie breaker resolution
3. Phase weight visualization
4. Symbol map management
5. Real-world codebase analysis
"""

import unittest
import os
import tempfile
from PhaseSync.symbol_compressor import (
    compress_word,
    analyze_file_complexity,
    extract_phase_tags,
    create_compressed_map
)
from PhaseSync.visualizer import (
    visualize_compression,
    visualize_phase_weights,
    get_phase_by_weight,
    get_weight_by_phase
)

class TestPhaseSyncIntegration(unittest.TestCase):
    def setUp(self):
        """Set up test environment with sample files."""
        self.test_dir = tempfile.mkdtemp()
        self.create_test_files()
    
    def tearDown(self):
        """Clean up test environment."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)
    
    def create_test_files(self):
        """Create sample files with phase tags for testing."""
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
        
        # Create architecture module
        arch_content = """
        # @phase:architecture
        # @task:design_system
        # @weight:high
        
        def design_system():
            pass
        """
        with open(os.path.join(self.test_dir, 'architecture.py'), 'w') as f:
            f.write(arch_content)
    
    def test_end_to_end_phase_analysis(self):
        """Test complete phase analysis workflow."""
        # Analyze core module
        core_mass, core_reduced, core_total = analyze_file_complexity(
            os.path.join(self.test_dir, 'core.py')
        )
        
        # Analyze architecture module
        arch_mass, arch_reduced, arch_total = analyze_file_complexity(
            os.path.join(self.test_dir, 'architecture.py')
        )
        
        # Verify results
        self.assertIsInstance(core_mass, int)
        self.assertIsInstance(core_reduced, int)
        self.assertIsInstance(core_total, int)
        self.assertLess(core_reduced, 10)
        
        self.assertIsInstance(arch_mass, int)
        self.assertIsInstance(arch_reduced, int)
        self.assertIsInstance(arch_total, int)
        self.assertLess(arch_reduced, 10)
    
    def test_tie_breaker_resolution(self):
        """Test tie breaker system with real phase names."""
        # Get weights for phases that might have same reduced sum
        phase1 = "Foundation and Definition"
        phase2 = "Core Feature Development"
        
        reduced1, total1 = compress_word(phase1)
        reduced2, total2 = compress_word(phase2)
        
        # If reduced sums match, verify tie breaker
        if reduced1 == reduced2:
            self.assertNotEqual(total1, total2)
            print(f"\nTie breaker example:")
            print(f"{phase1}: Reduced={reduced1}, Total={total1}")
            print(f"{phase2}: Reduced={reduced2}, Total={total2}")
            print(f"Tie broken by total sum difference: {abs(total1 - total2)}")
    
    def test_phase_weight_visualization(self):
        """Test phase weight visualization with tie breaker information."""
        # Create visualization
        visualization = visualize_phase_weights()
        
        # Verify visualization contains tie breaker information
        self.assertIn("Total:", visualization)
        self.assertIn("used as tie breaker", visualization)
        
        # Print visualization for manual inspection
        print("\nPhase Weight Visualization:")
        print(visualization)
    
    def test_symbol_map_management(self):
        """Test symbol map handling with tie breaker values."""
        # Get phases by weight
        weight_8_phases = get_phase_by_weight("8")
        
        if len(weight_8_phases) > 1:
            # Verify multiple phases are returned
            self.assertGreater(len(weight_8_phases), 1)
            
            # Print phases with same weight for manual inspection
            print("\nPhases with weight 8:")
            for phase in weight_8_phases:
                print(f"{phase}")
            
            # Verify each phase has a different total sum
            totals = set()
            for phase in weight_8_phases:
                _, total = compress_word(phase)
                totals.add(total)
            self.assertEqual(len(totals), len(weight_8_phases))
    
    def test_real_world_codebase_analysis(self):
        """Test analysis of real-world codebase structure."""
        # Analyze all files in test directory
        results = {}
        for file in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file)
            mass, reduced, total = analyze_file_complexity(file_path)
            results[file] = (mass, reduced, total)
        
        # Verify results
        self.assertGreater(len(results), 0)
        for file, (mass, reduced, total) in results.items():
            print(f"\nAnalysis for {file}:")
            print(f"Mass: {mass}")
            print(f"Reduced: {reduced}")
            print(f"Total: {total}")
            
            # Verify values
            self.assertIsInstance(mass, int)
            self.assertIsInstance(reduced, int)
            self.assertIsInstance(total, int)
            self.assertLess(reduced, 10)
            self.assertEqual(mass, total)

if __name__ == '__main__':
    unittest.main() 