# Task: Fix Composition Engine Coordinate Mapping

## Problem
User reported that generated crops for `1X7A4538.jpg` were "bad" and did not match the descriptions (e.g., "Classic Naturalist" didn't actually follow Rule of Thirds as described).

## Evidence
- Image: 1X7A4538.jpg
- Parameters sent: 
  - Option 1: {"cx": 0.55, "cy": 0.45, "cw": 0.7, "ch": 0.7}
  - Option 2: {"cx": 0.5, "cy": 0.5, "cw": 0.9, "ch": 0.506}
  - Option 3: {"cx": 0.5, "cy": 0.4, "cw": 0.5, "ch": 0.625}

## Objective
Investigate if `dt-ai` is correctly normalizing coordinates or if there is an offset/scaling issue when applying these to the XMP.
