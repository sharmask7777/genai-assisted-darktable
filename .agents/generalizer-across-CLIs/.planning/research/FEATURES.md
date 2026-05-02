# Feature Landscape

**Domain:** CLI-agnostic AI agent integration (Cross-CLI Skills)
**Researched:** 2026-05-01

## Table Stakes

Features users expect. Missing = product feels incomplete or broken across CLIs.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Standardized Tool Definitions** | AI clients need to know what functions they can call (`init-session`, `apply-variations`). | Low | Using `@mcp.tool()` via FastMCP automatically generates correct JSON schema. |
| **Standardized Prompts** | The agent persona ("photography mentor") must be preserved across CLIs. | Low | Using `@mcp.prompt()` removes reliance on `.gemini/skills/SKILL.md`. |
| **Cross-Platform STDIO** | Must work on macOS, Windows, Linux seamlessly. | Low | MCP handles standard transport safely. |

## Differentiators

Features that set product apart. Not expected, but highly valued.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| **Live Resources** | Exposing the `dt-ai-progress.json` as an MCP Resource allows the AI to passively read state without needing to call a tool. | Medium | `@mcp.resource()` can watch the Darktable progress file. |
| **Parallel Tool Execution** | Allowing the AI to query metadata, read progress, and apply variations concurrently. | Medium | Supported natively by major providers (Claude/Gemini) through MCP. |

## Anti-Features

Features to explicitly NOT build.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| **CLI-Specific Abstraction Layers** | Building custom wrappers for Claude vs. Kiro creates massive technical debt. | Standardize entirely on MCP and force the clients to comply. |
| **Custom Logging** | Writing logs to stdout corrupts JSON-RPC. | Route all logs to `stderr` or a dedicated log file (`dt-ai.log`). |

## Feature Dependencies

```
Standardized Tool Definitions -> Standardized Prompts (Prompts instruct the LLM to use the tools)
```

## MVP Recommendation

Prioritize:
1. Wrap `apply-variations` and `init-session` as MCP Tools.
2. Port the mentor instructions to an MCP Prompt.
3. Establish STDIO transport for a single client (Claude Desktop).

Defer: Parallel execution and complex Resource monitoring until base tools are stable.

## Sources
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification) (HIGH)
