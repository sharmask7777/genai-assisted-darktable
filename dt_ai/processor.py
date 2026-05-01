import subprocess
import os
import hashlib
from pathlib import Path

PREVIEW_DIR = ".dt-ai/previews"

def get_preview_path(input_path: str) -> str:
    """
    Generates a deterministic and collision-safe path for the JPEG preview.
    """
    abs_path = os.path.abspath(input_path)
    # Generate a short hash of the absolute path to prevent collisions
    path_hash = hashlib.md5(abs_path.encode()).hexdigest()[:8]
    
    input_path_obj = Path(input_path)
    filename = f"{input_path_obj.stem}_{path_hash}.jpg"
    
    return os.path.join(PREVIEW_DIR, filename)

def extract_preview(input_path: str, output_path: str = None) -> str:
    """
    Extracts a 2048px JPEG preview from a RAW file using macOS sips.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if output_path is None:
        output_path = get_preview_path(input_path)
        
    parent_dir = os.path.dirname(output_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
        
    cmd = [
        "sips",
        "-s", "format", "jpeg",
        "--resampleHeightWidthMax", "2048",
        input_path,
        "--out", output_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"sips failed: {result.stderr}")
        
    return output_path
