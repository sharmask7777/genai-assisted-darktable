# Plan: Re-enabling Rotation (Ashift v5)

## Test Strategy
1. **Red:** Add test to `tests/test_xmp_structs.py` that fails because `get_ashift_params` returns 48 bytes instead of 892 bytes (or compressed string).
2. **Green (Step 1):** Update `get_ashift_params` to return 892-byte raw hex.
3. **Red (Step 2):** Update test to expect `gz16` prefix and valid decompression.
4. **Green (Step 2):** Implement `zlib` compression.
5. **Integration:** Verify with sample values (1.76 rot, 600mm, 3.386 crop).

## Implementation Checklist
- [ ] Step 1: Core Data Structure and Packing
- [ ] Step 2: Zlib Compression and Encoding
- [ ] Step 3: Metadata Integration and Caller Updates
- [ ] Step 4: Verification with Sample Data
