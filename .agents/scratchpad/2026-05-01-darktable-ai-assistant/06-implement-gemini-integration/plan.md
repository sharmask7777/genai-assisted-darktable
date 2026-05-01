# Plan: 06-implement-gemini-integration

## Test Strategy
1. **Mocked Command Test**: Mock `subprocess.run` to verify that `gemini-cli` is called with the image path and the prompt.
2. **Success Test**: Verify that the function returns the stdout from the mocked call.
3. **Availability Test**: Implement and test a function `is_gemini_cli_available()` using `shutil.which`.
4. **Error Handling Test**: Verify that a non-zero exit code or missing binary raises a `RuntimeError`.

## Implementation Steps
1. Create `dt_ai/ai.py`.
2. Implement `is_gemini_cli_available()` using `shutil.which`.
3. Implement `analyze_image(preview_path, prompt)` using `subprocess.run`.
