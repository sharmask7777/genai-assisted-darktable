# Requirements: Darktable GenAI Assistant (Enhanced Editing & Cropping)

## v1 Requirements

### Core Infrastructure (Table Stakes)
- [ ] **CORE-01**: Discover RAW files (ARW, CR3, DNG) in target directories and manage session state via `.dt-ai-state.json`.
- [ ] **CORE-02**: Extract high-quality JPEG previews using macOS `sips` for AI analysis.
- [ ] **CORE-03**: Support non-destructive editing via Darktable XMP sidecar files, managing multi-instance history stacks.
- [ ] **CORE-04**: Enforce a modern scene-referred pipeline (Exposure -> Color Calibration -> AgX/Sigmoid) in all generated variations.

### Intelligent Cropping
- [ ] **CROP-01**: Use Multimodal AI (Gemini) to analyze image composition and suggest up to three distinct crops (e.g., Rule of Thirds, Cinematic, Tight Subject).
- [ ] **CROP-02**: Implement a CLI-based selection step where the user chooses a crop before aesthetic edits are generated.
- [ ] **CROP-03**: Ensure crop coordinates are correctly translated to Darktable's XMP `crop` module parameters.

### Advanced Detail & Noise (Diffuse or Sharpen)
- [ ] **MOD-01**: Integrate the `diffuse or sharpen` module into the XMP engine, translating AI intent ("deblur", "sharpen", "denoise") into binary-encoded parameters.
- [ ] **MOD-02**: Apply hardware-aware sensor corrections (black-point offsets, ISO-specific noise handling) automatically during XMP generation.

### Knowledge & Mentorship
- [ ] **KB-01**: Research and encode expert best practices for `diffuse or sharpen` and `denoise (profiled)` modules into the AI's internal knowledge base or system prompt.
- [ ] **KB-02**: Generate a "Mentor Report" for each image explaining the rationale behind the chosen crop and technical settings.

## v2 Requirements
- [ ] **BATCH-01**: Support parallel batch processing with token-aware rate limiting.
- [ ] **EXT-01**: Integration with `darktable-cli` for automated high-quality JPEG export of all variations.
- [ ] **GEN-01**: Support "Generative Expand" logic via external tools (out of scope for core dt-ai but planned for v2).

## Out of Scope
- **GUI-01**: Building a custom graphical image browser or photo culling interface.
- **RENDER-01**: Implementing a custom RAW rendering engine (rely on `sips` or `darktable-cli`).
- **LOCAL-01**: Hosting vision models locally (primary intelligence remains cloud-based Multimodal APIs).

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CORE-01 | Phase 1 | Pending |
| CORE-02 | Phase 1 | Pending |
| CORE-03 | Phase 3 | Pending |
| CORE-04 | Phase 3 | Pending |
| CROP-01 | Phase 2 | Pending |
| CROP-02 | Phase 2 | Pending |
| CROP-03 | Phase 2 | Pending |
| MOD-01 | Phase 3 | Pending |
| MOD-02 | Phase 3 | Pending |
| KB-01 | Phase 4 | Pending |
| KB-02 | Phase 4 | Pending |
