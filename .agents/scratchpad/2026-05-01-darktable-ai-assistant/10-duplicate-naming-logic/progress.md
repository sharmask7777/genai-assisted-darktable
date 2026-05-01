# Progress: 10-duplicate-naming-logic

## Tasks
- [x] Implement `get_next_version_path` logic
- [x] Implement sidecar template cloning logic (implicit in future tasks)
- [x] Verify naming with synthetic tests
- [x] Verify naming with real data from `~/Pictures`

## TDD Cycles
1. **Cycle 1: Naming Logic**: Implemented `get_next_version_path` following Darktable's `_nn.xmp` convention.
2. **Cycle 2: Real-World Verification**: Verified against real XMP files in `~/Pictures`. Successfully identified existing XMPs and proposed correct duplicate filenames.
