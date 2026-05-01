# Project: Darktable GenAI Assistant

## What This Is
A macOS CLI tool that leverages Gemini (via Gemini CLI) to provide a "GenAI first-pass" for RAW photo editing in Darktable. It analyzes images for composition and aesthetics, provides technical recommendations, and generates multiple editing variations directly into Darktable XMP sidecar files.

## Core Value
Empower photographers to delegate the initial "heavy lifting" of RAW processing—specifically denoising, composition, and aesthetic balancing—to a GenAI assistant that understands the Darktable module ecosystem.

## Context
- **User:** Wildlife and landscape photographer.
- **Data Source:** \`~/Pictures\` (contains multiple RAW directories and existing XMP edits).
- **Platform:** macOS (MacBook).
- **Primary Tool:** Darktable (XMP sidecars).
- **Intelligence:** Gemini CLI (Cloud APIs).

## Requirements

### Validated
(None yet — ship to validate)

### Active
- [ ] **CLI-01**: Targeted file selection (single file or glob patterns).
- [ ] **VIS-01**: Extraction of low-token JPEG previews from RAW files for Gemini analysis.
- [ ] **AUD-01**: Aesthetic & technical auditing (composition, wildlife-specific sharpness, etc.).
- [ ] **VAR-01**: Generation of 3 distinct editing "variations" per image.
- [ ] **XMP-01**: Automated generation/injection of Darktable XMP sidecar modules based on AI recommendations.
- [ ] **REC-01**: Specific Darktable tool recommendations (e.g., 'Denoise (profiled)', 'Diffuse or Sharpen').

### Out of Scope
- **GUI-01**: Desktop application (v1 is CLI-only).
- **BAT-01**: Full-library batch processing (focus is on frugal, targeted usage).
- **LOC-01**: Local-only vision models (using Cloud APIs as primary).

## Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| XMP Sidecars | Non-destructive, integrates natively with Darktable without Lua complexity. | Pending |
| JPEG Previews | Minimizes token usage while providing enough detail for vision analysis. | Pending |
| Gemini CLI | High-performance vision and reasoning with easy CLI integration. | Pending |

## Evolution
This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026-05-01 after initialization*
