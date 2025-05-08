"""
PyTest Configuration for PhaseSync Tests
"""

import os
import sys
import pytest

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def test_dir(tmpdir):
    """Create a temporary directory for test files."""
    return tmpdir 