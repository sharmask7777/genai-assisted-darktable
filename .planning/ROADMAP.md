# Project Roadmap: Darktable GenAI Assistant

## Phase 1: Scaffold (CLI & Extraction)
**Goal:** Build the foundational CLI and RAW preview pipeline.
- [ ] **CLI-BASE**: Implement argument parsing for file targets.
- [ ] **PREVIEW-EXTRACT**: Integrate `sips` to generate 2048px JPEG previews.
- **Success Criteria:** Running `dt-ai --file image.ARW` produces a temporary JPEG preview.

## Phase 2: Auditor (Intelligence & Interactivity)
**Goal:** Connect to Gemini for aesthetic analysis and tool advice.
- [ ] **AI-CONFIG**: Configure Gemini CLI integration and system prompts.
- [ ] **AUDIT-FLOW**: Implement the "Aesthetic Audit" output (Dry-run mode).
- [ ] **INTERACTIVE-GATES**: Implement the base interactive loop for user validation.
- **Success Criteria:** Tool outputs a text-based critique and recommended Darktable modules.

## Phase 3: Basic Edit (XMP Automation)
**Goal:** Write basic processing modules to Darktable sidecars.
- [ ] **XMP-SKELETON**: Create logic to generate/parse .xmp files.
- [ ] **VAR-GEN**: Implement logic for 3 variations (Natural/Dramatic/Creative).
- [ ] **BASIC-INJECT**: Automate Exposure and Color Balance hex-injection.
- **Success Criteria:** Darktable opens the image with AI-applied exposure and color variations.

## Phase 4: Denoise (The Challenge)
**Goal:** Implement automated, interactive denoising.
- [ ] **DENOISE-RESEARCH**: Map camera-specific noise profile hex structures.
- [ ] **DENOISE-INJECT**: Implement the interactive Denoise automation with user "Take a call" gates.
- **Success Criteria:** Tool successfully applies denoising or gracefully defers to user after interaction.
