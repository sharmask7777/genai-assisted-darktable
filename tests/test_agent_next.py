import pytest
import json
from click.testing import CliRunner
from dt_ai.main import cli
from unittest.mock import patch, MagicMock

def test_agent_next_json_output(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("data")
    
    runner = CliRunner()
    
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze,          patch("dt_ai.main.get_neighboring_files") as mock_neighbors,          patch("dt_ai.main.load_state") as mock_state:
        
        mock_extract.return_value = "test.jpg"
        mock_analyze.return_value = "```json\n{\"audit\": \"AI audit\", \"recommendations\": []}\n```"
        mock_neighbors.return_value = []
        mock_state.return_value = {"history": []}
        
        result = runner.invoke(cli, ['agent-next', str(f)])
        
    assert result.exit_code == 0
    # The output must be valid JSON
    payload = json.loads(result.output)
    assert "nudge" in payload
    assert payload["target_image"] == str(f.absolute())
    assert "ai_result" in payload
