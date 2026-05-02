# Project: Darktable GenAI Assistant (Enhanced Editing & Cropping)

## What This Is
An enhancement to the existing Darktable GenAI Assistant (`dt-ai`). This project adds a preliminary intelligent cropping step (generating three distinct crop suggestions for user selection before further edits) and expands the AI's editing repertoire to include advanced Darktable modules like `diffuse or sharpen` for noise reduction, deblurring, and sharpening. It also enriches the underlying knowledge base with expert research on how and when to apply these advanced tools.

## Core Value
To provide photographers with intelligent, AI-driven composition (cropping) options *before* aesthetic edits, and to leverage Darktable's most advanced scene-referred modules (`diffuse or sharpen`) for professional-grade detail and noise management.

## Context
- **Codebase:** Existing `dt-ai` Click CLI application in Python.
- **Workflow:** The current flow goes straight to aesthetic edits; this introduces a two-stage flow (Crop Selection -> Aesthetic Edits).
- **Domain:** Professional photography editing using Darktable's scene-referred workflow.

## Requirements

### Validated
- ✓ **FS-01**: Discover RAW files and manage `.dt-ai-state.json` sessions.
- ✓ **PREV-01**: Extract previews using macOS `sips`.
- ✓ **AI-01**: Generate multiple aesthetic variations (exposure, color calibration) using Gemini.
- ✓ **XMP-01**: Safely duplicate and inject parameters into Darktable XMP sidecar files.

### Active
- [ ] **CROP-01**: Analyze the original image's composition and generate up to three distinct crop suggestions (if the original composition can be improved).
- [ ] **CROP-02**: Present the crop options to the user and require selection before proceeding to the aesthetic editing phase.
- [ ] **MOD-01**: Integrate the `diffuse or sharpen` module into the XMP generation engine to support noise reduction, deblurring, and sharpening.
- [ ] **KB-01**: Research best practices for Darktable's advanced detail modules (`diffuse or sharpen`, denoise) and encode these rules into the AI's system prompt or research database.

### Out of Scope
- **GUI-01**: Building a full graphical interface for crop selection (will rely on Darktable or existing workflows to review and choose).

## Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Two-Stage Flow | Cropping fundamentally changes the composition, which might affect the AI's aesthetic analysis. Therefore, cropping must precede other edits. | Pending |

## Evolution
This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-05-02 after initialization*