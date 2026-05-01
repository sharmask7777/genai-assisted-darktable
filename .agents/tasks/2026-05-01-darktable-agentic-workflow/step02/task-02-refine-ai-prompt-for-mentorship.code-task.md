# Task: Refine AI Prompt for Talkative Mentorship

## Description
Update the `AESTHETIC_PROMPT` in `dt_ai/ai.py` to adopt a "Talkative Mentor" persona. The prompt should instruct the AI to be educational, explaining its technical reasoning (e.g., explaining why it suggests a certain exposure or white balance) and using a supportive tone.

## Background
The user explicitly requested a "talkative and educational" experience. The AI should not just provide values, but act as a mentor guiding the user through the Darktable ecosystem.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Modify `AESTHETIC_PROMPT` in `dt_ai/ai.py`.
2. Add explicit instructions for the persona:
   - "Adopt a talkative, educational tone."
   - "Explain technical concepts (e.g., dynamic range, ISO noise, local contrast) as you analyze."
   - "Provide guidance on *why* specific modules are recommended."
3. Ensure the JSON output requirement remains intact but is preceded by this educational commentary.

## Dependencies
- `dt_ai/ai.py` (from Step 3 of v1).

## Implementation Approach
1. Draft the new persona instructions.
2. Ensure the "audit" field in the JSON result is where the majority of this talkative commentary lives.

## Acceptance Criteria

1. **Tone Shift**
   - When the prompt is used
   - Then the resulting "audit" text is more descriptive and educational than the v1 output.

2. **Concept Explanation**
   - When analyzing a high-ISO image
   - Then the AI explains what sensor noise is and why 'Denoise (profiled)' is the solution.

## Metadata
- **Complexity**: Low
- **Labels**: Prompt Engineering, Persona, Mentorship
- **Required Skills**: Prompt Engineering
