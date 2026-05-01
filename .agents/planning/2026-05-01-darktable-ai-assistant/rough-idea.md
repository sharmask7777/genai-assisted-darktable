# Rough Idea: Darktable GenAI Assistant

I am on a macbook, I want to design a workflow that automates how I do photo editting by using gemini CLI (or similar GenAI tools). I use Darktable to do it today. I primarily do wildlife but i have always been interested in landscapes. Essentially, I want to delegate my image processing expertise to genAI for a first pass. I want a convenient CLI or a UI to help me have a GenAI driven assistant for my image editting needs.

Key requirements identified:
- Frugal token usage (selective RAW processing).
- Use of Darktable sidecar (XMP) files for non-destructive editing.
- Features: Denoising, composition analysis, aesthetic commentary, tool recommendations.
- Multiple editing variations per image.
- Automated Denoise (with interactive validation gates).
- Platform: macOS.
- Primary Tool: Gemini CLI (Cloud APIs).
