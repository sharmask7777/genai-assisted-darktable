import pytest
import json
import os
from dt_ai.ai import parse_ai_response
from dt_ai.xmp import generate_variations, load_xmp, NS

def test_parse_ai_response_valid():
    text = """
    Here is the audit.
    ```json
    {
        "audit": "Looks good",
        "recommendations": ["exposure"],
        "variations": {
            "natural": {"exposure": 0.5, "kelvin": 5500}
        }
    }
    ```
    """
    result = parse_ai_response(text)
    assert result["audit"] == "Looks good"
    assert result["variations"]["natural"]["exposure"] == 0.5

def test_generate_variations(tmp_path):
    raw = tmp_path / "img.ARW"
    raw.write_text("data")
    
    ai_result = {
        "audit": "Test audit",
        "recommendations": ["exposure", "temperature"],
        "variations": {
            "natural": {"exposure": 0.0, "kelvin": 5500},
            "dramatic": {"exposure": 1.0, "kelvin": 6500},
            "creative": {"exposure": -1.0, "kelvin": 4500}
        }
    }
    
    generated_files = generate_variations(str(raw), ai_result)
    assert len(generated_files) == 3
    
    # Verify the first one (Version 0 since it's greenfield)
    v0 = load_xmp(generated_files[0])
    seq = v0.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    # Should have 6 items: lens, cacorrect, denoiseprofile, exposure, temperature, sigmoid
    assert len(list(seq)) == 6

