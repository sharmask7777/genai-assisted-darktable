# Technology Stack

**Project:** generalizer-across-CLIs
**Researched:** 2026-05-01

## Recommended Stack

### Core Framework & Specification
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **Model Context Protocol (MCP)** | v1.0+ | Core Specification | The industry standard for CLI-agnostic AI agent integration. Natively supported by Claude (via `mcpServers` config) and other major AI ecosystems (Gemini, Kiro) via standardized MCP clients (e.g., Apigene, open-source adapters). |
| **mcp (Python SDK)** | Latest | Server Implementation | The official Python SDK for building MCP servers. Provides `FastMCP` which makes it incredibly simple to wrap existing Python tools (`dt-ai`) into standard MCP tools, resources, and prompts. |

### Transport & Integration
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **STDIO Transport** | Standard | Local Desktop Integration | Standard transport method for local CLI tools. Allows major AI CLIs (Claude Desktop, Kiro) to spawn the Python process securely and communicate via JSON-RPC over standard input/output. |
| **SSE (Server-Sent Events)** | Standard | Remote/Networked Agents | For future-proofing if the Darktable assistant needs to run on a separate network node or headless server while the CLI connects remotely. |

### Supporting Libraries
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| **click** | >=8.1.7 | CLI Entrypoint | Already used in `dt-ai`. Maintained as the local user-facing CLI, but its core logic is extracted and exposed to the MCP server. |
| **pydantic** | v2.x | Schema Validation | Used by FastMCP to define strict, cross-CLI compatible JSON schemas for tool arguments (e.g., image paths, AgX/Sigmoid configurations). |

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Core Spec | **MCP** | OpenAI Functions / Custom JSON | Vendor lock-in. Custom schemas require building specialized adapters for each CLI (Claude, Gemini, Kiro). MCP is standard and supported universally. |
| Python Server | **mcp (FastMCP)** | Custom FastAPI/Flask | Writing JSON-RPC handling from scratch is error-prone. The official MCP SDK handles transport, protocol negotiation, and schema reflection automatically. |
| Transport | **STDIO** | REST HTTP | STDIO is much easier for desktop AI CLIs to spawn without dealing with port collisions, firewalls, or local network CORS issues. |

## Installation

```bash
# Core MCP SDK
uv add mcp pydantic

# To run the MCP server with FastMCP
uv run mcp run <path_to_server.py>
```

## Migration Strategy

Currently, the `genai-assisted-darktable` skill relies on a proprietary `.gemini/skills/SKILL.md` structure with inline instructions telling the model to run `uv run dt-ai ...`.

To generalize this:
1. Wrap the `dt-ai` commands (`init-session`, `agent-next`, `apply-variations`) as **MCP Tools** using `@mcp.tool()`.
2. Wrap the Darktable directory/state files as **MCP Resources** to allow any CLI to read context safely.
3. Migrate the mentorship and tone guidelines from `SKILL.md` into **MCP Prompts** (`@mcp.prompt()`).

## Sources
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification) (HIGH)
- [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk) (HIGH)
- Context7 MCP Docs (`@modelcontextprotocol/sdk`) (HIGH)
