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
        mock_neighbors.return_value = ["n1.ARW", "n2.ARW"]
        mock_state.return_value = {"history": []}
        
        result = runner.invoke(cli, ['agent-next', str(f)])
        
    assert result.exit_code == 0
    payload = json.loads(result.output)
    
    # Check for preview mapping
    assert "previews" in payload
    assert payload["previews"][str(f.absolute())] == "test.jpg"
    # Verify mock_extract was called for target + 2 neighbors
    assert mock_extract.call_count == 3

def test_agent_next_neighbor_resilience(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("data")
    
    runner = CliRunner()
    
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze,          patch("dt_ai.main.get_neighboring_files") as mock_neighbors,          patch("dt_ai.main.load_state") as mock_state:
        
        def side_effect(path, output_path=None):
            if "n1.ARW" in path:
                raise RuntimeError("Extraction failed")
            return "ok.jpg"
            
        mock_extract.side_effect = side_effect
        mock_analyze.return_value = "```json\n{\"audit\": \"A\", \"recommendations\": []}\n```"
        mock_neighbors.return_value = ["n1.ARW"]
        mock_state.return_value = {"history": []}
        
        result = runner.invoke(cli, ['agent-next', str(f)])
        
    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert payload["previews"][str(f.absolute())] == "ok.jpg"
    assert "n1.ARW" not in payload["previews"]
