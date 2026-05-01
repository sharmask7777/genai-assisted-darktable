# Plan: 04-mentorship-prompt

## Prompt Strategy
1. **Persona Update**: Explicitly state "You are a supportive, talkative, and educational photography mentor."
2. **Instruction Refinement**:
   - Add a requirement to explain technical terms (e.g., "Don't just say 'increase exposure', explain what EV means in this context").
   - Direct the AI to use the "audit" section for the bulk of its mentorship text.
   - Instruct the AI to encourage the user to explore and learn.
3. **Preserve Structure**: Maintain the mandatory JSON block for the agent to parse.

## Verification
- **Unit Test**: Verify the presence of mentorship keywords ("mentor", "educational", "explain", "why") in the updated `AESTHETIC_PROMPT`.
