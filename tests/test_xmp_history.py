import pytest
import os
import xml.etree.ElementTree as ET
from dt_ai.xmp import generate_skeleton, write_xmp, load_xmp, sync_history_end, NS

def test_load_xmp(tmp_path):
    xmp = tmp_path / "test.xmp"
    root = generate_skeleton()
    write_xmp(root, str(xmp))
    
    loaded_root = load_xmp(str(xmp))
    assert loaded_root.tag == f"{{{NS['x']}}}xmpmeta"

def test_sync_history_end():
    root = generate_skeleton()
    # Initially 0
    desc = root.find(f".//{{{NS['rdf']}}}Description")
    assert desc.get(f"{{{NS['darktable']}}}history_end") == "0"
    
    # Add a module to the CORRECT history list
    history_seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    ET.SubElement(history_seq, f"{{{NS['rdf']}}}li", {f"{{{NS['darktable']}}}operation": "exposure"})
    
    sync_history_end(root)
    assert desc.get(f"{{{NS['darktable']}}}history_end") == "1"

def test_sync_history_end_multiple():
    root = generate_skeleton()
    history_seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    for _ in range(5):
        ET.SubElement(history_seq, f"{{{NS['rdf']}}}li")
    
    sync_history_end(root)
    desc = root.find(f".//{{{NS['rdf']}}}Description")
    assert desc.get(f"{{{NS['darktable']}}}history_end") == "5"

from dt_ai.xmp import initialize_new_version, add_history_item, get_diffuse_params

def test_multiple_diffuse_instances():
    root = generate_skeleton()
    # Add one for denoise
    add_history_item(root, "diffuse", get_diffuse_params(iterations=20), "2", multi_name="denoise")
    # Add one for deblur
    add_history_item(root, "diffuse", get_diffuse_params(iterations=40), "2", multi_name="deblur")
    
    history_seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    items = list(history_seq)
    assert len(items) == 2
    assert items[0].get(f"{{{NS['darktable']}}}multi_name") == "denoise"
    assert items[1].get(f"{{{NS['darktable']}}}multi_name") == "deblur"

from dt_ai.xmp import generate_variations

def test_default_optical_fixes(tmp_path):
    raw = tmp_path / "test.ARW"
    raw.touch()
    
    ai_result = {
        "variations": {
            "natural": {"exposure": 0.0}
        }
    }
    
    generated = generate_variations(str(raw), ai_result)
    assert len(generated) == 1
    
    root = load_xmp(generated[0])
    history_seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    ops = [li.get(f"{{{NS['darktable']}}}operation") for li in list(history_seq)]
    
    assert "lens" in ops
    assert "cacorrect" in ops

def test_initialize_new_version_cloning(tmp_path):
    raw = tmp_path / "test.ARW"
    raw.write_text("d")
    base_xmp = tmp_path / "test.ARW.xmp"
    
    # Create base XMP with 1 module
    root = generate_skeleton()
    seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    ET.SubElement(seq, f"{{{NS['rdf']}}}li", {f"{{{NS['darktable']}}}operation": "exposure"})
    write_xmp(root, str(base_xmp))
    
    target_xmp = tmp_path / "test_01.ARW.xmp"
    from dt_ai.xmp import initialize_new_version
    initialize_new_version(str(raw), str(target_xmp))
    
    # Verify target has 1 module
    target_root = load_xmp(str(target_xmp))
    target_seq = target_root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    assert len(list(target_seq)) == 1
    target_desc = target_root.find(f".//{{{NS['rdf']}}}Description")
    assert target_desc.get(f"{{{NS['darktable']}}}history_end") == "1"
