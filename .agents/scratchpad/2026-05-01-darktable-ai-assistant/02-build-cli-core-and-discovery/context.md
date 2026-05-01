# Context: 02-build-cli-core-and-discovery

## Requirements
1. Implement `dt_ai/main.py` with a `click` CLI group.
2. Add an `audit` command that accepts a file or directory path.
3. Implement file discovery logic in `dt_ai/discovery.py`.
4. Support common RAW extensions (ARW, CR2, NEF, ORF, DNG) case-insensitively.
5. Support `--dry-run` flag.

## Implementation Paths
- `dt_ai/main.py`: CLI entry point.
- `dt_ai/discovery.py`: File discovery logic.
