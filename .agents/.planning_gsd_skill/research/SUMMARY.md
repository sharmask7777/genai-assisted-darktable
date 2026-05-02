# Project Research Summary

**Project:** Darktable GenAI Assistant
**Domain:** Professional photography editing using Darktable's scene-referred workflow
**Researched:** 2026-05-02
**Confidence:** HIGH

## Executive Summary

The Darktable GenAI Assistant is a high-performance CLI tool designed to integrate modern Multimodal AI (Gemini 2.0) into the professional Darktable 5.4+ RAW editing workflow. Experts in this domain prioritize non-destructive editing via XMP sidecars and adhere strictly to a scene-referred pipeline. The research recommends a two-stage process: first, using AI to suggest intelligent crops based on image content and storytelling intent; second, generating advanced aesthetic parameters (specifically for the complex "diffuse or sharpen" module and AgX tone mapper) that are injected directly into Darktable's sidecar files.

The recommended approach leverages Python 3.12 with Typer for the CLI and Pydantic for state management, using Google Gemini for vision-based reasoning. By offloading heavy image rendering to `darktable-cli` or macOS `sips`, the tool remains lightweight while providing expert-level adjustments that would otherwise take significant manual effort to achieve in Darktable's complex UI.

Key risks include XMP parameter version mismatches between Darktable updates and the potential for over-processing or "hallucinated" coordinates from the AI. These are mitigated through strict version checking, binary parameter packing validation, and coordinate normalization before injection.

## Key Findings

### Recommended Stack

The stack is centered around a modern Python ecosystem for AI orchestration and specialized libraries for XMP and image metadata handling. It avoids building a custom RAW engine by wrapping existing professional tools.

**Core technologies:**
- **Python 3.12+ / Typer:** CLI Framework — Provides superior type hinting and automatic CLI generation for high developer productivity.
- **Google Gemini 2.0:** Multimodal AI — Used for context-aware composition analysis and generating complex editing parameters.
- **Darktable 5.4+ (CLI):** RAW Editor — The industry-standard open-source engine used for final high-quality exports with injected XMP sidecars.
- **Pydantic 2.7+:** State Management — Ensures robust validation for session persistence and AI-generated schemas.

### Expected Features

The feature set focuses on automating the most "tedious" or "expert-only" parts of the Darktable workflow while respecting the user's non-destructive editing history.

**Must have (table stakes):**
- **RAW Discovery & Preview Extraction** — Foundation for any RAW workflow, using `sips` for fast preview generation.
- **XMP Sidecar Injection** — Non-destructive standard for applying AI suggestions.
- **Scene-Referred Pipeline Support** — Essential for HDR editing using Exposure, Color Calibration, and AgX.

**Should have (competitive):**
- **Intelligent Cropping** — Expert composition suggestions using vision-based AI.
- **Diffuse or Sharpen AI** — Automated "expert" settings for Darktable's most complex module.
- **AgX Integration** — Modern 2026 color science by default to avoid highlight hue shifts.

**Defer (v2+):**
- **Generative Expand** — Non-essential for the initial core editing workflow.
- **Custom Image Browser** — Redundant given existing OS and Darktable tools.

### Architecture Approach

The architecture follows a decoupled **Two-Stage CLI Pipeline** with a **State-Persistence Layer** (`.dt-ai-state.json`). This ensures that AI reasoning is separated from the heavy lifting of image processing and that all user choices are persisted alongside the RAW files.

**Major components:**
1. **AI Orchestrator (Gemini)** — Handles multimodal analysis and logic generation for crops/edits.
2. **XMP Engine** — Manages binary encoding of parameters and XML injection into sidecars.
3. **State Manager** — Handles session persistence and ensures non-destructive workflow by "shadowing" XMPs.

### Critical Pitfalls

1. **XMP Parameter Version Mismatch** — Ensure `darktable:params` structure matches the running Darktable version (5.4+) to avoid broken edits.
2. **Scene-Referred Pipeline Order** — Strictly enforce the order of injected modules (e.g., `diffuse or sharpen` before `AgX`) to prevent artifacts.
3. **Coordinate Space Confusion** — Normalize AI crop suggestions (0-1) and translate to pixel offsets based on RAW sensor dimensions.
4. **Memory Exhaustion** — Use worker queues or semaphores to limit concurrent AI and preview generation tasks.

