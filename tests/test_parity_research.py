import pytest
import os
import shutil
from dt_ai.parity import ExternalResearcher, get_progress_dir

def test_external_researcher_saves_files():
    progress_dir = get_progress_dir()
    researcher = ExternalResearcher(progress_dir=progress_dir)
    
    def mock_search(query):
        return f"Results for {query}"
        
    query = "latest darktable changes 2026"
    researcher.perform_search(mock_search, query)
    
    # Verify directory and file exist
    assert os.path.exists(os.path.join(progress_dir, "research"))
    
    # Expected filename based on slug logic
    filename = "latest_darktable_changes_2026.txt"
    file_path = os.path.join(progress_dir, "research", filename)
    assert os.path.exists(file_path)
    
    with open(file_path, "r") as f:
        assert f.read() == f"Results for {query}"
        
    # Cleanup
    shutil.rmtree(progress_dir)

def test_get_progress_dir_is_hidden():
    dir_name = get_progress_dir()
    assert dir_name.startswith(".")
    assert "parity-sync" in dir_name
