# Task: Implement Mentorship Response Synthesis

## Description
Finalize the logic that generates the "talkative nudge" returned to the Agent. This logic must synthesize the raw AI analysis with the project state and neighbor context to produce a truly helpful, educational prompt.

## Background
This is the "soul" of the overhaul. The nudge needs to feel like it comes from a mentor who knows what you've done so far and what's coming up in your folder.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `synthesize_nudge(target_info, neighbor_info, state)` in `dt_ai/ai.py`.
2. The synthesis should:
   - Reference the current image's strengths (from Gemini analysis).
   - Briefly mention if neighbors look similar or better (lookahead context).
   - Use the "Talkative Mentor" tone defined in Step 2.
   - Advise on the next Darktable step (e.g., "Once you've imported these, try the 'Dramatic' variation...").

## Dependencies
- `dt_ai/ai.py` (Prompt from Step 2).
- `dt_ai/state.py` (History from Step 1).

## Implementation Approach
1. Combine the AI `audit` text with state-based context.
2. Use Python string templates or simple concatenation to build the final nudge.

## Acceptance Criteria

1. **Contextual Nudge**
   - Given an image that is the 3rd in a burst
   - Then the nudge mentions the sequence (e.g., "This is a great follow-up to the previous shot...").

2. **Educational Content**
   - Then the nudge includes at least one technical explanation (e.g., about 'local contrast').

## Metadata
- **Complexity**: Medium
- **Labels**: Natural Language, Mentorship, Synthesis
- **Required Skills**: Python, String Manipulation
