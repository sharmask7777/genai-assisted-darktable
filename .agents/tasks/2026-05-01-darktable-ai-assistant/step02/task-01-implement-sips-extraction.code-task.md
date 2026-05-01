# Task: Implement sips Extraction Logic

## Description
Implement the core logic to extract high-quality, low-token JPEG previews from RAW files using the macOS-native `sips` tool. This extraction must be constrained to 2048px for optimal Vision model processing.

## Background
Gemini Vision models are most efficient with images around 2048px. `sips` is built into macOS and provides a high-quality "Apple-style" RAW development that is faster than a full Darktable render but more accurate than a simple metadata thumbnail extraction.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Additional References (if relevant to this task):**
- .agents/planning/2026-05-01-darktable-ai-assistant/research/STACK.md (Preview Extraction section)

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Create `dt_ai/processor.py`.
2. Implement `extract_preview(input_path: str, output_path: str) -> str`.
3. Use `subprocess.run` to execute: `sips -s format jpeg --resampleHeightWidthMax 2048 [input] --out [output]`.
4. Handle `sips` errors gracefully by raising descriptive exceptions.
5. Validate that the input file exists before calling `sips`.

## Dependencies
- macOS `sips` utility.
- Base project structure.

## Implementation Approach
1. Implement the extraction function in `processor.py`.
2. Ensure the output path is correctly passed to `sips`.
3. Verify return codes and capture stderr on failure.

## Acceptance Criteria

1. **Successful Extraction**
   - Given a valid RAW file path
   - When `extract_preview` is called
   - Then a JPEG file is created at the specified output path.

2. **Resolution Constraint**
   - Given a high-resolution RAW file
   - When a preview is extracted
   - Then the resulting JPEG's longest edge does not exceed 2048 pixels.

3. **Error Handling**
   - Given a non-existent file or corrupted RAW
   - When `extract_preview` is called
   - Then a `RuntimeError` or similar descriptive exception is raised.

4. **Unit Test Coverage**
   - Given the `processor` module
   - When running tests with mocked `subprocess.run`
   - Then the command string generation and error handling are verified.

## Metadata
- **Complexity**: Medium
- **Labels**: Image Processing, MacOS, Subprocess, SIPS
- **Required Skills**: Python, Subprocess handling
