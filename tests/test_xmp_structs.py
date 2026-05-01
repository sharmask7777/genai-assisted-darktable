import pytest
import struct
from dt_ai.xmp import get_exposure_params, get_temperature_params

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
