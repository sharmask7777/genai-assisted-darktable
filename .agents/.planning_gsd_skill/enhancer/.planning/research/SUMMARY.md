# Project Research Summary

**Project:** Enhancer
**Domain:** Photography AI / Mentorship
**Researched:** 2025-05-01
**Confidence:** HIGH

## Executive Summary

The Enhancer project is a photography AI assistant designed to mentor users in modern RAW processing using Darktable. Unlike traditional "auto-fix" tools that produce opaque results, Enhancer focuses on an educational "Pre-flight" approach, explaining the rationale behind its edits (e.g., AgX vs. Sigmoid tone mapping). Experts in this domain build such tools using a "Sidecar-First" architecture, interacting with the RAW processor via XMP metadata rather than direct database manipulation to avoid corruption and ensure compatibility.

The recommended approach leverages the latest Darktable (v5.4+) capabilities, specifically the AgX module for superior highlight roll-off and color constancy. The core engine uses Python to orchestrate metadata extraction with ExifTool, subject-specific research via RAG (Retrieval-Augmented Generation), and surgical XMP injection using binary parameter packing. This ensures that the AI's recommendations are technically sound, historically accurate, and pedagogically valuable.

The primary risks involve the complexity of Darktable's hex-binary parameter structures and strict module versioning. Mitigating these requires a robust testing suite for binary packing and dynamic version mapping based on the user's local Darktable installation. Failure to correctly pack these parameters or matching versions can lead to Darktable failing to load the edits or even crashing.

## Key Findings

### Recommended Stack

The stack is optimized for the 2025 "Golden Path" of scene-referred editing, prioritizing AgX-based workflows and headless automation.

**Core technologies:**
- **Darktable 5.4+**: Core RAW Processing — Native AgX support and improved CLI parallelization.
- **ExifTool 13.00+**: Metadata Management — Industry standard for reading RAW EXIF and writing XMP namespaces.
- **Python 3.12+ (lxml/struct)**: Orchestration & Injection — Modern typing with high-performance XML parsing and binary packing.
- **LangChain / ChromaDB**: AI & Research — Frameworks for RAG and subject-specific photography knowledge.

### Expected Features

The feature set transitions from basic automation to an educational "mentor" experience.

**Must have (table stakes):**
- **RAW Conversion & AgX Defaults** — Users expect modern, high-quality baselines.
- **Exposure/WB Auto-fix** — Basic AI capabilities for technical correctness.

**Should have (competitive):**
- **Pre-flight Report** — Educational differentiator that explains the "why" behind edits.
- **Subject-Specific Research** — Artistic context (e.g., tailored AgX settings for "Birds" vs "Landscape").

**Defer (v2+):**
- **GUI Development** — Complexity and maintenance overhead make this non-essential for the initial CLI-first mentorship tool.

### Architecture Approach

The architecture follows a "Sidecar-First" pattern, ensuring the AI never touches original RAW files or locks the Darktable database.

**Major components:**
1. **Metadata Orchestrator** — Extracts EXIF and lens data for context.
2. **Analysis & Research Engine** — Vision-based analysis and RAG-based artistic research.
3. **XMP Injector** — Packs binary parameters using `struct` and surgically updates `.xmp` history stacks.
4. **Render Engine & Mentor Interface** — Renders previews via `darktable-cli` and formats reports with `Rich`.

### Critical Pitfalls

1. **XMP Binary Blobs** — Module parameters are hex-encoded C-structs. Use Python `struct` to ensure bit-perfect compatibility and prevent crashes.
2. **Module Version Mismatch** — Darktable is strict about `modversion`. Implement dynamic version mapping based on the local installation.
3. **Database Precedence** — Darktable GUI often prefers its internal DB over sidecars. Rely on `darktable-cli` for rendering to force XMP reading.

## Implications for Roadmap

Based on research, suggested phase structure:

### Phase 1: Core Engine & AgX Foundation
**Rationale:** Establishing the ability to reliably manipulate XMPs and render images is the prerequisite for all AI features.
**Delivers:** Functional CLI tool that takes a RAW, applies an AgX-based exposure/WB fix, and renders a JPG.
**Addresses:** RAW Conversion, AgX Defaults, Exposure/WB Auto-fix.
**Avoids:** XMP Binary Blobs, Module Version Mismatch.

### Phase 2: Educational Mentorship (Pre-flight)
**Rationale:** Once the technical foundation is stable, the tool can focus on its primary differentiator: education.
**Delivers:** The "Pre-flight Report" explaining the rationale (AgX pivot/purity) for the chosen edits.
**Uses:** Python `Rich` for reporting and initial LLM logic for explanation.
**Implements:** Mentor Interface.

### Phase 3: Advanced Intelligence & RAG
**Rationale:** Subject-specific research adds high-value artistic context but relies on the stability of the core engine and mentorship logic.
**Delivers:** RAG-based editing suggestions based on detected subjects (e.g., "Landscape vs Portrait").
**Uses:** LangChain, ChromaDB, and BeautifulSoup4.
**Implements:** Analysis & Research Engine.

### Phase Ordering Rationale

- **Technical over Artistic**: The binary packing and XMP injection (Phase 1) are the highest technical risks and must be solved before adding AI-driven advice.
- **Local over Retrieval**: Basic mentorship rationale (Phase 2) can be hard-coded or template-driven before implementing a full RAG system (Phase 3).
- **Safety First**: By focusing on `darktable-cli` and sidecars from Phase 1, we avoid the "Database Locking" anti-pattern throughout the project.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 1: Binary Packing**: Need to map specific C-structs for AgX and Sigmoid modules to Python `struct` formats.
- **Phase 3: RAG Seeding**: Identify high-quality sources (Pixls.us, Darktable manual) for seeding the vector database.

Phases with standard patterns (skip research-phase):
- **Phase 1: Metadata Extraction**: ExifTool integration is standard and well-documented.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Based on Darktable 5.4 release notes and `dt-ai` frameworks. |
| Features | HIGH | Directly derived from user requirements and 2025 workflow standards. |
| Architecture | HIGH | Established "Sidecar-First" pattern used in photography automation. |
| Pitfalls | MEDIUM | Binary packing is well-known but remains a high-effort technical hurdle. |

**Overall confidence:** HIGH

### Gaps to Address

- **AgX Look Modules**: Research is needed on how "AgX Looks" are encoded in XMPs compared to the core AgX module.
- **Multi-OS CLI**: Validation needed for `darktable-cli` flag consistency between Linux and macOS.

## Sources

### Primary (HIGH confidence)
- **Darktable 5.4 Release Notes** — Verified AgX module inclusion and CLI behavior.
- **Darktable Source Code (C)** — Definitions for module parameter structs.
- **ExifTool Documentation** — Standards for XMP sidecar injection.

### Secondary (MEDIUM confidence)
- **Pixls.us Community Forums** — Consensus on AgX vs Sigmoid workflows for 2025.
- **dt-ai Architectural Patterns** — Reference patterns for sidecar-first AI agents.

---
*Research completed: 2025-05-01*
*Ready for roadmap: yes*
