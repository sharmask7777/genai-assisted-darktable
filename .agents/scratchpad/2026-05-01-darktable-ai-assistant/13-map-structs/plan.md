# Plan: 13-map-structs

## Test Strategy
1. **Exposure Test**: Verify that `get_exposure_params(1.0, 0.0)` returns a 40-character hex string (20 bytes) with `1.0` at the correct offset.
2. **Temperature Test**: Verify that `get_temperature_params(5500)` returns a 32-character hex string (16 bytes).

## Implementation Steps
1. Implement `get_exposure_params(ev, black)` using `struct.pack('<iffff', 0, black, ev, 0.5, 0.0)`.
2. Implement `get_temperature_params(kelvin)` using a simplified RGB coefficient mapping.
3. Add these to `dt_ai/xmp.py`.
