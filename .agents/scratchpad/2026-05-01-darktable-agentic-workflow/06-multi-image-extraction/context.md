# Context: 06-multi-image-extraction

## Requirements
1. Update `agent-next` to extract previews for both target and neighbors.
2. Ensure neighbors don't crash the main pipeline if they fail.
3. Return a mapping of original paths to preview paths in the JSON.
4. Use existing `extract_preview` and `get_neighboring_files`.

## Implementation Paths
- `dt_ai/main.py`: Update `agent_next` command logic.
