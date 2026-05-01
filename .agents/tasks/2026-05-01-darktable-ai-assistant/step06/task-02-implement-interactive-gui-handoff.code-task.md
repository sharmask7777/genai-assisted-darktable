# Task: Implement Interactive GUI Handoff

## Description
Implement the "Interactive Denoise" flow. When the AI recommends denoising, the tool should pause, open the image in the Darktable GUI for user inspection, and wait for a "take a call" confirmation.

## Background
Denoising is complex and sensor-dependent. By opening the GUI, we let the user leverage their expertise to validate the AI's "best guess" before proceeding.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `open_in_darktable(file_path: str)` using `subprocess.run(["open", "-a", "darktable", file_path])`.
2. Implement an interactive prompt loop: `click.confirm("Does the Denoise look correct in Darktable?")`.
3. Ensure the tool gracefully handles cases where the user declines or adjusts manually.
4. Integrate this loop into the main editing flow when a 'denoise' recommendation is detected.

## Dependencies
- macOS `open` command.
- Active Darktable installation.

## Implementation Approach
1. Add the GUI handoff function to a new or existing utility module.
2. Implement the logic to detect 'Denoise' in the AI recommendations.

## Acceptance Criteria

1. **GUI Activation**
   - Given an image path
   - When `open_in_darktable` is called
   - Then Darktable opens and focuses on that specific image.

2. **Interactive Pause**
   - Given a denoise recommendation
   - When the tool runs
   - Then it pauses execution and waits for user input after opening Darktable.

## Metadata
- **Complexity**: Medium
- **Labels**: UX, MacOS, Interactivity, Darktable
- **Required Skills**: Python, Subprocess, Click
