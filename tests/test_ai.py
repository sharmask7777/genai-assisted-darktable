import pytest
from unittest.mock import patch, MagicMock
from dt_ai.ai import analyze_image, is_gemini_cli_available
import os

def test_is_gemini_cli_available():
    with patch("shutil.which") as mock_which:
        mock_which.return_value = "/usr/local/bin/gemini-cli"
        assert is_gemini_cli_available() is True
        
        mock_which.return_value = None
        assert is_gemini_cli_available() is False

@patch("dt_ai.ai.is_gemini_cli_available")
@patch("os.path.exists")
def test_analyze_image_success(mock_exists, mock_available):
    mock_available.return_value = True
    mock_exists.return_value = True
    
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stdout="AI Analysis Result")
        
        result = analyze_image("test.jpg", "Analyze this")
        assert result == "AI Analysis Result"
        
        args = mock_run.call_args[0][0]
        assert "gemini-cli" in args
        assert "test.jpg" in args
        assert "Analyze this" in args

@patch("dt_ai.ai.is_gemini_cli_available")
@patch("os.path.exists")
def test_analyze_image_failure(mock_exists, mock_available):
    mock_available.return_value = True
    mock_exists.return_value = True
    
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1, stderr="API Error")
        
        with pytest.raises(RuntimeError) as excinfo:
            analyze_image("test.jpg", "prompt")
        assert "gemini-cli failed" in str(excinfo.value)
