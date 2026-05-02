# Roadmap: Darktable GenAI Assistant (Enhanced Editing & Cropping)

## Phases

- [ ] **Phase 1: Foundation** - Core discovery, preview extraction, and session state management.
- [ ] **Phase 2: Composition** - Intelligent cropping suggestions and CLI selection logic.
- [ ] **Phase 3: Aesthetic Engine** - XMP injection, scene-referred pipeline, and advanced detail modules.
- [ ] **Phase 4: Knowledge & Mentorship** - Expert rule encoding and rationale reporting.

## Phase Details

### Phase 1: Foundation
**Goal**: Establish the base infrastructure for finding RAW files and persisting session state.
**Depends on**: Nothing
**Requirements**: CORE-01, CORE-02
**Success Criteria**:
  1. User can point the tool at a directory and see a list of discovered RAW files.
  2. System generates and updates `.dt-ai-state.json` to track progress across sessions.
  3. High-quality JPEG previews are extracted using macOS `sips` for each discovered RAW.
**Plans**: TBD

### Phase 2: Composition
**Goal**: Enable intelligent AI-driven cropping as a mandatory first creative step.
**Depends on**: Phase 1
**Requirements**: CROP-01, CROP-02, CROP-03
**Success Criteria**:
  1. AI analyzes RAW previews and suggests up to three distinct, valid crop variations.
  2. User can choose a crop variation through an interactive CLI prompt.
  3. Chosen crop coordinates are correctly translated and written to a Darktable XMP sidecar.
**Plans**: TBD
**UI hint**: yes

### Phase 3: Aesthetic Engine
**Goal**: Implement the core editing pipeline using expert scene-referred modules and XMP injection.
**Depends on**: Phase 2
**Requirements**: CORE-03, CORE-04, MOD-01, MOD-02
**Success Criteria**:
  1. System generates multiple non-destructive XMP variations for a single RAW.
  2. Modern scene-referred pipeline (Exposure, Color Calibration, AgX) is applied by default.
  3. `diffuse or sharpen` module parameters are successfully injected based on AI-detected image needs (sharpening/noise).
  4. Hardware-aware corrections (ISO/black-point) are applied during the XMP generation process.
**Plans**: TBD

### Phase 4: Knowledge & Mentorship
**Goal**: Finalize the "Expert-in-a-Box" experience with technical reports and refined rules.
**Depends on**: Phase 3
**Requirements**: KB-01, KB-02
**Success Criteria**:
  1. System generates a "Mentor Report" explaining the artistic and technical rationale for each edit.
  2. Advanced `diffuse or sharpen` presets (deblur vs. denoise) adhere to refined expert best practices encoded in the knowledge base.
**Plans**: TBD

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 0/1 | Not started | - |
| 2. Composition | 0/1 | Not started | - |
| 3. Aesthetic Engine | 0/1 | Not started | - |
| 4. Knowledge & Mentorship | 0/1 | Not started | - |
