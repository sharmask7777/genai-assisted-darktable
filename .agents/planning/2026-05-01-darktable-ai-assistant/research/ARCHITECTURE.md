# Architecture: Vision-to-XMP Pipeline

## Data Flow
1. **Input:** User provides RAW file path via CLI.
2. **Preprocessing:** `sips` extracts a 2048px JPEG preview.
3. **Analysis:** Gemini CLI processes the JPEG + a "Photography Expert" prompt.
4. **Output Generation:** Gemini returns JSON containing:
   - Aesthetic audit text.
   - 3 variation profiles (Module Name, Parameter Intent).
5. **XMP Construction:** CLI script maps Intent -> Hex Params and writes/updates `.xmp` files.

## Module Mapping (v1)
- **exposure:** exposure (EV), black level.
- **temperature:** Kelvin, green/magenta tint.
- **colorbalance:** saturation, contrast.
- **denoiseprofile:** (Advice-only in v1 due to cam-profile complexity).
