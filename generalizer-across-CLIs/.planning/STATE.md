# Project State: generalizer-across-CLIs

## Project Reference
**Core Value**: Zero lock-in to specific AI CLIs, ensuring long-term portability and flexibility for the photography editing skills across the evolving AI ecosystem.
**Current Focus**: Refactoring `genai-assisted-darktable` and `darktable-parity-sync` from CLI-specific formats to the universal Model Context Protocol (MCP) standard.

## Current Position

**Phase**: 1 - Core MCP Infrastructure
**Plan**: N/A
**Status**: Roadmap created, ready for planning.

### Progress
[ ] Phase 1: Core MCP Infrastructure
[ ] Phase 2: Refactoring Darktable Core Tools
[ ] Phase 3: Darktable Context & Prompts
[ ] Phase 4: Refactoring Parity Sync Tools
[ ] Phase 5: Parity Sync Prompts
[ ] Phase 6: Client Configuration & Documentation
[ ] Phase 7: Multi-Client Verification

## Accumulated Context

### Architectural Decisions
- Standardizing completely on the Model Context Protocol (MCP) to achieve CLI-agnostic operations.
- Utilizing FastMCP with STDIO transport for the server architecture.
- Forcing all operational logging to `stderr` to prevent JSON-RPC transport corruption over `stdout`.

### Known Blockers/Risks
- `stdout` pollution from legacy `print()` statements can silently crash the MCP server.

### Unresolved Questions
- Specifics of Kiro CLI configuration for registering local STDIO MCP servers compared to Claude Desktop.

## Next Steps
- Run `/gsd:plan-phase 1` to define the execution plan for Core MCP Infrastructure.
