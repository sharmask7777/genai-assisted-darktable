import pytest
import os
import json
from pathlib import Path
from dt_ai.state import load_state, save_state, get_state_path

def test_get_state_path(tmp_path):
    shoot_dir = tmp_path / "shoot1"
    shoot_dir.mkdir()
    
    # Should be in the parent of shoot1
    expected = tmp_path / ".dt-ai-progress.json"
    assert get_state_path(str(shoot_dir)) == expected

def test_load_state_default(tmp_path):
    shoot_dir = tmp_path / "new_shoot"
    shoot_dir.mkdir()
    state = load_state(str(shoot_dir))
    
    assert state["project_path"] == str(shoot_dir.absolute())
    assert state["history"] == []
    assert state["last_processed"] is None

def test_save_and_load_roundtrip(tmp_path):
    shoot_dir = tmp_path / "shoot2"
    shoot_dir.mkdir()
    
    initial_state = load_state(str(shoot_dir))
    initial_state["history"].append({"image": "img1.ARW", "styles": ["natural"]})
    initial_state["last_processed"] = "img1.ARW"
    
    save_state(str(shoot_dir), initial_state)
    
    # Verify file exists in parent
    state_file = tmp_path / ".dt-ai-progress.json"
    assert state_file.exists()
    
    reloaded = load_state(str(shoot_dir))
    assert reloaded["last_processed"] == "img1.ARW"
    assert len(reloaded["history"]) == 1
