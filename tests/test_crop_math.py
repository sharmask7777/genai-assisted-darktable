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
    
    # Verify Version 01 (Center Crop: cx=0.5, cy=0.5, cw=0.5, ch=0.5)
    # Resulting: left=0.25, top=0.25, right=0.75, bottom=0.75
    xmp_v1 = tmp_path / "test_math_01.ARW.xmp"
    assert xmp_v1.exists()
    
    root = ET.parse(xmp_v1)
    # Find the crop params
    history = root.find(".//{http://darktable.sf.net/}history/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
    crop_item = None
    for li in history:
        if li.get("{http://darktable.sf.net/}operation") == "crop":
            crop_item = li
            break
            
    assert crop_item is not None
    params_hex = crop_item.get("{http://darktable.sf.net/}params")
    data = bytes.fromhex(params_hex)
    left, top, right, bottom = struct.unpack('<ffff', data[:16])
    
    assert left == pytest.approx(0.25)
    assert top == pytest.approx(0.25)
    assert right == pytest.approx(0.75)
    assert bottom == pytest.approx(0.75)

    # Verify Version 02 (Edge Case: cx=0.1, cy=0.1, cw=0.4, ch=0.4)
    # left = max(0, 0.1 - 0.2) = 0.0
    # top = max(0, 0.1 - 0.2) = 0.0
    # right = 0.1 + 0.2 = 0.3
    # bottom = 0.1 + 0.2 = 0.3
    xmp_v2 = tmp_path / "test_math_02.ARW.xmp"
    root = ET.parse(xmp_v2)
    history = root.find(".//{http://darktable.sf.net/}history/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
    crop_item = None
    for li in history:
        if li.get("{http://darktable.sf.net/}operation") == "crop":
            crop_item = li
            break
            
    params_hex = crop_item.get("{http://darktable.sf.net/}params")
    data = bytes.fromhex(params_hex)
    left, top, right, bottom = struct.unpack('<ffff', data[:16])
    
def test_rotation_application(tmp_path):
    # Setup dummy RAW file
    raw_file = tmp_path / "test_rot.ARW"
    raw_file.touch()
    
    suggestions = {
        "options": [
            {
                "id": 1,
                "name": "Rotated Crop",
                "params": {"cx": 0.5, "cy": 0.5, "cw": 0.5, "ch": 0.5, "rotation": 5.0}
            }
        ]
    }
    
    # Metadata for ashift
    metadata = {"focal_length": 35.0, "crop_factor": 1.0}
    
    generate_crop_previews(str(raw_file), suggestions, metadata=metadata)
    
    xmp_v1 = tmp_path / "test_rot_01.ARW.xmp"
    assert xmp_v1.exists()
    
    root = ET.parse(xmp_v1)
    # Find the ashift params
    history = root.find(".//{http://darktable.sf.net/}history/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
    ashift_item = None
    for li in history:
        if li.get("{http://darktable.sf.net/}operation") == "ashift":
            ashift_item = li
            break
            
    assert ashift_item is not None
    params_enc = ashift_item.get("{http://darktable.sf.net/}params")
    assert params_enc.startswith("gz16")
    
    # Decompress and verify rotation
    import zlib
    import base64
    b64_data = params_enc[4:]
    compressed_data = base64.b64decode(b64_data)
    data = zlib.decompress(compressed_data)
    
    rotation = struct.unpack('<f', data[:4])[0]
    assert rotation == pytest.approx(5.0)
    
    focal = struct.unpack('<f', data[16:20])[0]
    assert focal == pytest.approx(35.0)
