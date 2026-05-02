# Domain Pitfalls

**Domain:** Professional photography editing using Darktable's scene-referred workflow.
**Researched:** 2026-05-02

## Critical Pitfalls

### Pitfall 1: XMP Parameter Version Mismatches
**What goes wrong:** Darktable modules evolve; a `darktable:params` string from DT 3.8 might fail or produce artifacts in DT 5.4.
**Why it happens:** Internal structs change (fields added/removed), but the XMP format remains opaque.
**Consequences:** AI-generated edits look broken or "extreme."
**Prevention:** Always check `darktable:modversion` and `darktable:params` structure against the *running* Darktable version.
**Detection:** Validate with a test export using `darktable-cli` and check for errors in stdout.

### Pitfall 2: Scene-Referred Pipeline Order
**What goes wrong:** Injecting modules in the wrong order (e.g., placing `diffuse or sharpen` after `AgX`).
**Why it happens:** The XMP `darktable:num` attribute determines the history stack order, but doesn't strictly enforce pipeline logic.
**Consequences:** Haloing, color artifacts, or ineffective noise reduction.
**Prevention:** Encode the standard scene-referred sequence into the `XMP Engine` logic.

## Moderate Pitfalls

### Pitfall 1: Coordinate Space Confusion (Cropping)
**What goes wrong:** AI suggests a crop in "normalized" coordinates (0.0 to 1.0), but Darktable's `crop` module uses specific pixel or aspect-ratio-locked offsets.
**Prevention:** Normalize all AI outputs to 0-1 and have a translation layer that knows the RAW sensor dimensions.

### Pitfall 2: Memory Exhaustion during Batch Processing
**What goes wrong:** Processing 100+ RAWs simultaneously (AI calls + Preview generation).
**Prevention:** Implement a semaphore or worker queue (e.g., `TaskIQ` or `AnyIO` CapacityLimiter) to limit concurrent subprocesses.

## Minor Pitfalls

### Pitfall 1: Filename Encoding
**What goes wrong:** RAW files with spaces or special characters (`DSC_001 (Edit).ARW`).
**Prevention:** Use Python's `pathlib` consistently; never construct shell commands via string interpolation.

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Intelligent Cropping | AI hallucinating crop boxes outside image bounds. | Add a validation step in `XMP Engine` to clip coordinates to [0.0, 1.0]. |
| Diffuse or Sharpen | Over-processing leads to "crunchy" or "plastic" looks. | Research conservative AI prompt constraints for "expert-level" settings. |
| AgX Workflow | Double-tonemapping if `Sigmoid` is also active. | Ensure the `XMP Engine` explicitly disables competing tone mappers. |

## Sources

- [Darktable User Forum: Common XMP Issues](https://discuss.pixls.us/c/software/darktable/)
- [Scene-Referred Workflow Pitfalls](https://ansel.photos/en/doc/theory/scene-referred-workflow/)
