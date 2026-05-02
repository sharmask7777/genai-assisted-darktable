# Idea Honing: Darktable GenAI Assistant Enhancements

This document tracks the requirements clarification process for the cropping and advanced module enhancements.

## Requirements Questions & Answers

1. **How should the user interaction for the 3-crop selection be handled in the CLI?**
   - For example: Should the AI present a descriptive list of the 3 options (e.g., "1. Rule of Thirds - Focus on the eyes", "2. Tight Crop - Portrait style") and have you type a number (1, 2, or 3)? Or would you prefer a different mechanism to identify them?
   - **Answer**: Use a descriptive list. Since a lot of the work is wildlife photography, descriptions will help clarify the intent. Rotation should also be included as part of the cropping step.

2. **For the rotation feature, should the AI prioritize "technical leveling" (fixing slanted horizons/trees) or "creative tilt" (dynamic angles often used in wildlife/action), or should it offer a mix of both?**
   - **Answer**: Offer a mix of both technical leveling and creative tilt.

3. **Regarding the `diffuse or sharpen` module, how should the AI decide between its different modes (e.g., 'sharpen', 'deblur', 'denoise')? Should it rely purely on its visual analysis of the image, or should it prioritize certain modes based on the camera metadata (like high ISO)?**
   - **Answer**: Use both visual analysis and camera metadata. It is acceptable and encouraged to use multiple instances of the module (e.g., one for denoising and one for deblurring).

4. **Once the user selects one of the 3 suggested crops, should the AI then proceed to generate its standard 3 aesthetic variations (Natural, Dramatic, etc.) *using that specific crop*?**
   - **Answer**: Yes. The flow is: User selects 1 of 3 crops -> AI generates 3 aesthetic variations based on that crop. (Lens/camera/CA fixes applied by default).

5. **After presenting the 3 crop descriptions, should the AI provide a way to 'preview' the crop (e.g., generating a temporary low-res JPEG for you to glance at) before you make a final choice, or is the text description sufficient for your workflow?**
   - **Answer**: Create temporary XMP sidecars for the 3 crops. The user will review them in the Darktable Lighttable interface and then tell the AI which one to keep. The temporary files will be cleaned up afterward.

6. **Regarding the 'research' for the `diffuse or sharpen` module: Should the best practices we discover be baked directly into the `AESTHETIC_PROMPT` in `ai.py` (making the AI "inherently" smarter), or should they be stored in a separate knowledge base file (like `research.py` or a markdown file) that the AI reads dynamically?**
   - **Answer**: Store best practices in a separate knowledge base file. Additionally, add a dedicated step in the `SKILL.md` SOP where the AI searches for creative tutorials and aesthetic ideas relevant to the current image's subject to mimic a professional's approach.

7. **Should the results from the creative tutorial search be presented as part of the "Mentor Report" (explaining *where* the ideas came from), or should they just be used "under the hood" to refine the AI's technical suggestions?**
   - **Answer**: Yes, include the research findings and tutorial insights in the "Mentor Report" to explain the professional rationale and source of inspiration.

8. **How should the `darktable-parity-sync` skill be updated based on these enhancements?**
   - **Answer**: The parity sync skill must be aware of the new `clipping`, `ashift`, and `diffuse or sharpen` implementations. Its audit logic should check that the `dt_ai` codebase maintains the correct binary struct layouts and expert sequencing (e.g., denoise before sharpen) established in this project.