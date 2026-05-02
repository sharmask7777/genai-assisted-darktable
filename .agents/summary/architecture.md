# Architecture

## System Architecture

The dt-ai system is designed as a CLI-first application that acts as an intermediary between the user's filesystem (RAW photos), an AI Assistant (Gemini), and Darktable.

```mermaid
graph TD
    User[User / AI Agent] --> CLI[dt-ai CLI]
    CLI --> Discovery[Discovery & Metadata]
    CLI --> Processor[Image Processor]
    CLI --> State[State Management]
    
    Discovery --> FileSystem[(File System)]
    Processor --> SIPS[macOS sips]
    
    CLI --> AI[AI Integration]
    CLI --> XMP[XMP Sidecar Engine]
    
    XMP --> FileSystem
    FileSystem --> Darktable[Darktable GUI]
```

## Architectural Principles

1. **Non-Destructive Operations**: The system NEVER modifies the original RAW files. All edits and variations are written to Darktable-compatible `.xmp` sidecar files.
2. **Stateless Operations with Persistent Sessions**: The CLI commands are mostly stateless but utilize a hidden `.dt-ai-state.json` file in the working directory to track session progress.
3. **Hardware & Pipeline Awareness**: The architecture enforces modern scene-referred workflows (AgX, sigmoid) and applies hardware-specific sensor corrections automatically.