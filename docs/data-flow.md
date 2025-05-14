# Data Flow for PhaseSync
#
# @phase: Blueprint and Canonical Structure
# @weight: Raw sum: 353, Reduced sum (digital root): 2
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## Overview

This document describes the flow of data and commands through the PhaseSync system, from user input in the IDE or CLI to the SWP Engine and back.



## Typical Data Flow Scenarios

### 1. Weight Analysis via IDE Extension

1. **User Action:**  
   User triggers a weight analysis command in the IDE (Cursor/VS Code).
2. **IDE Extension:**  
   Sends a request to the Bridge (Node.js).
3. **Bridge:**  
   Forwards the request to the SWP Engine (Python) via python-shell or RPC.
4. **SWP Engine:**  
   Processes the request, performs weight analysis, and returns the result.
5. **Bridge:**  
   Receives the result and passes it back to the IDE Extension.
6. **IDE Extension:**  
   Displays the result to the user.



### 2. Weight Analysis via CLI

1. **User Action:**  
   User runs a CLI command (e.g., `phasesync calculate-weight "Python"`).
2. **CLI:**  
   Sends the request directly to the SWP Engine.
3. **SWP Engine:**  
   Processes the request and outputs the result to the CLI.



### 3. Tagging and Export Operations

- Follows a similar flow:  
  User action → IDE Extension/CLI → Bridge (if needed) → SWP Engine → Result back to user.



## Data Flow Diagram

See `component-diagram.json` for a visual representation of component interactions.



## Next Steps

- Update this document as new data flows or features are added.
- Ensure all flows are kept in sync with the component diagram and architecture documentation. 