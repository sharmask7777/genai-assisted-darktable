# Plan: 10-duplicate-naming-logic

## Test Strategy
1. **Greenfield Test**: Verify `image.ARW` -> `image.ARW.xmp`.
2. **First Duplicate Test**: Verify `image.ARW.xmp` exists -> `image_01.ARW.xmp`.
3. **Sequential Duplicate Test**: Verify `image_01.ARW.xmp` exists -> `image_02.ARW.xmp`.
4. **Real-World Verification**: Run the logic against a directory in `~/Pictures` and print the proposed next versions.

## Implementation Steps
1. Implement `get_next_version_path(raw_path)` in `dt_ai/xmp.py`.
2. Use `os.path.exists` to check for sidecar availability.
3. Handle the regex/string formatting for `_01`, `_02`, etc.
