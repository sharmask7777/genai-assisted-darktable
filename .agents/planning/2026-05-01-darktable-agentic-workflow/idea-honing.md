# Requirements Clarification & Honing

## Established Requirements
- **Tone**: Talkative and educational.
- **Persistence**: Stored in `~/.progress/`.
- **Method**: Agent SOP guided, Python as prompt provider.
- **Workflow**: Open Darktable -> Import -> Nudge -> Variations -> Nudge Next.

## Clarification Questions

**Question 1: The "Nudge" Interaction**

**Question 1: The "Nudge" Interaction**
Answer: User-led selection. Avoid parsing thousands of files. The agent focuses on the image provided by the user, with potential lookahead at 2-3 adjacent images for better context.

**Question 2: "Processed" Directory Structure**

**Question 2: "Processed" Directory Structure**
Answer: XMP sidecars stay with RAW files. Exports (JPGs) go to a 'processed' folder (managed by the user in Darktable). Session state is persisted in the parent directory of the images.

**Question 3: Seamless Flipping (Handoff)**

**Question 3: Seamless Flipping (Handoff)**
Answer: C) Interactive Wait. The agent waits for user confirmation after variations are generated before proceeding.

**Question 4: Initial State Discovery**

**Question 4: Initial State Discovery**
Answer: Explicit Input. The agent asks the user for the image directory upfront.

## Conclusion
The agentic workflow overhaul is defined as a talkative, educational, and user-led experience. The agent guides the user through the Darktable lifecycle, focusing on user-selected images, looking ahead at adjacent frames for context, and persisting state within the project directory for portability. The interaction is a supportive "Mentor" model that respects the user's manual creative adjustments.
