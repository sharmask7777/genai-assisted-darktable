# Roadmap: Darktable GenAI Assistant Enhancements

## Phases
- [ ] **Phase 1: Intelligent Composition (Cropping)** - Implement crop analysis and selection logic in `dt-ai` and `SKILL.md`.
- [ ] **Phase 2: Advanced Technical Modules** - Implement `diffuse or sharpen` and `clipping` binary XMP injection.
- [ ] **Phase 3: Expert Knowledge & Mentorship** - Refine the AI prompt with research-backed rules and technical rationale.

## Phase Details

### Phase 1: Intelligent Composition (Cropping)
**Goal**: Users can select from 3 AI-suggested crops before proceeding to edits.
**Requirements**: CROP-01, CROP-02
**Success Criteria**:
1. `dt-ai agent-next` outputs 3 crop variants with coordinates.
2. `SKILL.md` implements a pause for user selection of the preferred crop.

### Phase 2: Advanced Technical Modules
**Goal**: Support professional detail and noise management via `diffuse or sharpen`.
**Requirements**: CROP-03, MOD-01, MOD-02
**Success Criteria**:
1. XMP files correctly include the `clipping` (cropping) module.
2. XMP files correctly include `diffuse or sharpen` with valid binary-packed parameters.
3. Hardware-aware noise offsets are applied automatically.

### Phase 3: Expert Knowledge & Mentorship
**Goal**: The AI explains "why" it chose specific detail settings based on sensor physics and domain research.
**Requirements**: KB-01, KB-02
**Success Criteria**:
1. `AESTHETIC_PROMPT` includes logic for "denoise before sharpen" and subject-specific detail rules.
2. Mentor reports include rationale for the chosen detail workflow.
