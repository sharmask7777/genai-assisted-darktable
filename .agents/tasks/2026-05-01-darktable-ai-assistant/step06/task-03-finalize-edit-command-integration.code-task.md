# Task: Finalize edit Command Integration

## Description
Finalize the `dt-ai edit` command by wiring all components together: Discovery -> Extraction -> AI Analysis -> Multi-Variation Generation -> Interactive Handoff.

## Background
This task completes the v1 MVP, delivering the full end-to-end "GenAI First Pass" workflow.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement the `edit` command in `dt_ai/main.py`.
2. Use the full pipeline developed in previous steps.
3. Add summary feedback at the end of the run (e.g., "Generated 12 versions for 4 images").
4. Ensure dry-run mode works correctly for the `edit` command (analyzing but not writing XMPs).

## Dependencies
- All previous steps (1 through 6-02).

## Implementation Approach
1. Refactor the `audit` loop if necessary to share logic with `edit`.
2. Implement the final orchestrator loop in `main.py`.

## Acceptance Criteria

1. **Full Pipeline Success**
   - Given a directory of images in `~/Pictures`
   - When `dt-ai edit <dir>` is run
   - Then all images are analyzed, and versions appear in the filesystem.

2. **Summary Report**
   - When the command completes
   - Then the user sees a clear summary of actions taken and files created.

## Metadata
- **Complexity**: Low
- **Labels**: Integration, MVP, CLI
- **Required Skills**: Python, Workflow Orchestration
