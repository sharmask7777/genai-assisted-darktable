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

def get_neighboring_files(target_path: str, count: int = 2) -> List[str]:
    """
    Returns up to 'count' files before and after the target file in the same directory.
    Files are sorted alphabetically.
    """
    abs_target = os.path.abspath(target_path)
    dir_path = os.path.dirname(abs_target)
    
    # Use existing discovery to get all RAW files in the directory
    all_files = discover_raw_files(dir_path)
    
    if abs_target not in all_files:
        return []
        
    idx = all_files.index(abs_target)
    
    before = all_files[max(0, idx - count):idx]
    after = all_files[idx + 1:min(len(all_files), idx + 1 + count)]
    
    return before + after
