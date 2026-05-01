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

def get_exposure_params(ev: float, black: float = 0.0) -> str:
    """
    Generates hex-encoded parameters for the 'exposure' v6 module.
    Struct: { int32 mode, float black, float exposure, float percentile, float target }
    """
    # mode=0 (manual), percentile=0.5, target=0.0
    data = struct.pack('<iffff', 0, black, ev, 0.5, 0.0)
    return data.hex()

def get_temperature_params(kelvin: float) -> str:
    """
    Generates hex-encoded parameters for the 'temperature' v3 module.
    Struct: { float red, float green1, float blue, float green2 }
    This uses a simplified mapping where 5500K is roughly [2.0, 1.0, 1.5, 1.0].
    """
    # Simple linear approximation for WB coefficients (relative to 5500K)
    # Higher Kelvin = More Blue, Less Red
    ratio = 5500.0 / kelvin
    red = 2.0 * ratio
    blue = 1.5 / ratio
    green = 1.0
    
    data = struct.pack('<ffff', red, green, blue, green)
    return data.hex()

def add_history_item(root: ET.Element, operation: str, params: str, modversion: str, enabled: bool = True):
    """
    Injects a new processing module into the history stack.
    """
    seq = root.find(f".//{{{NS['rdf']}}}Seq")
    if seq is None:
        raise RuntimeError("Could not find rdf:Seq in XMP history")
        
    num = len(list(seq))
    
    # Required attributes for Darktable to recognize the module
    attribs = {
        f"{{{NS['darktable']}}}num": str(num),
        f"{{{NS['darktable']}}}operation": operation,
        f"{{{NS['darktable']}}}enabled": "1" if enabled else "0",
        f"{{{NS['darktable']}}}modversion": modversion,
        f"{{{NS['darktable']}}}params": params,
        f"{{{NS['darktable']}}}multi_name": "",
        f"{{{NS['darktable']}}}multi_priority": "0",
        f"{{{NS['darktable']}}}blendop_version": "11",
        f"{{{NS['darktable']}}}blendop_params": "gz14eJxjYIAACQYYOOHEgAZY0QVwggZ7CB6pfNoAAE8gGQg=", # Standard bypass
    }
    
    ET.SubElement(seq, f"{{{NS['rdf']}}}li", attribs)
    sync_history_end(root)
