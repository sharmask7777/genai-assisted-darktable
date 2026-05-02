# Idea Honing: Re-enabling Rotation (Ashift v5)

## Question 1: Parameter Determination
The new `ashift` v5 structure requires focal length and crop factor to calculate the transformation correctly. How should these be determined?

### Options Considered:
*   **A: Metadata Extraction (Recommended):** Automatically extract focal length and crop factor from the image's EXIF data.
*   **B: Hardcoded Defaults:** Use standard defaults (e.g., 50mm, 1.0 crop) if metadata is missing.
*   **C: User Override:** Allow these to be passed as optional arguments to the `get_ashift_params` function.

### User Decision:
**A: Metadata Extraction with Override.** The system should automatically extract focal length and crop factor from the image's EXIF data (already part of the `genai-assisted-darktable` skill workflow), but allow these to be overridden via function arguments.

## Question 2: Default Values for Transformation Parameters
The `ashift` v5 structure includes several transformation parameters besides `rotation`. Should we provide a way to modify these, or should they remain at their defaults for now?

### Parameters in Scope:
*   `lensshift_v`, `lensshift_h` (Default: 0.0)
*   `shear` (Default: 0.0)
*   `aspect` (Default: 1.0)
*   `orthocorr` (Default: 100.0)

### User Decision:
**A: Rotation Only.** For now, only the `rotation` parameter will be exposed. All other transformation parameters will be set to their neutral defaults to simplify the fix and address the immediate error.

## Question 3: Automatic Cropping (Fitting)
The `ashift` module has a `cropmode` (or `fitting`) parameter that determines how the image is cropped after rotation. How should we handle this?

### Options Considered:
*   **A: Largest Area (Recommended):** Set the module to automatically crop to the largest possible rectangular area that fits within the rotated image. (This is usually what users want).
*   **B: Off:** Do not perform any automatic cropping. The user will have to manually adjust the crop in the `clipping` module.
*   **C: Match Existing Crop:** Try to preserve the existing crop settings if possible (though this is technically complex in `ashift`).

### User Decision:
**A: Largest Area.** The module will be configured to automatically crop to the largest possible rectangular area after rotation.

## Conclusion
The requirements for the `ashift` v5 fix are:
1.  **Binary Structure:** Implement the 892-byte `dt_iop_ashift_params_t` structure.
2.  **Parameters:** Expose `rotation`, `f_length`, and `crop_factor`.
3.  **Defaults:** 
    *   `lensshift_v`, `lensshift_h`, `shear` = 0.0
    *   `aspect`, `orthocorr` = 1.0 (or 100.0 for orthocorr)
    *   `mode` = 0 (Generic)
    *   `cropmode` = 1 (Largest Area)
    *   `cl`, `ct` = 0.0; `cr`, `cb` = 1.0
    *   All line-related fields (`last_drawn_lines`, etc.) = Zeroed out.
4.  **Metadata:** Integrate with the existing workflow to extract focal length and crop factor, but allow overrides.
5.  **Encoding:** Use Zlib compression and Base64 encoding with the `gz16` prefix.
