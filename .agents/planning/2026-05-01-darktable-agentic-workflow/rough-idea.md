# Rough Idea: Darktable Agentic Workflow Overhaul

Modify the customer experience to be agent-led (invoked from inside an agentic CLI like Gemini). 
Instead of the Python script managing the entire flow, the Python code acts as a data/prompt provider that the agent uses to guide the user.

Key Features:
- **SOP-Driven**: Create `GENAI_ASSISTED_DARKTABLE.sop.md` following Strands CLI best practices.
- **Guided Lifecycle**: Open Darktable -> Import (create "processed" dir) -> Nudge for image -> Generate variations -> Nudge for next.
- **Persistence**: Store session progress in `~/.progress/`.
- **Seamless Handoff**: User can flip between UI and CLI seamlessly.
- **Modular Python**: Refactor Python to return prompts and data to the agent session.
