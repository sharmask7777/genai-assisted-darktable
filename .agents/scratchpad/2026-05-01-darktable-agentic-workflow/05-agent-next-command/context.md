# Context: 05-agent-next-command

## Requirements
1. Add `agent-next` command to `dt_ai/main.py`.
2. Input: `image_path`.
3. Output: Strict JSON payload for the Agent.
4. Payload Schema:
   - `nudge`: Talkative mentor text.
   - `target_image`: Absolute path.
   - `neighbor_images`: List of paths.
   - `ai_result`: JSON from Gemini.
5. Must not print extraneous logs to stdout.

## Implementation Paths
- `dt_ai/main.py`: Adding the command and orchestrating the payload generation.
