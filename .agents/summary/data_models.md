# Data Models

## AI Payload Schema

When `agent-next` is called, it outputs a JSON payload structured as follows:

```json
{
  "prompt": "String containing instructions",
  "target_image": "/absolute/path/to/raw",
  "target_preview": "/path/to/extracted/jpeg",
  "neighbors": ["/path/to/neighbor1.raw"],
  "metadata": {
    "model": "Camera Model",
    "lens": "Lens Info",
    "iso": "100",
    "exposure": "1/200",
    "aperture": "f/8"
  },
  "state": { "history": [], "last_processed": null },
  "research_database": {
    "wildlife": "...",
    "landscape": "..."
  }
}
```

## AI Result JSON

When calling `apply-variations`, the expected input JSON must contain:

```json
{
  "subject": "wildlife",
  "analysis": "Image needs contrast and shadow recovery.",
  "research_rationale": "Wildlife benefits from sharp subject isolation.",
  "audit": "Full markdown text of the mentor review.",
  "recommendations": ["denoiseprofile", "diffuse"],
  "variations": {
    "natural": {"exposure": 0.5, "kelvin": 5500},
    "dramatic": {"exposure": 1.0, "kelvin": 6000}
  }
}
```

## Session State (`.dt-ai-state.json`)

```json
{
  "history": [
    {
      "image": "IMG_001.ARW",
      "styles": ["natural", "dramatic"],
      "timestamp": "now"
    }
  ],
  "last_processed": "IMG_001.ARW"
}
```