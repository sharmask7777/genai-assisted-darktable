# Requirements: Darktable GenAI Assistant (Enhanced Editing & Cropping)

## v1 Requirements (New Enhancements)

### Intelligent Cropping
- [ ] **CROP-01**: Enhance `dt-ai agent-next` to include a composition analysis phase where Gemini suggests up to 3 crops (coordinates and rationale).
- [ ] **CROP-02**: Update `SKILL.md` to implement the "Selection Step": User picks a crop via CLI before aesthetic edits are generated.
- [ ] **CROP-03**: Implement `clipping` module support in `xmp.py` to translate AI coordinates into Darktable-compatible hex parameters.

### Advanced Detail & Noise (Diffuse or Sharpen)
- [ ] **MOD-01**: Implement the `diffuse or sharpen` module in `xmp.py`, specifically handling the binary packing of its PDE-based parameters (deblur, denoise, sharpen).
- [ ] **MOD-02**: Integrate hardware-aware noise presets for common sensors (e.g., Sony A7III, Canon R5) based on the existing `SENSOR_DATABASE`.

### Knowledge Base Integration
- [ ] **KB-01**: Conduct research on Darktable's scene-referred detail modules and encode "expert rules" (e.g., "denoise before diffuse") into the `AESTHETIC_PROMPT` in `ai.py`.
- [ ] **KB-02**: Update `SKILL.md` to provide mentorship on *why* specific detail modules were chosen (noise management vs. structural sharpening).

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CROP-01 | Phase 1 | Pending |
| CROP-02 | Phase 1 | Pending |
| CROP-03 | Phase 2 | Pending |
| MOD-01 | Phase 2 | Pending |
| MOD-02 | Phase 2 | Pending |
| KB-01 | Phase 3 | Pending |
| KB-02 | Phase 3 | Pending |
