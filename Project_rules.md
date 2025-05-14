# PhaseSync Project Rules and Standards
Version 0.1.0

## Table of Contents
1. [Core Principles](#core-principles)
2. [Development Phases](#development-phases)
3. [Symbolic Weight Protocol (SWP)](#symbolic-weight-protocol-swp)
4. [File Structure Requirements](#file-structure-requirements)
5. [Development Standards](#development-standards)
6. [IDE Integration](#ide-integration)
7. [Testing Requirements](#testing-requirements)
8. [Build Process](#build-process)
9. [Security Standards](#security-standards)
10. [Maintenance Rules](#maintenance-rules)
11. [License Compliance](#license-compliance)

## Core Principles
1. All code must follow the Symbolic Weight Protocol (SWP)
2. Every file must be properly tagged with @phase and @weight metadata
3. All components must support AI-assisted development workflows
4. Code must be maintainable and well-documented
5. Use semantic versioning for all releases
6. Maintain comprehensive documentation
7. Follow security best practices

## Development Phases
Files must be tagged with one of these phases in order:
1. **Foundation and Definition**
   - Establish core project architecture
   - Define fundamental concepts and protocols
   - Set up basic project structure

2. **Blueprint and Canonical Structure**
   - Define system architecture
   - Establish coding standards
   - Create component relationships

3. **Scaffolding and Schema Definition**
   - Create project structure
   - Define data models
   - Set up development environment

4. **Core Feature Development**
   - Implement main functionality
   - Create core components
   - Develop primary features

5. **Intelligence Learning Test Suites**
   - Create comprehensive tests
   - Implement AI learning components
   - Develop validation systems

6. **User Interface and Orchestration**
   - Develop user interfaces
   - Create orchestration systems
   - Implement user workflows

7. **Finalization and Product**
   - Complete documentation
   - Prepare for deployment
   - Finalize product features

## Symbolic Weight Protocol (SWP)

### Character-to-Number Mapping
- A = 1, B = 2, C = 3, D = 4, E = 5
- F = 6, G = 7, H = 8, I = 9, J = 10
- K = 11, L = 12, M = 13, N = 14, O = 15
- P = 16, Q = 17, R = 18, S = 19, T = 20
- U = 21, V = 22, W = 23, X = 24, Y = 25, Z = 26

### Compression Rules
1. Convert all letters to their numeric values
2. Sum all numeric values to get symbolic mass
3. Reduce to single digit through iterative addition
4. Use original sum as tiebreaker when reduced digits match

### Example Compression
Input: "Python"
1. P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
2. 98 → 9 + 8 = 17
3. 17 → 1 + 7 = 8
4. Final values:
   - Symbolic mass: 98
   - Reduced digit: 8
   - Tie breaker: 98

## File Structure Requirements

### Core Components
1. **Main Logic**
   - PhaseSync.py
   - SymbolCompressor.py
   - requirements.txt
   - setup.py

2. **Documentation**
   - docs/api.md
   - docs/user-guide.md
   - docs/developer-guide.md
   - docs/plugin.md

3. **Configuration**
   - PluginManifest.json
   - .gitignore

4. **Testing**
   - tests/test_compressor.py
   - tests/test_phasesync.py

### Required Functions

def calculate_weight(label):
    compressed = compress_title(label)
    reduced = reduce_sum(compressed)
    return {
        "label": label,
        "compressed": compressed,
        "reduced": reduced,
        "sum": sum(compressed),
    }

### File Metadata Requirements
- All files must include `@phase` and `@weight` metadata in their header.
- The `@weight` tag should include both the raw sum and the reduced sum (digital root) as calculated by the SWP.
- Example:
  ```
  # @phase: Core Feature Development
  # @weight: Raw sum: 353, Reduced sum (digital root): 2
  ```

## Development Standards

### Code Quality
1. All code must be properly documented
2. Follow PEP 8 for Python code
3. Include type hints
4. Write unit tests for all functions
5. Use clear and consistent naming conventions
6. Implement proper error handling
7. Follow security guidelines

### Documentation
1. Each function must have docstrings
2. Include usage examples
3. Document all parameters and return values
4. Maintain up-to-date README
5. Keep documentation synchronized with code changes
6. Document all architectural decisions
7. Include examples in documentation

## IDE Integration

### Cursor IDE Plugin
1. **Commands**
   - phaseSync.runWeightAnalysis
   - phaseSync.tagPhaseFiles
   - phaseSync.exportWeights

2. **Version Requirements**
   - Cursor IDE: >=1.10.0
   - Node.js: Latest LTS
   - esbuild: ^0.17.0

3. **Configuration**

{
  "phasesync.enableAutoTagging": true,
  "phasesync.defaultPhase": "Core Feature Development",
  "phasesync.weightThreshold": 5
}


## Testing Requirements
1. **Primary Reference**
   - See docs/testing-plan.md for complete testing protocol
   - Follow all stages and requirements defined therein

2. **Coverage**
   - Test coverage must be >90%
   - Unit tests for all functions
   - Integration tests for phase management
   - End-to-end tests for plugin functionality

3. **Test Types**
   - Unit tests for compression logic
   - Integration tests for phase management
   - End-to-end tests for plugin functionality
   - Performance tests for large codebases

4. **Test Documentation**
   - Document test cases
   - Maintain test coverage reports
   - Track performance metrics

## Build Process

### Development
1. Use virtual environment
2. Install all dependencies
3. Run tests before commits
4. Follow semantic versioning
5. Maintain changelog
6. Document breaking changes

### Deployment
1. Build plugin bundle
2. Generate documentation
3. Create release notes
4. Update version numbers
5. Test deployment process
6. Verify all requirements are met

## Security Standards

### Code Security
1. No hardcoded credentials
2. Secure file handling
3. Input validation
4. Error handling
5. Regular security audits
6. Follow security guidelines

### Data Protection
1. Secure weight storage
2. Protected phase information
3. Safe file operations
4. Regular security updates
5. Document security measures

## Maintenance Rules

### Version Control
1. Use semantic versioning
2. Maintain changelog
3. Document breaking changes
4. Regular dependency updates
5. Security patches
6. Performance improvements

### Support
1. Document known issues
2. Provide upgrade guides
3. Maintain compatibility
4. Regular maintenance schedule
5. Performance monitoring

## License Compliance
1. Apache 2.0 License
2. Include license headers in all files
3. Document all third-party dependencies
4. Maintain license compliance
5. Regular license audits

## Future Considerations
1. **Plugin Features**
   - Real-time weight analysis
   - Automatic phase tagging
   - Weight manifest generation
   - IDE integration

2. **Performance**
   - Optimize compression algorithm
   - Cache results where appropriate
   - Handle large codebases efficiently

3. **Extensibility**
   - Support custom phase definitions
   - Allow custom weight calculations
   - Enable plugin customization 