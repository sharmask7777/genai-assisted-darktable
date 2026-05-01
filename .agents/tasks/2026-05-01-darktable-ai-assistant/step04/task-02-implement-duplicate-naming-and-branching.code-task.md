# Task: Implement Duplicate Version Naming & Branching Logic

## Description
Implement the logic to handle Darktable's versioning system. This includes naming files correctly (`_01.xmp`, `_02.xmp`) and ensuring existing edits (Version 0) are preserved while creating new AI-driven variations.

## Background
We want a "least intrusive" workflow. If a user already has a sidecar, we branch off it. If not, we start fresh. Darktable detects duplicates based on specific filename suffixes.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `get_next_version_path(raw_path: str) -> str`.
2. Support the naming pattern: `<basename>_01.<ext>.xmp`.
3. If `_01` exists, the next should be `_02`, etc.
4. Implement the "Branching" logic: if a base `.xmp` exists, use it as the template for the new duplicates but do not modify the original.

## Dependencies
- `dt_ai/xmp.py` (Task 4-01).

## Implementation Approach
1. Use `pathlib` or `glob` to check for existing sidecars.
2. Implement a loop to find the first available version number.
3. Ensure the `edit` command (to be implemented in next step) uses this logic.

## Acceptance Criteria

1. **Correct Naming (Greenfield)**
   - Given a file \`image.ARW\` and NO existing sidecar
   - When \`get_next_version_path\` is called
   - Then it returns \`image.ARW.xmp\`.

2. **Real-World Verification (Brownfield)**
   - Given a real photo directory in \`~/Pictures\` with existing \`.xmp\` files
   - When the tool is run on those files
   - Then it correctly identifies the highest version number and proposes \`_nn.xmp\` for the next version.

3. **Incremental Versioning**
   - Given \`image.ARW.xmp\` and \`image_01.ARW.xmp\` exist
   - When called
   - Then it returns \`image_02.ARW.xmp\`.

## Metadata
- **Complexity**: Low
- **Labels**: Filesystem, Versioning, Logic
- **Required Skills**: Python, Pathlib
