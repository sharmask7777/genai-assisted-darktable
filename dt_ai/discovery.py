import os
import glob
import subprocess
import json
from pathlib import Path
from typing import List, Dict

RAW_EXTENSIONS = {'.ARW', '.CR2', '.NEF', '.ORF', '.DNG', '.JPG', '.JPEG'}

def get_raw_metadata(path: str) -> Dict[str, str]:
    """
    Extracts metadata from an image file using macOS native tools (mdls and sips).
    Returns a dictionary of keys: model, lens, iso, exposure, aperture.
    """
    if not os.path.exists(path):
        return {}

    metadata = {}
    
    # 1. Try mdls first (best for macOS metadata indexing)
    try:
        cmd = ['mdls', '-name', 'kMDItemModel', '-name', 'kMDItemLensModel', 
               '-name', 'kMDItemISOSpeed', '-name', 'kMDItemExposureTimeSeconds', 
               '-name', 'kMDItemFNumber', path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout
            mdls_mappings = {
                'kMDItemModel': 'model',
                'kMDItemLensModel': 'lens',
                'kMDItemISOSpeed': 'iso',
                'kMDItemExposureTimeSeconds': 'exposure',
                'kMDItemFNumber': 'aperture'
            }
            for line in output.splitlines():
                for key, internal in mdls_mappings.items():
                    if key in line and '=' in line:
                        val = line.split("=", 1)[1].strip()
                        if val != "(null)":
                            metadata[internal] = val.strip('"')
    except Exception:
        pass

    # 2. Use sips as fallback or for missing keys
    try:
        result = subprocess.run(['sips', '-g', 'all', path], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout
            sips_mappings = {
                'model': 'model',
                'lensModel': 'lens',
                'ISO': 'iso',
                'exposureTime': 'exposure',
                'aperture': 'aperture'
            }
            
            for line in output.splitlines():
                line = line.strip()
                for sips_key, internal_key in sips_mappings.items():
                    if f" {sips_key}:" in line and not metadata.get(internal_key):
                        val = line.split(":", 1)[1].strip()
                        metadata[internal_key] = val
    except Exception:
        pass
                    
    return metadata

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
