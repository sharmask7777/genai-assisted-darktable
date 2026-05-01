# Plan: 03-neighbor-discovery

## Test Strategy
1. **Central Position Test**: In a list of 5 files, pick #3 and verify neighbors are #1, #2, #4, #5 (for count=2).
2. **Start Boundary Test**: Pick #1 and verify only #2, #3 are returned.
3. **End Boundary Test**: Pick #5 and verify only #3, #4 are returned.
4. **Small Directory Test**: 2 files total, pick #1, verify only #2.

## Implementation Steps
1. In `dt_ai/discovery.py`, implement `get_neighboring_files(target_path, count=2)`.
2. Get the directory of `target_path`.
3. Call `discover_raw_files(dir_path)` to get the sorted absolute paths.
4. Find index of `os.path.abspath(target_path)`.
5. Calculate slice indices: `max(0, index-count)` to `index` and `index+1` to `min(len, index+1+count)`.
