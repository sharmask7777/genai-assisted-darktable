# Context: 11-history-stack-initialization

## Requirements
1. Implement logic to count modules in `darktable:history`.
2. Automatically update `darktable:history_end` to match the module count.
3. If cloning an existing XMP, ensure the new version's history starts with the parent's history.
4. Implement a helper to clear existing AI-injected modules if re-running (optional but recommended for idempotency).

## Implementation Paths
- `dt_ai/xmp.py`: Adding history management and synchronization logic.
