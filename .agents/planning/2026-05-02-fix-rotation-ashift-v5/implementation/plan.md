# Implementation Plan: Re-enabling Rotation (Ashift v5)

## Implementation Checklist
- [ ] Step 1: Core Data Structure and Packing
- [ ] Step 2: Zlib Compression and Encoding
- [ ] Step 3: Metadata Integration and Caller Updates
- [ ] Step 4: Verification with Sample Data

## Implementation Steps

### Step 1: Core Data Structure and Packing
**Objective:** Implement the initial 892-byte buffer and the logic to pack the transformation parameters into the first 56 bytes.

**General Implementation Guidance:**
- Define the `ASHIFT_STRUCT_SIZE = 892` constant.
- Update `get_ashift_params` in `dt_ai/xmp.py` to create a `bytearray(ASHIFT_STRUCT_SIZE)`.
- Use `struct.pack_into` with the format `<8f2i4f` to fill the first 56 bytes with `rotation`, `lensshift_v`, `lensshift_h`, `shear`, `f_length`, `crop_factor`, `orthocorr`, `aspect`, `mode`, `cropmode`, `cl`, `cr`, `ct`, `cb`.
- For now, return the raw hex of the buffer for testing.

**Test Requirements:**
- Create a test in `tests/test_xmp_structs.py` that calls `get_ashift_params` and verifies the first 56 bytes of the returned hex match the expected binary representation for a set of known values (e.g., 0.0 rotation, 50mm focal length, 1.0 crop factor).

**Integration:**
- This is the foundation for the updated `get_ashift_params`.

**Demo:**
- A test run showing that the first 56 bytes of the generated hex correctly represent the transformation parameters in little-endian float/int format.

---

### Step 2: Zlib Compression and Encoding
**Objective:** Implement Zlib compression, Base64 encoding, and the `gz16` prefix to match Darktable's XMP format.

**General Implementation Guidance:**
- Import `zlib` and `base64` in `dt_ai/xmp.py`.
- Apply `zlib.compress(buffer)` to the 892-byte buffer.
- Prepend the `gz16` prefix to the Base64-encoded compressed data.
- Ensure the compression level or header matches what Darktable expects (standard `zlib.compress` should work).

**Test Requirements:**
- Update the test in `tests/test_xmp_structs.py` to decode and decompress the returned string and verify it results in exactly 892 bytes.
- Verify that the decompressed buffer contains the correct parameters at the expected offsets.

**Integration:**
- Replaces the raw hex output from Step 1 with the final encoded string format.

**Demo:**
- A test showing that the generated `gz16...` string can be successfully decompressed back to the 892-byte buffer using standard Zlib tools.

---

### Step 3: Metadata Integration and Caller Updates
**Objective:** Ensure `get_ashift_params` receives the correct `focal_length` and `crop_factor` from the image metadata and re-enable the module in the history flow.

**General Implementation Guidance:**
- Update the caller of `get_ashift_params` (likely in `dt_ai/xmp.py` or `dt_ai/processor.py`) to pass the focal length and crop factor extracted from EXIF.
- Ensure default values (28.0mm, 1.0) are used if metadata is missing.
- Uncomment or re-enable the code that adds the `ashift` module to the XMP history.

**Test Requirements:**
- Add an integration test in `tests/test_xmp_history.py` that generates a complete XMP for a sample raw file and verifies that the `ashift` entry is present and correctly encoded.

**Integration:**
- Connects the new parameter generation to the actual XMP generation pipeline.

**Demo:**
- An XMP file generated for a sample image containing a valid, compressed `ashift` history item.

---

### Step 4: Verification with Sample Data
**Objective:** Final validation using the reverse-engineered parameters from the `1X7A4488.jpg.xmp` sample.

**General Implementation Guidance:**
- Use the values from the sample: `rotation=1.76`, `f_length=600.0`, `crop_factor=3.386362`.
- Verify that the generated encoded string matches (or is functionally equivalent to) the sample's `gz16...` string.

**Test Requirements:**
- A specific test case in `tests/test_xmp_structs.py` using these exact values and comparing the resulting 892-byte decompressed buffer with the one we reverse-engineered.

**Integration:**
- Ensures the implementation perfectly matches the behavior of Darktable 2026.

**Demo:**
- Comparison output showing a match between our generated buffer and the reverse-engineered sample buffer.
