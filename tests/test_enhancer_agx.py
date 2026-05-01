import pytest
import xml.etree.ElementTree as ET
from dt_ai.xmp import generate_skeleton, NS, add_history_item, enforce_agx_workflow

def test_enforce_agx_workflow_disables_legacy_modules():
    """
    Test that legacy modules (filmicrgb, basecurve) are disabled 
    when the AgX workflow is enforced.
    """
    root = generate_skeleton()
    
    # Add legacy modules enabled
    add_history_item(root, "filmicrgb", "000000", "5", enabled=True)
    add_history_item(root, "basecurve", "000000", "4", enabled=True)
    
    # Ensure they are enabled initially
    history = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    items = list(history)
    assert any(i.get(f"{{{NS['darktable']}}}operation") == "filmicrgb" and i.get(f"{{{NS['darktable']}}}enabled") == "1" for i in items)
    assert any(i.get(f"{{{NS['darktable']}}}operation") == "basecurve" and i.get(f"{{{NS['darktable']}}}enabled") == "1" for i in items)

    # Act
    enforce_agx_workflow(root)
    
    # Assert legacy modules are disabled
    items_after = list(history)
    for item in items_after:
        op = item.get(f"{{{NS['darktable']}}}operation")
        if op in ["filmicrgb", "basecurve"]:
            assert item.get(f"{{{NS['darktable']}}}enabled") == "0", f"{op} should be disabled"

def test_enforce_agx_workflow_enables_agx_modules():
    """
    Test that AgX-related modules (sigmoid) are ensured in the stack.
    Note: For now, we just check if it ensures they are NOT disabled if present.
    Future: It might inject them if missing.
    """
    root = generate_skeleton()
    add_history_item(root, "sigmoid", "000000", "3", enabled=False)
    
    enforce_agx_workflow(root)
    
    history = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    items = list(history)
    assert any(i.get(f"{{{NS['darktable']}}}operation") == "sigmoid" and i.get(f"{{{NS['darktable']}}}enabled") == "1" for i in items)

def test_apply_hardware_corrections_sony():
    """Verify that Sony A7III gets the correct black point offset."""
    from dt_ai.xmp import apply_hardware_corrections
    meta = {"model": "ILCE-7M3", "lens": "FE 200-600mm F5.6-6.3 G OSS"}
    hw = apply_hardware_corrections(meta)
    assert hw["black_offset"] == 0.0002

def test_apply_hardware_corrections_unknown():
    """Verify that unknown cameras get zero offsets."""
    from dt_ai.xmp import apply_hardware_corrections
    meta = {"model": "Nikon D850", "lens": "Unknown"}
    hw = apply_hardware_corrections(meta)
    assert hw["black_offset"] == 0.0

def test_get_sigmoid_params():
    """Verify sigmoid binary packing length."""
    from dt_ai.xmp import get_sigmoid_params
    import struct
    hex_str = get_sigmoid_params(contrast=1.6, skew=0.1)
    # contrast(f), skew(f), black(f), white(f), hue(i), atten(3f), rot(3f)
    # 4 + 4 + 4 + 4 + 4 + 12 + 12 = 44 bytes = 88 hex chars
    assert len(hex_str) == 88
    
    data = bytes.fromhex(hex_str)
    # Using struct.calcsize to verify
    assert len(data) == struct.calcsize('<ffffi3f3f')

def test_get_sigmoid_params_custom_rotations():
    """Verify sigmoid primary rotations are correctly packed."""
    from dt_ai.xmp import get_sigmoid_params
    import struct
    atten = [0.2, 0.2, 0.2]
    rot = [0.01, -0.02, 0.03]
    hex_str = get_sigmoid_params(attenuation=atten, rotation=rot)
    
    data = bytes.fromhex(hex_str)
    # contrast(f), skew(f), black(f), white(f), hue(i), atten(3f), rot(3f)
    unpacked = struct.unpack('<ffffi3f3f', data)
    
    # Check attenuation (indices 5, 6, 7)
    assert unpacked[5] == pytest.approx(0.2)
    # Check rotation (indices 8, 9, 10)
    assert unpacked[8] == pytest.approx(0.01)
    assert unpacked[9] == pytest.approx(-0.02)
    assert unpacked[10] == pytest.approx(0.03)
