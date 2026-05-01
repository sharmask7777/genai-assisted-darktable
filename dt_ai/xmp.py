import xml.etree.ElementTree as ET
import os
import struct
from typing import List

# Darktable XMP Namespaces
NS = {
    "x": "adobe:ns:meta/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "darktable": "http://darktable.sf.net/",
    "exif": "http://ns.adobe.com/exif/1.0/",
    "xmpMM": "http://ns.adobe.com/xap/1.0/mm/",
    "xmp": "http://ns.adobe.com/xap/1.0/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "lr": "http://ns.adobe.com/lightroom/1.0/",
}

# Register namespaces
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def generate_skeleton() -> ET.Element:
    """Generates a valid Darktable XMP skeleton based on user's manual edits."""
    xmpmeta = ET.Element(f"{{{NS['x']}}}xmpmeta", {f"{{{NS['x']}}}xmptk": "XMP Core 4.4.0-Exiv2"})
    rdf = ET.SubElement(xmpmeta, f"{{{NS['rdf']}}}RDF")
    
    # All namespaces required by the user's Darktable version
    description_attribs = {
        f"{{{NS['rdf']}}}about": "",
        f"{{{NS['darktable']}}}xmp_version": "5",
        f"{{{NS['darktable']}}}internal_version": "5",
        f"{{{NS['darktable']}}}history_end": "0",
        f"{{{NS['darktable']}}}iop_order_version": "5",
        f"{{{NS['darktable']}}}history_basic_hash": "00000000000000000000000000000000",
        f"{{{NS['darktable']}}}history_current_hash": "00000000000000000000000000000000",
    }
    
    description = ET.SubElement(rdf, f"{{{NS['rdf']}}}Description", description_attribs)
    
    # Masks history (Required)
    masks = ET.SubElement(description, f"{{{NS['darktable']}}}masks_history")
    ET.SubElement(masks, f"{{{NS['rdf']}}}Seq")
    
    # History sequence
    history = ET.SubElement(description, f"{{{NS['darktable']}}}history")
    ET.SubElement(history, f"{{{NS['rdf']}}}Seq")
    
    return xmpmeta

def write_xmp(root: ET.Element, path: str):
    """Writes the XMP XML with perfect header/footer and UTF-8 encoding."""
    xpacket_header = '<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
    footer = '\n<?xpacket end="w"?>'
    
    xml_bytes = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    xml_str = xml_bytes.decode('utf-8')
    
    if "<?xml" in xml_str:
        parts = xml_str.split("?>", 1)
        final_str = parts[0] + "?>\n" + xpacket_header + parts[1].lstrip()
    else:
        final_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + xpacket_header + xml_str
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(final_str)
        f.write(footer)

def load_xmp(path: str) -> ET.Element:
    """Loads an XMP file and returns the root Element."""
    tree = ET.parse(path)
    return tree.getroot()

def sync_history_end(root: ET.Element):
    """Updates darktable:history_end to match history list size."""
    desc = root.find(f".//{{{NS['rdf']}}}Description")
    history_node = root.find(f".//{{{NS['darktable']}}}history")
    if history_node is not None:
        seq = history_node.find(f"{{{NS['rdf']}}}Seq")
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
    binary_data = b"".join(struct.pack('<f', v) for v in values)
    return binary_data.hex()

def get_exposure_params(ev: float, black: float = 0.0) -> str:
    """Generates hex-encoded parameters for the 'exposure' v6 module."""
    return encode_params([0.0, black, ev, 0.5, 0.0]) # mode=0, black, ev, percentile, target

def get_temperature_params(kelvin: float) -> str:
    """Generates hex-encoded parameters for the 'temperature' v3 module."""
    # Using a much safer neutral baseline (1.0) instead of aggressive guesses.
    # Higher Kelvin (10000) = cooler/bluer (lower red ratio)
    # Lower Kelvin (2000) = warmer/redder (higher red ratio)
    base_kelvin = 5500.0
    ratio = base_kelvin / kelvin
    
    # We use a very gentle curve to avoid the "incredible red" cast
    red = 1.0 * ratio
    blue = 1.0 / ratio
    green = 1.0
    
    data = struct.pack('<ffff', red, green, blue, green)
    return data.hex()

def add_history_item(root: ET.Element, operation: str, params: str, modversion: str, enabled: bool = True):
    """Injects a new processing module into the history stack with modern blendops."""
    # Specifically target the Seq inside darktable:history
    history_node = root.find(f".//{{{NS['darktable']}}}history")
    if history_node is None:
        raise RuntimeError("Could not find darktable:history in XMP")
    
    seq = history_node.find(f"{{{NS['rdf']}}}Seq")
    if seq is None:
        raise RuntimeError("Could not find rdf:Seq inside darktable:history")
        
    num = len(list(seq))
    attribs = {
        f"{{{NS['darktable']}}}num": str(num),
        f"{{{NS['darktable']}}}operation": operation,
        f"{{{NS['darktable']}}}enabled": "1" if enabled else "0",
        f"{{{NS['darktable']}}}modversion": modversion,
        f"{{{NS['darktable']}}}params": params,
        f"{{{NS['darktable']}}}multi_name": "",
        f"{{{NS['darktable']}}}multi_name_hand_edited": "0",
        f"{{{NS['darktable']}}}multi_priority": "0",
        f"{{{NS['darktable']}}}blendop_version": "14",
        f"{{{NS['darktable']}}}blendop_params": "gz11eJxjYIAACQYYOOHEgAZY0QWAgBGLGANDgz0Ej1Q+dcF/IADRAGpyHQU=",
    }
    ET.SubElement(seq, f"{{{NS['rdf']}}}li", attribs)
    sync_history_end(root)

def generate_variations(raw_path: str, ai_result: dict) -> List[str]:
    """Generates Darktable version sidecars based on all AI variations provided."""
    generated = []
    variations = ai_result.get("variations", {})
    
    for style, params in variations.items():
        if not params: continue
        
        target_path = get_next_version_path(raw_path)
        initialize_new_version(raw_path, target_path)
        
        root = load_xmp(target_path)
        
        # Inject Exposure (now supporting black level for that "background dark" look)
        exp_hex = get_exposure_params(
            ev=params.get("exposure", 0.0),
            black=params.get("black", 0.0)
        )
        add_history_item(root, "exposure", exp_hex, "6")
        
        # Inject Temperature
        add_history_item(root, "temperature", get_temperature_params(params.get("kelvin", 5500.0)), "3")
        
        write_xmp(root, target_path)
        generated.append(target_path)
        
    return generated
