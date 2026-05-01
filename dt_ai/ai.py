import subprocess
import shutil
import os
import json
import re

AESTHETIC_PROMPT = """
You are a supportive, talkative, and educational photography mentor and Darktable Expert. 
Your goal is to guide the user through a "first pass" RAW development audit while helping them learn the technical nuances of photo editing.

### 1. Identify Genre & Mood
Determine if the image is primarily **Wildlife** or **Landscape**. Describe the mood you sense in the capture.

### 2. Mentorship Audit (Aesthetic & Technical)
Provide a detailed, educational critique. Use this section to explain "the why" behind your observations:
- **Composition**: Explain subject placement (e.g., Rule of Thirds). If you see distractions, explain how they impact the viewer's eye.
- **Subject Detail**: For wildlife, discuss the importance of eye focus. For landscapes, explain foreground/background clarity and depth of field.
- **Lighting & Exposure**: Don't just identify issues; explain concepts like highlight clipping or dynamic range.
- **ISO Noise**: Explain what sensor noise is in this specific context and why cleanup might be necessary.

### 3. Darktable Module Recommendations
Recommend specific Darktable modules. For each, give a 1-sentence "mentor tip" on how it works.

### 4. Variation Parameters (JSON)
You MUST provide 3 distinct editing variations in a JSON code block at the end.
- **natural**: Balanced, accurate, "true-to-life".
- **dramatic**: High contrast, moody, explain how you're using light here.
- **creative**: An artistic interpretation to inspire the user.

Required JSON format:
```json
{
  "audit": "Your full, talkative, and educational audit text here",
  "recommendations": ["exposure", "denoiseprofile", ...],
  "variations": {
    "natural": {"exposure": float_ev, "kelvin": float_k},
    "dramatic": {"exposure": float_ev, "kelvin": float_k},
    "creative": {"exposure": float_ev, "kelvin": float_k}
  }
}
```
Keep Kelvin values between 2000 and 12000. Exposure between -4.0 and +4.0.
"""

def is_gemini_cli_available() -> bool:
    """Checks if gemini-cli is installed and in the system PATH."""
    return shutil.which("gemini-cli") is not None

def parse_ai_response(text: str) -> dict:
    """
    Extracts the JSON block from the AI's response.
    """
    # Look for JSON block
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON block found in AI response")
    
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON in AI response: {str(e)}")

def analyze_image(preview_path: str, prompt: str) -> str:
    """
    Sends an image preview to Gemini CLI for analysis.
    """
    if not is_gemini_cli_available():
        raise RuntimeError("gemini-cli not found. Please install it to use AI features.")
        
    if not os.path.exists(preview_path):
        raise FileNotFoundError(f"Preview file not found: {preview_path}")

    cmd = ["gemini-cli", preview_path, prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"gemini-cli failed: {result.stderr}")
        
    return result.stdout.strip()

def synthesize_nudge(ai_result: dict, neighbors: list, state: dict) -> str:
    """
    Combines AI analysis with project context to create a talkative mentorship nudge.
    """
    audit = ai_result.get("audit", "I've looked at your photo and have some thoughts.")
    history = state.get("history", [])
    
    # 1. Greeting / Contextual Opening
    if not history:
        opening = "Welcome to our first image of this session! "
    else:
        opening = f"Great work on those previous shots. Let's dive into the next one. "
        
    # 2. Main Audit
    body = f"\n\n{audit}\n\n"
    
    # 3. Lookahead Context
    context_note = ""
    if neighbors:
        context_note = (
            f"I've also peeked at the {len(neighbors)} adjacent frames in your folder to get a better sense of the sequence. "
            "This seems like a particularly strong moment to focus our efforts on! "
        )
        
    # 4. Technical Advice / Next Steps
    closing = (
        "\nI've gone ahead and generated three variations in Darktable for you to explore. "
        "Feel free to tweak my suggestions—your artistic eye is the final judge. "
        "Let me know when you're ready to move to the next frame!"
    )
    
    return f"{opening}{context_note}{body}{closing}"
