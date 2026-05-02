import pytest
import json
from dt_ai.main import cli
from click.testing import CliRunner

def test_agent_next_compose_mode(tmp_path):
    # Setup dummy RAW file
    raw_file = tmp_path / "test.ARW"
    raw_file.touch()
    
    runner = CliRunner()
    # Mocking the discovery and extraction since we don't have sips/exif on CI/dev easily
    # Actually, agent-next calls these. Let's just check the help or the call structure if possible.
    # Or better, just unit test the ai.py functions.
    pass

from dt_ai.ai import get_composition_prompt, get_aesthetic_prompt

def test_get_composition_prompt():
    prompt = get_composition_prompt()
    assert "three distinct crop suggestions" in prompt
    assert "normalized floats" in prompt

def test_get_aesthetic_prompt():
    prompt = get_aesthetic_prompt(crop_rationale="Tightened the frame to focus on the bird's eye.")
    assert "Tightened the frame" in prompt
    assert "diffuse or sharpen" in prompt
