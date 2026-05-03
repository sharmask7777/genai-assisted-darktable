# Indian Wildlife Editing (High ISO focus)

## Overview
Wildlife photography in Indian parks like Nagarhole often occurs in low light (dawn/dusk) or dense canopy, necessitating high ISO settings (3200+). The challenge is balancing noise reduction with the preservation of fine textures (fur, feathers).

## Technical Strategy

### 1. Denoising First
- **Module**: `denoise (profiled)`
- **Setting**: Use 'wavelets' or 'non-local means'.
- **Rationale**: Profiling ensures noise is handled based on your camera's specific sensor characteristics at ISO 3200.

### 2. Surgical Detail with `diffuse or sharpen`
- **Denoise (Post-filter)**: Use the module with positive diffusion on the 4th order. This is excellent for cleaning up residual grain in out-of-focus areas (bokeh) while keeping the subject's fur/feathers crisp.
- **Sharpening**: Apply the 'lens deblur' or 'sharpen: demosaicing' preset. 
- **Edge Protection**: Increase 'edge sensitivity' and 'edge threshold' to avoid halos around high-contrast edges (e.g., a leopard's spots or a bird's silhouette).

### 3. Tonal Balance with AgX
- **Highlight Safety**: AgX prevents hue shifts in highlights. This is critical for animals with white or bright fur in sunlight.
- **Contrast**: Keep contrast moderate (1.1 - 1.3) to maintain a natural "safari" look.

## Pro Tips
- **1:1 Evaluation**: Always check your results at 100% zoom.
- **Don't Over-sanitize**: A little grain is better than "plastic" looking fur.
- **Bokeh Protection**: Use masks if the background starts looking "crunchy" from sharpening.
