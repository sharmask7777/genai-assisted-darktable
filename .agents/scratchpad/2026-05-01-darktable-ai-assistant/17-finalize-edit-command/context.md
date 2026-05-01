# Context: 17-finalize-edit-command

## Requirements
1. Implement the `edit` command in `dt_ai/main.py`.
2. Wire all components: Discovery -> Extraction -> AI Analysis -> Multi-Variation Generation -> Interactive Handoff.
3. Support `--dry-run` (analyze but no XMP write).
4. Provide a final summary report to the user.

## Implementation Paths
- `dt_ai/main.py`: Final orchestration logic and command definition.
