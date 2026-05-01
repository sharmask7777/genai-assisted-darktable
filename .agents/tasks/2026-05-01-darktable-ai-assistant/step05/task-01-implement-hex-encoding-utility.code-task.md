# Task: Implement Float-to-Hex Encoding Utility

## Description
Implement the core utility to convert Python values (primarily floats) into the hex-encoded binary strings used by Darktable for module parameters. This is essential for programmatically adjusting sliders in XMP files.

## Background
Darktable's `darktable:params` attribute contains hex-encoded C-structs. For simple modules like Exposure, this is often just a series of IEEE 754 floats.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Additional References (if relevant to this task):**
- Research: .planning/research/ARCHITECTURE.md (Hex Injection section)

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `encode_params(values: List[float]) -> str` in `dt_ai/xmp.py`.
2. Use Python's `struct` module to pack floats as little-endian (`<`) binary data.
3. Convert the binary data into a lowercase hex string.
4. Ensure the utility can handle multiple values (e.g., exposure + black level).

## Dependencies
- `xmp.py` module.

## Implementation Approach
1. Use `struct.pack('<f', value)` for 32-bit floats.
2. Convert to hex using `.hex()`.

## Acceptance Criteria

1. **Correct Float Encoding**
   - Given the float `1.0`
   - When encoded
   - Then it results in `0000803f` (IEEE 754 little-endian).

2. **Multi-Value Encoding**
   - Given two floats `0.0` and `1.0`
   - When encoded
   - Then it results in `000000000000803f`.

3. **Unit Test Coverage**
   - Given the encoding utility
   - When running tests with known Darktable hex values
   - Then the results match exactly.

## Metadata
- **Complexity**: Medium
- **Labels**: XML, Binary, Hex, Darktable
- **Required Skills**: Python, Binary packing (struct)
