import os
from click.testing import CliRunner
from dt_ai.main import cli
from unittest.mock import patch

def test_edit_command_still_works(tmp_path):
    f = tmp_path / "legacy.ARW"
    f.write_text("data")
    runner = CliRunner()
    
    with patch("dt_ai.main.extract_preview") as mock_ext,          patch("dt_ai.main.analyze_image") as mock_ai,          patch("dt_ai.main.parse_ai_response") as mock_parse:
        
        mock_ext.return_value = "l.jpg"
        mock_ai.return_value = "r"
        mock_parse.return_value = {"audit": "A", "recommendations": [], "variations": {}}
        
        # Should still be able to run bulk edit manually
        result = runner.invoke(cli, ['edit', str(f)])
        assert result.exit_code == 0
        assert "PIPELINE COMPLETE" in result.output
