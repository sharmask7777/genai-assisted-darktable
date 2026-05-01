# Plan: 11-history-stack-initialization

## Test Strategy
1. **Load Test**: Verify that an existing XMP can be loaded into an ElementTree root.
2. **Sync History End Test**: Add modules to a history stack and verify that `sync_history_end` updates the tag to the correct integer count.
3. **Cloning Test**: Verify that `clone_xmp` creates a new file with the same history stack as the source.

## Implementation Steps
1. Implement `load_xmp(path) -> ET.Element` in `dt_ai/xmp.py`.
2. Implement `sync_history_end(root)` helper.
3. Implement `create_version_from_base(source_path, target_path)` logic.
