# Workflows

## Standard AI Agent Workflow

This workflow represents how an external AI agent interacts with the `dt-ai` tools.

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant DTAI as dt-ai CLI
    participant FS as File System
    
    User->>Agent: Start session on /folder
    Agent->>DTAI: dt-ai init-session /folder
    DTAI->>FS: Create .dt-ai-state.json
    
    User->>Agent: Process IMG_001.ARW
    Agent->>DTAI: dt-ai agent-next IMG_001.ARW
    DTAI->>FS: extract preview with sips
    DTAI-->>Agent: JSON payload (metadata, preview path)
    
    Agent->>Agent: Analyze preview visually
    Agent->>Agent: Generate editing strategy
    
    Agent->>DTAI: dt-ai apply-variations IMG_001.ARW <json_strategy>
    DTAI->>FS: Write IMG_001.ARW.xmp files
    DTAI->>FS: Update .dt-ai-state.json
    DTAI-->>Agent: Success report
    
    Agent->>User: Done! Review in Darktable
```

## Variation Generation Pipeline

1. **Pre-flight Report**: `main.py` formats the AI's intent into a readable summary.
2. **Hardware Corrections**: `xmp.py` checks metadata (e.g. camera model) and applies necessary offsets (like black-point fixes).
3. **AgX Enforcement**: Darktable legacy tone mappers are disabled, and modern scene-referred modules are enabled.
4. **Encoding**: Target parameters (exposure, kelvin) are converted to IEEE 754 little-endian hex strings.
5. **XML Writing**: Duplicate `.xmp` files are written to disk.