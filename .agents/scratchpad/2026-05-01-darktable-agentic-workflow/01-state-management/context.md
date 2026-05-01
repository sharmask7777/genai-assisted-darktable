# Context: 01-state-management

## Requirements
1. Create `dt_ai/state.py`.
2. Schema for `.dt-ai-progress.json`:
   - `project_path`: Absolute path to images.
   - `history`: List of dicts `{"image": str, "applied": list}`.
   - `last_processed`: Filename.
3. `load_state(image_dir)`: Read from parent of `image_dir`.
4. `save_state(image_dir, state)`: Write to parent of `image_dir`.
5. Use `pathlib` for all path math.

## Implementation Paths
- `dt_ai/state.py`: Core state management.
