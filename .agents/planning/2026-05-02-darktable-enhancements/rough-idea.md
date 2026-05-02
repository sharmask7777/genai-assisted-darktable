# Rough Idea: Darktable GenAI Assistant Enhancements

## Goal
Enhance the existing `dt-ai` tool and `genai-assisted-darktable` skill to support intelligent cropping and advanced technical editing.

## Key Features
1. **Intelligent Cropping Selection**: 
   - Gemini suggests 3 crops (Rule of Thirds, tight, etc.).
   - User selects one via CLI.
   - Coordinates are injected into Darktable's `clipping` module.
2. **Advanced Detail Modules**: 
   - Integrate `diffuse or sharpen` into `xmp.py`.
   - Use binary C-struct packing for PDE-based deblurring and denoising.
   - Apply hardware-aware noise presets.
3. **Mentorship & KB**: 
   - Research best practices for scene-referred detail management.
   - Provide technical rationale in "Mentor Reports."

## Baseline
- Existing `dt-ai` Click CLI (Python).
- Existing `genai-assisted-darktable` skill (SOP).
- Darktable 5.x scene-referred (AgX) pipeline.