# Project: Enhancer (Darktable AI Extension)

## What This Is
A specialized extension and workflow for the Darktable GenAI Assistant. It transforms the AI from a simple "preset generator" into a **Photography Mentor**. It adds research-driven analysis for specific subjects (e.g., raptors, landscapes), prioritizes the modern AgX/Scene-Referred pipeline, and provides educational "Pre-flight" reports to explain technical choices.

## Core Value
Bridge the gap between raw data and professional artistry by educating the user on *why* specific Darktable modules are used, while automatically handling technical hurdles like color shifts and metadata-specific noise profiles.

## Context
- **Tooling**: Built on top of the existing `dt-ai` infrastructure.
- **Pipeline**: Strict preference for **AgX**, **Color Calibration**, and **Sigmoid**.
- **User Experience**: "Educational Pre-flight" via terminal before XMP injection.
- **Intelligence**: Combined vision analysis + RAG-style research of photography tutorials/best practices.

## Requirements

### Validated
(None yet — ship to validate)

### Active
- [ ] **AGX-01**: Force use of AgX/Sigmoid and Color Calibration as the default workflow.
- [ ] **EDU-01**: Generate "Pre-flight Review" text explaining tool choices for the specific image.
- [ ] **RES-01**: Perform subject-specific research (e.g., "how to edit wildlife in darktable") to inform AI decisions.
- [ ] **META-01**: Extract and analyze Lens/Sensor metadata for combination-specific denoising and color corrections.
- [ ] **FIX-01**: Detect and fix automatic color casts (green/red shifts) using lens profile awareness.
- [ ] **INT-01**: Interactive fallback—ask the user if EXIF data is missing or ambiguous.

### Out of Scope
- **LEG-01**: Deep support for legacy Display-Referred modules (base curve, etc.) unless as a last resort.
- **VID-01**: Video editing tutorials or support.

## Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| AgX Default | Industry-standard color science for modern high-dynamic-range editing. | Pending |
| Pre-flight Reports | Educational value; builds user trust and technical skill. | Pending |
| Subject Research | Moves beyond generic edits to "best practice" artistry. | Pending |

## Evolution
This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026-05-01 after initialization*
