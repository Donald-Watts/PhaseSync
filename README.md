# PhaseSync v0.1.0
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Cursor IDE](https://img.shields.io/badge/Cursor-IDE-1.10.0%2B-green)](https://cursor.sh)

## Overview
PhaseSync is a powerful development tool that implements the Symbolic Weight Protocol (SWP) to help manage and organize large codebases, particularly in AI-centric development environments. It provides architectural control through symbolic compression and phase-based organization.

## Features
- **Semantic Tag Scanning**: Automatically scan codebases for @phase and @weight tags
- **Symbolic Compression**: Convert text into weighted numeric values using the SWP algorithm
- **Phase Management**: Organize code into 7 distinct development phases
- **AI Integration**: Designed for seamless integration with AI-assisted development tools
- **IDE Support**: Native integration with Cursor IDE and VS Code

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js (Latest LTS version)
- Cursor IDE >= 1.10.0

### Setup

# Clone the repository
git clone https://github.com/Donald-Watts/PhaseSync.git
cd phasesync

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install IDE plugin
npm install
npm run build


## Quick Start

### Basic Usage

from phasesync import PhaseSync, SymbolCompressor

# Initialize PhaseSync
ps = PhaseSync()

# Calculate weight for a label
weight = ps.calculate_weight("Python")
print(weight)
# Output: {
#     "label": "Python",
#     "compressed": [16, 25, 20, 8, 15, 14],
#     "reduced": 8,
#     "sum": 98
# }


### Phase Tagging

# Tag a file with phase and weight
ps.tag_file("my_file.py", phase="Core Feature Development")


## Symbolic Weight Protocol (SWP)

### How It Works
1. **Character Mapping**: Each letter is assigned a numeric value (A=1 to Z=26)
2. **Compression**: Text is converted to numeric values and summed
3. **Reduction**: Sum is reduced to a single digit through iterative addition
4. **Tie Breaking**: Original sum is used as tiebreaker when reduced digits match

### Example
For the word "Python":

P(16) + Y(25) + T(20) + H(8) + O(15) + N(14) = 98
98 → 9 + 8 = 17
17 → 1 + 7 = 8


## Development Phases
1. Foundation and Definition
2. Blueprint and Canonical Structure
3. Scaffolding and Schema Definition
4. Core Feature Development
5. Intelligence Learning Test Suites
6. User Interface and Orchestration
7. Finalization and Product

## IDE Integration

### Cursor IDE Plugin
The PhaseSync plugin provides three main commands:
- `phaseSync.runWeightAnalysis`: Analyze file weights
- `phaseSync.tagPhaseFiles`: Tag files with phase metadata
- `phaseSync.exportWeights`: Export weight manifest

### Configuration

{
  "phasesync.enableAutoTagging": true,
  "phasesync.defaultPhase": "Core Feature Development",
  "phasesync.weightThreshold": 5
}


## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Testing
See [docs/testing-plan.md](docs/testing-plan.md) for the complete testing protocol, including:
- Static analysis requirements
- Unit, integration, and end-to-end testing
- Performance benchmarks
- Debugging procedures
- CI/CD pipeline configuration

## Documentation
- [API Reference](docs/api.md)
- [User Guide](docs/user-guide.md)
- [Developer Guide](docs/developer-guide.md)
- [Plugin Documentation](docs/plugin.md)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.  Commercial Use Requests
To request permission for commercial use:

Email: limited.adls@gmail.com,
Subject: PhaseSync Commercial Use Request
Include:
Your name, organization, and role,
Description of commercial use,
Expected scope and duration.

ADLS Consulting will respond with:
Approval and attribution terms,
Optional licensing fee (if applicable),
A license key or usage agreement.

Built By
Donald Watts / ADLS Consulting- www.adlsconsulting.com
For support, open issues on GitHub or reach out to the author.

## Acknowledgments
- ADLS Creations
- Donald Watts
- The Cursor IDE team

## Support
- [GitHub Issues](https://github.com/Donald-Watts/PhaseSync/issues)
- [Documentation](https://PhaseSync.readthedocs.io)
- [Discord Community](https://discord.gg/PhaseSync)

## Roadmap
- [ ] Real-time weight analysis
- [ ] Custom phase definitions
- [ ] Advanced caching system
- [ ] Multi-IDE support
- [ ] Cloud synchronization

## Version History
- v0.1.0: Initial release with core SWP implementation 
