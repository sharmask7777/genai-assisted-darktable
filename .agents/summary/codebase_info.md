# Codebase Information

## Overview
- **Name**: dt-ai (Darktable GenAI Assistant)
- **Version**: 0.1.0
- **Language**: Python (>=3.12)
- **Frameworks**: Click (CLI)
- **Build System**: Hatchling

## Structure
The codebase consists of a single primary package `dt_ai` containing the core logic, along with a `tests` directory.

- `dt_ai/`: Main application package
- `tests/`: Pytest suite

## Key Technologies
- **macOS `sips`**: Used for fast, native preview extraction of RAW files.
- **Darktable**: The target application; the system generates `.xmp` sidecar files compatible with Darktable's pipeline (specifically targeting the modern AgX workflow).
- **Gemini**: The AI provider used for visual analysis and aesthetic recommendations.