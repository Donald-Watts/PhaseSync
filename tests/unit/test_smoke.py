"""Smoke test for PhaseSync testing infrastructure."""

import os
import sys
import pytest
from pathlib import Path

def test_dummy():
    """Verify that pytest is working."""
    assert True

def test_import_phasesync():
    """Verify that PhaseSync can be imported."""
    try:
        import phasesync
        assert phasesync is not None
    except ImportError:
        assert False, "Failed to import phasesync"

def test_environment_variables():
    """Verify that required environment variables are set."""
    # Check if we're in a development environment
    if os.environ.get('PHASESYNC_DEV', '0') == '1':
        assert 'PYTHONPATH' in os.environ, "PYTHONPATH environment variable not set"
        assert 'PHASESYNC_HOME' in os.environ, "PHASESYNC_HOME environment variable not set"
    else:
        # In production, these variables might be set by the system
        pass

def test_workspace_structure():
    """Verify that the workspace has the required structure."""
    workspace_root = Path(os.environ.get('PHASESYNC_HOME', ''))
    assert workspace_root.exists(), "Workspace root directory not found"
    
    required_dirs = ['src', 'tests', 'docs', 'scripts']
    for dir_name in required_dirs:
        dir_path = workspace_root / dir_name
        assert dir_path.exists(), f"Required directory {dir_name} not found"
        assert dir_path.is_dir(), f"{dir_name} is not a directory"

def test_python_version():
    """Verify that Python version meets requirements."""
    major, minor = sys.version_info[:2]
    assert major >= 3, "Python 3.x is required"
    assert minor >= 8, "Python 3.8 or higher is required"

def test_required_packages():
    """Verify that required packages are installed."""
    required_packages = ['pytest', 'numpy', 'pandas']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            assert False, f"Required package {package} is not installed"

def test_test_configuration():
    """Verify that test configuration is properly set up."""
    assert 'pytest' in sys.modules, "pytest is not properly configured"
    # Check for pytest configuration file
    config_files = ['pytest.ini', 'setup.cfg', 'pyproject.toml']
    workspace_root = Path(os.environ.get('PHASESYNC_HOME', ''))
    assert any((workspace_root / f).exists() for f in config_files), "No pytest configuration file found" 