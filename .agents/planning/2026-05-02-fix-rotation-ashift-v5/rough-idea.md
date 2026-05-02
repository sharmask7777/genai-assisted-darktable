# Rough Idea: Re-enabling Rotation (Ashift v5)

## The Issue
The current `ashift` v5 implementation using 48-byte raw hex triggers "insane data" errors in Darktable 2026. Manual analysis shows that the actual structure used in the user's version is much larger (approx 160+ bytes) and often Gzip-compressed in the XMP.

## Reverse-Engineered Structure (Ashift v5)
Decompressed hex from a working XMP:
`ae47e13f0000000000000000000000000000164428ba58400000c8420000803f00000000010000000a51a53c38207b3f0ecb3b3d1997743f...`

## Plan
1.  **Binary Mapping**: Map the 160+ bytes to the Darktable source code for `iop_ashift_params_t`.
2.  **Gzip Compression**: Implement `zlib` compression for the params to match the native XMP style.
3.  **TDD**: Create a test case that verifies the generated hex matches the reverse-engineered string for a 0.0 rotation.

## Sample Data
A working XMP for `1X7A4488.jpg` has been found with the following `ashift` params:
`gz16eJxb5/7QngEFiLlo7IpwYGA44cTA0ACWYwRirsClNhYK1fZ8p61tJaeXoOkZBaNgFJAKAAkPCrY=`
