import pytest
import os
from dt_ai.xmp import get_next_version_path

def test_get_next_version_path_greenfield(tmp_path):
    raw = tmp_path / "img.ARW"
    raw.write_text("d")
    # No xmp exists
    assert get_next_version_path(str(raw)) == str(tmp_path / "img.ARW.xmp")

def test_get_next_version_path_first_duplicate(tmp_path):
    raw = tmp_path / "img.ARW"
    raw.write_text("d")
    (tmp_path / "img.ARW.xmp").write_text("x")
    
    # img.ARW.xmp exists, so next should be img_01.ARW.xmp
    assert get_next_version_path(str(raw)) == str(tmp_path / "img_01.ARW.xmp")

def test_get_next_version_path_sequential(tmp_path):
    raw = tmp_path / "img.ARW"
    raw.write_text("d")
    (tmp_path / "img.ARW.xmp").write_text("x")
    (tmp_path / "img_01.ARW.xmp").write_text("x")
    
    assert get_next_version_path(str(raw)) == str(tmp_path / "img_02.ARW.xmp")
