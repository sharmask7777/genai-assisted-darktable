import pytest
import os
import shutil
from unittest.mock import MagicMock
from dt_ai.parity import TDDOrchestrator, get_progress_dir

def test_tdd_orchestrator_creates_plan():
    progress_dir = get_progress_dir()
    os.makedirs(progress_dir, exist_ok=True)
    orchestrator = TDDOrchestrator(progress_dir=progress_dir)
    
    plan_path = orchestrator.create_plan("REPORT.md")
    
    assert os.path.exists(plan_path)
    with open(plan_path, "r") as f:
        content = f.read()
        assert "TDD Implementation Plan" in content
        assert "Task 1" in content
        
    shutil.rmtree(progress_dir)

def test_tdd_orchestrator_runs_test_and_logs():
    progress_dir = get_progress_dir()
    os.makedirs(progress_dir, exist_ok=True)
    orchestrator = TDDOrchestrator(progress_dir=progress_dir)
    
    # Create a dummy test file
    test_path = "tests/test_dummy_parity.py"
    with open(test_path, "w") as f:
        f.write("def test_pass(): assert True")
        
    success = orchestrator.run_test(test_path)
    
    assert success is True
    assert os.path.exists(os.path.join(progress_dir, "logs"))
    
    # Cleanup dummy test and progress dir
    os.remove(test_path)
    shutil.rmtree(progress_dir)

def test_tdd_orchestrator_applies_fix():
    orchestrator = TDDOrchestrator(progress_dir="/tmp/dummy")
    mock_fix = MagicMock()
    
    orchestrator.apply_fix(mock_fix)
    
    mock_fix.assert_called_once()
