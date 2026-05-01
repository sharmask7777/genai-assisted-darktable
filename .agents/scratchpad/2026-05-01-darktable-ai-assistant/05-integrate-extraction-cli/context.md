# Context: 05-integrate-extraction-cli

## Requirements
1. Update `dt_ai/main.py` to import `extract_preview`.
2. Modify `audit` command to iterate through discovered files and extract previews.
3. Add progress feedback to the CLI.
4. Ensure one failed extraction doesn't crash the entire batch.

## Implementation Paths
- `dt_ai/main.py`: CLI logic update.
