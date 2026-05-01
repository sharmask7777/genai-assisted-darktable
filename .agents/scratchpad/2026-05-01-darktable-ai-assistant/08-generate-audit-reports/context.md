# Context: 08-generate-audit-reports

## Requirements
1. Update `dt_ai/main.py` to call `analyze_image`.
2. Save AI response to `<basename>_audit.md` in the same directory as the RAW file.
3. Print the report location to the CLI.
4. Handle file-writing errors gracefully.

## Implementation Paths
- `dt_ai/main.py`: CLI logic update to coordinate analysis and report saving.
