# Context: 16-interactive-gui-handoff

## Requirements
1. Implement `open_in_darktable(file_path)` using macOS `open -a darktable`.
2. Implement interactive confirmation using `click.confirm`.
3. Detect 'denoise' in AI recommendations to trigger the handoff.
4. "Take a Call" flow: Tool opens image, user adjusts, tool waits for confirmation.

## Implementation Paths
- `dt_ai/gui.py`: New module for GUI-related interactions.
- `dt_ai/main.py`: Integration of the interactive loop.
