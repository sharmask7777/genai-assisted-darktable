# Codebase Information - Darktable GenAI Assistant (dt-ai)

## Project Overview
`dt-ai` is a macOS CLI tool designed to integrate Generative AI (Gemini) into the RAW photo editing workflow of Darktable. It provides an "AI first-pass" by analyzing images for aesthetics and composition, then injecting processing recommendations directly into Darktable XMP sidecar files.

## Technology Stack
- **Language:** Python 3.12+
- **CLI Framework:** [Click](https://click.palletsprojects.com/)
- **AI Integration:** Gemini API (via Gemini CLI wrapper)
- **Image Processing:** macOS native `sips` (for preview extraction)
- **Metadata Management:** XML (for Darktable XMP sidecars)
- **Build System:** `uv` with `hatchling` backend
- **Testing:** `pytest`

## Key Packages & Modules
- `dt_ai/`: Main application logic.
  - `main.py`: CLI entry point and command definitions.
  - `ai.py`: Gemini Vision integration and prompt management.
  - `xmp.py`: Low-level XMP generation and module injection logic.
  - `processor.py`: RAW-to-JPEG preview extraction using `sips`.
  - `discovery.py`: File system traversal for RAW and sidecar files.
  - `state.py`: Session management and persistence.
  - `gui.py`: Automation for opening Darktable.

## Directory Structure
- `dt_ai/`: Source code.
- `tests/`: Comprehensive test suite covering all modules.
- `.planning/`: Project requirements, roadmap, and design docs.
- `.agents/`: AI-specific context and task tracking.
- `.venv/`: Virtual environment (managed by `uv`).

## Core Principles
1. **Non-Destructive:** Never modifies RAW originals; only writes to `.xmp` sidecars.
2. **Frugal Token Usage:** Uses low-resolution JPEG previews for Vision analysis.
3. **Multi-Variation:** Generates multiple editing styles (Natural, Dramatic, Creative) for user selection.
4. **Interactive Handoff:** Pauses for user confirmation on critical technical adjustments (e.g., Denoising).
