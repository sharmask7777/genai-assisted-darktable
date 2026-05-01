# Task: Implement state.py for Persistent Session Tracking

## Description
Create a dedicated `state.py` module to handle the persistence of photo-editing sessions. This module will manage a JSON file named `.dt-ai-progress.json` located in the parent directory of the RAW image folder. This ensures portability and context-awareness across different sessions.

## Background
The overhaul requires the agent to "remember" which project it is pursuing. Storing this in the project's own directory (the parent of the images) follows the user's preference for local, portable state.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Create `dt_ai/state.py`.
2. Implement a `SessionState` class or data structure with fields:
   - `project_path`: Path to the RAW images.
   - `history`: List of processed images and their applied variations.
   - `last_processed`: The last image the user worked on.
3. Implement `load_state(image_dir: str) -> dict`:
   - Resolve the parent directory of `image_dir`.
   - Read `.dt-ai-progress.json` if it exists.
   - Return a default state if not.
4. Implement `save_state(image_dir: str, state: dict)`:
   - Write the state to the `.dt-ai-progress.json` file in the parent directory.
5. Use `pathlib` for robust path resolution.

## Dependencies
- Base project structure from v1.

## Implementation Approach
1. Define the JSON schema in the code.
2. Implement file I/O with error handling for permissions or malformed JSON.
3. Add a helper to find the "parent" directory accurately (handling trailing slashes).

## Acceptance Criteria

1. **State File Location**
   - Given an image directory `/Users/me/Pictures/Shoot1/`
   - When `save_state` is called
   - Then the file `/Users/me/Pictures/.dt-ai-progress.json` is created/updated.

2. **Persistence Integrity**
   - Given a state object with 5 processed files
   - When saved and re-loaded
   - Then the loaded object matches the original exactly.

3. **Unit Test Coverage**
   - Given the `state` module
   - When running tests for loading/saving with various directory depths
   - Then all scenarios pass without side effects.

## Metadata
- **Complexity**: Low
- **Labels**: Persistence, JSON, Filesystem
- **Required Skills**: Python, JSON, Pathlib
