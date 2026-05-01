# Implementation Plan: Darktable GenAI Assistant

## Progress Checklist
- [ ] Step 1: Project Environment & CLI Harness
- [ ] Step 2: Image Preview Extraction Pipeline
- [ ] Step 3: Aesthetic Auditor (AI Integration)
- [ ] Step 4: XMP Versioning & Sidecar Creation (Verified with ~/Pictures)
- [ ] Step 5: Automated Parameter Injection (Exposure & Color)
- [ ] Step 6: Interactive Denoise & Multi-Variation Flow

## Implementation Steps

### Step 1: Project Environment & CLI Harness
**Objective:** Set up the Python environment and a basic CLI that can discover target RAW files.
- **Guidance:** Initialize with `uv`. Use `click` to create a command-line interface. Implement file discovery logic using `pathlib` that supports single files and folder-based globbing.
- **Test Requirements:** Unit tests for the file discovery logic (mocking a file system).
- **Integration:** Initial setup; no previous work.
- **Demo:** Run `dt-ai audit . --dry-run` and see a list of discovered RAW files in the terminal.

### Step 2: Image Preview Extraction Pipeline
**Objective:** Implement the `sips`-based extraction of JPEG previews.
- **Guidance:** Create a `processor.py` module. Use `subprocess` to call macOS `sips`. Constrain output to 2048px on the longest edge. Store previews in a hidden `.dt-ai/previews` directory.
- **Test Requirements:** Verify `sips` command string generation. Ensure temporary directory management works.
- **Integration:** Integrates with the `audit` command from Step 1.
- **Demo:** Run the CLI and verify that a 2048px JPEG is generated for every discovered RAW file.

### Step 3: Aesthetic Auditor (AI Integration)
**Objective:** Connect the pipeline to Gemini CLI and generate Markdown audit reports.
- **Guidance:** Use the `gemini-cli` to send extracted JPEGs for analysis. Implement a robust system prompt for aesthetic auditing. Write the resulting AI commentary to `<basename>_audit.md` next to the RAW file.
- **Test Requirements:** Mock Gemini CLI response to test the Markdown file generation and content formatting.
- **Integration:** Follows the extraction step in the `audit` workflow.
- **Demo:** Run the CLI and see a Markdown audit report generated for a target image, containing AI-driven aesthetic feedback.

### Step 4: XMP Versioning & Sidecar Creation
**Objective:** Implement the logic for creating Darktable duplicate versions via sidecars.
- **Guidance:** Build the `xmp.py` module. Implement the `_nn.xmp` naming convention. Ensure `internal_version` and `history_end` tags are correctly initialized in the XML structure. Implement the "Branching" strategy to preserve existing edits.
- **Test Requirements:** Verify XML structure generation using `xml.etree.ElementTree`. Confirm file naming logic for duplicates.
- **Integration:** Adds the foundation for the `edit` command.
- **Demo:** Run `dt-ai edit <file>` and see empty duplicate sidecars (e.g., `_01.xmp`) appear in the filesystem, which Darktable recognizes as new versions.

### Step 5: Automated Parameter Injection (Exposure & Color)
**Objective:** Automate the injection of basic editing modules using hex-encoded parameters.
- **Guidance:** Implement hex-encoding for `exposure` and `temperature` modules. Map AI-recommended values (EV, Kelvin) to the correct binary structs. Inject these into the generated XMP files.
- **Test Requirements:** Unit tests for the float-to-hex conversion logic for Darktable modules.
- **Integration:** Enhances the duplicate sidecars created in Step 4 with actual AI-driven edits.
- **Demo:** Open Darktable after running the tool and see the "Natural" version of a photo with AI-applied exposure and color adjustments.

### Step 6: Interactive Denoise & Multi-Variation Flow
**Objective:** Implement the "Interactive Denoise" challenge and generate three distinct style variations.
- **Guidance:** Implement the logic for 3 variations (Natural, Dramatic, Creative). Integrate the macOS `open` command to focus the Darktable GUI for interactive denoising. Add the CLI pause/prompt loop for user validation.
- **Test Requirements:** Verify the logic for generating three distinct XMP files. Mock the GUI handoff to test the interaction loop.
- **Integration:** Finalizes the `edit` command with full multi-variation support and the interactive "take a call" gate.
- **Demo:** Run `dt-ai edit <file>`. The tool generates three styles and pauses to open Darktable for you to validate the denoise settings before finishing.
