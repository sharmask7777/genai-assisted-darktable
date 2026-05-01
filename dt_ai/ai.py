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
- **dramatic**: High contrast, moody, high impact.
- **creative**: An artistic interpretation to inspire the user.

Required JSON format:
```json
{
  "audit": "Your full, talkative, and educational audit text here",
  "recommendations": ["exposure", "temperature", "colorbalance rgb"],
  "variations": {
    "natural": {"exposure": float_ev, "kelvin": float_k},
    "dramatic": {"exposure": float_ev, "kelvin": float_k},
    "creative": {"exposure": float_ev, "kelvin": float_k}
  }
}
```
**CRITICAL TECHNICAL CONSTRAINTS:**
- **Exposure**: Range -4.0 to +4.0. (Maps to Darktable Exposure v6).
- **Kelvin**: Range 2000.0 to 12000.0. (Maps to Darktable Temperature v3).
- **Format**: Ensure numbers are standard floats.
"""

def parse_ai_response(text: str) -> dict:
    """
    Extracts the JSON block from the AI's response.
    """
    # Look for JSON block
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        # Try to find any JSON-like structure if code blocks are missing
        match = re.search(r"(\{.*?\})", text, re.DOTALL)
        
    if not match:
        raise ValueError("No JSON block found in AI response")
    
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON in AI response: {str(e)}")

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
