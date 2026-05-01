import json
import os
from pathlib import Path
from typing import Dict, Any

STATE_FILENAME = ".dt-ai-progress.json"

def get_state_path(image_dir: str) -> Path:
    """
    Returns the path to the state file, which lives in the parent of the image directory.
    """
    path = Path(image_dir).absolute()
    # If it's a file, get its directory first
    if path.is_file():
        path = path.parent
    return path.parent / STATE_FILENAME

def load_state(image_dir: str) -> Dict[str, Any]:
    """
    Loads the session state from the parent directory.
    Returns a default state if no file exists.
    """
    state_path = get_state_path(image_dir)
    abs_image_dir = str(Path(image_dir).absolute())
    
    if state_path.exists():
        try:
            with open(state_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            # Fallback to default on error
            pass
            
    return {
        "project_path": abs_image_dir,
        "history": [],
        "last_processed": None,
        "session_started": None # Can be added later if needed
    }

def save_state(image_dir: str, state: Dict[str, Any]):
    """
    Saves the session state to the parent directory.
    """
    state_path = get_state_path(image_dir)
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
