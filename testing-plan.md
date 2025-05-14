# Find This File In: Project/docs/testing-plan.md 
# PhaseSync Testing Protocol
Version 0.1.0

## Overview
This document defines the complete testing and debugging strategy for PhaseSync, covering both the Python SWP engine and the Cursor IDE extension. It serves as the authoritative reference for Phase 5 requirements and CI/CD implementation.

## Testing Stages

### 1. Static Analysis
**Purpose**: Catch issues before runtime
**Tools**:
- Python: ruff/flake8, mypy, bandit
- TypeScript: eslint, tsc
**Requirements**:
- No lint errors
- Type score ≥ 90%
- No security vulnerabilities
**Command**:

# Python
ruff check .
mypy .
bandit -r .

# TypeScript
npm run lint
npm run type-check


### 2. Unit Tests
**Purpose**: Test pure logic in isolation
**Tools**:
- Python: pytest + coverage
- TypeScript: jest
**Requirements**:
- 90% branch coverage (per Project_rules.md)
- All tests pass
- No skipped tests
**Command**:

# Python
pytest --cov=phasesync tests/unit/
pytest --cov=phasesync tests/unit/ --cov-report=html

# TypeScript
npm run test:unit


### 3. Integration Tests
**Purpose**: Test Python⇄Node bridge and CLI
**Tools**:
- Python: pytest
- TypeScript: jest
**Requirements**:
- All bridge operations work
- CLI commands exit successfully
- Error handling works
**Command**:

# Python
pytest tests/integration/

# TypeScript
npm run test:integration


### 4. End-to-End Tests
**Purpose**: Test full plugin functionality
**Tools**:
- vscode-test runner
**Requirements**:
- Extension activates
- Commands appear in palette
- Status bar shows weight
**Command**:

npm run test:e2e


### 5. Performance Tests
**Purpose**: Prevent regressions
**Tools**:
- pytest-benchmark
**Requirements**:
- Compression of 10k files < 5s
- Memory usage < 500MB
**Command**:

pytest tests/performance/ -v


## Debugging Protocol

### 1. CLI Debugging
**Purpose**: Troubleshoot engine issues
**Tools**:
- Python debugger (debugpy)
- Structured logging
**Usage**:

# Enable debug mode
export PHASESYNC_DEBUG=1
phasesync calculate-weight "Python" --debug

# Attach debugger
python -m debugpy --listen 5678 --wait-for-client phasesync/main.py


### 2. Extension Debugging
**Purpose**: Troubleshoot IDE integration
**Tools**:
- VS Code Developer Tools
- Node.js debugger
**Usage**:
1. Enable Developer Tools in Cursor
2. Set breakpoints in TypeScript code
3. Monitor bridge IPC logs

### 3. Bridge Debugging
**Purpose**: Troubleshoot Python⇄Node communication
**Tools**:
- Bridge debug mode
- IPC logging
**Usage**:

const bridge = new SWPBridge({ debug: true });
bridge.on('log', (msg) => console.log(msg));


## CI/CD Pipeline

### GitHub Actions Workflow

name: PhaseSync CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9]
        node-version: [16.x, 18.x]

    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: ${{ matrix.node-version }}
    
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Install Node.js dependencies
      run: npm install
    
    - name: Run static analysis
      run: |
        ruff check .
        mypy .
        bandit -r .
        npm run lint
        npm run type-check
    
    - name: Run tests
      run: |
        pytest --cov=phasesync tests/
        npm run test
    
    - name: Build extension
      run: npm run package
    
    - name: Upload coverage
      uses: codecov/codecov-action@v2


## Test Directory Structure

tests/
├── unit/
│   ├── test_compressor.py
│   ├── test_phasesync.py
│   └── test_extension.ts
├── integration/
│   ├── test_bridge.py
│   ├── test_cli.py
│   └── test_extension.ts
├── e2e/
│   └── test_plugin.ts
└── performance/
    └── test_benchmark.py


## Debug Logging

### Python Engine

import logging

logger = logging.getLogger('phasesync')
logger.setLevel(logging.DEBUG)

# Debug mode
if os.getenv('PHASESYNC_DEBUG'):
    handler = logging.FileHandler('phasesync.log')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(handler)


### TypeScript Extension

class Logger {
    private static instance: Logger;
    private debug: boolean;

    constructor() {
        this.debug = process.env.PHASESYNC_DEBUG === '1';
    }

    log(message: string, data?: any) {
        if (this.debug) {
            console.log(`[PhaseSync] ${message}`, data);
        }
    }
}


## Test Data Management

### Fixtures

# tests/fixtures/sample_files.py
SAMPLE_FILES = {
    'python': {
        'content': 'def hello(): pass',
        'expected_weight': 42
    },
    'typescript': {
        'content': 'function hello() {}',
        'expected_weight': 38
    }
}


### Test Repositories

# Large test repository
git clone https://github.com/example/large-repo.git tests/fixtures/large-repo


## Performance Baselines

### Compression Speed

# tests/performance/baseline.py
BASELINE_METRICS = {
    'compression_time': 5.0,  # seconds
    'memory_usage': 500,      # MB
    'file_count': 10000
}


### Memory Usage

# tests/performance/memory.py
MEMORY_LIMITS = {
    'max_heap': 500,  # MB
    'max_stack': 100  # MB
}


## Next Steps

1. **Immediate Actions**
   - [ ] Set up GitHub Actions workflow
   - [ ] Create initial test suite
   - [ ] Implement debug logging
   - [ ] Add performance benchmarks

2. **Documentation Updates**
   - [ ] Update PHASE_RULES.md to reference this document
   - [ ] Update PHASE_SYNC_SPEC.md with testing details
   - [ ] Update Project_rules.md with testing protocol

3. **Tooling Setup**
   - [ ] Configure ruff/flake8
   - [ ] Set up mypy
   - [ ] Configure jest
   - [ ] Set up vscode-test

4. **Monitoring**
   - [ ] Set up coverage reporting
   - [ ] Configure performance tracking
   - [ ] Implement debug logging
   - [ ] Set up error tracking 
