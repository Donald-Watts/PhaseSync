# PhaseSync Project Rules and Standards
Version 0.1.0

## Core Principles
1. All code must follow the Symbolic Weight Protocol (SWP)
2. Every file must be properly tagged with @phase and @weight metadata
3. All components must support AI-assisted development workflows
4. Code must be maintainable and well-documented

## Symbolic Weight Protocol (SWP) Standards

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

## Development Phases
Files must be tagged with one of these phases in order:
1. Foundation and Definition
2. Blueprint and Canonical Structure
3. Scaffolding and Schema Definition
4. Core Feature Development
5. Intelligence Learning Test Suites
6. User Interface and Orchestration
7. Finalization and Product

## File Structure Requirements
1. Core Components:
   - PhaseSync.py (main logic)
   - SymbolCompressor.py (compression engine)
   - PluginManifest.json (IDE integration)
   - README.md (documentation)

2. Required Functions:
   
   def calculate_weight(label):
       compressed = compress_title(label)
       reduced = reduce_sum(compressed)
       return {
           "label": label,
           "compressed": compressed,
           "reduced": reduced,
           "sum": sum(compressed),
       }
   

## IDE Plugin Requirements
1. Commands:
   - phaseSync.runWeightAnalysis
   - phaseSync.tagPhaseFiles
   - phaseSync.exportWeights

2. Version Requirements:
   - Cursor IDE: >=1.10.0
   - Node.js: Latest LTS
   - esbuild: ^0.17.0

## Development Standards
1. Code Quality:
   - All code must be properly documented
   - Follow PEP 8 for Python code
   - Include type hints
   - Write unit tests for all functions

2. Documentation:
   - Each function must have docstrings
   - Include usage examples
   - Document all parameters and return values
   - Maintain up-to-date README

3. Testing:
   - Unit tests for compression logic
   - Integration tests for phase management
   - End-to-end tests for plugin functionality

## Build Process
1. Development:
   - Use virtual environment
   - Install all dependencies
   - Run tests before commits
   - Follow semantic versioning

2. Deployment:
   - Build plugin bundle
   - Generate documentation
   - Create release notes
   - Update version numbers

## License Compliance
- Apache 2.0 License
- Include license headers in all files
- Document all third-party dependencies

## Future Considerations
1. Plugin Features:
   - Real-time weight analysis
   - Automatic phase tagging
   - Weight manifest generation
   - IDE integration

2. Performance:
   - Optimize compression algorithm
   - Cache results where appropriate
   - Handle large codebases efficiently

3. Extensibility:
   - Support custom phase definitions
   - Allow custom weight calculations
   - Enable plugin customization

## Security Standards
1. Code Security:
   - No hardcoded credentials
   - Secure file handling
   - Input validation
   - Error handling

2. Data Protection:
   - Secure weight storage
   - Protected phase information
   - Safe file operations

## Maintenance Rules
1. Version Control:
   - Use semantic versioning
   - Maintain changelog
   - Document breaking changes

2. Updates:
   - Regular dependency updates
   - Security patches
   - Performance improvements

3. Support:
   - Document known issues
   - Provide upgrade guides
   - Maintain compatibility 