# Dependencies - Darktable GenAI Assistant

## External Tools (Mandatory)
The system relies on native OS tools and third-party software for core functionality.

| Tool | Purpose | Source |
|------|---------|--------|
| `sips` | Native macOS Scriptable Image Processing System for JPEG extraction. | Pre-installed on macOS |
| `darktable` | Target application for photo editing and XMP consumption. | [darktable.org](https://www.darktable.org/) |
| `gemini-cli` | Provides the interface to Google Gemini Vision models. | Internal CLI Tool |

## Python Dependencies
Managed via `pyproject.toml` and `uv`.

### Core
- **`click` (>=8.1.7):** Used for building the CLI interface.
- **`xml.etree.ElementTree`:** Built-in library for XMP (XML) manipulation.
- **`struct`:** Built-in library for binary parameter encoding (IEEE 754).

### Development
- **`pytest` (>=9.0.3):** Primary testing framework.
- **`hatchling`:** Build backend.

## Environment Requirements
- **OS:** macOS (required for `sips` and `open` commands).
- **Python:** 3.12 or higher.
- **API Keys:** Requires a valid configuration for Gemini CLI to reach cloud vision models.
