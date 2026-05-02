# Composition Logic: Two-Stage Cropping & Rotation

This document outlines the logic for the intelligent cropping enhancement and the user selection flow.

## 1. Two-Stage Workflow

To ensure high-quality results, the `dt-ai` workflow will be split into two discrete creative phases.

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant CLI as dt-ai CLI
    
    User->>Agent: Start session
    Agent->>CLI: init-session
    Agent->>CLI: agent-next (First Pass)
    CLI-->>Agent: Original Preview + Metadata
    
    Agent->>Agent: Analyze Composition
    Agent-->>User: Suggest 3 Crops (Description + Rationale)
    Agent->>CLI: apply-crop-previews (3 temp XMPs)
    
    User->>User: Review in Darktable Lighttable
    User-->>Agent: "Select Option 2"
    
    Agent->>CLI: agent-next (Second Pass - Cropped)
    CLI-->>Agent: Cropped Preview + Rationale
    
    Agent->>Agent: Analyze Aesthetics (Exposure/Color/Detail)
    Agent-->>User: Mentor Report (Tutorials + Technicals)
    Agent->>CLI: apply-variations (3 aesthetic XMPs)
```

## 2. Coordinate Mapping
- **Normalized Scale**: Darktable uses a **0.0 to 1.0** coordinate system for its `clipping` module.
- **Orientation Awareness**: The AI must account for the `orientation` module (EXIF rotation) when calculating crop coordinates to avoid "flipped" crops.
- **Rotation (Leveling)**:
    - **Technical**: Small adjustments (±0.1° to ±2.0°) for leveling horizons.
    - **Creative**: Aggressive tilts (±5.0° to ±15.0°) for dynamic wildlife shots.
    - **Implementation**: Rotation values are stored in the `ashift` module's `rotation` field (float).

## 3. Temporary Preview Pattern
1. **Creation**: When the AI suggests 3 crops, it calls `apply-variations` with a special `mode="crop-preview"`.
2. **Naming**: The files are named `<image>_crop1.xmp`, `<image>_crop2.xmp`, etc.
3. **Selection**: Once the user chooses a crop (e.g., "1"), the AI promotes `crop1.xmp` to the "base" for aesthetic variations.
4. **Cleanup**: All other `_crop*.xmp` files are deleted.
