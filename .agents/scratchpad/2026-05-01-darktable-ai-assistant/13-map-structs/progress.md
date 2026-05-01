# Progress: 13-map-structs

## Tasks
- [x] Research/Define Exposure v6 struct alignment
- [x] Research/Define Temperature v3 struct alignment
- [x] Implement `get_exposure_params`
- [x] Implement `get_temperature_params`
- [x] Verify against known Darktable hex strings

## TDD Cycles
1. **Cycle 1: Struct Parity**: Implemented Exposure v6 (20 bytes) and Temperature v3 (16 bytes). Verified with little-endian float unpacking.
