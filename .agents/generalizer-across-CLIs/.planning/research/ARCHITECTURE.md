# Architecture Patterns

**Domain:** CLI-agnostic AI agent integration (Cross-CLI Skills)
**Researched:** 2026-05-01

## Recommended Architecture

```
[ AI Client (Claude/Gemini/Kiro) ]
       |
       | (JSON-RPC over STDIO)
       v
[ MCP Transport Layer ]
       |
       v
[ FastMCP Server (Python) ]
       |
       | (Function Calls)
       v
[ dt-ai Core Logic (xmp.py, metadata.py) ]
       |
       v
[ Darktable Application / File System ]
```

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| **AI Client** | User interface, LLM execution, Tool calling. | FastMCP Server (via Transport) |
| **FastMCP Server** | Exposes tools, prompts, resources. Translates schemas. | AI Client, `dt-ai` backend |
| **dt-ai Core** | Executes photo editing logic, reads/writes XMP. | FastMCP Server, File System |

## Patterns to Follow

### Pattern 1: Declarative Tool Exposure
**What:** Using decorators to expose existing Python functions directly.
**When:** Exposing `dt-ai` CLI actions to the LLM.
**Example:**
```python
from mcp.server.fastmcp import FastMCP
from dt_ai import main as dt_main

mcp = FastMCP("darktable-assistant")

@mcp.tool()
def apply_variations(image_path: str, parameters_json: str) -> str:
    """Applies AgX or Sigmoid variations to a Darktable image."""
    result = dt_main.apply_variations(image_path, parameters_json)
    return f"Success: {result}"
```

### Pattern 2: Prompt Templates as Code
**What:** Embedding the "mentorship" persona directly in the Python server rather than a markdown file.
**When:** Defining the initial system state and instructions.
**Example:**
```python
@mcp.prompt()
def mentor_instructions() -> str:
    return "You are a talkative, educational photography mentor..."
```

## Anti-Patterns to Avoid

### Anti-Pattern 1: Leaking Transport to Logic
**What:** Having `dt-ai` core functions read from `sys.stdin` or assume a specific CLI context.
**Why bad:** Makes the code untestable and tightly coupled to the transport mechanism.
**Instead:** Keep `dt-ai` functions completely agnostic (accepting standard Python types), and let FastMCP handle the schema validation and transport.

## Scalability Considerations

| Concern | Resolution |
|---------|------------|
| Multi-user concurrency | Since MCP via STDIO spins up a dedicated process per client session, concurrency is handled entirely by the OS process manager. |
| Large metadata reads | Use MCP Resources (paginated or targeted URIs) instead of returning massive strings from a single Tool call. |

## Sources
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification) (HIGH)
- [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk) (HIGH)
