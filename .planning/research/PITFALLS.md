# Pitfalls & Mitigations

## 1. Hex Encoding Drift
- **Problem:** Darktable module versions (`modversion`) change between releases.
- **Mitigation:** Script must detect Darktable version or default to safe, standard modversions.

## 2. Preview Accuracy
- **Problem:** `sips` doesn't apply current XMP settings.
- **Mitigation:** For "Update" passes, use `darktable-cli` to generate a preview that reflects existing edits.

## 3. Token Overhead
- **Problem:** Sending full-res JPEGs is expensive.
- **Mitigation:** Downscale to 2048px (standard Vision model sweet spot).
