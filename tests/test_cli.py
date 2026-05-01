from click.testing import CliRunner
from dt_ai.main import cli
from unittest.mock import patch
import os

def test_audit_dry_run(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("dummy")
    
    runner = CliRunner()
    # Mock extraction and AI to avoid calling sips and gemini
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze:
        
        mock_extract.return_value = "dummy.jpg"
        mock_analyze.return_value = "Aesthetic Audit Text"
        
        result = runner.invoke(cli, ['audit', str(f), '--dry-run'])
    
    assert result.exit_code == 0
    assert "DRY-RUN mode" in result.output
    assert "Discovered 1 RAW file(s)" in result.output
    assert "Extracting preview" in result.output
    assert "Audit report saved" in result.output
    
    audit_file = tmp_path / "test_audit.md"
    assert audit_file.exists()
    assert audit_file.read_text() == "Aesthetic Audit Text"

def test_audit_resilience(tmp_path):
    f1 = tmp_path / "good.ARW"
    f1.write_text("d1")
    f2 = tmp_path / "bad.ARW"
    f2.write_text("d2")
    
    runner = CliRunner()
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze:
        
        # Fail extraction on bad.ARW
        def side_effect(path, output_path=None):
            if "bad.ARW" in path:
                raise RuntimeError("Extraction failed")
            return "good.jpg"
        
        mock_extract.side_effect = side_effect
        mock_analyze.return_value = "Good Audit"
        
        result = runner.invoke(cli, ['audit', str(tmp_path)])
    
    assert result.exit_code == 0
    assert "good.ARW" in result.output
    assert "bad.ARW" in result.output
    assert "Error: Extraction failed" in result.output
    assert "Audit report saved: good_audit.md" in result.output
