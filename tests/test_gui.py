import pytest
from unittest.mock import patch, MagicMock
from dt_ai.gui import open_in_darktable

@patch("subprocess.run")
def test_open_in_darktable(mock_run):
    open_in_darktable("test.ARW")
    mock_run.assert_called_once()
    args = mock_run.call_args[0][0]
    assert args == ["open", "-a", "darktable", "test.ARW"]

def test_denoise_detection():
    # We will test the detection logic that we'll add to main.py
    from dt_ai.main import needs_denoise_interaction
    assert needs_denoise_interaction(["exposure", "denoiseprofile"]) is True
    assert needs_denoise_interaction(["exposure", "denoise"]) is True
    assert needs_denoise_interaction(["exposure", "sharpen"]) is False
