# Research: Agent-Python Handoff Architecture

## 1. SOP Best Practices (Strands CLI)
- **Modality**: Declarative instructions.
- **Components**: Overview, Parameters, Steps (with Constraints), Metadata.
- **Tone**: Talkative and educational (per user preference).

## 2. State Persistence (JSON Schema)
- **Location**: `~/.progress/darktable-assistant.json`
- **Fields**:
  - `active_project_path`: Root RAW directory.
  - `processed_dir`: Path to generated exports/XMPs.
  - `processed_files`: List of already completed images.
  - `last_nudge_timestamp`: For session continuity.

## 3. Python as Prompt Provider
- **Refactoring**: `dt_ai/main.py` adds an `agent-next` command.
- **Output**: JSON containing a user-facing nudge and technical metadata.
- **Workflow**:
  1. Agent calls `dt-ai agent-next`.
  2. Python reads `~/.progress/`, finds the next image, and generates a talkative prompt.
  3. Agent presents the prompt to the user and waits for the "flip" back to Darktable.
