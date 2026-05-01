# Requirements: Darktable GenAI Assistant (v1)

## v1 Requirements

### Core CLI & Workflow
- [ ] **CLI-01**: Targeted file selection using single paths or glob patterns (e.g., `*.ARW`).
- [ ] **CLI-02**: Interactive Mode: The tool must pause and ask for validation before performing high-complexity tasks (like Denoise injection).
- [ ] **CLI-03**: Dry-run mode to output AI audit text without modifying files.

### Vision & Image Intelligence
- [ ] **VIS-01**: Automated JPEG extraction from RAW using macOS `sips`.
- [ ] **AUD-01**: Aesthetic Audit: Provide commentary on composition, wildlife/landscape focus, and lighting.
- [ ] **AUD-02**: Module Mapping: Recommend specific Darktable modules (e.g., 'Exposure', 'Denoise (profiled)') based on image flaws.

### Sidecar (XMP) Automation
- [ ] **VAR-01**: Generate 3 distinct editing variations (Natural, Dramatic, Creative).
- [ ] **XMP-01**: Automated injection of Basic Modules (Exposure, Temperature, Color Balance) into sidecar files.
- [ ] **XMP-02**: **Automated Denoise (Challenge Requirement)**: Attempt to inject 'Denoise (profiled)' parameters, prompting the user for validation if camera-specific profiles are missing or ambiguous.

## Out of Scope
- Full library synchronization.
- Non-macOS support.
- Direct RAW pixel manipulation (XMP-only).

## Traceability
*Requirement mappings to phases will be handled in the Roadmap.*
