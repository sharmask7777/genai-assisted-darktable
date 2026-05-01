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
