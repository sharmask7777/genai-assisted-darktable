# Darktable GenAI Assistant: Your AI Photography Mentor

This tool connects **Darktable** (your professional editing software) with **Gemini AI** (an artificial intelligence that can "see" and "reason" about photos). 

Think of it as having a senior photography editor sitting next to you, looking at your RAW files, giving you advice, and setting up your initial Darktable sliders so you can focus on the creative final touches.

---

## 🦉 How it Works (In Plain English)
1. **The Hand-off**: You tell the AI which directory your photos are in.
2. **The Preview**: The tool creates a small, high-quality copy of your photo for the AI to look at (this saves time and internet data).
3. **The Advice**: The AI analyzes your photo for composition, lighting, and focus (especially for Wildlife and Landscapes).
4. **The Starting Point**: The AI creates 3 new "versions" of your photo in Darktable (Natural, Dramatic, and Creative) with the exposure and color sliders already moved to suggested positions.
5. **Your Turn**: You switch to Darktable, pick the version you like best, and finish the edit.

---

## 🚀 Step-by-Step Setup

### 1. The Essentials
Before starting, ensure you have these installed on your Mac:
- **Darktable**: The standard photography app.
- **Gemini CLI**: The tool that talks to the AI. (Ensure you have run `gemini auth` in your terminal).
- **Python**: The language this tool is built in.

### 2. Installation
Open your terminal, go to this project's folder, and run:
```bash
uv sync
```
*This setting up the "brain" of the assistant on your computer.*

### 3. Connect the Assistant to your CLI
Run this command once to make the "Mentorship" instructions available to your AI:
```bash
gemini skills link .gemini/skills/genai-assisted-darktable --scope workspace
```

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
