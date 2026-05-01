# Task: Map Exposure & Temperature Structs

## Description
Define the specific parameter structures for the Darktable `exposure` and `temperature` modules. Map the AI-friendly values (EV for exposure, Kelvin for temperature) to the binary format required by Darktable.

## Background
Each Darktable module has a specific `modversion` and parameter alignment.
- **Exposure (v6)**: Usually 4 floats (black level, exposure, etc.).
- **Temperature (v3)**: 3 floats (Kelvin, red/blue/green coefficients).

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Additional References (if relevant to this task):**
- Darktable Source (referenced in Research): `src/iop/exposure.c`.

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `get_exposure_params(ev: float, black: float = 0.0) -> str`.
2. Implement `get_temperature_params(kelvin: float) -> str`.
3. Use the encoding utility from Task 5-01.
4. Hardcode safe defaults for auxiliary parameters (like clipping threshold) to ensure module stability.

## Dependencies
- Hex Encoding Utility (Task 5-01).

## Implementation Approach
1. Research or use known constants for the struct alignment of these modules.
2. Exposure v6 struct: `{ 0.0, 0.0, ev, 1.0 }` (simplified check).
3. Temperature v3 struct: `{ red, green, blue }` derived from Kelvin.

## Acceptance Criteria

1. **Exposure Parity**
   - Given an exposure adjustment of `+1.0 EV`
   - When encoded
   - Then the hex string matches a known valid Darktable exposure string.

2. **Module Stability**
   - Given an AI-generated Kelvin value (e.g., `5500`)
   - When encoded
   - Then the resulting hex string is exactly the length Darktable expects for that modversion.

## Metadata
- **Complexity**: High
- **Labels**: Domain Knowledge, Binary, Darktable
- **Required Skills**: Python, Struct, Research
