# Initial Knowledge Base Research

This document bootstraps the `.agents/knowledge-base/` tree with expert information gathered during the research phase.

## 1. Core Workflow (2026 Scene-Referred)
The standard is centered on the **AgX** tone mapper and early-pipeline technical fixes.

- **Sequence**: Lens Correction -> Chromatic Aberrations -> Denoise (profiled) -> Capture Sharpen -> Exposure -> Color Calibration -> AgX.
- **Denoising**: Use **Wavelets** in **Y0U0V0** mode. Focus on Chroma noise first.
- **Sharpening**: Use **Capture Sharpen** (in Demosaic module) for baseline detail. Use **Diffuse or Sharpen** for surgical enhancement with masks.

## 2. Subject-Specific leaf Nodes

### Wildlife (`wildlife.md`)
- **Key Modules**: AgX + Demosaic (Capture Sharpen).
- **Pro Tip**: Use AgX Pivot on the animal to make it pop against backgrounds.
- **Sharpening**: Apply Diffuse or Sharpen (lens deblur preset) only to the subject (eyes/fur) using drawn masks.

### Landscape (`landscape.md`)
- **Key Modules**: AgX + Diffuse or Sharpen (Dehaze).
- **Pro Tip**: Use AgX Shoulder Power to save delicate cloud details and sunset highlights.
- **Sharpening**: Use a second instance of Diffuse or Sharpen for distant features.

### Macro (`macro.md`)
- **Key Modules**: AgX + Contrast Equalizer.
- **Pro Tip**: AgX handles extreme floral saturations better than legacy modules.
- **Detail**: Use Contrast Equalizer (Clarity preset) for insect carapaces.

## 3. Runtime Detection Pattern
The agent should scan for tools like `google_web_search`, `web_fetch`, or platform-specific discovery tools (e.g., `tool_search_tool`) to determine its research capabilities.
