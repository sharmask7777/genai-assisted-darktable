# Idea Honing

This document tracks the iterative refinement of the intelligent knowledge base and research system requirements.

## Requirements Questions & Answers

1. **How should the user choice between "Shallow" and "Deep" research be presented?**
   - For example: Should it be a CLI flag (e.g., `uv run dt-ai agent-next --research deep`), or should the AI agent ask you interactively in the conversation (e.g., "I'm ready to research this image. Should I do a quick local check or a deep dive on the web?")?
   - **Answer**: Ask interactively as part of the `genai-assisted-darktable` agent SOP script, which is designed for multi-step interactions.

2. **When "Deep Research" is performed, should the local knowledge base be updated immediately, or should the AI summarize all research at the end of the session to update the KB in one batch?**
   - **Answer**: Update the local knowledge base immediately after the research is performed. It should follow progressive disclosure principles to ensure optimal token management (only loading relevant context).

3. **How should the local knowledge base be structured to support this progressive disclosure?**
   - **Answer**: Use multiple markdown files categorized by subject, with an `index.md` that describes which file to consult for specific topics. Only the `index.md` should be loaded in the initial skill context, following progressive disclosure best practices.

4. **When updating the knowledge base immediately, should the agent create new dedicated markdown files for specific niche subjects (e.g., `raptors.md`) or append/update existing broad category files (e.g., `wildlife.md`)?**
   - **Answer**: Create niche markdown files as well, forming a "tree of disclosures" (e.g., `index.md` -> `wildlife.md` -> `raptors.md`). This allows for very granular information retrieval.

5. **Where should this local knowledge base (the tree of markdown files) be stored within the project?**
   - **Answer**: Store the knowledge base in `.agents/knowledge-base/`.

6. **For "Deep Research," should the agent use a specific tool (like `google_web_search`) and then synthesize the findings into the KB, or should it search and then simply append the raw research findings to the niche files?**
   - **Answer**: The agent should dynamically determine and use the research tools available on its current platform (Gemini, Claude, etc.) at runtime. Findings should be synthesized into the KB for better clarity and token management.
