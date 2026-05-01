# Plan: 16-interactive-gui-handoff

## Test Strategy
1. **GUI Call Test**: Mock `subprocess.run` and verify `open -a darktable` is called with the image path.
2. **Interaction Detection Test**: Verify that `handle_denoise_interaction` triggers only when "denoise" or "denoiseprofile" is in the recommendations list.
3. **Prompt Test**: Mock `click.confirm` and verify the flow pauses and returns the user's choice.

## Implementation Steps
1. Create `dt_ai/gui.py`.
2. Implement `open_in_darktable(path)`.
3. In `dt_ai/main.py`, implement `handle_denoise_interaction(raw_path, recommendations)`.
