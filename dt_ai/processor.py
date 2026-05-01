import subprocess
import os

def extract_preview(input_path: str, output_path: str) -> str:
    """
    Extracts a 2048px JPEG preview from a RAW file using macOS sips.
    
    Args:
        input_path: Path to the RAW source file.
        output_path: Path where the JPEG preview should be saved.
        
    Returns:
        The path to the generated JPEG preview.
        
    Raises:
        FileNotFoundError: If the input file does not exist.
        RuntimeError: If sips execution fails.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
        
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
