# Niche: Mammals & Fur Texture (2026 Standards)

## Core Workflow
For mammals (Tigers, Leopards, Deer), the primary challenge is preserving the "softness" of fur while bringing out the "bite" of individual hairs and whiskers.

### 1. The AgX Foundation
*   **AgX Contrast:** Set between 1.4 and 1.6 for jungle subjects.
*   **Toe Power:** Slightly increase (0.1 - 0.2) to add depth to shadow regions in fur, preventing a flat look.

### 2. Surgical Sharpening (Diffuse or Sharpen)
*   **Iterations over Amount:** Instead of a high amount, use 10-20 iterations of "lens deblur: medium".
*   **Edge Management:** Increase the "Edge Threshold" to avoid halos around whiskers or fine hair against bright backgrounds.
*   **Radius Span:** Keep low (2-4px) for fine fur.

### 3. Micro-Detail (Contrast Equalizer)
*   Use the "clarity" preset, but raise the fine-scale (left side) of the Luma tab to target individual hairs. Avoid raising the coarse-scale to keep the transition to bokeh smooth.

### 4. Color Calibration
*   For Indian jungle environments, ensure the "greens" are calibrated so they don't overpower the warm tones of the animal's coat.
