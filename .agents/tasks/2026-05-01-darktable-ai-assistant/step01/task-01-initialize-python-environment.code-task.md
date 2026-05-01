# Task: Initialize Python Environment & Dependency Management

## Description
Set up the Python development environment for the Darktable GenAI Assistant using `uv`. This includes initializing the project, configuring dependencies, and setting up the basic package structure.

## Background
The project requires a modern, fast Python environment. We've chosen `uv` for dependency management and `click` for the CLI framework.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Additional References (if relevant to this task):**
- .agents/planning/2026-05-01-darktable-ai-assistant/research/STACK.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Initialize a new Python project named `dt-ai` using `uv`.
2. Configure `pyproject.toml` with metadata.
3. Add `click` as a core dependency.
4. Create the initial package structure: `dt_ai/` directory with `__init__.py`.
5. Ensure a `.gitignore` is present, excluding `.venv` and `__pycache__`.

## Dependencies
- `uv` installed on the system.

## Implementation Approach
1. Run `uv init --name dt-ai`.
2. Add dependencies via `uv add click`.
3. Create the `dt_ai` source directory.

## Acceptance Criteria

1. **Environment Ready**
   - Given a clean workspace
   - When `uv sync` is run
   - Then the virtual environment is created and `click` is installed.

2. **Package Structure**
   - Given the project root
   - When listing files
   - Then `dt_ai/__init__.py` and `pyproject.toml` exist.

3. **Unit Test Coverage**
   - Given the environment setup
   - When running a smoke test (e.g., `python -c "import click; print(click.__version__)"`)
   - Then it completes successfully without errors.

## Metadata
- **Complexity**: Low
- **Labels**: Environment, Python, UV, Setup
- **Required Skills**: Python, CLI tools
