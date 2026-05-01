# Project Summary: Darktable Agentic Workflow Overhaul

This project transforms the standalone Darktable assistant into an agent-led mentorship experience.

## Artifacts Created:
- **.agents/planning/2026-05-01-darktable-agentic-workflow/**
  - `rough-idea.md`: The vision for talkative, educational guidance.
  - `idea-honing.md`: Requirements for persistence, neighbor context, and interactive waits.
  - `research/architecture.md`: Prompt-provider and JSON-persistence patterns.
  - `design/detailed-design.md`: Architecture for the Agent SOP and refactored Python API.
  - `implementation/plan.md`: Step-by-step roadmap for refactoring and SOP creation.

## Key Changes:
- **State Location**: `.dt-ai-progress.json` in the image parent directory.
- **Neighbor Context**: AI will look at 2-3 adjacent images for better nudging.
- **Agent Skill**: A new Strands-style SOP to guide the Gemini session.
- **Tone**: Talkative and educational mentor persona.

## Next Steps:
1. Begin implementation with Step 1 at .agents/planning/2026-05-01-darktable-agentic-workflow/implementation/plan.md.
2. Refactor state management to support project-local persistence.

Ready to begin?
