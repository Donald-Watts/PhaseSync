# Developer Guide for PhaseSync
#
# @phase: Foundation and Definition
# @weight: Raw sum: 243, Reduced sum (digital root): 9 
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

## Developer Guide Placeholder 

## File Metadata Requirements

All files in the PhaseSync project must include the following metadata in their header:
- `@phase`: Indicates the current development phase of the file.
- `@weight`: Includes both the raw sum and the reduced sum (digital root) as calculated by the Symbolic Weight Protocol (SWP).

### How to Calculate @weight
1. Use the SWP character mapping to convert the file's name (or relevant label) to numeric values.
2. Sum the values to get the raw sum.
3. Reduce the sum to a single digit (digital root) by iterative addition.

### Example
```
# @phase: Core Feature Development
# @weight: Raw sum: 353, Reduced sum (digital root): 2
```

Update the @weight tag if the file's content or name changes significantly. 