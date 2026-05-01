# Plan: 02-integrate-state-cli

## Test Strategy
1. **New Session Test**: Provide a directory without an XMP and verify "Started new session" output.
2. **Resumed Session Test**: Create a mock state file, provide the directory, and verify "Resuming session" output.
3. **Invalid Directory Test**: Provide a non-existent path and verify the error message.

## Implementation Steps
1. In `dt_ai/main.py`, import `load_state` and `get_state_path`.
2. Implement `@cli.command() init_session(path)`.
3. Check `get_state_path(path).exists()` to determine the session type.
4. Call `load_state(path)` to initialize/load.
