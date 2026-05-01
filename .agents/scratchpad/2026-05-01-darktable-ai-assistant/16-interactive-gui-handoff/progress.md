# Progress: 16-interactive-gui-handoff

## Tasks
- [x] Implement `open_in_darktable` in `gui.py`
- [x] Implement `needs_denoise_interaction` in `main.py`
- [x] Verify GUI call with mock
- [x] Verify interactive prompt behavior (Logic implemented, wiring in next task)

## TDD Cycles
1. **Cycle 1: GUI Handoff**: Implemented `dt_ai/gui.py` and verified that it calls the correct macOS command to open Darktable.
2. **Cycle 2: Interaction Detection**: Added logic to `main.py` to detect when a denoise recommendation should trigger a user "take a call" moment.