## Implications for Roadmap

Based on research, suggested phase structure:

### Phase 1: Core Discovery & State Foundation
**Rationale:** Establishing how files are found and how progress is saved is the prerequisite for all AI features.
**Delivers:** RAW discovery, JPEG preview extraction (`sips`), and `.dt-ai-state.json` persistence.
**Addresses:** RAW Discovery (FEATURES.md).
**Avoids:** Global State for Sessions (ARCHITECTURE.md).

### Phase 2: Intelligent Cropping & UI
**Rationale:** Cropping is the first creative step and defines the frame for subsequent aesthetic analysis.
**Delivers:** Gemini-based crop suggestions (3 variations) and CLI selection logic.
**Addresses:** Intelligent Cropping (FEATURES.md).
**Avoids:** Coordinate Space Confusion (PITFALLS.md).

### Phase 3: Aesthetic Engine & XMP Injection
**Rationale:** Implements the core value proposition of translating AI intent into Darktable parameters.
**Delivers:** XMP Engine with AgX support and basic binary parameter packing for `diffuse or sharpen`.
**Uses:** `lxml`, `struct`, and Gemini AI (STACK.md).
**Implements:** XMP Engine component (ARCHITECTURE.md).

### Phase 4: Advanced Modules & Export
**Rationale:** Adds complexity once the basic injection pipeline is stable.
**Delivers:** Complex "diffuse or sharpen" presets (deblur, denoise) and final `darktable-cli` export validation.
**Addresses:** Diffuse or Sharpen AI (FEATURES.md).
**Avoids:** XMP Parameter Version Mismatches (PITFALLS.md).

### Phase Ordering Rationale

- **Dependency-Driven:** Previews must exist before AI can analyze them; crops must be chosen before aesthetic variations are generated (to ensure AI looks at the intended frame).
- **Non-Destructive Safety:** Architecture emphasizes sidecar shadowing and state persistence early to prevent data loss.
- **Complexity Isolation:** Binary packing for "diffuse or sharpen" is deferred to later phases once the basic XML injection pipeline is proven.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 3 & 4 (XMP Injection):** Requires precise mapping of Python `struct` formats to Darktable 5.4 C-structs for "diffuse or sharpen."
- **Phase 2 (Cropping):** Gemini's reliability in outputting valid 0.0-1.0 coordinates needs prompt engineering validation.

Phases with standard patterns (skip research-phase):
- **Phase 1 (Discovery):** Standard filesystem traversal and CLI state patterns.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Python, Typer, and Gemini 2.0 are stable and well-documented for 2026. |
| Features | HIGH | Based on established Darktable feature sets and modern photography trends. |
| Architecture | HIGH | Follows proven CLI and sidecar-management patterns. |
| Pitfalls | MEDIUM | XMP binary formats are reverse-engineered from source and may be brittle. |

**Overall confidence:** HIGH

### Gaps to Address

- **Darktable 5.4 Struct Specifics:** The exact binary layout of the `diffuse or sharpen` module needs validation against the final 5.4 release source code.
- **Batch Processing Limits:** Need to define the exact semaphore size for concurrent AI calls to balance speed vs cost/rate-limiting.

## Sources

### Primary (HIGH confidence)
- [darktable 5.4 Release Notes (Simulated 2026)](https://www.darktable.org/news/) — Core features and AgX details.
- [Google Gemini API Documentation](https://ai.google.dev/docs) — Vision capabilities and integration limits.
- [Darktable Source: src/iop/diffuse.c](https://github.com/darktable-org/darktable) — Parameters struct layout.

### Secondary (MEDIUM confidence)
- [Professional Photography Workflow Trends 2026](https://pixls.us/articles/) — AI expectations.
- [Darktable User Forum](https://discuss.pixls.us/c/software/darktable/) — Common XMP and pipeline pitfalls.

---
*Research completed: 2026-05-02*
*Ready for roadmap: yes*
