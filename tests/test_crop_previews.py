import pytest
import os
import json
from dt_ai.main import cli
from click.testing import CliRunner

def test_apply_variations_crop_preview(tmp_path):
    # Setup dummy RAW file and state
    raw_file = tmp_path / "test.ARW"
    raw_file.touch()
    
    # Mock AI result for cropping
    crop_suggestions = {
        "options": [
            {
                "id": 1,
                "name": "Rule of Thirds",
                "params": {"cx": 0.1, "cy": 0.1, "cw": 0.8, "ch": 0.8, "rotation": 0.0}
            },
            {
                "id": 2,
                "name": "Tight Crop",
                "params": {"cx": 0.2, "cy": 0.2, "cw": 0.6, "ch": 0.6, "rotation": 1.5}
            }
        ]
    }
    
    runner = CliRunner()
    result = runner.invoke(cli, ['apply-variations', str(raw_file), json.dumps(crop_suggestions), '--mode', 'crop-preview'])
    
    assert result.exit_code == 0
    output = json.loads(result.output)
    assert len(output["versions"]) == 2
    assert os.path.exists(tmp_path / "test_01.ARW.xmp")
    assert os.path.exists(tmp_path / "test_02.ARW.xmp")
