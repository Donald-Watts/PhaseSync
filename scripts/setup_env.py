#!/usr/bin/env python3
"""Setup script for PhaseSync environment variables."""

import os
import sys
from pathlib import Path

def setup_environment():
    """Set up required environment variables for PhaseSync."""
    # Get the workspace root directory
    workspace_root = Path(__file__).parent.parent.absolute()
    
    # Set PHASESYNC_HOME
    os.environ['PHASESYNC_HOME'] = str(workspace_root)
    
    # Set PYTHONPATH to include the workspace root and src directory
    python_path = os.environ.get('PYTHONPATH', '')
    python_path_parts = python_path.split(os.pathsep) if python_path else []
    
    # Add workspace root and src directory to PYTHONPATH
    new_paths = [
        str(workspace_root),
        str(workspace_root / 'src')
    ]
    
    # Combine existing and new paths, removing duplicates
    python_path_parts.extend(new_paths)
    python_path_parts = list(dict.fromkeys(python_path_parts))
    
    # Set the new PYTHONPATH
    os.environ['PYTHONPATH'] = os.pathsep.join(python_path_parts)
    
    print("Environment variables set successfully:")
    print(f"PHASESYNC_HOME: {os.environ['PHASESYNC_HOME']}")
    print(f"PYTHONPATH: {os.environ['PYTHONPATH']}")

if __name__ == "__main__":
    setup_environment() 