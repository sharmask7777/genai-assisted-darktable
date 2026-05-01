# Implementation Plan: darktable-parity-sync Skill

## Implementation Checklist
- [ ] **Phase 1: Scaffolding & Core Metadata**
    - [x] Step 1: Create skill directory and initial `SKILL.md` structure.
    - [x] Step 2: Implement parameter acquisition logic.
- [ ] **Phase 2: Internal Scan & External Research**
    - [x] Step 3: Implement `codebase-summary` style internal scanner.
    - [x] Step 4: Implement external research engine (GitHub + Blogs + Search).
- [ ] **Phase 3: Parity Auditing**
    - [x] Step 5: Implement Audit Engine to generate `REPORT.md`.
- [ ] **Phase 4: TDD Orchestration**
    - [x] Step 6: Implement TDD loop (Explore -> Plan -> Code).
    - [x] Step 7: Integrate `code-assist` logic for automated testing/fixing.
- [ ] **Phase 5: Visibility & Documentation**
    - [ ] Step 8: Implement README.md auto-update logic.
    - [ ] Step 9: Final validation and end-to-end dry-run.

---

## Implementation Steps

### Step 1: Initialize Skill Structure
**Objective:** Create the foundational `SKILL.md` file in the root directory.
**Guidance:** Follow the established template in `.gemini/skills/`. Define the skill name as `darktable-parity-sync` and add the basic "Overview" and "Parameters" sections.
**Test Requirements:** Verify that `activate_skill darktable-parity-sync` correctly returns the instructions.
**Demo:** Run `activate_skill` and see the new skill instructions in the logs.

### Step 2: Parameter Acquisition
**Objective:** Implement the logic to ask for `codebase_path`, `interaction_mode`, and `research_depth`.
**Guidance:** Use the `ask_user` tool pattern. Ensure all parameters are requested upfront.
**Test Requirements:** Create a test script that mocks `ask_user` and verifies all variables are captured.
**Demo:** A working initialization turn that prompts for all 3 parameters.

### Step 3: Internal Implementation Scanner
**Objective:** Build the module that analyzes `dt_ai/*.py` and maps existing logic.
**Guidance:** Use `list_directory` and `read_file` to build an in-memory map of prompts (from `ai.py`) and schemas (from `xmp.py`).
**Test Requirements:** Write a test that provides a mock `dt_ai` directory and verifies the scanner correctly identifies "Exposure v6" or "Aesthetic Prompt".
**Demo:** The skill prints a summary of the current codebase capabilities during the scan phase.

### Step 4: External Research Engine
**Objective:** Implement the web-search and GitHub-fetch logic.
**Guidance:** Use `google_web_search` with targeted queries for "Darktable 5.x schema" and "Darktable AgX module".
**Test Requirements:** Verify that the research results are saved to the hidden progress directory.
**Demo:** View research artifacts in `.parity-sync-{TIMESTAMP}/research/`.

### Step 5: Parity Audit Engine
**Objective:** Generate the `REPORT.md` comparing internal vs. external data.
**Guidance:** Implement logic to detect "Gaps" (e.g., "Industry uses AgX, codebase uses Filmic").
**Test Requirements:** Unit test that compares two JSON objects (Internal vs. External) and outputs a Markdown table of discrepancies.
**Demo:** A generated `REPORT.md` file in the progress directory.

### Step 6: TDD Planning Phase
**Objective:** Transform the `REPORT.md` into an actionable TDD plan.
**Guidance:** For each gap, generate a task that includes "Expected Test" and "Implementation Path".
**Test Requirements:** Verify the generated `plan.md` contains at least one task for each identified gap.
**Demo:** A `plan.md` file exists in the progress directory.

### Step 7: TDD Execution Loop
**Objective:** Implement the logic to write and fix parity tests.
**Guidance:** Dynamically create `tests/test_parity_*.py` files. Use `replace` to update `dt_ai/` code until `pytest` passes.
**Test Requirements:** Ensure existing tests are not broken during this phase (Regression check).
**Demo:** A passing parity test and updated source code for a specific module (e.g., updating Kelvin mapping).

### Step 8: README Documentation
**Objective:** Update the project root `README.md` with invocation instructions.
**Guidance:** Append a "GenAI Skills" section with examples for Claude, Gemini, and Kiro.
**Test Requirements:** Verify `README.md` contains the string "/activate_skill darktable-parity-sync".
**Demo:** View the updated `README.md` in the root.

### Step 9: Final Validation
**Objective:** Perform a full end-to-end test of the skill.
**Guidance:** Run the skill against a simulated "outdated" version of the codebase.
**Test Requirements:** 100% pass rate on all parity and regression tests.
**Demo:** A final summary log showing "Parity Achieved".
