# Implementation Plan - Phase 1: Scaffold

## Goal
Build the foundational CLI harness and the `sips`-based RAW preview extraction pipeline.

## Proposed Changes

### 1. Environment Setup
- Initialize Python project with `uv`.
- Add dependencies: `click`, `pathlib`.

### 2. CLI Harness (dt_ai/main.py)
- Create a `click` group with an `audit` command.
- Implement file targeting logic (single file, directories, globs).

### 3. Extraction Pipeline (dt_ai/processor.py)
- Implement `extract_preview(input_path, output_path)` using `subprocess` to call `sips`.
- Ensure output is constrained to 2048px for token frugality.
- Manage temporary directory for previews (`.dt-ai/previews`).

## Verification Plan

### Automated Tests
- Test file globbing logic.
- Test `sips` command generation and execution (mocked).

### Manual Verification
- Run `python -m dt_ai audit image.ARW` and verify a JPEG is created in `.dt-ai/previews`.
