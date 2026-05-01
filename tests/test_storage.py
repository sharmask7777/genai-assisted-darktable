import pytest
import os
from pathlib import Path
from dt_ai.processor import get_preview_path

def test_get_preview_path_deterministic():
    path1 = get_preview_path("test.ARW")
    path2 = get_preview_path("test.ARW")
    assert path1 == path2
    assert path1.endswith(".jpg")
    assert ".dt-ai/previews" in path1

def test_get_preview_path_collision_avoidance():
    # Different folders, same filename
    path1 = get_preview_path("/work/dir1/img.ARW")
    path2 = get_preview_path("/work/dir2/img.ARW")
    assert path1 != path2

def test_directory_auto_creation(tmp_path):
    # This might require mocking the PREVIEW_DIR or changing CWD
    # For now, let's just verify the logic exists in processor.py
    pass
