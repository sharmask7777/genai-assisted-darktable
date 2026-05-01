import subprocess
import shutil
import os

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
Recommend 2-3 specific Darktable modules to address identified issues. Use the exact names of the modules:
- 'Exposure': For overall brightness and dynamic range.
- 'Tone Equalizer': For localized shadow/highlight recovery.
- 'Denoise (profiled)': For sensor noise reduction.
- 'Diffuse or Sharpen': For local contrast or sharpness.
- 'Color Balance RGB': For creative color grading or white balance correction.

### 4. Output Format
Provide your response in structured Markdown. Use headings for each section. Keep the tone professional, encouraging, and highly technical.
"""

def is_gemini_cli_available() -> bool:
    """Checks if gemini-cli is installed and in the system PATH."""
    return shutil.which("gemini-cli") is not None

def analyze_image(preview_path: str, prompt: str) -> str:
    """
    Sends an image preview to Gemini CLI for analysis.
    
    Args:
        preview_path: Path to the JPEG preview file.
        prompt: The instructions/prompt for the AI.
        
    Returns:
        The text response from Gemini.
        
    Raises:
        RuntimeError: If gemini-cli is missing or execution fails.
    """
    if not is_gemini_cli_available():
        raise RuntimeError("gemini-cli not found. Please install it to use AI features.")
        
    if not os.path.exists(preview_path):
        raise FileNotFoundError(f"Preview file not found: {preview_path}")

    cmd = [
        "gemini-cli",
        preview_path,
        prompt
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"gemini-cli failed: {result.stderr}")
        
    return result.stdout.strip()
