# Context: 03-implement-sips-extraction

## Requirements
1. Create `dt_ai/processor.py`.
2. Implement `extract_preview(input_path, output_path)` using macOS `sips`.
3. Command: `sips -s format jpeg --resampleHeightWidthMax 2048 [input] --out [output]`.
4. Handle errors and validate input existence.

## Implementation Paths
- `dt_ai/processor.py`: Core extraction logic.
