# Workflows - Darktable GenAI Assistant

## 1. Aesthetic Audit Workflow (`dt-ai audit`)
This workflow focuses on technical and aesthetic evaluation without modifying image state.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant SIPS
    participant Gemini
    participant FS

    User->>CLI: dt-ai audit [path]
    CLI->>FS: Discover RAW files
    loop Each File
        CLI->>SIPS: Extract preview (downscaled JPEG)
        CLI->>Gemini: analyze_image(preview)
        Gemini-->>CLI: Markdown (Audit + JSON)
        CLI->>FS: Save [file]_audit.md
    end
    CLI-->>User: Pipeline Complete
```

## 2. GenAI Edit Workflow (`dt-ai edit`)
This workflow extends the audit by generating three distinct processing variations.

```mermaid
sequenceDiagram
    participant CLI
    participant Gemini
    participant XMP
    participant DT as Darktable
    participant User

    CLI->>Gemini: analyze_image(preview)
    Gemini-->>CLI: Recommendations + 3 Variations
    
    loop Style in [Natural, Dramatic, Creative]
        CLI->>XMP: get_next_version_path()
        XMP->>XMP: Generate XMP Skeleton
        XMP->>XMP: Inject Exposure (Hex)
        XMP->>XMP: Inject Temperature (Hex)
        XMP->>XMP: Write [file]_0[N].xmp
    end
    
    alt Denoise Recommended
        CLI->>DT: Open File for Validation
        CLI->>User: Pause for Interactive Handoff
        User-->>CLI: Continue
    end
    
    CLI-->>User: Versions Created
```

## 3. Interactive Handoff (Denoise Safety)
Because AI-driven denoising is risky and hardware-dependent, the system includes a "Take a Call" safety check:
1.  **Detection:** `main.py` checks recommendations for "denoise".
2.  **Automation:** Launches Darktable using `gui.py`.
3.  **Interaction:** Prompts the user to validate settings before moving to the next image in a batch.
