# Review Notes - Darktable GenAI Assistant

## Consistency Check
- **Project Name vs. Package Name:** The project is named `dt-ai` in `pyproject.toml`, but the source package is `dt_ai`. This is correctly documented in `codebase_info.md`.
- **Module Versions:** XMP module versions (e.g., Exposure v6) are consistently documented across `interfaces.md` and `data_models.md`.

## Completeness Check
- **Discovery Patterns:** `discovery.py` logic for identifying RAW files was not deeply analyzed. It is assumed to use standard photographic extensions (.ARW, .CR2, etc.).
- **GUI Automation:** `gui.py` uses the macOS `open` command. This is documented but the specific CLI flags used by Darktable (if any) are not detailed.
- **Error Handling:** Pipeline error handling (try/except in `main.py`) is mentioned but not detailed in the workflow diagrams.

## Recommendations
1.  **Expand Discovery Docs:** Explicitly list supported RAW extensions in `components.md`.
2.  **Add Testing Guide:** Create a `testing.md` or add a section to `dependencies.md` explaining how to run the extensive test suite.
3.  **Refine GUI Docs:** Verify if Darktable requires specific arguments to open a file in the "darkroom" view vs "lighttable" view.
