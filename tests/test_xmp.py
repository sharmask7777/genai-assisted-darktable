import pytest
import os
import xml.etree.ElementTree as ET
from dt_ai.xmp import generate_skeleton, write_xmp

def test_generate_skeleton():
    root = generate_skeleton()
    # Check namespaces indirectly by looking for tags
    xml_str = ET.tostring(root, encoding='unicode')
    assert "adobe:ns:meta" in xml_str
    assert "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in xml_str
    assert "http://darktable.sf.net/" in xml_str
    
    # Check required tags
    assert "history_end" in xml_str
    assert "internal_version" in xml_str
    assert "history" in xml_str

def test_write_xmp_header(tmp_path):
    root = generate_skeleton()
    xmp_path = tmp_path / "test.xmp"
    write_xmp(root, str(xmp_path))
    
    content = xmp_path.read_text()
    assert content.startswith('<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>')
    assert content.strip().endswith('<?xpacket end="w"?>')
