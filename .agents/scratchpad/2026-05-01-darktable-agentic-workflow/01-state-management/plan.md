# Plan: 01-state-management

## Test Strategy
1. **Default State Test**: Verify `load_state` on a new directory returns a valid empty schema.
2. **Persistence Test**: Save a complex state and verify the JSON on disk is correct and re-loadable.
3. **Path Resolution Test**: Verify that `image_dir/subdir/` and `image_dir/subdir` both resolve to the same parent for the state file.

## Implementation Steps
1. Create `dt_ai/state.py`.
2. Implement `get_state_path(image_dir) -> Path`.
3. Implement `load_state(image_dir) -> dict`.
4. Implement `save_state(image_dir, state)`.
