# Long Telephoto (500mm-600mm) Wildlife Expert Rules

Specialized techniques for handling diffraction, atmospheric haze, and dynamic range in long-lens wildlife photography using the 2026 Darktable workflow.

## 1. Baseline Detail (Demosaic)
- **Capture Sharpening**: ALWAYS enable this in the demosaic module. At 500mm+, it's the cleanest way to address sensor-level blur and diffraction without adding noise artifacts.

## 2. Tone Mapping (AgX)
- **Exposure for Subject**: AgX handles high dynamic range beautifully. Push your **Exposure** until the subject's midtones are perfect, then let AgX manage the highlight roll-off in the background.
- **Slope & Lift**: Use these within the AgX module to balance the "pop" of the subject against the forest backdrop.

## 3. Surgical Detail (Diffuse or Sharpen)
- **Masked Lens Deblur**: Use the "lens deblur: medium" preset early in the pipeline, but apply it using a **drawn & parametric mask** only on the subject.
- **Atmospheric Dehaze**: Long lenses are prone to haze. Use a second instance of Diffuse or Sharpen with a subtle "dehaze" setting to restore clarity.

## 4. Color & Contrast
- **Tone Equalizer**: Use this for surgical shadow recovery (e.g., under a bird's belly or a mammal's fur) where a global exposure boost might wash out the rest of the scene.
- **Purity Boost**: Use a 10-15% purity boost in the AgX primaries tab to maintain the saturation of natural plumage and forest greens.

## 5. Processing Order
1. Denoise (Profiled)
2. Exposure & AgX
3. Demosaic (Enable Capture Sharpening)
4. Diffuse or Sharpen (Lens Deblur) - Masked
5. Tone Equalizer (Shadow Recovery)
