# Requirements: Enhancer

## v1 Requirements

### 🧪 AgX Core
- [ ] **AGX-01**: The system MUST automatically enforce the AgX/Sigmoid scene-referred pipeline by disabling legacy modules (Filmic RGB, Base Curve) in the XMP history stack.
- [ ] **AGX-02**: The system MUST calculate and apply a mid-gray exposure normalization (18% gray) before AgX parameters are tuned to ensure consistent tonal mapping.
- [ ] **AGX-03**: The system MUST implement primary rotation tuning to mitigate the 'Notorious 6' color issues in high-saturation highlights.

### 📖 Educational Mentor
- [ ] **EDU-01**: The system MUST generate a "Pre-flight Review" terminal report that summarizes the intended edits before they are applied to the XMP file.
- [ ] **EDU-02**: The system MUST provide a technical rationale for each module choice, explicitly linking it to the image's metadata (e.g., "ISO 3200 detected: applying profiled denoise").
- [ ] **EDU-03**: The system MUST include educational snippets explaining the purpose and function of modern modules like Sigmoid, Color Calibration, and Diffuse/Sharpen.

### 🔍 Subject Research
- [ ] **RES-01**: The system MUST use vision analysis to classify the subject (e.g., Wildlife, Landscape, Portrait) and adjust the editing strategy accordingly.
- [ ] **RES-02**: The system MUST perform RAG-based research to retrieve subject-specific best practices from trusted photography sources (e.g., Pixls.us, official Darktable docs).
- [ ] **RES-03**: The system MUST offer at least two artistic style variations (e.g., 'Natural' vs 'Dramatic') informed by the retrieved subject research.

### 🛠 Technical Fixes
- [ ] **FIX-01**: The system MUST detect and correct sensor-specific color casts (green/red shifts) by referencing lens profile data and sensor characteristics.
- [ ] **FIX-02**: The system MUST identify and fix sensor black point mismatches in the shadows for known problematic camera models.
- [ ] **FIX-03**: The system MUST provide an interactive CLI fallback to prompt the user for essential metadata if EXIF data is missing or corrupted.

## v2 Requirements (Deferred)
- [ ] **BAT-01**: Full-library batch processing optimization.
- [ ] **GUI-01**: Desktop interface for visual side-by-side comparisons of AI logic.

## Out of Scope
- **LEG-01**: Comprehensive support for legacy Display-Referred module workflows.
- **VID-01**: Support for video-based photography tutorials.

## Traceability Matrix

| Requirement | Phase | Status |
|-------------|-------|--------|
| AGX-01 | Phase 1 | Pending |
| AGX-02 | Phase 4 | Pending |
| AGX-03 | Phase 5 | Pending |
| EDU-01 | Phase 6 | Pending |
| EDU-02 | Phase 7 | Pending |
| EDU-03 | Phase 7 | Pending |
| RES-01 | Phase 8 | Pending |
| RES-02 | Phase 9 | Pending |
| RES-03 | Phase 10 | Pending |
| FIX-01 | Phase 3 | Pending |
| FIX-02 | Phase 3 | Pending |
| FIX-03 | Phase 2 | Pending |

---
*Last updated: 2026-05-01*
