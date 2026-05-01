# Task: Generate Markdown Audit Reports

## Description
Implement the logic to save the AI's analysis into a permanent Markdown sidecar file alongside the original RAW image. Update the CLI to display these reports.

## Background
Users need a way to review the AI's "expertise" without opening the CLI every time. Sidecar Markdown files (`IMG_1234_audit.md`) provide a persistent record of the AI's advice.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Update `dt_ai/main.py` to call the AI analysis logic.
2. Implement a function to save the AI response to `<basename>_audit.md` in the same directory as the RAW file.
3. Ensure the tool doesn't crash if it can't write the audit file (e.g., read-only drive).
4. Print the location of the generated audit file to the CLI output.

## Dependencies
- AI Integration (Tasks 3-01, 3-02).
- CLI Harness (Step 1).

## Implementation Approach
1. Integrate the `analyze_image` call into the `audit` command loop.
2. Add file-writing logic to save the Markdown report.

## Acceptance Criteria

1. **Sidecar Creation**
   - Given a RAW file `bird.ARW`
   - When `dt-ai audit bird.ARW` is run
   - Then a file `bird_audit.md` is created in the same folder.

2. **Content Fidelity**
   - Given an AI response
   - When the audit file is written
   - Then the content matches the AI's analysis exactly.

3. **CLI Feedback**
   - When the audit completes
   - Then the CLI outputs: `  ✓ Audit report saved: bird_audit.md`.

## Metadata
- **Complexity**: Low
- **Labels**: Filesystem, Integration, Workflow
- **Required Skills**: Python, IO
