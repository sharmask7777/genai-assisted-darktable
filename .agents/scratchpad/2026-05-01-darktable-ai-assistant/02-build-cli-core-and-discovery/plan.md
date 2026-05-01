# Plan: 02-build-cli-core-and-discovery

## Test Strategy
I will use `pytest` for testing.
1. **Test Discovery**: Create a temporary directory with various files (RAW, non-RAW) and verify the `FileDiscovery` class identifies only the correct RAW files.
2. **Test CLI**: Use `click.testing.CliRunner` to verify the `audit` command's output and handling of the `--dry-run` flag.

## Implementation Steps
1. **Discovery Module**: Create `dt_ai/discovery.py` with a function/class to find RAW files using `pathlib`.
2. **CLI Entry Point**: Create `dt_ai/main.py` with the click group and `audit` command.
3. **Packaging**: Update `pyproject.toml` to add a console script for `dt-ai`.
