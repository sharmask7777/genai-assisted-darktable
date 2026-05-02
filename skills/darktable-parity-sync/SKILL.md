---
name: darktable-parity-sync
description: Agentic skill to maintain parity between the dt-ai codebase and the latest Darktable industry standards, modules, and XMP schemas.
---

# Darktable Parity Sync

## Overview
This skill autonomously audits the `dt-ai` codebase against the latest Darktable industry trends and technical specifications. It identifies gaps in prompts, module logic, and XMP schemas, and proposes TDD-driven updates to bring the system into parity with current cutting-edge usage.

## Parameters
- **codebase_path** (optional, default: current directory): Path to the `dt-ai` project.
- **interaction_mode** (optional, default: "hybrid"): 
  - "hybrid": Propose changes for user approval (recommended).
  - "advisor": Generate audit report and suggestions only.
- **research_depth** (optional, default: "balanced"): 
  - "fast": Quick check of primary GitHub repos.
  - "balanced": Web search + Blogs + GitHub.
  - "deep": Exhaustive research including mailing lists and dev discussions.

## Steps

### 1. Project Initialization & Internal Scan
Initialize the parity sync environment and perform a full codebase analysis of `dt_ai/*.py` to map current capabilities, prompts, and XMP module versions.
- Create a hidden, time-stamped directory: `.parity-sync-{TIMESTAMP}/`
- Document current state in `{progress_dir}/internal_map.md`

### 2. External Parity Research
Conduct research using web search, official Darktable blogs, and the primary GitHub repository to identify:
- New modules (e.g., AgX, Capture Sharpness).
- Current version numbers for `clipping`, `ashift`, and `diffuse or sharpen`.
- Industry best practices for RAW editing in 2026.

### 3. Parity Audit & Gap Analysis
Generate a structured `REPORT.md` in the progress directory:
- **Gap Analysis Table**: Current State vs. Industry Standard.
- **Module Version Check**: Verify `clipping` (v5), `ashift` (v5), and `diffuse` (v2) struct offsets.
- **Sequence Check**: Ensure the "Denoise-before-Sharpen" pipeline order is enforced in `xmp.py`.
- **Remediation Plan**: Proposed TDD implementation steps.

### 4. TDD Planning & Proposal
Transform the audit findings into a Test-Driven Development plan.
- Present the `REPORT.md` and the proposed `plan.md` to the user.
- Wait for user approval or refinement of the plan.

### 5. Automated TDD Implementation
For each approved task, execute the red-green-refactor cycle:
- Write failing parity tests in `tests/test_parity_*.py`.
- Apply targeted fixes to `dt_ai/` modules.
- Verify all tests pass and ensure no regressions in existing test suite.

### 6. Finalization & Documentation
- Update the project `README.md` with invocation instructions for the skill.
- Provide a final summary of changes and suggest next steps for validation.

## Troubleshooting
- **Research Failures:** Check network connectivity or Gemini CLI configuration.
- **Test Failures:** Review the `logs/` directory in the progress folder for detailed pytest output.
- **Schema Conflicts:** Ensure Darktable is installed to verify XMP compatibility manually if needed.
