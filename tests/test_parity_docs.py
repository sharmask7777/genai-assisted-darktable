import pytest
import os
import shutil
from dt_ai.parity import DocUpdater

def test_doc_updater_updates_readme():
    temp_dir = "/tmp/test_readme_parity"
    os.makedirs(temp_dir, exist_ok=True)
    readme_path = os.path.join(temp_dir, "README.md")
    
    # Start with empty readme
    with open(readme_path, "w") as f:
        f.write("# Project Name")
        
    updater = DocUpdater(repo_root=temp_dir)
    updater.update_readme()
    
    with open(readme_path, "r") as f:
        content = f.read()
        assert "GenAI Skills" in content
        assert "darktable-parity-sync" in content
        assert "Claude:" in content
        
    shutil.rmtree(temp_dir)
