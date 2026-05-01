# GSD Workflow: Darktable GenAI Assistant

## Current Context
Building a macOS CLI for GenAI-driven photo editing in Darktable.

## Workflow Commands
- `/gsd:progress` - Check current project state
- `/gsd:discuss-phase [N]` - Clarify approach for a phase
- `/gsd:plan-phase [N]` - Generate implementation plans
- `/gsd:execute-phase [N]` - Execute plans

## Project Guidelines
- **Frugal Token Usage:** Always use downscaled previews for Vision.
- **Interactivity:** Pause for user validation on complex module injections (Denoise).
- **Non-Destructive:** Only modify .xmp sidecar files, never RAW originals.
