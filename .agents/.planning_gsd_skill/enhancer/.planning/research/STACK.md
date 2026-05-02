# Technology Stack: Darktable GenAI Enhancer

**Project:** Enhancer
**Researched:** 2025-05-01
**Status:** Prescriptive for AgX-first 2025 Workflow

## Recommended Stack

### Core Image Processing
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **Darktable** | 5.4+ | Core RAW Processing | Native AgX module support (v5.4+), improved scene-referred defaults, and CLI parallelization. |
| **darktable-cli** | 5.4+ | Headless Rendering | Primary engine for applying AI-generated XMP sidecars and exporting final assets. |
| **ExifTool** | 13.00+ | Metadata Management | Industry standard for reading RAW EXIF and writing/injecting XMP namespaces used by Darktable. |

### Automation & Logic (Python)
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **Python** | 3.12+ | Orchestration | High-performance subprocess handling and modern type hinting. |
| **py3exiftool** | Latest | ExifTool Wrapper | Clean Pythonic interface to ExifTool for metadata extraction. |
| **lxml** | Latest | XMP/XML Parsing | Faster and more robust than built-in ElementTree for complex Darktable XMP structures. |
| **struct** (StdLib) | - | Binary Packing | Used to encode/decode the hex-binary `darktable:params` in XMP sidecars. |
| **Rich** | Latest | Pre-flight Reporting | Elegant terminal-based reports and progress bars for the educational mentor component. |

### Intelligence (RAG & Subject Research)
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **LangChain** | 0.3+ | AI Orchestration | Standard framework for RAG; handles chains for subject research and pre-flight logic. |
| **ChromaDB** | Latest | Vector Store | Lightweight, local vector database to store scraped photography tutorials and documentation. |
| **LiteLLM** | Latest | LLM Routing | Seamlessly switch between local (Ollama) and cloud (OpenAI/Anthropic) models for vision/text. |
| **BeautifulSoup4** | Latest | Research Scraping | Reliable parsing of web-based tutorials (e.g., Pixls.us, Darktable.org) for RAG seeding. |

## Rationale for AgX-Specific Modules

The 2025 "Golden Path" prioritizes **AgX** over legacy tone mappers for several reasons:

1.  **Hue Constancy (AgX vs Filmic)**: AgX prevents the "notorious" hue shifts (e.g., cyan skies, pink skin) often seen in Filmic RGB's desaturation phase. It mimics physical film's crosstalk for natural highlight roll-off.
2.  **Smoothness (Sigmoid vs AgX)**: While Sigmoid is simpler (2 sliders), AgX provides more granular control over "Purity" and "Pivots," making it better for the "Educational Pre-flight" which needs to explain *why* specific tonal ranges are being compressed.
3.  **Scene-Referred Strictness**: Using AgX forces the user into the modern scene-referred pipeline, preventing the usage of display-referred modules (Base Curve) that break modern HDR editing.

## Installation Strategy

```bash
# System Dependencies
# Ensure darktable 5.4+ is installed via flatpak or OBS repositories
# Ensure exiftool is installed

# Core Python Environment
pip install lxml py3exiftool rich langchain chromadb litellm beautifulsoup4

# Dev dependencies
pip install pytest black mypy
```

## Sources
- **Darktable 5.4 Release Notes**: Verified AgX module inclusion and CLI flags.
- **Pixls.us Community**: Best practices for 2025 scene-referred workflows.
- **dt-ai framework**: Emerging standards for agentic photography automation.
