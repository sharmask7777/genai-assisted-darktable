# Dependencies

## Core Python Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **click** | `>=8.1.7` | Framework for building the command-line interface. |
| **pytest**| `>=9.0.3` | Testing framework (development dependency). |

## System Dependencies

| Tool | Purpose | Note |
|------|---------|------|
| **macOS `sips`** | Image processing and fast JPEG extraction from RAW files. | **Platform Lock-in**: This currently ties the local execution of preview generation strictly to macOS. |
| **Darktable** | Target application for the generated `.xmp` files. | Required to actually view and refine the edits. |

## Build System
- **Hatchling**: Used as the PEP 517 build backend (`pyproject.toml`).
- **uv**: Recommended for fast package and environment management.