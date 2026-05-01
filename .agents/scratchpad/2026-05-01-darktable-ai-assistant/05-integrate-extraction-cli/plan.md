# Plan: 05-integrate-extraction-cli

## Test Strategy
1. **End-to-End Success Test**: Use `CliRunner` and mock `extract_preview` to verify that the CLI reports successful extraction for all files.
2. **Resilience Test**: Mock `extract_preview` to fail for one file and succeed for another, verifying that the CLI continues processing and reports the error.

## Implementation Steps
1. Update `dt_ai/main.py` to include the extraction loop.
2. Add `try-except` block around `extract_preview` call.
3. Use `click.echo` for progress updates.
