# Context: 07-develop-aesthetic-prompt

## Requirements
1. Define `AESTHETIC_PROMPT` in `dt_ai/ai.py`.
2. Expert Photographer persona focusing on Wildlife and Landscapes.
3. Analyze:
   - Composition (Rule of thirds, distractions).
   - Technicals (Focus/Sharpness, Highlights/Shadows, Noise).
   - Genre detection.
4. Recommend specific Darktable modules:
   - Exposure, Denoise (profiled), Diffuse or Sharpen, Color Balance RGB, Tone Equalizer.
5. Format output as structured Markdown for sidecar reports.

## Reference Research
- **Wildlife**: Focus on eye sharpness, background separation.
- **Landscape**: Focus on dynamic range, color temperature.

## Implementation Paths
- `dt_ai/ai.py`: Adding the constant prompt string.
