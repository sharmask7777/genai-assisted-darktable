# Plan: 14-module-injection

## Test Strategy
1. **Basic Injection Test**: Start with an empty skeleton, add one module, and verify the history stack size and `history_end`.
2. **Sequential Numbering Test**: Add two modules and verify that their `darktable:num` attributes are `0` and `1` (or `1` and `2` depending on base).
3. **Attribute Verification Test**: Check that all required attributes (`operation`, `enabled`, `params`, etc.) are present in the injected element.

## Implementation Steps
1. Implement `add_history_item` in `dt_ai/xmp.py`.
2. Define a safe default for `blendop_params` (e.g., a standard "no mask" hex string if required, or empty).
3. Ensure `sync_history_end` is called within `add_history_item`.
