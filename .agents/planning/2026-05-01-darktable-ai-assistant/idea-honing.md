# Requirements Clarification & Honing

## Established Requirements

### Core Workflow
- **Targeting**: CLI must support single files and glob patterns.
- **Platform**: macOS exclusive (utilizing `sips` and `darktable-cli`).
- **Token Frugality**: Use 2048px JPEG previews for vision analysis.
- **Interactivity**: The tool must be interactive, especially for high-complexity tasks like Denoise injection.

### AI Features
- **Aesthetic Auditor**: Analyze composition and technical quality (focus, etc.).
- **Variations**: Generate 3 distinct editing styles (Natural, Dramatic, Creative).
- **Tool Mapping**: Suggest specific Darktable modules to address identified issues.

### Automation (XMP Sidecars)
- **Non-destructive**: Only modify .xmp files.
- **Basic Modules**: Automated injection of Exposure, Temperature, and Color Balance.
- **Denoise (Challenge)**: Automated but interactive; ask user to "take a call" if complexity is high.

## Key Decisions
- **Language**: Python (Click for CLI, subprocess for system tools).
- **Intelligence**: Gemini CLI (Cloud Vision).
- **Automation Method**: Hex-encoded binary parameter injection for Darktable XMP modules.


## Clarification Questions

1. **Interactive Denoise Flow**: When the GenAI assistant identifies that an image needs denoising, but the camera-specific profile is missing or the parameters are ambiguous, how should the "take a call" interaction look to you? 

   *Options could include:*
   - A) The CLI shows a textual description of the noise and asks you to pick a preset (e.g., "Light", "Medium", "Heavy").
   - B) The CLI opens Darktable with a "best guess" applied and waits for you to confirm or adjust before proceeding with other edits.
   - C) The CLI provides the exact hex parameters it *would* use and asks for a Yes/No confirmation.

**Question 1: Interactive Denoise Flow**
Answer: B) Interactive Preview. The CLI will open Darktable with a "best guess" applied and wait for user confirmation/adjustment.

**Question 2: Aesthetic Commentary Delivery**

**Question 2: Aesthetic Commentary Delivery**
Answer: B) Sidecar Markdown File. Audit reports will be saved alongside the RAW images.

**Question 3: Representing Variations in Darktable**

**Question 3: Representing Variations in Darktable**
Answer: A) Duplicate Versions (Native). The tool will create multiple sidecar files (e.g., .xmp, .1.xmp, .2.xmp).

**Question 4: Handling Existing Edits**

**Question 4: Handling Existing Edits**
Answer: B) Branching. Original .xmp remains untouched; AI variations are added as new versions (.1.xmp, .2.xmp, etc.).

**Question 5: Technical Expertise Focus**

**Question 5: Technical Expertise Focus**
Answer: A) Subject-Background Balance (Primary). B) Dynamic Range and C) Color/Atmosphere (Secondary).

**Question 6: Success Criteria**

**Question 6: Success Criteria**
Answer: A) Minimal Manual Work and C) Aesthetic Inspiration.

**Question 7: Feedback Loop**

**Question 7: Feedback Loop**
Answer: B) One-off corrections only. Every image is a fresh start; adjustments are made manually in Darktable.

## Conclusion
The requirements clarification process has reached a natural conclusion. The project is defined as a macOS CLI tool using Gemini CLI to automate Darktable workflows via XMP sidecar manipulation, with a focus on wildlife/landscape expertise, side-by-side variations, and interactive validation for complex denoising.
