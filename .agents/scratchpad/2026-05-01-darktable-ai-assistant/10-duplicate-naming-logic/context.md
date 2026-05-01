# Context: 10-duplicate-naming-logic

## Requirements
1. Implement `get_next_version_path(raw_path)`.
2. Follow Darktable naming: `<basename>.<ext>.xmp` (v0), `<basename>_nn.<ext>.xmp` (v1+).
3. "Branching" strategy: Use highest existing version as parent, do not overwrite.
4. Verify using real data from `~/Pictures`.

## Implementation Paths
- `dt_ai/xmp.py`: Adding versioning and path resolution logic.
