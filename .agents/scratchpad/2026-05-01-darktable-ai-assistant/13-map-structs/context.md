# Context: 13-map-structs

## Requirements
1. Implement `get_exposure_params(ev, black)`.
2. Implement `get_temperature_params(kelvin)`.
3. Map to specific Darktable modversions:
   - Exposure: v5 or v6 (Research says v6 is standard now).
   - Temperature: v3.
4. Ensure hex string length matches Darktable expectations.

## Implementation Paths
- `dt_ai/xmp.py`: Adding module-specific parameter mapping.
