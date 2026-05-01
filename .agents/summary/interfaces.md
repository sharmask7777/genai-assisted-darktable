# Interfaces - Darktable GenAI Assistant

## CLI Interface
The CLI is built with `click`.

| Command | Argument | Options | Description |
|---------|----------|---------|-------------|
| `init-session` | `PATH` | None | Initializes/Resumes a session in the given directory. |
| `audit` | `PATH` | `--dry-run` | Performs image analysis and saves Markdown reports. |
| `edit` | `PATH` | `--dry-run` | Performs analysis and generates 3 XMP sidecar variations. |

## Gemini API Contract
The system communicates with Gemini via a Vision prompt. The expected response is a Markdown block containing a JSON object.

### Request Payload
- **Image:** Downscaled JPEG preview (max ~1MB).
- **Prompt:** Aesthetic audit instructions + request for specific Darktable parameters (Exposure, Kelvin).

### Response Schema
```json
{
  "audit": "Detailed aesthetic analysis text...",
  "recommendations": ["Denoise (profiled)", "Exposure", "Color balance RGB"],
  "variations": {
    "natural": { "exposure": 0.5, "kelvin": 5500 },
    "dramatic": { "exposure": -0.8, "kelvin": 6200 },
    "creative": { "exposure": 0.2, "kelvin": 4800 }
  }
}
```

## Darktable XMP Structure
Sidecars are XML files with specific namespaces and history sequences.

### Core Namespace Map
```python
NS = {
    "x": "adobe:ns:meta/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "darktable": "http://darktable.sf.net/",
}
```

### Module History Item Schema
Each history item (`li` in `rdf:Seq`) requires:
- `darktable:num`: Position in stack.
- `darktable:operation`: Module name (e.g., `exposure`).
- `darktable:modversion`: Module version (e.g., `6` for exposure).
- `darktable:params`: Hex-encoded IEEE 754 little-endian binary data.
- `darktable:enabled`: "1" or "0".
