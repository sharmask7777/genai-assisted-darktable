# Plan: 15-multi-variation-strategy

## Test Strategy
1. **JSON Parser Test**: Verify that the parser can extract JSON from a markdown code block and handle malformed input.
2. **Variation Generation Test**: Mock AI result and verify that 3 distinct XMP files are created with correct hex values.
3. **Prompt Test**: Verify that the updated prompt mentions the JSON schema.

## Implementation Steps
1. Update `dt_ai/ai.py`:
   - Modify `AESTHETIC_PROMPT` to include JSON instructions.
   - Implement `parse_ai_response(text) -> dict`.
2. Update `dt_ai/xmp.py`:
   - Implement `generate_variations(raw_path, ai_result)`.
   - Use `get_next_version_path` and `add_history_item`.
