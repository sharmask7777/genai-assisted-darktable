import pytest
import struct
import xml.etree.ElementTree as ET
from dt_ai.xmp import generate_crop_previews, load_xmp, NS

def test_clipping_v5_parity(tmp_path):
    # Setup dummy RAW file
    raw_file = tmp_path / "parity.ARW"
    raw_file.touch()
    
    # Suggest a crop
    suggestions = {
        "options": [
            {
                "id": 1,
                "name": "Parity Crop",
                "params": {"cx": 0.5, "cy": 0.5, "cw": 0.5, "ch": 0.5, "rotation": 0.0}
            }
        ]
    }
    
    # We will modify generate_crop_previews to use clipping v5 in the next step.
    # For now, let's see what happens.
    generate_crop_previews(str(raw_file), suggestions)
    
    xmp_v1 = tmp_path / "parity_01.ARW.xmp"
    assert xmp_v1.exists()
    
    root = ET.parse(xmp_v1)
    history = root.find(".//{http://darktable.sf.net/}history/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
    
    clipping_item = None
    for li in history:
        if li.get("{http://darktable.sf.net/}operation") == "clipping":
            clipping_item = li
            break
            
    # assert clipping_item is not None
    assert clipping_item is not None
    assert clipping_item.get("{http://darktable.sf.net/}operation") == "clipping"
    assert clipping_item.get("{http://darktable.sf.net/}modversion") == "5"
