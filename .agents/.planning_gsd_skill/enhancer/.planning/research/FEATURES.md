# Feature Landscape: Darktable GenAI Enhancer

**Domain:** Photography AI / Mentorship
**Researched:** 2025-05-01

## Table Stakes

Features users expect in any modern photography AI assistant.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **RAW Conversion** | Base functionality. | Low | Handled by `darktable-cli`. |
| **AgX Defaults** | 2025 industry standard. | Low | Requires setting correct XMP params. |
| **Exposure/WB Auto-fix** | Basic AI capability. | Medium | Requires vision analysis or metadata hints. |
| **Denoising** | Camera-specific noise handling. | Medium | Requires sensor metadata mapping. |

## Differentiators

Features that set this "Enhancer" apart as a **Mentor**.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| **Pre-flight Report** | Educational value; builds trust. | Medium | Generates text explaining *why* AgX was chosen over Sigmoid for a specific sky. |
| **Subject-Specific Research** | Artistic context (e.g. "Landscape vs Portrait"). | High | Uses RAG to find best practices for the detected subject. |
| **Lens Shift Correction** | Technical precision. | Medium | Fixes color casts based on lens metadata and known profiles. |
| **Mentorship Rationale** | "Teach a man to fish." | Medium | Explains the "Pivot" and "Purity" settings in the AgX module. |

## Anti-Features

Features to explicitly NOT build.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| **GUI Development** | Darktable's GUI is complex and out of scope. | Stay headless; inject XMPs for the user to open in Darktable. |
| **Legacy Support** | Base curves/Display-referred modules are deprecated. | Hard-fail or warn if legacy modules are detected. |
| **Direct DB Writing** | Risk of database corruption. | Only interact via XMP sidecars and CLI. |

## Feature Dependencies

```
Metadata Extraction (META-01) → Subject Detection (RES-01) → Mentorship Generation (EDU-01)
AgX/Sigmoid Foundation (AGX-01) → Pre-flight Reports (EDU-01)
```

## MVP Recommendation

Prioritize:
1.  **AGX-01 (AgX Foundation)**: Prove we can reliably inject and render AgX-based edits.
2.  **META-01 (Metadata Analysis)**: Extract lens/sensor data to prove "context awareness."
3.  **EDU-01 (Basic Pre-flight)**: Simple report explaining the "AgX vs Sigmoid" decision.

Defer: **RES-01 (Subject Research)**: RAG-based research is high complexity and can be added once the engine is stable.

## Sources
- **Project Enhancer Requirements**: Internal documentation.
- **2025 Workflow Research**: Community best practices for scene-referred editing.
