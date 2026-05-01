# Context: 07-mentorship-synthesis

## Requirements
1. Implement `synthesize_nudge(ai_result, neighbors, state)`.
2. Logic should:
   - Use the talkative, educational mentor tone.
   - Reference AI analysis of the current image.
   - Mention adjacent images (neighbors) if relevant (lookahead context).
   - Use session history from `state` to avoid repetitive advice.
   - Advise on the next Darktable step.
3. Integrate into the `agent-next` payload.

## Implementation Paths
- `dt_ai/ai.py`: Adding the synthesis logic.
- `dt_ai/main.py`: Wiring the synthesized nudge into the CLI command.
