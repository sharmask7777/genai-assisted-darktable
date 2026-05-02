import pytest
import os
import struct
import xml.etree.ElementTree as ET
from dt_ai.xmp import generate_crop_previews, load_xmp

# Namespace mapping for XMP parsing
NS = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'darktable': 'http://darktable.sf.net/'
}

def test_crop_coordinate_conversion(tmp_path):
    # Setup dummy RAW file
    raw_file = tmp_path / "test_math.ARW"
    raw_file.touch()
    
    # 1. Center crop: cx=0.5, cy=0.5, cw=0.5, ch=0.5
    # Should result in left=0.25, top=0.25
    suggestions = {
        "options": [
            {
                "id": 1,
                "name": "Center Crop",
                "params": {"cx": 0.5, "cy": 0.5, "cw": 0.5, "ch": 0.5, "rotation": 0.0}
            },
            {
                "id": 2,
                "name": "Edge Case",
                "params": {"cx": 0.1, "cy": 0.1, "cw": 0.4, "ch": 0.4, "rotation": 0.0}
            }
        ]
    }
    
    generate_crop_previews(str(raw_file), suggestions)
    
    # Verify Version 01 (Center Crop)
    xmp_v1 = tmp_path / "test_math_01.ARW.xmp"
    assert xmp_v1.exists()
    
    root = ET.parse(xmp_v1)
    # Find the clipping params
    history = root.find(".//{http://darktable.sf.net/}history/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
    clipping_item = None
    for li in history:
        if li.get("{http://darktable.sf.net/}operation") == "clipping":
            clipping_item = li
            break
            
    assert clipping_item is not None
    params_hex = clipping_item.get("{http://darktable.sf.net/}params")
    data = bytes.fromhex(params_hex)
    angle, cx, cy, cw, ch = struct.unpack('<fffff', data[:20])
    
    assert cx == pytest.approx(0.5)
    assert cy == pytest.approx(0.5)
    assert cw == pytest.approx(0.5)
    assert ch == pytest.approx(0.5)

    # Verify Version 02 (Edge Case: cx=0.1, cy=0.1, cw=0.4, ch=0.4)
    xmp_v2 = tmp_path / "test_math_02.ARW.xmp"
    root = ET.parse(xmp_v2)
    history = root.find(".//{http://darktable.sf.net/}history/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
    clipping_item = None
    for li in history:
        if li.get("{http://darktable.sf.net/}operation") == "clipping":
            clipping_item = li
            break
            
    params_hex = clipping_item.get("{http://darktable.sf.net/}params")
    data = bytes.fromhex(params_hex)
    angle, cx, cy, cw, ch = struct.unpack('<fffff', data[:20])
    
    assert cx == pytest.approx(0.1)
    assert cy == pytest.approx(0.1)
    assert cw == pytest.approx(0.4)
    assert ch == pytest.approx(0.4)
