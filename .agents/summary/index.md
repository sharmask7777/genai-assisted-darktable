# Knowledge Base Index - Darktable GenAI Assistant

## Purpose
This directory contains comprehensive documentation for the `dt-ai` project. It is designed to be the primary context source for AI assistants.

## Navigation Guide
AI assistants should start with this file to identify where specific information is located.

| Document | Description | Key Metadata |
|----------|-------------|--------------|
| [index.md](./index.md) | This file; root navigation and assistant instructions. | Navigation, metadata. |
| [codebase_info.md](./codebase_info.md) | High-level overview, tech stack, and core principles. | Stack, structure, goals. |
| [architecture.md](./architecture.md) | Design patterns, architectural maps, and external integrations. | Mermaid diagrams, patterns. |
| [components.md](./components.md) | Module-by-module breakdown of responsibilities and functions. | Modules, API logic. |
| [interfaces.md](./interfaces.md) | CLI commands, Gemini API contract, and XMP schemas. | CLI, JSON schema, XML. |
| [data_models.md](./data_models.md) | Session state format, AI result mapping, and binary encoding. | JSON, IEEE 754, Structs. |
| [workflows.md](./workflows.md) | Sequence diagrams for Audit, Edit, and Handoff pipelines. | Workflows, automation. |
| [dependencies.md](./dependencies.md) | External tool requirements and Python libraries. | sips, darktable, dependencies. |

## Instructions for AI Assistants
- **Understanding logic:** Consult `components.md` and `architecture.md`.
- **Debugging XMP issues:** Check `data_models.md` (encoding) and `interfaces.md` (schemas).
- **Adding new CLI commands:** See `interfaces.md` for existing patterns and `main.py` via `components.md`.
- **Modifying AI prompts:** See `dt_ai/ai.py` linked in `components.md`.

## Example Queries
- *"How does the system encode exposure values for Darktable?"* -> See `data_models.md` and `xmp.py` in `components.md`.
- *"What is the flow for a dry-run audit?"* -> See `workflows.md` and `interfaces.md`.
- *"Where is the Gemini Vision prompt defined?"* -> See `components.md` under `dt_ai.ai`.
