# Task: Develop Aesthetic Audit System Prompt

## Description
Design and implement the "Expert Photographer" system prompt used to guide Gemini in analyzing images. The prompt must focus on wildlife and landscape aesthetics and map visual flaws to specific Darktable modules.

## Background
The quality of the AI's "first pass" depends on the precision of the prompt. It needs to act as a senior photography editor who knows the Darktable ecosystem intimately.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md
- Research: .agents/planning/2026-05-01-darktable-ai-assistant/research/FEATURES.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Define a constant `AESTHETIC_PROMPT` in `dt_ai/ai.py`.
2. The prompt must instruct the AI to:
   - Identify if the image is Wildlife or Landscape.
   - Comment on composition (e.g., rule of thirds, distractions).
   - Evaluate technicals (e.g., eye focus, highlight clipping, noise).
   - Recommend 2-3 specific Darktable modules (e.g., 'Denoise (profiled)', 'Diffuse or Sharpen').
3. Format the output for easy reading in a Markdown file.

## Dependencies
- `dt_ai/ai.py` (Task 3-01).

## Implementation Approach
1. Draft the prompt based on project requirements.
2. Test the prompt manually with a sample image via the actual Gemini CLI to ensure high-quality reasoning.

## Acceptance Criteria

1. **Comprehensive Reasoning**
   - Given an image of a bird
   - When analyzed with the prompt
   - Then the output includes specific comments on eye focus and background isolation.

2. **Module Recommendations**
   - Given an underexposed landscape
   - When analyzed
   - Then the output explicitly recommends the 'Exposure' or 'Tone Equalizer' modules.

3. **Consistent Formatting**
   - Given any analysis
   - Then the output follows a structured Markdown format (Headings, Bullet points).

## Metadata
- **Complexity**: Medium
- **Labels**: Prompt Engineering, Photography, Darktable
- **Required Skills**: Prompt Engineering, Domain Knowledge
