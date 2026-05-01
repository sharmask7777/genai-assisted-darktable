# Context: 15-multi-variation-strategy

## Requirements
1. Update `AESTHETIC_PROMPT` to request structured JSON.
2. AI must return parameters for 3 variations: Natural, Dramatic, Creative.
3. Schema: `{ "audit": "...", "recommendations": [...], "variations": { "natural": { "exposure": float, "kelvin": float }, ... } }`.
4. Implement `generate_variations(raw_path, ai_result)`.
5. Create `_01.xmp`, `_02.xmp`, and `_03.xmp`.

## Implementation Paths
- `dt_ai/ai.py`: Update prompt and result parsing.
- `dt_ai/xmp.py`: Implement variation generation logic.
