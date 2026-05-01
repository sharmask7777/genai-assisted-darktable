import pytest
from click.testing import CliRunner
from dt_ai.main import cli
from unittest.mock import patch, MagicMock

def test_edit_command_full_flow(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("dummy")
    
    runner = CliRunner()
    
    # Mock all external systems
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze,          patch("dt_ai.main.generate_variations") as mock_gen,          patch("dt_ai.main.open_in_darktable") as mock_open,          patch("click.confirm") as mock_confirm:
        
        mock_extract.return_value = "test.jpg"
        mock_analyze.return_value = "```json\n{\"audit\": \"A\", \"recommendations\": [\"denoise\"], \"variations\": {}}\n```"
        mock_gen.return_value = ["v1.xmp", "v2.xmp", "v3.xmp"]
        mock_confirm.return_value = True
        
        result = runner.invoke(cli, ['edit', str(f)])
        
    assert result.exit_code == 0
    assert "Processing test.ARW" in result.output
    assert "Take a Call: Denoise recommended" in result.output
    assert "Generated 3 versions" in result.output
    
    # Verify calls
    mock_extract.assert_called_once()
    mock_analyze.assert_called_once()
    mock_gen.assert_called_once()
    mock_open.assert_called_once()
    mock_confirm.assert_called_once()

def test_edit_command_dry_run(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("dummy")
    
    runner = CliRunner()
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze,          patch("dt_ai.main.generate_variations") as mock_gen:
        
        mock_extract.return_value = "test.jpg"
        mock_analyze.return_value = "```json\n{\"audit\": \"A\", \"recommendations\": [], \"variations\": {}}\n```"
        
        result = runner.invoke(cli, ['edit', str(f), '--dry-run'])
        
    assert result.exit_code == 0
    assert "DRY-RUN mode" in result.output
    mock_gen.assert_not_called()
