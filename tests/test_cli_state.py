import pytest
from click.testing import CliRunner
from dt_ai.main import cli
import os
import json

def test_init_session_new(tmp_path):
    shoot_dir = tmp_path / "shoot"
    shoot_dir.mkdir()
    
    runner = CliRunner()
    result = runner.invoke(cli, ['init-session', str(shoot_dir)])
    
    assert result.exit_code == 0
    assert "Started new session" in result.output
    # Verify file created in parent
    assert (tmp_path / ".dt-ai-progress.json").exists()

def test_init_session_resumed(tmp_path):
    shoot_dir = tmp_path / "existing"
    shoot_dir.mkdir()
    state_file = tmp_path / ".dt-ai-progress.json"
    state_file.write_text(json.dumps({"history": []}))
    
    runner = CliRunner()
    result = runner.invoke(cli, ['init-session', str(shoot_dir)])
    
    assert result.exit_code == 0
    assert "Resuming existing session" in result.output

def test_init_session_invalid():
    runner = CliRunner()
    result = runner.invoke(cli, ['init-session', '/non/existent/path'])
    assert result.exit_code != 0
    assert "Error" in result.output
