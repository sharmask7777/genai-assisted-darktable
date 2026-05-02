# Requirements: generalizer-across-CLIs

## v1 Requirements

### Core Architecture (MCP Standard)
- [ ] **MCP-01**: Implement a unified Model Context Protocol (MCP) server (e.g., using FastMCP) as the standardized interface.
- [ ] **MCP-02**: Ensure all server communication uses JSON-RPC over STDIO transport, routing logs strictly to `stderr`.

### Refactoring `gen-ai-assisted-darktable`
- [ ] **DT-01**: Refactor existing `dt-ai` commands (init-session, apply-variations, etc.) into standardized MCP Tools.
- [ ] **DT-02**: Port the "photography mentor" persona from `.gemini/skills/SKILL.md` into standardized MCP Prompts.
- [ ] **DT-03**: Expose the Darktable session state (`.dt-ai-state.json`) as an MCP Resource.

### Refactoring `darktable-parity-sync`
- [ ] **PAR-01**: Refactor parity sync capabilities (research, codebase audit) into standardized MCP Tools.
- [ ] **PAR-02**: Port the parity sync guidelines from `.gemini/skills/SKILL.md` into standardized MCP Prompts.

### Client Integration & Verification
- [ ] **VER-01**: Provide standardized configuration instructions for registering the MCP server.
- [ ] **VER-02**: Verify end-to-end functionality across at least two different MCP-compliant AI environments (e.g., Claude, Kiro).

## v2 Requirements
- **PAR-03**: Support parallel execution of metadata queries and variation application via MCP.
- **RES-01**: Implement dynamic, live-updating MCP Resources for real-time synchronization.

## Out of Scope
- **CUST-01**: Building custom CLI-specific abstraction layers or wrappers (standardize entirely on MCP).
- **API-01**: Building a custom CLI from scratch.
- **GUI-01**: Adding a graphical user interface.

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| MCP-01 | Phase 1 | Pending |
| MCP-02 | Phase 1 | Pending |
| DT-01 | Phase 2 | Pending |
| DT-02 | Phase 3 | Pending |
| DT-03 | Phase 3 | Pending |
| PAR-01 | Phase 4 | Pending |
| PAR-02 | Phase 5 | Pending |
| VER-01 | Phase 6 | Pending |
| VER-02 | Phase 7 | Pending |
