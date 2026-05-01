# Context: 04-manage-preview-storage

## Requirements
1. Define default preview directory: `.dt-ai/previews`.
2. Ensure directory exists (create if missing).
3. Implement deterministic path mapping (`photo.ARW` -> `.dt-ai/previews/photo.jpg`).
4. Prevent filename collisions (e.g., when files with same name are in different folders).

## Implementation Paths
- `dt_ai/processor.py`: Adding path management and directory initialization logic.
