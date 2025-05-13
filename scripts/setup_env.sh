#!/bin/bash

# Get the workspace root directory
WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Set PHASESYNC_HOME
echo "export PHASESYNC_HOME=$WORKSPACE_ROOT" >> ~/.bashrc
echo "export PHASESYNC_HOME=$WORKSPACE_ROOT" >> ~/.zshrc

# Set PYTHONPATH
PYTHONPATH="$WORKSPACE_ROOT:$WORKSPACE_ROOT/src"
echo "export PYTHONPATH=$PYTHONPATH" >> ~/.bashrc
echo "export PYTHONPATH=$PYTHONPATH" >> ~/.zshrc

echo "Environment variables set successfully:"
echo "PHASESYNC_HOME: $WORKSPACE_ROOT"
echo "PYTHONPATH: $PYTHONPATH"

# Source the updated environment
source ~/.bashrc 