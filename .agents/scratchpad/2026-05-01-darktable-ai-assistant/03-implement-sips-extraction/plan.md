# Plan: 03-implement-sips-extraction

## Test Strategy
1. **Mocked Command Test**: Use `unittest.mock.patch` on `subprocess.run` to verify that `sips` is called with the correct arguments (format, resample, input, output).
2. **Error Handling Test**: Mock a non-zero return code from `subprocess.run` and verify that `extract_preview` raises a `RuntimeError`.
3. **Input Validation Test**: Verify that providing a non-existent path raises a `FileNotFoundError`.

## Implementation Steps
1. Create `dt_ai/processor.py`.
2. Implement `extract_preview` using `subprocess.run`.
3. Add input path validation using `os.path.exists`.
