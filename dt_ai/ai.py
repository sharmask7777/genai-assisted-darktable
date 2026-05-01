import subprocess
import shutil
import os

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
