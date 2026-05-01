import pytest
import os
import shutil
from dt_ai.parity import AuditEngine, get_progress_dir

def test_audit_engine_generates_report():
    progress_dir = get_progress_dir()
    os.makedirs(progress_dir, exist_ok=True)
    engine = AuditEngine(progress_dir=progress_dir)
    
    internal_data = {
        "prompts": {"aesthetic": "Mentor mode"},
        "xmp_modules": {"exposure": {"version": "6"}}
    }
    external_findings = "Industry standard is now AgX and Workspaces."
    
    report_path = engine.generate_report(internal_data, external_findings)
    
    assert os.path.exists(report_path)
    assert os.path.basename(report_path) == "REPORT.md"
    
    with open(report_path, "r") as f:
        content = f.read()
        assert "Gap Analysis Table" in content
        assert "Missing AgX Support" in content
        assert "Exposure" in content
        assert "Version 6" in content
        
    # Cleanup
    shutil.rmtree(progress_dir)
