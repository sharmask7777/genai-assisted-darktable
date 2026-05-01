# Plan: 07-mentorship-synthesis

## Test Strategy
1. **Contextual Awareness Test**: Verify that if there are neighbors, the nudge mentions them (e.g., "I've also looked at adjacent shots...").
2. **Repetition Avoidance Test**: Verify that the nudge can vary based on whether it's the first image in a session or a continuation.
3. **Tone Test**: Verify that the nudge maintains a supportive, talkative tone.

## Implementation Steps
1. Implement `synthesize_nudge(ai_result: dict, neighbors: list, state: dict)` in `dt_ai/ai.py`.
2. Logic:
   - Start with a mentor-like greeting or transition.
   - Inject the AI's `audit` text.
   - If `neighbors`, add a line about having looked ahead at adjacent files.
   - Mention the next step in Darktable (e.g., "Ready for your creative touch!").
3. Update `agent_next` in `dt_ai/main.py` to call this function.
