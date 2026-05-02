# General Jungle Wildlife Expert Rules

Best practices for handling the dense canopy light and diverse wildlife of jungle/forest environments using the 2026 Darktable workflow.

## 1. Light & Tone Mapping (AgX)
- **Canopy Light**: Forest light is often dappled or heavily filtered. Use **AgX** to handle the high-contrast "hot spots" where sun hits the subject.
- **Pivot Point**: Set the AgX pivot directly on the subject's midtones (fur/feathers) to ensure they are the focus of the dynamic range.
- **Purity Boost**: AgX can desaturate highlights. Use a 10-15% **purity boost** in the primaries tab to maintain the "lushness" of the forest greens.

## 2. Detail Management (Diffuse or Sharpen)
- **Base Sharpening**: Use **demosaic sharpening** (within the demosaic module) for baseline sensor deblur. It's cleaner for high ISO wildlife.
- **Subject Acutance**: Apply a "local contrast" instance of **diffuse or sharpen**, but ONLY masked to the subject. This makes the animal "pop" from the busy forest background.
- **Lens Deblur**: For long telephotos (like 600mm), use "lens deblur: medium" early in the pipe (before the input color profile).

## 3. Color Strategy
- **Jungle Greens**: Use **Color Balance RGB** to ensure the forest background doesn't shift towards yellow. A slight push towards cyan/blue in the shadows can add depth to the foliage.
- **Natural Saturation**: Use **Color Calibration** for your base colors before applying AgX.

## 4. Processing Order
1. Denoise (Profiled) - Wavelets mode.
2. Exposure & AgX.
3. Diffuse or Sharpen (Lens Deblur).
4. Diffuse or Sharpen (Local Contrast) - Masked.
5. Color Balance RGB - Grading.
