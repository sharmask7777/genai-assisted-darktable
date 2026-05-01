# Plan: 06-multi-image-extraction

## Test Strategy
1. **Multi-Extraction Test**: Mock `extract_preview` and `get_neighboring_files`. Verify that `agent_next` calls `extract_preview` for each neighbor and the target.
2. **Resilience Test**: Mock `extract_preview` to fail for one neighbor but succeed for others. Verify that the command still returns a valid JSON with the target image processed.
3. **Payload Test**: Verify that the JSON contains a mapping like `previews: { "path": "preview_path" }`.

## Implementation Steps
1. Update `agent_next` in `dt_ai/main.py`.
2. Create a `previews` dictionary.
3. Loop through `[abs_path] + neighbors`.
4. Call `extract_preview` in a try-except block for neighbors.
5. Update the payload to include the preview mapping.
