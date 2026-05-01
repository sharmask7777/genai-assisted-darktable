# Task: Implement Multi-Variation AI Strategy

## Description
Update the AI orchestrator to generate three distinct editing variations (Natural, Dramatic, Creative) per image. This involves updating the prompt to request structured JSON and implementing the logic to produce three separate Darktable sidecar files.

## Background
One of our core value propositions is "Aesthetic Inspiration." Providing multiple AI interpretations allows the user to choose the best starting point for their work.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Update `AESTHETIC_PROMPT` to request a JSON block containing parameters for 3 variations.
2. Schema should include `exposure` (EV) and `kelvin` for each variation.
3. Implement `generate_variations(raw_path, ai_result) -> List[str]` to create `_01.xmp`, `_02.xmp`, and `_03.xmp`.
4. Parse the AI JSON response safely (using `json.loads`).

## Dependencies
- AI Integration (Step 3).
- XMP Versioning (Step 4).
- Module Injection (Step 5).

## Implementation Approach
1. Add JSON instructions to the system prompt.
2. Implement the variation loop that calls `initialize_new_version` and `add_history_item`.

## Acceptance Criteria

1. **Structured AI Response**
   - Given a RAW preview
   - When analyzed
   - Then Gemini returns valid JSON with 3 distinct sets of parameters.

2. **Multi-Version Output**
   - Given a single image
   - When processed
   - Then three distinct XMP files are created following the `_nn` naming convention.

3. **Parameter Parity**
   - Given the "Dramatic" variation parameters from AI
   - When injected
   - Then the corresponding XMP file contains those specific hex-encoded values.

## Metadata
- **Complexity**: Medium
- **Labels**: AI, JSON, Logic, Multi-Version
- **Required Skills**: Python, JSON, Prompt Engineering
