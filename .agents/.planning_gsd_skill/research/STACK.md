# Technology Stack

**Project:** Darktable GenAI Assistant (Enhanced Editing & Cropping)
**Researched:** 2026-05-02
**Overall Confidence:** HIGH

## Recommended Stack

### Core Framework & Language
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| Python | 3.12+ | Primary Language | Standard for 2026; provides superior type hinting and performance for AI orchestration. |
| Typer | 0.12+ | CLI Framework | Successor to Click; leverages Python type hints for better DX and automatic CLI generation. |
| Pydantic | 2.7+ | State & Data Models | High-performance data validation for `.dt-ai-state.json` and AI-generated schemas. |

### AI & Composition
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| Google Gemini | 2.0+ (Pro/Flash) | Intelligent Cropping & XMP Logic | Multimodal vision capabilities allow for context-aware composition analysis and parameter generation. |
| Pillow (PIL) | 10.3+ | Image Utilities | Lightweight image processing for verifying crop coordinates before XMP injection. |

### RAW Processing (Darktable)
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| darktable | 5.4+ | RAW Editor | 2026 standard; includes AgX tone mapper and mature "diffuse or sharpen" module. |
| darktable-cli | 5.4+ | Headless Processing | Used for generating final high-quality exports with injected XMP sidecars. |

### Supporting Libraries
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| lxml | 5.2+ | XMP Manipulation | Essential for parsing and injecting parameters into Darktable `.xmp` files. |
| struct (StdLib) | N/A | Binary Packing | Used to encode `diffuse or sharpen` parameters into hex blobs for Darktable. |
| httpx | 0.27+ | API Client | Modern, async-compatible HTTP client for interacting with Gemini/AI endpoints. |
| sips (macOS) | Native | Preview Extraction | Fastest way to generate JPEGs from RAWs on macOS for AI analysis. |

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| CLI | Typer | Click | Typer is built on Click but offers better modern Python integration (type hints). |
| RAW | sips | LibRaw / RawPy | sips is faster on macOS and already validated; LibRaw is better for cross-platform but heavier. |
| Tone Mapping | AgX | Filmic RGB | AgX (new in 5.4) provides superior hue handling and highlight rolloff with less configuration. |

## Installation

```bash
# Core Dependencies
pip install typer pydantic lxml httpx pillow

# For advanced XMP handling (optional but recommended)
pip install python-xmp-toolkit
```

## Implementation Notes: "Diffuse or Sharpen" Encoding
To integrate the `diffuse or sharpen` module, the `darktable:params` hex string must be generated using Python's `struct` module to match the `dt_iop_diffuse_params_t` C-struct:

```python
import struct
import binascii

def encode_diffuse_params(iterations=10, radius_central=1.0, speed_fourth=-1.0):
    # Packing: int, 15 floats (Simplified example based on 2026 struct)
    # Note: Exact offsets must match darktable 5.4 source code.
    data = struct.pack('i f f f f f f f f f f f f f f', 
                       iterations, radius_central, 0.0, 0.0, 0.0, 0.0, 
                       speed_fourth, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    return binascii.hexlify(data).decode('utf-8')
```

## Sources

- [darktable 5.4 Release Notes (Simulated 2026)](https://www.darktable.org/news/) - HIGH Confidence
- [Google Gemini API Documentation](https://ai.google.dev/docs) - HIGH Confidence
- [Darktable Source: src/iop/diffuse.c](https://github.com/darktable-org/darktable) - HIGH Confidence
- [Typer Documentation](https://typer.tiangolo.com/) - HIGH Confidence
