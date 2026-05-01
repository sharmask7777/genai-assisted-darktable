# Implementation Plan: Darktable Agentic Workflow Overhaul

## Progress Checklist
- [ ] Step 1: State Management Module (`state.py`)
- [ ] Step 2: Neighbor Discovery & Refined AI Prompts
- [ ] Step 3: Python "Prompt Provider" API Refactor
- [ ] Step 4: Strands Agent SOP (`GENAI_ASSISTED_DARKTABLE.sop.md`)
- [ ] Step 5: End-to-End Session Integration & "Interactive Wait"

## Implementation Steps

### Step 1: State Management Module (`state.py`)
**Objective:** Implement persistent session tracking in the project parent directory.
- **Guidance:** Create `dt_ai/state.py`. Implement `load_state` and `save_state` using JSON. The file should be named `.dt-ai-progress.json` and located in the parent folder of the RAW images.
- **Test Requirements:** Unit tests for loading/saving and verifying correct path resolution for the parent directory.
- **Demo:** Create a state file manually and verify Python can read it.

### Step 2: Neighbor Discovery & Refined AI Prompts
**Objective:** Implement the "context-aware" logic that looks at adjacent images.
- **Guidance:** Update `dt_ai/discovery.py` to find 2-3 images adjacent to the target (alphabetically). Update the AI system prompt to include "Mentorship" instructions (educational tone, explanations of technical choices).
- **Test Requirements:** Unit tests for "Neighbor Discovery" logic (ensure it handles boundary conditions like first/last image).
- **Demo:** Run a script that takes an image ID and prints the IDs of its neighbors.

### Step 3: Python "Prompt Provider" API Refactor
**Objective:** Refactor `main.py` to return Agent-ready JSON rather than direct execution.
- **Guidance:** Add a new CLI command `agent-next`. This command should:
  1. Extract previews for target + neighbors.
  2. Perform AI analysis on the target.
  3. Format the response as JSON: `{ "message": "talkative_nudge", "actions": ["extract", "analyze"], "data": {...} }`.
- **Test Requirements:** Verify that `agent-next` returns valid JSON and correct nudge text.
- **Demo:** Run `uv run dt-ai agent-next <image>` and see the JSON output.

### Step 4: Strands Agent SOP (`GENAI_ASSISTED_DARKTABLE.sop.md`)
**Objective:** Create the formal Agent SOP guided by Strands CLI best practices.
- **Guidance:** Draft the Markdown SOP. Define steps for:
  1. Parameter acquisition (`image_dir`).
  2. Darktable setup (Import, processed dir check).
  3. The iterative loop (Ask for image -> Call Python -> Mentor User -> Wait for manual edits).
- **Test Requirements:** Linter/Manual review against the Strands SOP template.
- **Demo:** Activate the skill in a Gemini session and verify it asks for the `image_dir`.

### Step 5: End-to-End Session Integration & "Interactive Wait"
**Objective:** Finalize the "Flip-flop" workflow and the interactive handoff.
- **Guidance:** Ensure the Agent SOP correctly handles the pause/wait step. Update the `edit` command logic if necessary to be more granular (allowing the Agent to call it one image at a time).
- **Test Requirements:** Manual end-to-end walkthrough from directory selection to variation generation and manual tweaking.
- **Demo:** Process 3 images in a row using only the Agent SOP and Darktable UI.
