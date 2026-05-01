import pytest
import xml.etree.ElementTree as ET
from dt_ai.xmp import generate_skeleton, add_history_item, NS

def test_add_history_item_basic():
    root = generate_skeleton()
    # Add exposure
    add_history_item(root, "exposure", "00000000", "6")
    
    seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    items = list(seq)
    assert len(items) == 1
    
    item = items[0]
    assert item.get(f"{{{NS['darktable']}}}operation") == "exposure"
    assert item.get(f"{{{NS['darktable']}}}params") == "00000000"
    assert item.get(f"{{{NS['darktable']}}}num") == "0"
    
    desc = root.find(f".//{{{NS['rdf']}}}Description")
    assert desc.get(f"{{{NS['darktable']}}}history_end") == "1"

def test_add_history_item_sequential():
    root = generate_skeleton()
    add_history_item(root, "exposure", "000", "6")
    add_history_item(root, "temperature", "111", "3")
    
    seq = root.find(f".//{{{NS['darktable']}}}history/{{{NS['rdf']}}}Seq")
    items = list(seq)
    assert len(items) == 2
    assert items[0].get(f"{{{NS['darktable']}}}num") == "0"
    assert items[1].get(f"{{{NS['darktable']}}}num") == "1"
