import json
from click.testing import CliRunner
from dt_ai.main import cli
from unittest.mock import patch

def test_sop_handshake_flow(tmp_path):
    shoot_dir = tmp_path / "shoot"
    shoot_dir.mkdir()
    img = shoot_dir / "photo.ARW"
    img.write_text("data")
    
    runner = CliRunner()
    
    # 1. Init Session (as Agent would)
    runner.invoke(cli, ['init-session', str(shoot_dir)])
    
    # 2. Call Next Image (as Agent would)
    with patch("dt_ai.main.extract_preview") as mock_extract,          patch("dt_ai.main.analyze_image") as mock_analyze,          patch("dt_ai.main.parse_ai_response") as mock_parse:
        
        mock_extract.return_value = "photo.jpg"
        mock_analyze.return_value = "raw"
        mock_parse.return_value = {"audit": "Expert thoughts", "recommendations": [], "variations": {}}
        
        result = runner.invoke(cli, ['agent-next', str(img)])
        
    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert "Expert thoughts" in payload["nudge"]
