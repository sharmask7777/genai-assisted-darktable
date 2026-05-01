# Components - Darktable GenAI Assistant

## Module Breakdown

### 1. `dt_ai.main`
- **Responsibility:** Entry point and workflow orchestration.
- **Key Functions:**
    - `cli()`: Root command group.
    - `init_session(path)`: Initializes directory-level state.
    - `audit(path)`: High-level image assessment workflow.
    - `edit(path)`: Full generation workflow (Audit + XMP injection).
    - `run_pipeline(...)`: The core engine that executes the step-by-step logic for a set of files.

### 2. `dt_ai.ai`
- **Responsibility:** Interface with Gemini for image analysis.
- **Key Functions:**
    - `analyze_image(preview_path, prompt)`: Sends image to Gemini and returns raw response.
    - `parse_ai_response(text)`: Extracts structured data (JSON) from the AI's markdown response.
- **Metadata:**
    - `AESTHETIC_PROMPT`: Specialized prompt engineering for photographic analysis.

### 3. `dt_ai.xmp`
- **Responsibility:** Managing Darktable sidecar files.
- **Key Functions:**
    - `generate_skeleton()`: Creates a fresh, valid XMP XML structure.
    - `add_history_item(...)`: Injects a specific module (e.g., exposure) into the history stack.
    - `generate_variations(raw_path, ai_result)`: High-level logic to create Natural, Dramatic, and Creative versions.
    - `encode_params(values)`: Low-level IEEE 754 hex encoding.

### 4. `dt_ai.processor`
- **Responsibility:** Visual data preparation.
- **Key Functions:**
    - `extract_preview(raw_path)`: Uses macOS `sips` to generate a low-token JPEG from a RAW file.
- **Storage:** Previews are stored in a hidden `.previews` directory within the target path.

### 5. `dt_ai.discovery`
- **Responsibility:** File system navigation.
- **Key Functions:**
    - `discover_raw_files(path)`: Recursively finds RAW files based on supported extensions (.ARW, .CR2, .NEF, etc.).
    - `get_neighboring_sidecars(raw_path)`: Locates existing XMP files for a given image.

### 6. `dt_ai.state`
- **Responsibility:** Session persistence.
- **Key Functions:**
    - `load_state(path)`: Retrieves session progress from `.dt-ai-state.json`.
    - `save_state(path, state)`: Persists current progress.

### 7. `dt_ai.gui`
- **Responsibility:** Darktable automation.
- **Key Functions:**
    - `open_in_darktable(file_path)`: Uses the macOS `open` command to launch Darktable focused on a specific image.
