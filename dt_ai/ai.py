import subprocess
import shutil
import os
import json
import re

AESTHETIC_PROMPT = """
You are a Senior Photography Editor and Darktable Expert. 
Analyze the provided image preview for a "first pass" RAW development audit.

### 1. Identify Genre
Determine if the image is primarily **Wildlife** or **Landscape**.

### 2. Aesthetic & Technical Audit
Comment on the following:
- **Composition**: Subject placement (e.g., Rule of Thirds), balance, and distracting elements.
- **Subject Detail**: For wildlife, check eye sharpness and feather/fur detail. For landscapes, check foreground/background clarity.
- **Lighting & Exposure**: Identify highlight clipping, blocked shadows, or dynamic range issues.
- **Noise**: Evaluate if the ISO noise is distracting or requires specialized cleanup.

### 3. Darktable Module Recommendations
Recommend specific Darktable modules to address identified issues.

### 4. Variation Parameters (JSON)
You MUST also provide 3 distinct editing variations in a JSON code block at the end of your response.
Variation styles:
- **natural**: Balanced, accurate, "true-to-life".
- **dramatic**: High contrast, punchy colors, moody.
- **creative**: Artistic interpretation (e.g., high-key, low-key, or specific color grade).

Required JSON format:
```json
{
  "audit": "Summary of your audit text here",
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
