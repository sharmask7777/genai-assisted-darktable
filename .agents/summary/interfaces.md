# Interfaces

## Command Line Interface (CLI)

The primary interface is the `dt-ai` CLI, built with Click.

### Internal Agent Commands
These commands are designed to be called by an AI agent script or wrapper:

- `dt-ai agent-next <image_path>`: Returns a JSON payload containing the image preview path, neighboring context, extracted metadata, and the appropriate AI prompt.
- `dt-ai apply-variations <image_path> <ai_result_json> [--yolo]`: Receives the AI's structured edit decisions, generates a pre-flight report, and writes the resulting `.xmp` sidecars.

### User Commands
- `dt-ai init-session <directory>`: Initializes a tracking state file in a given directory.
- `dt-ai audit <directory>`: Legacy/standalone command to run a read-only aesthetic audit.
- `dt-ai edit <directory>`: Legacy/standalone command to generate AI variations for all files in a directory.

## System Integration Points

- **macOS `sips`**: Called via `subprocess` to extract previews. This is a hard dependency on the host OS.
- **Darktable XMP Schema**: The application writes XML files that conform to Darktable's proprietary sidecar schema, including specific module names (`colorcalibration`, `sigmoid`, `exposure`) and hex-encoded parameters.