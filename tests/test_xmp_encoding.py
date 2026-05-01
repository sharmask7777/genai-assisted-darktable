import pytest
from dt_ai.xmp import encode_params

def test_encode_params_single():
    # 1.0 in IEEE 754 little-endian hex
    assert encode_params([1.0]) == "0000803f"
    assert encode_params([0.0]) == "00000000"
    assert encode_params([-1.0]) == "000080bf"

def test_encode_params_multiple():
    # 0.0 and 1.0 concatenated
    assert encode_params([0.0, 1.0]) == "000000000000803f"

def test_encode_params_empty():
    assert encode_params([]) == ""
