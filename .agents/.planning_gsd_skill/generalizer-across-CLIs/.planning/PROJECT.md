# Project: generalizer-across-CLIs

## What This Is
A refactoring project to remove Gemini CLI lock-in from the `gen-ai-assisted-darktable` and `darktable-parity-sync` skills. This will enable the skills to work seamlessly across multiple AI CLIs including Claude, Kiro, and others, transitioning from a Kiro-centric implementation to a generalized, CLI-agnostic architecture.

## Core Value
Zero lock-in to specific AI CLIs, ensuring long-term portability and flexibility for the photography editing skills across the evolving AI ecosystem.

## Context
- **Skills involved**: `gen-ai-assisted-darktable`, `darktable-parity-sync`.
- **Target CLIs**: Gemini, Claude, Kiro, and generic OpenCode-compliant CLIs.
- **Current State**: Heavily coupled to Kiro/Gemini-specific constructs.
- **Goal**: Generalize prompts, tools, and workflows to a standard format.

## Requirements

### Validated
(None yet — ship to validate)

### Active
- [ ] **GEN-01**: Audit existing skills for CLI-specific dependencies (Kiro/Gemini).
- [ ] **GEN-02**: Define a generalized skill interface/schema that works across major CLIs.
- [ ] **GEN-03**: Refactor `gen-ai-assisted-darktable` to use generalized prompts and tool calls.
- [ ] **GEN-04**: Refactor `darktable-parity-sync` to use generalized prompts and tool calls.
- [ ] **GEN-05**: Implement a compatibility layer or abstraction for CLI-specific features (e.g., vision APIs, tool registration).
- [ ] **GEN-06**: Verify functionality across at least two different CLI environments.

### Out of Scope
- **API-01**: Building a custom CLI from scratch.
- **GUI-01**: Adding a graphical user interface.

## Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Standard Interface | Ensures all skills follow a predictable pattern regardless of CLI. | Pending |
| Prompt Generalization | Removes CLI-specific "flavors" from core logic. | Pending |

## Evolution
This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026-05-01 after initialization*
