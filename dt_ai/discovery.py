import os
import glob
from pathlib import Path
from typing import List

RAW_EXTENSIONS = {'.ARW', '.CR2', '.NEF', '.ORF', '.DNG'}

def discover_raw_files(path_pattern: str) -> List[str]:
    """
    Discovers RAW files based on a path, directory, or glob pattern.
    Supports case-insensitive extensions.
    """
    discovered = []
    
    # Handle glob patterns
    if '*' in path_pattern or '?' in path_pattern:
        files = glob.glob(path_pattern, recursive=True)
        for f in files:
            if Path(f).suffix.upper() in RAW_EXTENSIONS:
                discovered.append(os.path.abspath(f))
        return sorted(discovered)

    path = Path(path_pattern)
    
    if not path.exists():
        return []

    if path.is_file():
        if path.suffix.upper() in RAW_EXTENSIONS:
            discovered.append(os.path.abspath(str(path)))
    elif path.is_dir():
        # Search for all files in the directory
        for f in path.iterdir():
            if f.is_file() and f.suffix.upper() in RAW_EXTENSIONS:
                discovered.append(os.path.abspath(str(f)))
                
    return sorted(discovered)
