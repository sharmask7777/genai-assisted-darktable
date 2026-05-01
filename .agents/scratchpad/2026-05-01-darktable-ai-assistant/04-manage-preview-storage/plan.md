# Plan: 04-manage-preview-storage

## Test Strategy
1. **Directory Creation Test**: Verify that `get_preview_path` creates the directory if it's missing.
2. **Deterministic Path Test**: Verify that the same input file always produces the same output path.
3. **Collision Avoidance Test**: Verify that `folder1/photo.ARW` and `folder2/photo.ARW` result in different output paths.

## Implementation Steps
1. Add `PREVIEW_DIR = ".dt-ai/previews"` to `processor.py`.
2. Implement `get_preview_path(input_path)` helper:
   - Calculate a hash of the absolute input path.
   - Return `PREVIEW_DIR / f"{stem}_{hash}.jpg"`.
3. Update `extract_preview` to use this helper and ensure the directory exists.
