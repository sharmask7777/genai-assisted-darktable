import pytest
from unittest.mock import patch, MagicMock
from dt_ai.processor import extract_preview
import os

def test_extract_preview_command_generation():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)
        
        # We need a real file to pass the existence check
        with open("dummy.raw", "w") as f:
            f.write("data")
            
        try:
            extract_preview("dummy.raw", "output.jpg")
            
            mock_run.assert_called_once()
            args = mock_run.call_args[0][0]
            assert "sips" in args
            assert "--resampleHeightWidthMax" in args
            assert "2048" in args
            assert "dummy.raw" in args
            assert "output.jpg" in args
        finally:
            if os.path.exists("dummy.raw"):
                os.remove("dummy.raw")

def test_extract_preview_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_preview("non_existent.raw", "output.jpg")

def test_extract_preview_sips_failure():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1, stderr="sips error")
        
        with open("dummy.raw", "w") as f:
            f.write("data")
            
        try:
            with pytest.raises(RuntimeError) as excinfo:
                extract_preview("dummy.raw", "output.jpg")
            assert "sips failed" in str(excinfo.value)
        finally:
            if os.path.exists("dummy.raw"):
                os.remove("dummy.raw")
