# PhaseSync AI Navigation Guide
Version 0.1.0

## File Hierarchy and Purpose

### 1. PHASE_SYNC_SPEC.md
**Primary Reference Document**
- Use this as the main source of truth for all technical specifications
- Contains complete implementation details and requirements
- Reference for:
  - Core architecture decisions
  - Technical implementation details
  - Complete SWP algorithm specification
  - Detailed phase requirements
  - Integration specifications

### 2. Project_rules.md
**Development Standards and Guidelines**
- Reference for:
  - Coding standards
  - Development practices
  - Quality assurance requirements
  - Security guidelines
  - Maintenance procedures
- Use when:
  - Enforcing coding standards
  - Implementing security measures
  - Following development practices
  - Maintaining code quality

### 3. PHASE_RULES.md
**Phase-Specific Requirements**
- Reference for:
  - Phase-specific deliverables
  - Phase transition rules
  - Phase completion criteria
- Use when:
  - Managing phase transitions
  - Validating phase completion
  - Tracking phase progress
  - Implementing phase-specific features

### 4. README.md
**Project Overview and Quick Reference**
- Reference for:
  - Project overview
  - Quick start guide
  - Basic usage examples
  - Installation instructions
- Use when:
  - Onboarding new developers
  - Quick reference checks
  - Basic implementation questions
  - Installation and setup

## AI Interaction Guidelines

### When to Use Each File

1. **For Technical Implementation**
   - Primary: PHASE_SYNC_SPEC.md
   - Secondary: Project_rules.md
   - Context: README.md

2. **For Development Standards**
   - Primary: Project_rules.md
   - Secondary: PHASE_SYNC_SPEC.md
   - Context: README.md

3. **For Phase Management**
   - Primary: PHASE_RULES.md
   - Secondary: PHASE_SYNC_SPEC.md
   - Context: Project_rules.md

4. **For Quick Reference**
   - Primary: README.md
   - Secondary: PHASE_SYNC_SPEC.md
   - Context: Project_rules.md

### File Relationships


graph TD
    A[PHASE_SYNC_SPEC.md] --> B[Project_rules.md]
    A --> C[PHASE_RULES.md]
    A --> D[README.md]
    B --> D
    C --> A
    D --> A

### Reference Rules

1. **Technical Decisions**
   - Always check PHASE_SYNC_SPEC.md first
   - Use Project_rules.md for implementation standards
   - Reference PHASE_RULES.md for phase-specific requirements
   - Use README.md for quick reference only

2. **Code Implementation**
   - Follow technical specifications from PHASE_SYNC_SPEC.md
   - Apply standards from Project_rules.md
   - Validate against phase requirements in PHASE_RULES.md
   - Use README.md for basic examples

3. **Documentation Updates**
   - Update PHASE_SYNC_SPEC.md for technical changes
   - Update Project_rules.md for standard changes
   - Update PHASE_RULES.md for phase requirement changes
   - Update README.md for user-facing changes

## AI Response Guidelines

### When to Reference Multiple Files

1. **Technical Implementation**
   
   Primary: PHASE_SYNC_SPEC.md
   Supporting: Project_rules.md
   Context: README.md
   

2. **Development Standards**
   
   Primary: Project_rules.md
   Supporting: PHASE_SYNC_SPEC.md
   Context: README.md
   

3. **Phase Management**
   
   Primary: PHASE_RULES.md
   Supporting: PHASE_SYNC_SPEC.md
   Context: Project_rules.md
   

### Response Structure

1. **Technical Questions**
   - Start with PHASE_SYNC_SPEC.md
   - Include relevant standards from Project_rules.md
   - Reference phase requirements if applicable
   - Link to README.md for examples

2. **Process Questions**
   - Start with Project_rules.md
   - Include relevant technical details from PHASE_SYNC_SPEC.md
   - Reference phase requirements if applicable
   - Link to README.md for context

3. **Phase-Specific Questions**
   - Start with PHASE_RULES.md
   - Include technical requirements from PHASE_SYNC_SPEC.md
   - Reference development standards from Project_rules.md
   - Link to README.md for examples

## Version Control

### File Update Protocol

1. **Technical Changes**
   - Update PHASE_SYNC_SPEC.md first
   - Propagate changes to other files as needed
   - Maintain version consistency across all files

2. **Standard Changes**
   - Update Project_rules.md first
   - Update related technical specifications if needed
   - Maintain consistency with phase requirements

3. **Phase Requirement Changes**
   - Update PHASE_RULES.md first
   - Update technical specifications if needed
   - Maintain consistency with development standards

4. **User-Facing Changes**
   - Update README.md first
   - Update other files as needed
   - Maintain consistency across all documentation

## AI Implementation Notes

1. **Reference Priority**
   - Always check PHASE_SYNC_SPEC.md first for technical details
   - Use Project_rules.md for development standards
   - Reference PHASE_RULES.md for phase-specific requirements
   - Use README.md for quick reference and examples

2. **Response Format**
   - Start with the most relevant file
   - Include supporting information from other files
   - Maintain clear separation of concerns
   - Avoid duplicate information

3. **Update Protocol**
   - Follow the file hierarchy for updates
   - Maintain consistency across all files
   - Update version numbers appropriately
   - Document changes in all affected files

## Dual-Build Architecture Guidelines

### Component-Specific References

1. **Extension Development**
   - Primary: PHASE_SYNC_SPEC.md (Interface Specifications)
   - Secondary: Project_rules.md (TypeScript Standards)
   - Context: README.md (Extension Setup)

2. **Engine Development**
   - Primary: PHASE_SYNC_SPEC.md (SWP Implementation)
   - Secondary: Project_rules.md (Python Standards)
   - Context: README.md (Engine Setup)

3. **Interface Development**
   - Primary: PHASE_SYNC_SPEC.md (Interface Protocols)
   - Secondary: Project_rules.md (Security Standards)
   - Context: README.md (Integration Guide)

### Response Structure for Dual-Build

1. **Extension Questions**
   
   Primary: PHASE_SYNC_SPEC.md (Interface Specs)
   Supporting: Project_rules.md (TypeScript Standards)
   Context: README.md (Extension Setup)

2. **Engine Questions**
   
   Primary: PHASE_SYNC_SPEC.md (SWP Implementation)
   Supporting: Project_rules.md (Python Standards)
   Context: README.md (Engine Setup)
   

3. **Integration Questions**
   
   Primary: PHASE_SYNC_SPEC.md (Interface Protocols)
   Supporting: Project_rules.md (Security Standards)
   Context: README.md (Integration Guide)
  

### Update Protocol for Dual-Build

1. **Extension Updates**
   - Update interface specifications in PHASE_SYNC_SPEC.md
   - Update TypeScript standards in Project_rules.md
   - Update extension setup in README.md
   - Maintain interface compatibility

2. **Engine Updates**
   - Update SWP implementation in PHASE_SYNC_SPEC.md
   - Update Python standards in Project_rules.md
   - Update engine setup in README.md
   - Maintain interface compatibility

3. **Interface Updates**
   - Update all interface specifications
   - Update security standards
   - Update integration documentation
   - Maintain backward compatibility 