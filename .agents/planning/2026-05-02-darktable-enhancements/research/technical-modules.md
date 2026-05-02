# Darktable Technical Module Specifications (v5.4+)

This document defines the binary C-struct layouts required for XMP parameter injection. All values are stored as **little-endian**.

## 1. Diffuse or Sharpen (`diffuse`)
**Modversion:** 2 (Approx.)
**Size:** 68 bytes

| Field | Type | Offset | Description |
|---|---|---|---|
| iterations | int | 0 | Number of diffusion steps |
| radius_central | float | 4 | Scale of targeted detail |
| radius_span | float | 8 | Bandwidth of wavelet scales |
| speed[4] | float[4] | 12 | Diffusion speeds (1st to 4th order) |
| anisotropy[4] | float[4] | 28 | Directionality across/along edges |
| sharpness | float | 44 | Global acutance adjustment |
| edge_sensitivity | float | 48 | Edge detection penalty |
| edge_threshold | float | 52 | Noise floor for edge detection |
| luma_threshold | float | 56 | Masking for highlights/shadows |
| regularization | float | 60 | Numerical stability |
| mode | int | 64 | Operating mode (RGB/Lab/etc) |

---

## 2. Clipping (Crop) (`clipping`)
**Modversion:** 5
**Size:** 84 bytes

| Field | Type | Offset | Description |
|---|---|---|---|
| angle | float | 0 | Rotation (usually 0, handled by ashift) |
| cx | float | 4 | Left crop margin (0.0 to 1.0) |
| cy | float | 8 | Top crop margin (0.0 to 1.0) |
| cw | float | 12 | Crop width (0.0 to 1.0) |
| ch | float | 16 | Crop height (0.0 to 1.0) |
| ratio_n | int | 76 | Aspect ratio numerator |
| ratio_d | int | 80 | Aspect ratio denominator |

---

## 3. Rotate and Perspective (`ashift`)
**Modversion:** 5
**Size:** 48 bytes

| Field | Type | Offset | Description |
|---|---|---|---|
| rotation | float | 0 | Angle in degrees |
| lensshift_v | float | 4 | Vertical keystone |
| lensshift_h | float | 8 | Horizontal keystone |
| shear | float | 12 | Shear angle |
| clip | int | 20 | Clipping mode (1: largest area) |
| guide | int | 32 | Guide overlay (e.g., Rule of Thirds) |

---

## 4. Chromatic Aberration (`cacorrect`)
**Modversion:** 1
**Size:** 8 bytes

| Field | Type | Offset | Description |
|---|---|---|---|
| avoidshift | int | 0 | Boolean: avoid color shifts |
| iterations | int | 4 | 1-5 passes |

---

## 5. Denoise Profiled (`denoiseprofile`)
**Note:** Uses string profile IDs. For "Auto" mode, use empty or special tags.
**Algorithm:** 1 (Wavelets) is standard for 2026.
