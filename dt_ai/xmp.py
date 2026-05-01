import xml.etree.ElementTree as ET
import os

# Darktable XMP Namespaces
NS = {
    "x": "adobe:ns:meta/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "darktable": "http://darktable.sf.net/",
}

# Register namespaces to keep the prefixes clean
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def generate_skeleton() -> ET.Element:
    """
    Generates a valid Darktable XMP skeleton.
    """
    xmpmeta = ET.Element(f"{{{NS['x']}}}xmpmeta", {f"{{{NS['x']}}}xmptk": "XMP Core 4.4.0-Exiv2"})
    rdf = ET.SubElement(xmpmeta, f"{{{NS['rdf']}}}RDF")
    description = ET.SubElement(rdf, f"{{{NS['rdf']}}}Description", {
        f"{{{NS['rdf']}}}about": "",
        f"{{{NS['darktable']}}}xmp_version": "5",
        f"{{{NS['darktable']}}}internal_version": "5",
        f"{{{NS['darktable']}}}history_end": "0",
    })
    
    # History sequence
    history = ET.SubElement(description, f"{{{NS['darktable']}}}history")
    ET.SubElement(history, f"{{{NS['rdf']}}}Seq")
    
    return xmpmeta

def write_xmp(root: ET.Element, path: str):
    """
    Writes the XMP XML to disk with mandatory xpacket headers.
    """
    header = '<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
    footer = '\n<?xpacket end="w"?>'
    
    xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(xml_str)
        f.write(footer)

def get_next_version_path(raw_path: str) -> str:
    """
    Returns the path for the next available sidecar version.
    Version 0: basename.ext.xmp
    Version 1+: basename_nn.ext.xmp
    """
    # Version 0 check
    v0_path = f"{raw_path}.xmp"
    if not os.path.exists(v0_path):
        return v0_path
        
    # Find next available _nn version
    base, ext = os.path.splitext(raw_path)
    version = 1
    while True:
        v_path = f"{base}_{version:02d}{ext}.xmp"
        if not os.path.exists(v_path):
            return v_path
        version += 1

def load_xmp(path: str) -> ET.Element:
    """
    Loads an XMP file and returns the root Element.
    """
    # Note: ElementTree parser ignores xpacket processing instructions
    tree = ET.parse(path)
    return tree.getroot()

def sync_history_end(root: ET.Element):
    """
    Updates the darktable:history_end attribute to match the number of items in history.
    """
    desc = root.find(f".//{{{NS['rdf']}}}Description")
    seq = root.find(f".//{{{NS['rdf']}}}Seq")
    if desc is not None and seq is not None:
        count = len(list(seq))
        desc.set(f"{{{NS['darktable']}}}history_end", str(count))

def initialize_new_version(raw_path: str, target_xmp_path: str):
    """
    Initializes a new XMP version. 
    If a base XMP exists, it is used as a template (cloned).
    Otherwise, a new skeleton is generated.
    """
    base_xmp = f"{raw_path}.xmp"
    if os.path.exists(base_xmp):
        root = load_xmp(base_xmp)
    else:
        root = generate_skeleton()
    
    sync_history_end(root)
    write_xmp(root, target_xmp_path)
