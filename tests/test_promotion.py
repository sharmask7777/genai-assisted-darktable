import pytest
import os
from dt_ai.main import cli
from click.testing import CliRunner

def test_promote_variation(tmp_path):
    raw_file = tmp_path / "test.jpg"
    raw_file.touch()
    
    # Create a dummy crop sidecar
    crop_xmp = tmp_path / "test_01.jpg.xmp"
    crop_xmp.write_text("crop_data")
    
    runner = CliRunner()
    # This command now exists
    result = runner.invoke(cli, ['promote-variation', str(raw_file), '1'])
    
    assert result.exit_code == 0
    # The original sidecar should now match the crop sidecar
    base_xmp = tmp_path / "test.jpg.xmp"
    assert base_xmp.exists()
    assert base_xmp.read_text() == "crop_data"
    
    # Other previews should be cleaned up (if we added a cleanup flag)
