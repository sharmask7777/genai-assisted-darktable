# Task: Implement agent-next CLI Command

## Description
Refactor `main.py` to add a new command, `agent-next`, specifically designed for the Agent-led workflow. This command should return a structured JSON object containing everything the Agent needs to guide the user: a talkative nudge message, technical data, and any required actions.

## Background
Instead of the Python script directly interacting with the user, the `agent-next` command acts as a "backend" for the Gemini session. It provides the "next move" for the Agent to execute.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md
- Research: .agents/planning/2026-05-01-darktable-agentic-workflow/research/architecture.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Add `@cli.command() agent_next(image_path)` to `dt_ai/main.py`.
2. The command must output ONLY a valid JSON object to stdout.
3. The JSON schema should include:
   - `nudge`: The talkative/educational text for the user.
   - `target_image`: The absolute path of the image being processed.
   - `neighbor_images`: List of paths for adjacent images.
   - `ai_result`: The parsed JSON from Gemini Vision.
4. Integrate with `load_state` to ensure the nudge is informed by history.

## Dependencies
- `dt_ai/state.py` (Step 1).
- `dt_ai/discovery.py` (Step 2).

## Implementation Approach
1. Create a helper function `generate_agent_payload(image_path)`.
2. Ensure `Click` doesn't print any extraneous logs or decorative text when this command is called (use `click.echo(json.dumps(...))`).

## Acceptance Criteria

1. **JSON Output**
   - Given a valid image path
   - When `dt-ai agent-next <path>` is run
   - Then the output is a single, parsable JSON block.

2. **Nudge Presence**
   - Given a wildlife photo
   - Then the `nudge` field contains talkative mentorship text about the photo.

3. **State Awareness**
   - Given a photo that was already processed
   - Then the JSON response reflects this in the history or nudge text.

## Metadata
- **Complexity**: Medium
- **Labels**: API, JSON, Orchestration
- **Required Skills**: Python, JSON, CLI Design
