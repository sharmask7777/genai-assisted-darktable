# Architecture Patterns

**Domain:** Professional photography editing using Darktable's scene-referred workflow.
**Researched:** 2026-05-02

## Recommended Architecture

The system follows a **Two-Stage CLI Pipeline** with a **State-Persistence Layer**.

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| `CLI (Typer)` | Command entry, user interaction, session management. | `Processor`, `State Manager` |
| `Discovery` | Scans directories for RAW files and existing XMPs. | Filesystem |
| `Previewer` | Extracts low-res JPEGs using macOS `sips`. | `AI Orchestrator` |
| `AI Orchestrator` | Multimodal analysis (Gemini); generates crop and XMP logic. | Gemini API, `XMP Engine` |
| `XMP Engine` | Binary encoding of params; XML injection into `.xmp` files. | `Processor`, Filesystem |
| `State Manager` | Persistence of crop selections and AI variations in `.dt-ai-state.json`. | All components |

### Data Flow

1. **Discovery Stage**: CLI identifies RAWs -> `State Manager` initializes session.
2. **Crop Stage**: `Previewer` extracts JPEG -> `AI Orchestrator` suggests 3 crops -> User selects crop -> `State Manager` saves choice.
3. **Aesthetic Stage**: `AI Orchestrator` analyzes *cropped* image -> Generates XMP parameters (AgX, Exposure, Diffuse/Sharpen).
4. **Injection Stage**: `XMP Engine` creates sidecar files -> `darktable-cli` (optional) exports final preview.

## Patterns to Follow

### Pattern 1: Binary Param Packing
**What:** Packing high-level AI suggestions into Darktable's hex-encoded binary blobs.
**When:** Whenever modifying advanced modules like `diffuse or sharpen`.
**Example:**
```python
import struct
import binascii

def pack_params(iterations: int, speeds: list[float]):
    # Matches C-struct dt_iop_diffuse_params_t
    fmt = 'i' + 'f' * 14 
    data = struct.pack(fmt, iterations, *speeds, 0.0, 0.0, 0.0) 
    return binascii.hexlify(data).decode('utf-8')
```

### Pattern 2: Sidecar Shadowing
**What:** Always work on copies of XMPs (`.xmp_ai_1`, `.xmp_ai_2`) to avoid destructive changes to original user edits.

## Anti-Patterns to Avoid

### Anti-Pattern 1: Direct RAW Modification
**What:** Attempting to write metadata back into the RAW file.
**Why bad:** Risk of file corruption; professional workflows demand non-destructive sidecar-only edits.
**Instead:** Always use `.xmp` sidecars.

### Anti-Pattern 2: Global State for Sessions
**What:** Storing session data in a central DB or user home folder.
**Why bad:** Photos are often moved or archived; sessions should live *with* the photos.
**Instead:** Use a hidden `.dt-ai-state.json` file in the project directory.

## Scalability Considerations

| Concern | At 100 images | At 10K images | At 1M images |
|---------|--------------|--------------|-------------|
| AI API Costs | Negligible | Significant ($100+) | Extreme (Needs Batch API) |
| Processing Time | Seconds | Hours | Days (Needs Distributed) |
| Disk Space | 10 MB (State) | 1 GB (Previews) | 100 GB (Previews) |

## Sources

- [Darktable Development Guide: XMP Format](https://www.darktable.org/usermanual/5.4/en/special-topics/program-internals/xmp-metadata/)
- [Twelve-Factor App (CLI Adaptation)](https://12factor.net/)
