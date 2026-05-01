# Task: Implement XMP Parsing & Skeleton Generation

## Description
Create a module to manage the XML structure of Darktable sidecar (.xmp) files. This task involves building the capability to read an existing sidecar (if it exists) or generate a valid skeleton for a new one.

## Background
Darktable sidecars are standard XML files using the Adobe XMP namespace. To automate edits, we must be able to generate a valid XML structure that Darktable recognizes as a processing history.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Additional References (if relevant to this task):**
- .agents/planning/2026-05-01-darktable-ai-assistant/research/SUMMARY.md (XMP section)

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Create `dt_ai/xmp.py`.
2. Use `xml.etree.ElementTree` (standard library) for XML manipulation.
3. Implement a function to generate a valid XMP skeleton with required namespaces (`x`, `rdf`, `darktable`).
4. Include core metadata tags: `darktable:internal_version`, `darktable:history_end`, and `darktable:history`.
5. Ensure the XML is written with proper formatting (indentation) to match Darktable's style.

## Dependencies
- Base project structure.

## Implementation Approach
1. Define the XML namespaces.
2. Build the root element and required nested structures (`rdf:Description`).
3. Implement a `write_xmp(root, path)` helper.

## Acceptance Criteria

1. **Valid XML Generation**
   - Given a request for a new sidecar
   - When the skeleton is generated and saved
   - Then the file starts with `<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>`.

2. **Required Tags Presence**
   - Given a generated XMP
   - When parsed as XML
   - Then it contains `<darktable:history>` and `<darktable:internal_version>`.

3. **Unit Test Coverage**
   - Given the `xmp` module
   - When generating skeletons
   - Then the presence of all required namespaces and tags is verified.

## Metadata
- **Complexity**: Medium
- **Labels**: XML, Darktable, Metadata, XMP
- **Required Skills**: Python, XML (ElementTree)
