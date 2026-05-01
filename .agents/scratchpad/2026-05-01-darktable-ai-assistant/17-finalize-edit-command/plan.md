# Plan: 17-finalize-edit-command

## Test Strategy
1. **End-to-End Edit Test**: Use `CliRunner` and mock all external calls (sips, ai, gui). Verify that for a single image, it calls extraction, analysis, variation generation, and (if needed) the GUI handoff.
2. **Dry-Run Edit Test**: Verify that `--dry-run` skips variation generation and GUI calls.

## Implementation Steps
1. Refactor `main.py`:
   - Create a common `run_pipeline(path, dry_run, mode='audit')` orchestrator.
   - Implement the `edit` command.
   - Add the interactive loop: if `needs_denoise_interaction`, call `open_in_darktable` and `click.confirm`.
   - Add the final summary print.
