import xml.etree.ElementTree as ET
import os
import struct
from typing import List

# Darktable XMP Namespaces
NS = {
    "x": "adobe:ns:meta/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "darktable": "http://darktable.sf.net/",
}

# Register namespaces
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def generate_skeleton() -> ET.Element:
    """Generates a valid Darktable XMP skeleton."""
    xmpmeta = ET.Element(f"{{{NS['x']}}}xmpmeta", {f"{{{NS['x']}}}xmptk": "XMP Core 4.4.0-Exiv2"})
    rdf = ET.SubElement(xmpmeta, f"{{{NS['rdf']}}}RDF")
    description = ET.SubElement(rdf, f"{{{NS['rdf']}}}Description", {
        f"{{{NS['rdf']}}}about": "",
        f"{{{NS['darktable']}}}xmp_version": "5",
        f"{{{NS['darktable']}}}internal_version": "5",
        f"{{{NS['darktable']}}}history_end": "0",
    })
    history = ET.SubElement(description, f"{{{NS['darktable']}}}history")
    ET.SubElement(history, f"{{{NS['rdf']}}}Seq")
    return xmpmeta

def write_xmp(root: ET.Element, path: str):
    """Writes the XMP XML to disk with mandatory xpacket headers."""
    header = '<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
    footer = '\n<?xpacket end="w"?>'
    xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    with open(path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(xml_str)
        f.write(footer)

def load_xmp(path: str) -> ET.Element:
    """Loads an XMP file and returns the root Element."""
    tree = ET.parse(path)
    return tree.getroot()

def sync_history_end(root: ET.Element):
    """Updates darktable:history_end to match history list size."""
    desc = root.find(f".//{{{NS['rdf']}}}Description")
    seq = root.find(f".//{{{NS['rdf']}}}Seq")
    if desc is not None and seq is not None:
        count = len(list(seq))
        desc.set(f"{{{NS['darktable']}}}history_end", str(count))

def get_next_version_path(raw_path: str) -> str:
    """Returns the path for the next available sidecar version."""
    v0_path = f"{raw_path}.xmp"
    if not os.path.exists(v0_path):
        return v0_path
    base, ext = os.path.splitext(raw_path)
    version = 1
    while True:
        v_path = f"{base}_{version:02d}{ext}.xmp"
        if not os.path.exists(v_path):
            return v_path
        version += 1

def initialize_new_version(raw_path: str, target_xmp_path: str):
    """Initializes a new XMP version, cloning base if available."""
    base_xmp = f"{raw_path}.xmp"
    if os.path.exists(base_xmp):
        root = load_xmp(base_xmp)
    else:
        root = generate_skeleton()
    sync_history_end(root)
    write_xmp(root, target_xmp_path)

def encode_params(values: List[float]) -> str:
    """
    Encodes a list of floats into a Darktable hex-encoded binary string.
    Uses IEEE 754 little-endian format.
    """
    if not values:
        return ""
    # Pack as little-endian floats ('<f')
    binary_data = b"".join(struct.pack('<f', v) for v in values)
    return binary_data.hex()
