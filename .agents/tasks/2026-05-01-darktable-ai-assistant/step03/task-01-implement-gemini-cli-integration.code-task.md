# Task: Implement Gemini CLI Integration

## Description
Implement the core logic to interface with the `gemini-cli` for image analysis. This module will handle calling the CLI, passing the extracted JPEG previews, and capturing the AI's textual response.

## Background
The `gemini-cli` is our primary intelligence engine. We need a reliable way to invoke it from our Python application, ensuring we can send images and receive structured (or well-formatted) reasoning.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Create `dt_ai/ai.py`.
2. Implement `analyze_image(preview_path: str, prompt: str) -> str`.
3. Use `subprocess.run` to execute `gemini-cli` with the provided preview and prompt.
4. Capture and return the stdout (the AI response).
5. Handle errors if `gemini-cli` is not found or fails.

## Dependencies
- `gemini-cli` installed and authenticated on the system.
- Extracted previews from Step 2.

## Implementation Approach
1. Build the command string for `gemini-cli`.
2. Execute via subprocess and return the resulting text.
3. Add a check to verify `gemini-cli` availability.

## Acceptance Criteria

1. **Successful Communication**
   - Given a valid JPEG preview
   - When `analyze_image` is called with a simple prompt
   - Then the response from Gemini is returned as a string.

2. **Error Resilience**
   - Given a missing `gemini-cli` binary
   - When `analyze_image` is called
   - Then a descriptive `RuntimeError` is raised.

3. **Mocked Unit Tests**
   - Given the `ai` module
   - When running tests with mocked subprocess
   - Then the command invocation is verified.

## Metadata
- **Complexity**: Medium
- **Labels**: AI, Gemini, Integration, Subprocess
- **Required Skills**: Python, CLI Integration
