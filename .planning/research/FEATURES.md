# Feature Landscape

**Domain:** Professional photography editing using Darktable's scene-referred workflow.
**Researched:** 2026-05-02

## Table Stakes

Features users expect in a 2026 AI-assisted RAW editor.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| RAW Discovery | Foundation for any RAW workflow. | Low | Must support common formats (ARW, CR3, DNG). |
| Scene-Referred Pipeline | Essential for modern high-dynamic-range editing. | Medium | Use Exposure -> Color Calibration -> AgX/Sigmoid. |
| XMP Sidecar Support | Non-destructive editing standard. | Medium | Must handle Darktable's multi-instance and history stack. |
| Basic Exposure/Color AI | Table stakes for "AI" assistant. | Medium | Auto-exposure and white balance based on image content. |

## Differentiators

Features that set this GenAI assistant apart.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Intelligent Cropping | Provides expert composition suggestions before editing. | High | Uses Multimodal LLM to analyze "intent" and "storytelling." |
| Diffuse or Sharpen AI | Automates the most complex Darktable module for noise/detail. | High | Translates AI intent (e.g., "deblur") into PDE parameters. |
| AgX Integration | Leverages the latest 2026 color science (AgX) by default. | Medium | Avoids hue shifts in highlights automatically. |
| Two-Stage Workflow | Separates composition from aesthetics for better focus. | Low | User selects crop first, then AI refines colors for that frame. |

## Anti-Features

Features to explicitly NOT build.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| Built-in RAW Rendering | Extremely complex and redundant. | Use `darktable-cli` or `sips` for previews. |
| Custom Image Browser | Massive scope creep; competing with Adobe Bridge/PhotoMechanic. | Rely on existing filesystem or Darktable lighttable. |
| Local AI Model Hosting | High hardware requirements and maintenance. | Use cloud-based Multimodal APIs (Gemini) for high-level reasoning. |

## Feature Dependencies

```
RAW Discovery → Preview Extraction → Intelligent Cropping
Intelligent Cropping → User Selection → Aesthetic Variation Generation
Aesthetic Variation Generation → XMP Injection (AgX + Diffuse or Sharpen)
XMP Injection → Final Export (darktable-cli)
```

## MVP Recommendation

Prioritize:
1. **Intelligent Cropping (CROP-01/02)**: Use Gemini to suggest 3 crops.
2. **Diffuse or Sharpen Integration (MOD-01)**: Support basic "noise reduction" and "sharpening" presets via XMP.
3. **AgX Workflow**: Ensure all generated XMPs use AgX as the display transform.

Defer: **Generative Expand**: Wait until base cropping and editing are stable.

## Sources

- [Darktable Feature List](https://www.darktable.org/about/features/)
- [Professional Photography Workflow Trends 2026](https://pixls.us/articles/)
- [Project Requirements (.planning/PROJECT.md)](/Users/shaleensharma/workplace/gemini_ws/photo-editting/.planning/PROJECT.md)
