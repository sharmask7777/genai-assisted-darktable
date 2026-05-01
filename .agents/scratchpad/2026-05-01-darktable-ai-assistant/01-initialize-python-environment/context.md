# Context: 01-initialize-python-environment

## Existing Documentation
- **PROJECT.md**: Defines the Darktable GenAI Assistant.
- **REQUIREMENTS.md**: Specifies macOS, sips, and XMP-based non-destructive editing.
- **ARCHITECTURE.md**: Outlines the Vision-to-XMP pipeline.

## Functional Requirements
1. Initialize Python project named `dt-ai` using `uv`.
2. Configure `pyproject.toml`.
3. Add `click` dependency.
4. Create `dt_ai/` package directory with `__init__.py`.
5. Ensure `.venv` and `__pycache__` are ignored in `.gitignore`.

## Implementation Paths
- Root: `.`
- Source: `dt_ai/`
- Config: `pyproject.toml`
