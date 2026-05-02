# Codebase Summary Index

This directory contains comprehensive documentation for the dt-ai (Darktable GenAI Assistant) codebase. **AI Assistants should use this file as the primary context to understand the system.**

## How to use this documentation
1. Review this index to understand the available documentation.
2. If you need to understand the high-level design, consult `architecture.md`.
3. If you need to know how specific Python modules interact, read `components.md`.
4. If you need to interface with the CLI or write a wrapper, see `interfaces.md` and `data_models.md`.

## Documentation Files

- **[Architecture (architecture.md)](architecture.md)**: System design, data flow between the CLI, the File System, and Darktable.
- **[Components (components.md)](components.md)**: Breakdown of `dt_ai/` modules (`main.py`, `ai.py`, `discovery.py`, etc.) and their specific responsibilities.
- **[Interfaces (interfaces.md)](interfaces.md)**: Detailed breakdown of the CLI commands designed for both human users and AI agents.
- **[Data Models (data_models.md)](data_models.md)**: JSON schemas for the AI payload, AI results, and the hidden state tracker.
- **[Workflows (workflows.md)](workflows.md)**: Sequence diagrams detailing the end-to-end process of generating variations.
- **[Dependencies (dependencies.md)](dependencies.md)**: Python packages and critical system dependencies (like macOS `sips`).
- **[Codebase Info (codebase_info.md)](codebase_info.md)**: High-level metrics and language versions.
- **[Review Notes (review_notes.md)](review_notes.md)**: Identified gaps and potential areas for improvement (e.g., cross-platform support).