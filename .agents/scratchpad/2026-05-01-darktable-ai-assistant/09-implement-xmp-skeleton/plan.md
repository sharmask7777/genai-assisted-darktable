# Plan: 09-implement-xmp-skeleton

## Test Strategy
1. **Skeleton Structure Test**: Verify that the generated XML contains the expected namespaces (`x`, `rdf`, `darktable`).
2. **Tag Presence Test**: Verify that `darktable:history`, `darktable:history_end`, and `darktable:internal_version` are present.
3. **File Header Test**: Verify that the saved file starts with the mandatory `<?xpacket ...?>` header.

## Implementation Steps
1. Create `dt_ai/xmp.py`.
2. Define constant namespaces:
   - `x`: `adobe:ns:meta/`
   - `rdf`: `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
   - `darktable`: `http://darktable.sf.net/`
3. Implement `generate_skeleton() -> ET.Element`.
4. Implement `write_xmp(root, path)` that adds the xpacket header and footer.
