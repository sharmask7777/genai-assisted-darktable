import pytest
import os
from dt_ai.main import generate_preflight_report

def test_generate_preflight_report_contents():
    """Verify that the report contains metadata and planned actions."""
    image_path = "/path/to/test_image.ARW"
    ai_result = {
        "analysis": "Test bird photo",
        "variations": {
            "Natural": {"exposure": 0.5, "kelvin": 5500},
            "Dramatic": {"exposure": -1.0, "kelvin": 6000}
        }
    }
    metadata = {
        "model": "ILCE-7M3",
        "lens": "FE 200-600mm",
        "iso": "100"
    }
    ai_result["subject"] = "wildlife"
    
    report = generate_preflight_report(image_path, ai_result, metadata)
    
    assert "WILDLIFE" in report
    assert "ILCE-7M3" in report
    assert "FE 200-600mm" in report
    assert "SENSOR FIX" in report # Should trigger because ILCE-7M3 is in database
    assert "NATURAL" in report
    assert "DRAMATIC" in report
    assert "AgX" in report

def test_generate_preflight_report_with_research():
    """Verify that the report includes research insights."""
    image_path = "test.ARW"
    ai_result = {
        "research_rationale": "Pros use high contrast for raptors.",
        "variations": {"pro_research": {"exposure": 0.0}}
    }
    metadata = {}
    report = generate_preflight_report(image_path, ai_result, metadata)
    assert "RESEARCH INSIGHT" in report
    assert "Pros use high contrast" in report
