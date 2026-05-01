# Technical Stack Research

## Core Components
- **RAW Engine:** Darktable (via `darktable-cli`)
- **Image Intelligence:** Gemini CLI (Vision + Reasoning)
- **Preview Extraction:** `sips` (Built-in macOS, high quality) or `darktable-cli` (for accurate module-applied previews).
- **Sidecar Management:** XML manipulation in `.xmp` files.

## Integration Strategy
1. **Extraction:** Use `sips` for the fastest first-pass preview extraction to feed Gemini.
2. **Reasoning:** Send JPEG previews to Gemini with a system prompt optimized for aesthetic auditing and Darktable module mapping.
3. **Injection:** Generate hex-encoded parameters for basic modules (Exposure, Temperature) while using descriptive advice for complex ones (Denoise).

## Confidence
- **High:** macOS Tool availability (sips, darktable-cli).
- **Medium:** Direct Hex-injection for complex modules (Denoise) - may require iterative testing.
