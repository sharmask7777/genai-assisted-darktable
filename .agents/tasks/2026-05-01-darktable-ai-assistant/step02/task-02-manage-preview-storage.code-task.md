# Task: Manage Temporary Preview Storage

## Description
Implement a robust management system for the temporary storage of JPEG previews. This includes directory creation, path normalization, and ensuring previews are stored in the project-local `.dt-ai/previews` directory.

## Background
To keep the workspace clean and maintain "least intrusive" behavior, all intermediate artifacts like JPEG previews must be stored in a hidden, centralized directory that is ignored by Git.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Define the default preview directory as `.dt-ai/previews` relative to the project root.
2. Implement logic to ensure the preview directory exists (create if missing).
3. Implement a path mapper that generates a deterministic `.jpg` filename based on the input RAW filename (e.g., `photo.ARW` -> `photo.jpg`).
4. Prevent filename collisions within the preview directory.

## Dependencies
- `dt_ai/processor.py` (Task 2-01).

## Implementation Approach
1. Add utility functions or extend the `processor` to handle directory creation.
2. Ensure paths are handled using `pathlib` for cross-platform (though macOS focused) safety.

## Acceptance Criteria

1. **Auto-Directory Creation**
   - Given a clean environment where `.dt-ai/previews` does not exist
   - When an extraction is triggered
   - Then the directory is automatically created.

2. **Deterministic Naming**
   - Given an input file `my_photo.NEF`
   - When the preview path is generated
   - Then it results in `.dt-ai/previews/my_photo.jpg`.

3. **Collision Safety**
   - Given two files with the same name in different directories (e.g., `dir1/a.ARW` and `dir2/a.ARW`)
   - When previews are extracted
   - Then they do not overwrite each other (suggest appending a hash or path segment to the filename).

## Metadata
- **Complexity**: Low
- **Labels**: Filesystem, Storage, Pathlib
- **Required Skills**: Python, Pathlib
