# Project: Darktable GenAI Assistant (Enhanced Editing & Cropping)

## What This Is
An enhancement to the existing `dt-ai` tool and its associated `genai-assisted-darktable` skill. This project introduces a two-stage editing workflow: first, an intelligent cropping phase for compositional refinement, followed by advanced aesthetic edits leveraging Darktable's professional `diffuse or sharpen` module for noise, deblur, and detail management.

## Core Value
To elevate the `dt-ai` mentorship experience from basic exposure/color correction to professional-grade composition and detail management, ensuring photographers have high-quality, scene-referred starting points for every image.

## Context
- **Base Interface:** `genai-assisted-darktable` skill in `.gemini/skills/`.
- **Backend:** `dt-ai` Python application (Click-based).
- **Target App:** Darktable (Scene-referred AgX pipeline).

## Requirements

### Validated (Already Built)
- ✓ **CORE-01**: RAW discovery and session initialization (`init-session`).
- ✓ **CORE-02**: Preview extraction using macOS `sips` (`agent-next`).
- ✓ **CORE-03**: Basic XMP injection for Exposure, Temperature, Sigmoid, and AgX.
- ✓ **SKILL-01**: Initial "Mentorship" persona and step-by-step guidance.

### Active (New Enhancements)
- [ ] **CROP-01**: Update `agent-next` to include composition analysis and coordinate suggestions for 3 distinct crops.
- [ ] **CROP-02**: Update `SKILL.md` and `apply-variations` to support a two-stage selection flow: User selects a crop before aesthetic edits are applied.
- [ ] **MOD-01**: Implement `diffuse or sharpen` module support in `xmp.py` with binary C-struct parameter packing.
- [ ] **KB-01**: Research best practices for `diffuse or sharpen` (noise vs. deblur vs. sharpen) and integrate into the AI system prompt.

### Out of Scope
- **GUI-01**: Custom cropping interface (relying on CLI selection and Darktable preview).
- **LOC-01**: Local vision models (continuing with Gemini Cloud APIs).

## Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Two-Stage Flow | Cropping affects subsequent aesthetic analysis (e.g., exposure weighting). Must be selected first. | Pending |
| Binary Structs | `diffuse or sharpen` params are complex C-structs; requires precise `struct.pack` implementation. | Pending |

## Evolution
This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026-05-02 after initialization*
