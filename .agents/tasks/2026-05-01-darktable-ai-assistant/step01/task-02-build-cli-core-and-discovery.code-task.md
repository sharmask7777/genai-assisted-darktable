# Task: Build CLI Core & File Discovery Logic

## Description
Implement the core CLI structure using `click` and the logic to discover RAW files in the filesystem. The CLI should support targeting single files, directories, and glob patterns.

## Background
The tool needs a "least intrusive" way to find photos to process. Users will provide paths that might contain various RAW formats used in wildlife and landscape photography.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Define a `click` group in `dt_ai/main.py`.
2. Implement an `audit` command that accepts a `PATH` argument.
3. Implement a `--dry-run` flag for the `audit` command.
4. Implement a `FileDiscovery` utility that uses `pathlib` or `glob`.
5. Support common RAW extensions: `.ARW`, `.CR2`, `.NEF`, `.ORF`, `.DNG` (case-insensitive).
6. Ensure the tool gracefully handles empty directories or invalid paths.

## Dependencies
- `click`
- Project structure from Task 1-01.

## Implementation Approach
1. Create `dt_ai/main.py` with the CLI entry point.
2. Implement file discovery logic in a dedicated module or as a helper.
3. Wire the `audit` command to print the list of discovered files.

## Acceptance Criteria

1. **Single File Target**
   - Given a path to a single RAW file
   - When `dt-ai audit <file>` is run
   - Then exactly one file is identified for processing.

2. **Directory Target**
   - Given a directory containing 3 RAW files and 2 JPEGs
   - When `dt-ai audit <dir>` is run
   - Then exactly 3 RAW files are identified.

3. **Glob Support**
   - Given a glob pattern like `path/to/*.ARW`
   - When the CLI processes the input
   - Then all matching RAW files are discovered.

4. **Dry Run Indicator**
   - Given the `--dry-run` flag
   - When the audit command runs
   - Then the output explicitly states it is a dry run and no files will be modified.

5. **Unit Test Coverage**
   - Given the discovery logic
   - When running tests with various path combinations
   - Then all scenarios (single file, empty dir, mixed files) are covered with >90% coverage.

## Metadata
- **Complexity**: Medium
- **Labels**: CLI, Filesystem, Globbing, Python
- **Required Skills**: Python, Pathlib, Click
