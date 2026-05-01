# Darktable GenAI Assistant: Your AI Photography Mentor

This tool connects **Darktable** (your professional editing software) with **Gemini AI** (an artificial intelligence that can "see" and "reason" about photos). 

Think of it as having a senior photography editor sitting next to you, looking at your RAW files, giving you advice, and setting up your initial Darktable sliders so you can focus on the creative final touches.

---

## 📥 Get the Code (New to GitHub?)

If you don't know how to use GitHub, follow these 3 simple steps to get started:

1. **Download**: Click the green **"Code"** button at the top of this page and select **"Download ZIP"**.
2. **Unzip**: Find the `genai-assisted-darktable-main.zip` in your Downloads folder and double-click it to unzip it.
3. **Move**: Move the resulting folder to a permanent place, like your `Documents` or `Pictures` folder.

---

## 🦉 How it Works (In Plain English)
1. **The Hand-off**: You tell the AI which directory your photos are in.
2. **The Preview**: The tool creates a small, high-quality copy of your photo for the AI to look at (this saves time and internet data).
3. **The Intelligence**: Using **macOS-native metadata indexing (`mdls`)**, the tool gathers your camera settings (ISO, Lens, Aperture) to help the AI make smarter technical decisions like noise reduction.
4. **The Advice**: The AI analyzes your photo for composition, lighting, and focus (especially for Wildlife and Landscapes).
5. **The Pre-flight Review**: Before changing anything, the AI presents a **"Mentor Report"** explaining *why* it's choosing specific settings and which modern Darktable modules (like AgX) it's using.
6. **The Starting Point**: The AI creates 3 new "versions" of your photo in Darktable (Natural, Dramatic, and Research-based) using the cutting-edge **AgX Scene-Referred** pipeline.
7. **Your Turn**: You switch to Darktable, pick the version you like best, and finish the edit.

---

## 🛠 Advanced Features (2026 Edition)
- **AgX-First Workflow**: We prioritize the modern `AgX` tone mapper over legacy modules, ensuring your colors stay natural even in high-contrast highlights.
- **Hardware-Aware**: The system includes a sensor-correction database (e.g., Canon R7 high-ISO noise handling, Sony black-level offsets).
- **Troubleshooting**: If an image appears black, it's usually a `sigmoid` or `agx` version mismatch. Our `SKILL.md` contains a recovery guide for these rare schema updates.

---

## 🚀 Step-by-Step Setup

### 1. The Essentials
Before starting, ensure you have these installed on your Mac:
- **Darktable**: The standard photography app. [Download here](https://www.darktable.org/install/).
- **Gemini CLI**: The tool that talks to the AI. (Ensure you have run `gemini auth` in your terminal).
- **Python (uv)**: We use a tool called `uv` to manage the "brain" of the assistant. Open your **Terminal** (press `Cmd + Space` and type "Terminal") and run:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Installation
Now, let's set up the assistant. In your **Terminal**, you need to "go into" the folder you downloaded:
1. Type `cd ` (type cd followed by a space).
2. **Drag and drop** the folder you unzipped directly into the Terminal window. It will look something like this: `cd /Users/yourname/Documents/genai-assisted-darktable`
3. Press **Enter**.
4. Run this command to install everything:
   ```bash
   uv sync
   ```

### 3. Connect the Assistant to your CLI
Run this command once to make the "Mentorship" instructions available to your AI:
```bash
gemini skills link skills/genai-assisted-darktable --scope workspace
```

---

## 🤖 Using Other AI Assistants (Claude, Kiro)

While this project is designed for the Gemini CLI, the core workflow can be adapted to other conversational AI assistants.

### Gemini
Continue to use the `gemini` command as described.
```bash
gemini
```

### Claude
To use Claude, you would start its own command-line interface (if available):
```bash
claude
```

### Kiro
To use the Kiro assistant, you would use its dedicated CLI tool:
```bash
kiro-cli
```

After starting the alternative assistant, you would need to manually guide it through the mentorship steps outlined in the "How to Edit Your First Project" section, as the automated skill linking is specific to Gemini CLI.

---

## 📖 How to Edit Your First Project

### Step 1: Start the Mentorship
In your terminal, type:
```bash
gemini
```
Then, once inside the Gemini session, say:
> "Start the darktable mentorship workflow."

### Step 2: Provide Your Photo Path
The AI will ask: *"What is the directory for the images?"*
- **Copy and paste** the folder path where your RAW files are (e.g., `/Users/yourname/Pictures/Wildlife_Shoot`).

### Step 3: Set Up Darktable
The AI will guide you to:
1. Open **Darktable**.
2. **Import** that same folder into your Lighttable.
3. Tell the AI "I'm ready" when Darktable is open and the photos are visible.

### Step 4: Pick a Photo
Tell the AI which photo you want to work on (e.g., `IMG_001.ARW`).
- **The AI will analyze it**: It will explain *why* it likes the shot and what technical improvements it suggests.
- **The AI will move the sliders**: It creates 3 duplicate versions in Darktable for that specific photo.

### Step 5: The "Flip" to Darktable
1. Switch your screen to **Darktable**.
2. In the **Lighttable** view, select your photo.
3. On the right sidebar, click **"Selected images" -> "Read from sidecar"**.
4. You will now see 3 new versions of your photo! Pick one, move to the **Darkroom**, and fine-tune it.

### Step 6: Next Photo
Switch back to your terminal and tell the AI: *"I'm done with this one, let's do the next!"*

---

## 🛡 Safe & Non-Destructive
- **No Overwriting**: The AI *never* touches your original RAW files. 
- **Privacy**: The AI only sees the small preview copies, not your full-sized professional data.
- **Control**: Your manual edits (Version 0) are always preserved. The AI only adds *new* versions for you to try.

---
*Mentorship provided by Gemini AI & Strands Agent SOPs*
