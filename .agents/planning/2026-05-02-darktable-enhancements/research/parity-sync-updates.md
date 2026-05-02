# Parity Sync: Maintaining Standards

This document outlines how the `darktable-parity-sync` skill should be updated to maintain the new standards established in this project.

## 1. Audit Target: Binary Structs
The parity sync skill's internal research database must be updated to include the 2026 byte-offsets for:
- **`diffuse or sharpen`**: 68-byte struct (v2).
- **`clipping`**: 84-byte struct (v5).
- **`ashift`**: 48-byte struct (v5).

## 2. Audit Target: Pipeline Order
The skill should now audit `dt_ai/xmp.py` to ensure it enforces the following professional sequence:
1. `lens` / `cacorrect` (Base)
2. `denoiseprofile` (Cleaning)
3. `demosaic` (Capture Sharpening)
4. `exposure` (Anchoring)
5. `diffuse` (Surgical)
6. `agx` (Display)

## 3. Implementation Path
- **Task**: Update the `darktable-parity-sync` skill's "External Parity Research" step (Step 2) to prioritize verifying these specific module versions against the current Darktable source.
- **Task**: Ensure the "Parity Audit" step (Step 3) flags any deviations from the "Denoise-before-Sharpen" expert rule.
