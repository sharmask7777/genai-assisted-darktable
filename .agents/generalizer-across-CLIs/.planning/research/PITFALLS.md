# Domain Pitfalls

**Domain:** CLI-agnostic AI agent integration (Cross-CLI Skills)
**Researched:** 2026-05-01

## Critical Pitfalls

Mistakes that cause rewrites or major issues.

### Pitfall 1: Standard Output (stdout) Corruption
**What goes wrong:** The MCP server silently crashes or fails to respond to the AI client.
**Why it happens:** When using the `STDIO` transport, the MCP protocol uses `stdout` strictly for JSON-RPC messages. Any rogue `print("Processing...")` or unconfigured logger in the `dt-ai` backend will inject plain text into the JSON stream, invalidating it.
**Consequences:** Complete failure of the integration; the AI Client will report a "malformed JSON" or "connection lost" error.
**Prevention:** 
- Route all standard Python logging to `sys.stderr`.
- Example: `print("Debug info", file=sys.stderr)`.
- Configure the standard `logging` module to stream to `sys.stderr` explicitly.
**Detection:** Client logs show JSON parsing errors directly following the execution of a tool.

## Moderate Pitfalls

### Pitfall 2: Schema Type Mismatches
**What goes wrong:** The AI LLM repeatedly fails to call the tool correctly.
**Prevention:** Use `pydantic` strict models or well-annotated Python type hints in FastMCP. Do not rely on loose `**kwargs` or `dict` types. Explicitly define `image_path: str` and `parameters: dict[str, float]`.

### Pitfall 3: Relative Path Assumptions
**What goes wrong:** Tools fail to find files because the AI Client spawned the MCP server in a different working directory.
**Prevention:** Ensure the MCP tools always resolve paths to absolute paths immediately, using standard inputs (like `image_dir` passed via initial prompt or config).

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Phase 1: FastMCP Server | Breaking existing `dt-ai` CLI users. | Ensure FastMCP server runs on a completely separate entrypoint (e.g., `uv run mcp run dt_ai/mcp_server.py`) leaving `dt_ai.main:cli` untouched. |
| Phase 2: Prompts | AI ignores AgX constraints. | Ensure the `@mcp.prompt()` schema strictly requires AgX parameters and limits Sigmoid fallbacks. |

## Sources

- [Model Context Protocol Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk) (HIGH)
- Context7 MCP Tools/Resource Standards (HIGH)
