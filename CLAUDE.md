# CLAUDE.md - Darktable GenAI Assistant (Enhanced)

## Project Context
This project enhances the `dt-ai` assistant with intelligent cropping and advanced Darktable module support (`diffuse or sharpen`).

## GSD Workflow Instructions
This project follows the GSD (Get Shit Done) workflow.
- **Planning**: `.planning/` directory contains the roadmap and requirements.
- **Execution**: Run `/gsd:plan-phase 1` to begin the first phase.
- **Guidelines**: Use the `gsd-*` agents for research, planning, and execution.

## Directory Map
- `dt_ai/`: Core logic.
- `tests/`: Test suite.
- `.planning/`: Project memory and roadmap.
- `.agents/`: AI-specific summaries and internal docs.

## Tech Stack
- **Python 3.12+**
- **Click** (CLI)
- **Gemini 2.0** (Vision & Reasoning)
- **macOS sips** (Preview extraction)
- **Darktable** (XMP injection)

## Build & Test
- Install dependencies: `uv sync`
- Run tests: `uv run pytest`
- Run CLI: `uv run dt-ai`
