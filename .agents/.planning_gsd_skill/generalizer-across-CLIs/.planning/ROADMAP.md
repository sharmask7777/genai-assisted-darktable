# Roadmap: generalizer-across-CLIs

## Phases
- [ ] **Phase 1: Core MCP Infrastructure** - Establish the FastMCP server, STDIO transport, and secure logging.
- [ ] **Phase 2: Refactoring Darktable Core Tools** - Expose `dt-ai` actions as standardized MCP Tools.
- [ ] **Phase 3: Darktable Context & Prompts** - Expose `.dt-ai-state.json` as Resources and persona as Prompts.
- [ ] **Phase 4: Refactoring Parity Sync Tools** - Expose codebase audit and research actions as MCP Tools.
- [ ] **Phase 5: Parity Sync Prompts** - Port parity sync guidelines into standard MCP Prompts.
- [ ] **Phase 6: Client Configuration & Documentation** - Standardize registration instructions for clients.
- [ ] **Phase 7: Multi-Client Verification** - Test E2E functionality across multiple MCP-compliant AI environments.

## Phase Details

### Phase 1: Core MCP Infrastructure
**Goal**: The MCP server can start, communicate via STDIO, and log to stderr without breaking the JSON-RPC channel.
**Depends on**: None
**Requirements**: MCP-01, MCP-02
**Success Criteria**:
  1. Server process starts and remains running awaiting STDIO input.
  2. All internal and operational logs are output exclusively to stderr.
  3. Server responds correctly to standard MCP initialization requests over stdin/stdout.
**Plans**: TBD

### Phase 2: Refactoring Darktable Core Tools
**Goal**: Darktable-specific actions are exposed as standard MCP tools.
**Depends on**: Phase 1
**Requirements**: DT-01
**Success Criteria**:
  1. AI clients can discover `dt-ai` commands (e.g., init-session, apply-variations) as available tools.
  2. Tool execution successfully triggers the underlying Python logic.
  3. Tool errors are formatted correctly according to the MCP standard.
**Plans**: TBD

### Phase 3: Darktable Context & Prompts
**Goal**: Darktable context (state and persona) is exposed natively via MCP.
**Depends on**: Phase 1
**Requirements**: DT-02, DT-03
**Success Criteria**:
  1. AI clients can read the current `.dt-ai-state.json` via standard MCP resource requests.
  2. The "photography mentor" persona is available as an MCP prompt.
  3. Clients can instantiate the prompt and receive the correct system instructions.
**Plans**: TBD

### Phase 4: Refactoring Parity Sync Tools
**Goal**: Parity sync operations are accessible as standard MCP tools.
**Depends on**: Phase 1
**Requirements**: PAR-01
**Success Criteria**:
  1. AI clients can discover parity sync commands (audit, research) as tools.
  2. Clients can trigger parity checks without relying on legacy CLI-specific syntax.
**Plans**: TBD

### Phase 5: Parity Sync Prompts
**Goal**: Parity sync guidelines are ported to MCP prompts.
**Depends on**: Phase 1
**Requirements**: PAR-02
**Success Criteria**:
  1. The parity sync guidelines are discoverable and available as an MCP prompt.
  2. Clients can load the prompt to understand parity sync rules dynamically.
**Plans**: TBD

### Phase 6: Client Configuration & Documentation
**Goal**: Clear instructions exist for integrating the server with any MCP client.
**Depends on**: None
**Requirements**: VER-01
**Success Criteria**:
  1. Documentation provides copy-paste JSON configurations for Claude Desktop.
  2. Documentation provides integration steps for Kiro CLI.
  3. Troubleshooting steps for STDIO and path issues are clearly documented.
**Plans**: TBD

### Phase 7: Multi-Client Verification
**Goal**: The server is proven to work in multiple real-world AI environments.
**Depends on**: Phase 2, Phase 3, Phase 4, Phase 5, Phase 6
**Requirements**: VER-02
**Success Criteria**:
  1. Server successfully connects to Claude Desktop and exposes tools/resources.
  2. Server successfully connects to Kiro CLI and can execute at least one tool call.
  3. Both client environments maintain stable connections during operation without stdout corruption.
**Plans**: TBD

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Core MCP Infrastructure | 0/0 | Not started | - |
| 2. Refactoring Darktable Core Tools | 0/0 | Not started | - |
| 3. Darktable Context & Prompts | 0/0 | Not started | - |
| 4. Refactoring Parity Sync Tools | 0/0 | Not started | - |
| 5. Parity Sync Prompts | 0/0 | Not started | - |
| 6. Client Configuration & Documentation | 0/0 | Not started | - |
| 7. Multi-Client Verification | 0/0 | Not started | - |
