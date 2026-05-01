# Plan: 08-generate-audit-reports

## Test Strategy
1. **End-to-End Report Generation Test**: Use `CliRunner` and mock `analyze_image` and `extract_preview`. Verify that the `_audit.md` file is created with the correct content and the CLI outputs the success message.
2. **Permission Error Resilience Test**: Mock a `PermissionError` when writing the report and verify that the CLI reports the error but doesn't crash.

## Implementation Steps
1. In `dt_ai/main.py`, update the `audit` command:
   - Import `analyze_image` and `AESTHETIC_PROMPT`.
   - Call `analyze_image` after a successful extraction.
   - Implement a `save_audit_report` helper function.
   - Display the audit status in the CLI loop.
