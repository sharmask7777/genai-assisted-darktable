# Task: Implement Neighbor Discovery Logic

## Description
Update the `discovery.py` module to include logic that finds "neighboring" RAW files for a given target image. Specifically, the tool should identify 1-2 images before and after the target (alphabetically) within the same directory. This provides the AI with context to see if there is a "better" shot or a sequence of similar exposures.

## Background
In wildlife and landscape photography, shots often come in bursts or brackets. Looking at adjacent files helps the agent provide smarter "nudges" by understanding the sequence.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-agentic-workflow/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `get_neighboring_files(target_path: str, count: int = 2) -> List[str]` in `dt_ai/discovery.py`.
2. The logic should:
   - Identify the directory of the target file.
   - List all RAW files in that directory (sorted alphabetically).
   - Find the index of the target file.
   - Return up to `count` files before and `count` files after the target.
3. Handle boundary conditions (e.g., target is the first or last file).
4. Return absolute paths.

## Dependencies
- `dt_ai/discovery.py` from v1.

## Implementation Approach
1. Use existing `discover_raw_files` to get the full sorted list for the directory.
2. Find the index and slice the list safely.

## Acceptance Criteria

1. **Correct Slicing**
   - Given a directory with 10 RAW files and target #5
   - When `get_neighboring_files` is called with count=2
   - Then it returns files #3, #4, #6, #7.

2. **Boundary Handling**
   - Given the first file in a directory
   - When called
   - Then it returns only the subsequent files (no wrapping or errors).

3. **Unit Test Coverage**
   - Given various directory structures
   - When running tests with different counts and positions
   - Then the output matches expectations exactly.

## Metadata
- **Complexity**: Low
- **Labels**: Filesystem, Logic, Context
- **Required Skills**: Python, Pathlib
