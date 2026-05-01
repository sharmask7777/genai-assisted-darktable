# Task: Implement Multi-Image Preview Extraction

## Description
Optimize the `agent-next` flow by extracting previews for the target image AND its 2-3 neighbors in a single call. This provides the AI (and the Agent) with immediate visual context of the sequence.

## Background
Providing the AI with "neighboring" context helps it identify if the current image is the best of a burst, fulfilling the user's requirement for lookahead context.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Update the `agent-next` logic to call `get_neighboring_files`.
2. Ensure `extract_preview` is called for the target and all neighbors.
3. Return the preview paths in the JSON payload.
4. Ensure extraction failures for neighbors do not crash the target analysis.

## Dependencies
- `dt_ai/discovery.py` (Neighbor logic from Step 2).
- `dt_ai/processor.py` (v1 extraction logic).

## Implementation Approach
1. Iterate through neighbors and call the processor.
2. Store results in a mapping: `{ "original_path": "preview_path" }`.

## Acceptance Criteria

1. **Full Preview Set**
   - Given a target image with 4 neighbors
   - When processed
   - Then 5 JPEG previews are generated in `.dt-ai/previews/`.

2. **Resilience**
   - Given a folder where a neighbor file is corrupted
   - When processed
   - Then the target image preview is still extracted successfully.

## Metadata
- **Complexity**: Low
- **Labels**: Image Processing, Optimization
- **Required Skills**: Python, Subprocess
