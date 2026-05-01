import pytest
import os
from dt_ai.discovery import get_raw_metadata

def test_get_raw_metadata_missing_file():
    """Should return empty dict or handle error gracefully for non-existent files."""
    meta = get_raw_metadata("/tmp/non_existent.ARW")
    assert meta == {}

def test_get_raw_metadata_structure():
    """
    Since we don't have a real RAW file for testing in CI usually, 
    we test that the function exists and has the right interface.
    """
    # This will likely return empty or basic info if exiftool isn't present
    # but we want to define what we NEED.
    meta = get_raw_metadata("dummy.ARW")
    assert isinstance(meta, dict)
