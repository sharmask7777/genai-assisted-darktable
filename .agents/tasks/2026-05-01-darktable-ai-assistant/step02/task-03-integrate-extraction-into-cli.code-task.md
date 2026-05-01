# Task: Integrate Extraction into the audit Command

## Description
Wire the image extraction pipeline into the existing `dt-ai audit` command. When a user runs the audit, the tool should now not only find the files but also generate their previews for subsequent AI analysis.

## Background
This is the final step in the Scaffold phase, transitioning the tool from a simple file lister to an active image processing pipeline.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Update `dt_ai/main.py` to import the extraction logic.
2. Modify the `audit` command to iterate through discovered files and trigger extraction.
3. Add progress feedback to the CLI (e.g., "Extracting preview for IMG_1234.ARW...").
4. Ensure `--dry-run` still works by skipping the actual `sips` call if desired (or perform extraction but skip the future AI step). For v1, extraction should happen even in dry-run to verify the pipeline.

## Dependencies
- `dt_ai/main.py` (from Step 1).
- `dt_ai/processor.py` (from Tasks 2-01, 2-02).

## Implementation Approach
1. Update the `audit` loop in `main.py`.
2. Add graceful error handling so one failed extraction doesn't crash the entire batch.

## Acceptance Criteria

1. **End-to-End Extraction**
   - Given a folder of RAW files
   - When `dt-ai audit <folder>` is run
   - Then for every RAW file, a corresponding JPEG appears in `.dt-ai/previews`.

2. **CLI Progress Feedback**
   - When the tool runs
   - Then the user sees clear, real-time feedback for each file being processed.

3. **Failure Resilience**
   - Given a batch of files where one is corrupted
   - When the audit runs
   - Then the tool reports the error for the corrupted file but successfully processes the others.

## Metadata
- **Complexity**: Low
- **Labels**: CLI, Integration, Workflow
- **Required Skills**: Python, Click
