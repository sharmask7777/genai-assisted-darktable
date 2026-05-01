# Plan: 12-hex-encoding-utility

## Test Strategy
1. **Single Value Test**: Encode `1.0` and assert result is `0000803f`.
2. **Zero Value Test**: Encode `0.0` and assert result is `00000000`.
3. **Negative Value Test**: Encode `-1.0` and assert result is `000080bf`.
4. **Multi-Value Test**: Encode `[0.0, 1.0]` and assert result is `000000000000803f`.

## Implementation Steps
1. Import `struct` in `dt_ai/xmp.py`.
2. Implement `encode_params(values: List[float]) -> str`.
3. Use a loop or list comprehension with `struct.pack('<f', v)`.
4. Join the resulting bytes and call `.hex()`.
