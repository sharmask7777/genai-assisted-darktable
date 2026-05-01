# Data Models - Darktable GenAI Assistant

## Session State (`.dt-ai-state.json`)
The session state tracks progress across directory-level edits.

```json
{
  "directory": "/Users/shaleensharma/Pictures/Shoot_01",
  "files_processed": [
    "DSC0123.ARW",
    "DSC0124.ARW"
  ],
  "last_run": "2026-05-01T14:30:00Z"
}
```

## AI Variation Model
The `variations` dictionary returned by Gemini defines the targets for XMP injection.

### Attribute Mapping
| AI Key | Darktable Module | Darktable Version | Struct Format |
|--------|------------------|-------------------|---------------|
| `exposure` | `exposure` | 6 | `iffff` (mode, black, exposure, pct, target) |
| `kelvin` | `temperature` | 3 | `ffff` (red, green1, blue, green2) |

## Internal XMP Representation
The system uses `xml.etree.ElementTree` to model the XMP XML.

### Skeleton Description
- Root: `x:xmpmeta`
- Child: `rdf:RDF`
- Child: `rdf:Description` (contains `darktable:xmp_version`, `darktable:history_end`)
- Child: `darktable:history` -> `rdf:Seq` (contains the list of `rdf:li` module entries)

## Hex Encoding (IEEE 754)
Floating point values from AI are converted to little-endian bytes and then hex-encoded.
- Example: `0.0` (float) -> `00000000`
- Example: `1.0` (float) -> `0000803f`
