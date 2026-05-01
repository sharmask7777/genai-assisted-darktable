# Task: Integrate State Initialization into CLI

## Description
Add a CLI capability to initialize or resume a project state. This serves as the foundation for the Agent SOP to start its work by asking the user for a directory and having the Python backend confirm or create the session tracking file.

## Background
The Agent SOP starts by asking "What is the directory for the images?". The Python backend must then be able to take that path and set up the `.dt-ai-progress.json`.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Update `dt_ai/main.py` to include a way to handle project initialization.
2. Implement logic that takes a directory path, validates it, and calls `load_state`.
3. Provide feedback to the user/agent if a session is being resumed or started fresh.
4. Ensure the `audit` and `edit` commands remain functional but are aware of the current state.

## Dependencies
- `dt_ai/state.py` (Task 1-01).

## Implementation Approach
1. Refactor the CLI entry points to be state-aware.
2. Add a hidden or explicit `init-session` internal helper that the SOP can call.

## Acceptance Criteria

1. **Successful Initialization**
   - Given a valid image directory
   - When initialized via CLI
   - Then the tool reports "Resuming session" or "Started new session" correctly.

2. **Error Handling**
   - Given an invalid directory
   - When initialized
   - Then the tool provides a clear error message that the Agent can relay to the user.

## Metadata
- **Complexity**: Low
- **Labels**: CLI, Integration, Workflow
- **Required Skills**: Python, Click
