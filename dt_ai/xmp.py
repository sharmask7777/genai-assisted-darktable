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

# Legacy and Conflict-Prone Modules
LEGACY_MODULES = [
    "filmicrgb", 
    "basecurve", 
    "tonecurve",
    "shadhi",
]

# Preferred Modern Scene-Referred Modules
MODERN_PIPELINE = [
    "exposure",
    "colorbalancergb",
    "colorcalibration",
    "sigmoid",
    "agx",
]

# Hardware-specific correction database
# Keys are 'model' or 'lens' substrings. 
# Values are dicts with corrections: black_offset, green_gain, red_gain.
SENSOR_DATABASE = {
    "ILCE-7M3": {"black_offset": 0.0002, "green_gain": 1.0, "red_gain": 1.0}, # Sony A7III
    "ILCE-7RM4": {"black_offset": 0.0003, "green_gain": 1.0, "red_gain": 1.0}, # Sony A7RIV
    "SAMSUNG": {"black_offset": 0.0005, "green_gain": 0.98, "red_gain": 1.02}, # Generic Samsung shift
    "EOS R5": {"black_offset": 0.0, "green_gain": 1.0, "red_gain": 1.0}, # Canon usually neutral
}

# Register namespaces
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def apply_hardware_corrections(metadata: dict) -> dict:
    """
    Returns a set of technical offsets based on sensor/lens metadata.
    """
    model = metadata.get("model", "").upper()
    lens = metadata.get("lens", "").upper()
    
    corrections = {"black_offset": 0.0, "green_gain": 1.0, "red_gain": 1.0}
    
    # Check for model matches
    for key, data in SENSOR_DATABASE.items():
        if key in model or key in lens:
            corrections.update(data)
            break
            
    return corrections

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

def get_sigmoid_params(contrast: float = 1.5, 
                       skew: float = 0.0, 
                       preserve_hue: float = 1.0,
                       attenuation: List[float] = None,
                       rotation: List[float] = None) -> str:
    """
    Generates hex-encoded parameters for the 'sigmoid' v3 module (Darktable 5.x+).
    Based on Darktable 5.4.1 structure:
    middle_grey_contrast (float), contrast_skewness (float), 
    display_white_target (float), display_black_target (float),
    color_processing (int), preserve_hue (float), base_primaries (int),
    primary_attenuation (float[3]), primary_rotation (float[3]), primary_purity (float)
    """
    target_black = 0.0
    target_white = 100.0 # Standard SDR target
    color_processing = 0 # 0: per channel (AgX-like)
    base_primaries = 0   # 0: working profile
    primary_purity = 100.0 # Neutral purity
    
    attenuation = attenuation or [0.0, 0.0, 0.0] # 0.0 is neutral in v3 sliders
    rotation = rotation or [0.0, 0.0, 0.0]
    
    # Struct: ffff i f i 3f 3f f (14 fields, 56 bytes)
    data = struct.pack('<ffffif i3f3f f', 
                       contrast, skew, target_white, target_black, 
                       color_processing, preserve_hue, base_primaries,
                       *attenuation, *rotation, primary_purity)
    return data.hex()

def get_agx_params(contrast: float = 1.0, 
                    saturation: float = 1.0) -> str:
    """
    Generates hex-encoded parameters for the 'agx' v1 module.
    Structure: 14 floats (56 bytes) covering points, curve, look, and primaries.
    """
    white_point = 6.0
    black_point = -7.0
    toe_power = 1.0
    shoulder_power = 1.0
    shadow_offset = 0.0
    # Primaries (neutral: 0 rotation, 100 purity)
    rotate = [0.0, 0.0, 0.0]
    purity = [100.0, 100.0, 100.0]
    
    # Struct: 13 floats + 1 int (56 bytes)
    auto_tune = 0
    data = struct.pack('<13fi', 
                       white_point, black_point, contrast, toe_power, shoulder_power,
                       saturation, shadow_offset, *rotate, *purity, auto_tune)
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

def generate_variations(raw_path: str, ai_result: dict, metadata: dict = None) -> List[str]:
    """Generates Darktable version sidecars based on all AI variations provided."""
    generated = []
    variations = ai_result.get("variations", {})
    metadata = metadata or {}
    
    # Calculate hardware offsets once per image
    hw = apply_hardware_corrections(metadata)
    
    for style, params in variations.items():
        if not params: continue
        
        target_path = get_next_version_path(raw_path)
        initialize_new_version(raw_path, target_path)
        
        root = load_xmp(target_path)
        
        # Inject Exposure (including hardware black offset)
        exp_hex = get_exposure_params(
            ev=params.get("exposure", 0.0),
            black=params.get("black", 0.0) + hw["black_offset"]
        )
        add_history_item(root, "exposure", exp_hex, "6")
        
        # Inject Temperature (Note: Future phases can use hw['green_gain'] / hw['red_gain'])
        add_history_item(root, "temperature", get_temperature_params(params.get("kelvin", 5500.0)), "3")
        
        # Inject AgX or Sigmoid (Tone mapping)
        if "agx_contrast" in params or "agx_saturation" in params:
            agx_hex = get_agx_params(
                contrast=params.get("agx_contrast", 1.0),
                saturation=params.get("agx_saturation", 1.0)
            )
            add_history_item(root, "agx", agx_hex, "1")
        else:
            # Fallback to Sigmoid
            sig_hex = get_sigmoid_params(
                contrast=params.get("contrast", 1.5),
                skew=params.get("skew", 0.0),
                attenuation=params.get("attenuation"),
                rotation=params.get("rotation")
            )
            add_history_item(root, "sigmoid", sig_hex, "3")
        
        # Enforce modern workflow (disables legacy, ensures AgX-compatibility)
        enforce_agx_workflow(root)
        
        write_xmp(root, target_path)
        generated.append(target_path)
        
    return generated

def enforce_agx_workflow(root: ET.Element):
    """
    Enforces the AgX/Scene-referred workflow by disabling legacy modules
    and ensuring modern modules are active.
    """
    history_node = root.find(f".//{{{NS['darktable']}}}history")
    if history_node is None:
        return
    
    seq = history_node.find(f"{{{NS['rdf']}}}Seq")
    if seq is None:
        return

    for item in list(seq):
        operation = item.get(f"{{{NS['darktable']}}}operation")
        
        # Disable legacy modules
        if operation in LEGACY_MODULES:
            item.set(f"{{{NS['darktable']}}}enabled", "0")
        
        # Ensure modern modules are enabled if they exist
        if operation in MODERN_PIPELINE:
            item.set(f"{{{NS['darktable']}}}enabled", "1")
