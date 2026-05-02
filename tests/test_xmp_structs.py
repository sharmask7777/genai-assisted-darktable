import pytest
import struct
from dt_ai.xmp import (
    get_exposure_params, 
    get_temperature_params, 
    get_clipping_params,
    get_crop_params,
    get_ashift_params,
    get_diffuse_params
)

def test_get_exposure_params():
    # 20 bytes = 40 hex chars
    hex_str = get_exposure_params(1.5, 0.1)
    assert len(hex_str) == 40
    
    # Decode to verify
    data = bytes.fromhex(hex_str)
    mode, black, exposure, p, t = struct.unpack('<iffff', data)
    assert mode == 0
    assert black == pytest.approx(0.1)
    assert exposure == pytest.approx(1.5)

def test_get_temperature_params():
    # 16 bytes = 32 hex chars
    hex_str = get_temperature_params(5500)
    assert len(hex_str) == 32

def test_get_clipping_params():
    # 84 bytes = 168 hex chars
    hex_str = get_clipping_params(0.1, 0.2, 0.8, 0.6)
    assert len(hex_str) == 168
    
    data = bytes.fromhex(hex_str)
    # Struct: angle (f), cx (f), cy (f), cw (f), ch (f) ...
    angle, cx, cy, cw, ch = struct.unpack('<fffff', data[:20])
    assert angle == 0.0
    assert cx == pytest.approx(0.1)
    assert cy == pytest.approx(0.2)
    assert cw == pytest.approx(0.8)
    assert ch == pytest.approx(0.6)

def test_get_clipping_params_boundaries():
    # Test with 0.0 and 1.0
    hex_str = get_clipping_params(0.0, 0.0, 1.0, 1.0)
    data = bytes.fromhex(hex_str)
    angle, cx, cy, cw, ch = struct.unpack('<fffff', data[:20])
    assert cx == 0.0
    assert cy == 0.0
    assert cw == 1.0
    assert ch == 1.0

def test_get_crop_params():
    # 24 bytes = 48 hex chars
    hex_str = get_crop_params(0.1, 0.2, 0.8, 0.9)
    assert len(hex_str) == 48
    data = bytes.fromhex(hex_str)
    left, top, right, bottom, zero1, zero2 = struct.unpack('<6f', data)
    assert left == pytest.approx(0.1)
    assert top == pytest.approx(0.2)
    assert right == pytest.approx(0.8)
    assert bottom == pytest.approx(0.9)
    assert zero1 == 0.0
    assert zero2 == 0.0

import zlib
import base64

def test_get_ashift_params():
    # 892 bytes compressed will be much smaller, prefixed with gz16
    hex_encoded = get_ashift_params(rotation=-1.5, focal_length=50.0, crop_factor=1.5)
    assert hex_encoded.startswith("gz16")
    
    # Decode and decompress
    # format is gz<NN><base64>
    # gz16 is 4 chars.
    b64_data = hex_encoded[4:]
    compressed_data = base64.b64decode(b64_data)
    data = zlib.decompress(compressed_data)
    
    assert len(data) == 892
    
    # offset 0 is rotation (float)
    rotation = struct.unpack('<f', data[:4])[0]
    assert rotation == pytest.approx(-1.5)
    
    # offset 16 is focal length
    focal = struct.unpack('<f', data[16:20])[0]
    assert focal == pytest.approx(50.0)
    
def test_ashift_sample_verification():
    # Values from 1X7A4488.jpg.xmp
    rotation = 1.76
    focal = 600.0
    crop = 3.386362
    
    hex_encoded = get_ashift_params(rotation=rotation, focal_length=focal, crop_factor=crop)
    
    # Decode and decompress
    b64_data = hex_encoded[4:]
    compressed_data = base64.b64decode(b64_data)
    data = zlib.decompress(compressed_data)
    
    assert len(data) == 892
    
    # Verify values
    res_rotation = struct.unpack('<f', data[:4])[0]
    res_focal = struct.unpack('<f', data[16:20])[0]
    res_crop = struct.unpack('<f', data[20:24])[0]
    
    assert res_rotation == pytest.approx(rotation)
    assert res_focal == pytest.approx(focal)
    assert res_crop == pytest.approx(crop)
    
    # Verify cropmode
    cropmode = struct.unpack('<i', data[36:40])[0]
    assert cropmode == 1

def test_get_diffuse_params():
    # 68 bytes = 136 hex chars
    hex_str = get_diffuse_params(iterations=10, radius=2.0)
    assert len(hex_str) == 136
    
    data = bytes.fromhex(hex_str)
    iterations = struct.unpack('<i', data[:4])[0]
    radius = struct.unpack('<f', data[4:8])[0]
    assert iterations == 10
    assert radius == pytest.approx(2.0)
