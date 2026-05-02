# Research Summary: generalizer-across-CLIs

**Domain:** CLI-agnostic AI agent integration (Cross-CLI Skills)
**Researched:** 2026-05-01
**Overall confidence:** HIGH

## Executive Summary

The project aims to refactor the Darktable photography editing skills (`genai-assisted-darktable` and `darktable-parity-sync`) to remove their tight coupling with proprietary AI CLI formats (e.g., Kiro's `.gemini/skills/SKILL.md`). The research strongly confirms that the Model Context Protocol (MCP) has emerged as the definitive 2026 standard for generalizing AI skills across CLIs such as Claude, Gemini, Kiro, and OpenCode-compliant ecosystems.

By adopting MCP, the core `dt-ai` Python project can be wrapped into a standalone, portable server using the `mcp` SDK (via `FastMCP`). This transforms CLI-specific "skills" into standardized MCP **Tools** (for actions), **Resources** (for context), and **Prompts** (for instructions). The communication happens over JSON-RPC via `stdio`, allowing any modern AI client to securely spawn and interact with the Darktable assistant without custom configuration logic.

## Key Findings

**Stack:** Model Context Protocol (MCP) specification via the official Python `mcp` SDK (`FastMCP`) using STDIO transport.
**Architecture:** Standardized Client-Server model (AI Client -> STDIO Transport -> Python FastMCP Server -> dt-ai backend).
**Critical pitfall:** Writing standard Python `print()` statements to `stdout` breaks the JSON-RPC STDIO transport, silently crashing the MCP server.

## Implications for Roadmap

Based on research, suggested phase structure:

1. **Phase 1: Dependency Refactor & FastMCP Integration** - Integrates `mcp` and `pydantic`.
   - Addresses: Exposing basic `dt-ai` commands as simple MCP tools.
   - Avoids: Mixing core python business logic with transport logic.

2. **Phase 2: Context Generalization (Resources & Prompts)** - Moves `.gemini/skills/SKILL.md` text into standard MCP prompts.
   - Addresses: Portability of the "photography mentor" persona.
   - Avoids: Loss of context when switching from Kiro to Claude.

3. **Phase 3: Multi-CLI Verification** - End-to-end testing across Claude Desktop, Kiro, and Gemini clients.

**Phase ordering rationale:**
- We must establish the MCP server infrastructure (Phase 1) before we can migrate the rich prompt text and context handling (Phase 2). Verification naturally follows implementation.

**Research flags for phases:**
- Phase 3: Likely needs deeper research regarding specific configuration files required by Gemini and Kiro to register local STDIO MCP servers (Claude's `claude_desktop_config.json` equivalent).

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | MCP is universally recognized in official documentation for Claude/multi-LLM clients. |
| Features | HIGH | MCP native features map perfectly to the project's goal. |
| Architecture | HIGH | FastMCP provides a well-defined architectural boundary. |
| Pitfalls | HIGH | STDIO stdout corruption is a highly documented and common failure point in MCP development. |

## Gaps to Address

- **Kiro/Gemini Specific Configs:** While MCP is standard, the exact JSON/YAML config required to register an MCP server in the Kiro CLI needs specific testing.
