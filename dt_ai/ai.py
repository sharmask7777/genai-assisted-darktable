import json
import re

COMPOSITION_PROMPT = """
You are a supportive, talkative, and educational photography mentor and Composition Expert.
Your goal is to analyze the original frame of a RAW image and suggest three distinct crop and rotation options to improve the storytelling.

### 1. Analyze Original Composition
Describe what you see in the current frame. Identify the subject and any distractions.

### 2. Suggest 3 Crops
Provide three distinct crop suggestions. For each, give a descriptive name (e.g., "Rule of Thirds", "Cinematic Wide", "Tight Portrait") and explain the **"Why"** (how it improves the shot).

Include **Rotation** for leveling horizons or adding creative tilt (especially for wildlife).

### 3. Output Parameters (JSON)
You MUST provide the suggestions in a JSON code block at the end.
Coordinates (`cx`, `cy`, `cw`, `ch`) must be **normalized floats (0.0 to 1.0)**.
Rotation is in **degrees** (±180).

Required JSON format:
```json
{
  "analysis": "Your overview of the current composition",
  "options": [
    {
      "id": 1,
      "name": "Option Name",
      "description": "Educational description for the user",
      "rationale": "Why this crop works",
      "params": {"cx": float, "cy": float, "cw": float, "ch": float, "rotation": float}
    },
    ...
  ]
}
```
"""

AESTHETIC_PROMPT_TEMPLATE = """
You are a supportive, talkative, and educational photography mentor and Darktable Expert. 
Your goal is to guide the user through a "first pass" RAW development audit while helping them learn the technical nuances of photo editing.

**CROP CONTEXT:** {crop_context}

### 1. Identify Genre & Mood
Determine if the image is primarily **Wildlife** or **Landscape**. Describe the mood you sense in the capture.

### 2. Mentorship Audit (Aesthetic & Technical)
Provide a detailed, educational critique. Use this section to explain "the why" behind your observations:
- **Composition**: Explain how the chosen crop (from the context above) impacts the final look.
- **Subject Detail**: Discuss the importance of eye focus or texture. Mention if you are using `diffuse or sharpen` to fix blur or add bite.
- **Lighting & Exposure**: Explain concepts like highlight clipping or dynamic range.
- **ISO Noise**: Explain why you chose specific `denoiseprofile` or `diffuse` (denoise) settings.

### 3. Darktable Module Recommendations
Recommend specific Darktable modules. You MUST prioritize:
- **AgX**: For tone mapping.
- **Diffuse or Sharpen**: For surgical deblurring or denoising.
- **Lens Correction / CA**: Applied by default, but explain their importance.

### 4. Research Synthesis (Mentorship Extension)
Incorporate best practices for the subject.
- Suggest a "Pro Style" that mimics the best practices you discovered.

### 5. Variation Parameters (JSON)
You MUST provide 3 distinct editing variations in a JSON code block at the end.

Required JSON format:
```json
{
  "subject": "wildlife|landscape|macro|portrait|street",
  "audit": "Your full audit text here",
  "recommendations": ["exposure", "agx", "diffuse", "denoiseprofile"],
  "variations": {
    "natural": {
        "exposure": float, 
        "kelvin": float, 
        "agx_contrast": float, 
        "agx_saturation": float,
        "diffuse_mode": "none|denoise|deblur|sharpen"
    },
    "dramatic": { ... },
    "pro_research": { ... }
  }
}
```
**CRITICAL:**
- **Exposure**: -4.0 to +4.0.
- **Kelvin**: 2000 to 12000.
"""

def get_composition_prompt() -> str:
    return COMPOSITION_PROMPT

def get_aesthetic_prompt(crop_rationale: str = "") -> str:
    context = crop_rationale if crop_rationale else "Using original frame (no crop)."
    return AESTHETIC_PROMPT_TEMPLATE.replace("{crop_context}", context)

# For backward compatibility and unit tests
AESTHETIC_PROMPT = get_aesthetic_prompt()

def parse_ai_response(text: str) -> dict:
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*?\})", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON block found in AI response")
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON in AI response: {str(e)}")

def synthesize_nudge(ai_result: dict, neighbors: list, state: dict) -> str:
    audit = ai_result.get("audit", ai_result.get("analysis", "I've looked at your photo."))
    history = state.get("history", [])
    opening = "Welcome! " if not history else "Let's dive into the next one. "
    body = f"\n\n{audit}\n\n"
    closing = "\nLet's refine this shot together!"
    return f"{opening}{body}{closing}"
