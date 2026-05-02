# Roadmap: Enhancer

## Phases

- [ ] **Phase 1: Foundation & Workflow Enforcement** - Secure the AgX-first workflow by default.
- [ ] **Phase 2: Metadata & Interactive Resilience** - Ensure the system has reliable EXIF data via interactive fallback.
- [ ] **Phase 3: Hardware-Specific Corrections** - Apply technical fixes for sensor-specific color casts and black points.
- [ ] **Phase 4: Scene-Referred Pipeline (AgX)** - Implement mid-gray normalization and core AgX/Sigmoid logic.
- [ ] **Phase 5: High-Saturation Color Science** - Eliminate color shifts in highlights using primary rotation tuning.
- [ ] **Phase 6: Pre-flight Reporter** - Generate a terminal summary of changes before they are applied.
- [ ] **Phase 7: Technical Mentorship** - Explain the technical "why" behind module choices and provide educational snippets.
- [ ] **Phase 8: Subject Intelligence** - Use vision analysis to classify subjects and select editing strategies.
- [ ] **Phase 9: Knowledge Retrieval (RAG)** - Enrich edits with subject-specific research from photography sources.
- [ ] **Phase 10: Artistic Style Synthesis** - Provide 'Natural' vs 'Dramatic' variations informed by research.

## Phase Details

### Phase 1: Foundation & Workflow Enforcement
**Goal**: Secure the AgX-first workflow by default.
**Depends on**: Nothing
**Requirements**: AGX-01
**Success Criteria**:
  1. System automatically disables Filmic RGB and Base Curve in the generated XMP history.
  2. System ensures Color Calibration is enabled by default for all processed images.
**Plans**: TBD

### Phase 2: Metadata & Interactive Resilience
**Goal**: Ensure the system has reliable EXIF data via interactive fallback.
**Depends on**: Phase 1
**Requirements**: FIX-03
**Success Criteria**:
  1. CLI prompts the user for missing essential metadata (Camera, Lens) when EXIF is missing.
  2. System successfully processes images using manually provided metadata.
**Plans**: TBD

### Phase 3: Hardware-Specific Corrections
**Goal**: Apply technical fixes for sensor-specific color casts and black points.
**Depends on**: Phase 2
**Requirements**: FIX-01, FIX-02
**Success Criteria**:
  1. Sensor-specific color casts (green/red shifts) are detected and corrected using lens profiles.
  2. Black point mismatches for known camera models are normalized in the shadows.
**Plans**: TBD

### Phase 4: Scene-Referred Pipeline (AgX)
**Goal**: Implement mid-gray normalization and core AgX/Sigmoid logic.
**Depends on**: Phase 3
**Requirements**: AGX-02
**Success Criteria**:
  1. 18% mid-gray exposure normalization is calculated and applied before tone mapping.
  2. Sigmoid/AgX parameters are tuned to provide a consistent base exposure.
**Plans**: TBD

### Phase 5: High-Saturation Color Science
**Goal**: Eliminate color shifts in highlights using primary rotation tuning.
**Depends on**: Phase 4
**Requirements**: AGX-03
**Success Criteria**:
  1. Primary rotation tuning is applied to mitigate the 'Notorious 6' highlight color issues.
  2. High-saturation highlights maintain color constancy during roll-off.
**Plans**: TBD

### Phase 6: Pre-flight Reporter
**Goal**: Generate a terminal summary of changes before they are applied.
**Depends on**: Phase 5
**Requirements**: EDU-01
**Success Criteria**:
  1. System outputs a readable "Pre-flight Review" in the terminal.
  2. Changes are only committed to the XMP after the user has a chance to review the report.
**Plans**: TBD

### Phase 7: Technical Mentorship
**Goal**: Explain the technical "why" behind module choices and provide educational snippets.
**Depends on**: Phase 6
**Requirements**: EDU-02, EDU-03
**Success Criteria**:
  1. Report explicitly links module choices (e.g., Denoise) to specific metadata (e.g., High ISO).
  2. Users see educational snippets explaining Sigmoid and Color Calibration benefits.
**Plans**: TBD

### Phase 8: Subject Intelligence
**Goal**: Use vision analysis to classify subjects and select editing strategies.
**Depends on**: Phase 7
**Requirements**: RES-01
**Success Criteria**:
  1. Vision analysis correctly identifies common subjects (Wildlife, Landscape, Portrait).
  2. System automatically switches to a subject-specific editing baseline based on classification.
**Plans**: TBD

### Phase 9: Knowledge Retrieval (RAG)
**Goal**: Enrich edits with subject-specific research from photography sources.
**Depends on**: Phase 8
**Requirements**: RES-02
**Success Criteria**:
  1. System retrieves relevant best practices from Pixls.us or official docs for the detected subject.
  2. Artistic parameters (contrast, saturation) are informed by the retrieved knowledge.
**Plans**: TBD

### Phase 10: Artistic Style Synthesis
**Goal**: Provide 'Natural' vs 'Dramatic' variations informed by research.
**Depends on**: Phase 9
**Requirements**: RES-03
**Success Criteria**:
  1. System generates at least two distinct artistic variations for every image.
  2. Variations demonstrate clear differences in artistic intent (Natural vs Dramatic).
**Plans**: TBD

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation & Workflow Enforcement | 0/1 | Not started | - |
| 2. Metadata & Interactive Resilience | 0/1 | Not started | - |
| 3. Hardware-Specific Corrections | 0/1 | Not started | - |
| 4. Scene-Referred Pipeline (AgX) | 0/1 | Not started | - |
| 5. High-Saturation Color Science | 0/1 | Not started | - |
| 6. Pre-flight Reporter | 0/1 | Not started | - |
| 7. Technical Mentorship | 0/1 | Not started | - |
| 8. Subject Intelligence | 0/1 | Not started | - |
| 9. Knowledge Retrieval (RAG) | 0/1 | Not started | - |
| 10. Artistic Style Synthesis | 0/1 | Not started | - |
