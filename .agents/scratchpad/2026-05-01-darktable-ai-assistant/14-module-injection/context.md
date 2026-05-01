# Context: 14-module-injection

## Requirements
1. Implement `add_history_item(root, operation, params, modversion, enabled)`.
2. Generate sequential `darktable:num` values.
3. Automatically sync `history_end`.
4. Handle mandatory Darktable attributes for each history item.

## Darktable History Attributes
- `darktable:num`: Sequential integer.
- `darktable:operation`: Module name (e.g., 'exposure').
- `darktable:enabled`: '1' or '0'.
- `darktable:modversion`: Module version.
- `darktable:params`: Hex string.
- `darktable:multi_name`: Empty string.
- `darktable:multi_priority`: '0'.
- `darktable:blendop_version`: '11' (default).
- `darktable:blendop_params`: Safe default (bypass).

## Implementation Paths
- `dt_ai/xmp.py`: Adding the injection logic.
