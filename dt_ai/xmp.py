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
