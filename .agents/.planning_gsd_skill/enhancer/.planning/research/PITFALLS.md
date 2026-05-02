# Domain Pitfalls: Darktable GenAI Enhancer

**Domain:** Photography Automation
**Researched:** 2025-05-01

## Critical Pitfalls

### Pitfall 1: XMP Binary Blobs (`darktable:params`)
**What goes wrong:** Attempting to write module parameters as plain text or JSON.
**Why it happens:** Parameters are hex-encoded C-structs.
**Consequences:** Darktable will fail to load the module or crash if the struct padding is incorrect.
**Prevention:** Use Python `struct` to pack values exactly as the C-code expects.
**Detection:** Check if the length of your generated hex string matches a known "good" XMP for that module.

### Pitfall 2: Module Version Mismatch
**What goes wrong:** Injecting params for AgX v7 into a Darktable installation that only supports v6.
**Why it happens:** Darktable evolves modules quickly; the `modversion` attribute is strict.
**Consequences:** The module appears in the history stack but has no effect or "breaks" the image.
**Prevention:** Always verify the local Darktable version (`darktable --version`) and use a dynamic mapping for `modversion`.

## Moderate Pitfalls

### Pitfall 1: Database Precedence
**What goes wrong:** Changes to the XMP sidecar don't appear in the Darktable GUI.
**Why it happens:** Darktable prefers its internal `library.db` over the XMP file on disk.
**Prevention:** The user must manually "Refresh" the sidecar or the tool must use `darktable-cli` which ignores the DB and forces XMP reading.

### Pitfall 2: Color Space Shifts
**What goes wrong:** Colors look different in the `darktable-cli` render vs the GUI.
**Why it happens:** Different ICC profiles or display transforms being applied.
**Prevention:** Standardize on the **AgX** display transform and ensure `--core --conf display_profile=sRGB` is set if rendering for web previews.

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| **AgX Implementation** | Incorrect "Look" application. | AgX 'Look' settings are often display-referred; apply them last in the stack. |
| **Metadata Extraction** | Missing EXIF in older RAWs. | Implement the interactive fallback (INT-01) early. |
| **RAG Research** | Hallucinated photography advice. | Use strict temperature (0.0) for the RAG chain and cite specific tutorials. |

## Sources
- **Pixls.us Forum**: "XMP manipulation gone wrong" threads.
- **Darktable Issue Tracker**: Common CLI bugs in v4.x/v5.x.
