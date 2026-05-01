import pytest
import os
from dt_ai.discovery import discover_raw_files

def test_discover_single_file(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("dummy")
    results = discover_raw_files(str(f))
    assert len(results) == 1
    assert results[0].endswith("test.ARW")

def test_discover_directory(tmp_path):
    (tmp_path / "a.ARW").write_text("d")
    (tmp_path / "b.NEF").write_text("d")
    (tmp_path / "c.jpg").write_text("d")
    results = discover_raw_files(str(tmp_path))
    assert len(results) == 2
    assert any(f.endswith("a.ARW") for f in results)
    assert any(f.endswith("b.NEF") for f in results)

def test_discover_glob(tmp_path):
    subdir = tmp_path / "sub"
    subdir.mkdir()
    (subdir / "a.ARW").write_text("d")
    (tmp_path / "b.ARW").write_text("d")
    # Using python glob pattern
    results = discover_raw_files(str(tmp_path / "**/*.ARW"))
    assert len(results) == 2
