# Plan: 05-agent-next-command

## Test Strategy
1. **JSON Purity Test**: Run the command and verify that `json.loads()` can parse the entire output.
2. **Payload Completeness Test**: Verify all keys (`nudge`, `target_image`, `neighbor_images`, `ai_result`) are present in the JSON.
3. **Mock Integration Test**: Mock `extract_preview`, `analyze_image`, and `discover_raw_files` to verify the orchestrator calls them correctly.

## Implementation Steps
1. In `dt_ai/main.py`, import `get_neighboring_files` and `load_state`.
2. Implement `@cli.command() agent_next(path)`.
3. Orchestration logic:
   - Extract preview for target.
   - Call Gemini for audit/JSON.
   - Get neighbors.
   - Load state for context.
   - Synthesize `nudge` (preliminary implementation, to be refined in Task 3-03).
   - `click.echo(json.dumps(payload))`.
