# Niche: White Birds & High-Key Wildlife (2026 Standards)

## Core Workflow
The primary challenge with white birds (Flycatchers, Egrets, Swans) is maintaining tactile texture in near-clipped highlights while keeping the whites "brilliant" rather than muddy.

### 1. The AgX "Path to White"
*   **AgX Primaries:** Use the Primaries tab to ensure that as feathers approach peak brightness, they desaturate gracefully. This avoids the yellow/cyan shifts often seen in older workflows.
*   **Brilliance:** Set the AgX white point to preserve "pop," but use the "toe power" (0.1) to ensure the shadow-side of the feathers has enough depth to look 3D.

### 2. Texture Reconstruction (Highlight Reconstruction)
*   **Guided Laplacians:** Mandatory for white plumage. It uses the same math as "Diffuse or Sharpen" to reconstruct the *structure* of feathers in areas that are nearly blown out.
*   **Iterations:** Increase to 3-5 to propagate detail into bright spots.

### 3. Surgical Detail (Diffuse or Sharpen)
*   **Capture Sharpening:** Apply early in the pipeline (before input color profile) for a clean base.
*   **Plumage Pop:** Use "lens deblur: hard" at low opacity (15-20%) on a drawn mask over the bird. This brings out the "layering" of the wings and tail.
*   **Parametric Masking:** Use an 'L' (Lightness) mask to target sharpening *only* to the bright feathers, leaving the background bokeh smooth and noise-free.

### 4. Color Calibration
*   For white birds in the jungle, slightly cool the whites to counteract "green bounce" from the surrounding foliage, making the bird appear cleaner and more focused.
