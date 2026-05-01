import pytest
import os
from dt_ai.discovery import get_neighboring_files

def test_get_neighbors_central(tmp_path):
    files = []
    for i in range(5):
        f = tmp_path / f"img_{i}.ARW"
        f.write_text("d")
        files.append(str(f.absolute()))
    
    target = files[2] # img_2.ARW
    neighbors = get_neighboring_files(target, count=2)
    
    # Should be 0, 1, 3, 4
    assert len(neighbors) == 4
    assert files[0] in neighbors
    assert files[1] in neighbors
    assert files[3] in neighbors
    assert files[4] in neighbors
    assert target not in neighbors

def test_get_neighbors_start(tmp_path):
    files = []
    for i in range(5):
        f = tmp_path / f"img_{i}.ARW"
        f.write_text("d")
        files.append(str(f.absolute()))
    
    target = files[0]
    neighbors = get_neighboring_files(target, count=2)
    
    assert len(neighbors) == 2
    assert files[1] in neighbors
    assert files[2] in neighbors

def test_get_neighbors_end(tmp_path):
    files = []
    for i in range(5):
        f = tmp_path / f"img_{i}.ARW"
        f.write_text("d")
        files.append(str(f.absolute()))
    
    target = files[4]
    neighbors = get_neighboring_files(target, count=2)
    
    assert len(neighbors) == 2
    assert files[2] in neighbors
    assert files[3] in neighbors
