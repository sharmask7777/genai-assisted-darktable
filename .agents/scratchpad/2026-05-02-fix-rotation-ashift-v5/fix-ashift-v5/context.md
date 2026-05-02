# Context: Re-enabling Rotation (Ashift v5)

## Existing Documentation
- **Rough Idea:** `.agents/planning/2026-05-02-fix-rotation-ashift-v5/rough-idea.md`
- **Idea Honing:** `.agents/planning/2026-05-02-fix-rotation-ashift-v5/idea-honing.md`
- **Detailed Design:** `.agents/planning/2026-05-02-fix-rotation-ashift-v5/design/detailed-design.md`
- **Implementation Plan:** `.agents/planning/2026-05-02-fix-rotation-ashift-v5/implementation/plan.md`

## Project Structure
- `dt_ai/xmp.py`: Contains the logic for generating XMP and module parameters.
- `tests/test_xmp_structs.py`: Existing tests for XMP parameter structures.
- `sample_rotation.xmp`: Working sample from Darktable 2026.

## Requirements
1. Implement 892-byte `dt_iop_ashift_params_t` struct.
2. Expose `rotation`, `f_length`, and `crop_factor`.
3. Use `zlib` compression + Base64 encoding with `gz16` prefix.
4. Default `cropmode` to 1 (Largest Area).
5. Integrate with EXIF metadata in the workflow.

## Patterns and Dependencies
- **Pattern:** Binary struct packing with `struct`.
- **Pattern:** XMP generation with `xml.etree.ElementTree`.
- **Dependency:** `zlib` for compression.
- **Dependency:** `base64` for encoding.

## Implementation Paths
- `dt_ai/xmp.py`: Update `get_ashift_params`.
- `tests/test_xmp_structs.py`: Add TDD tests.
