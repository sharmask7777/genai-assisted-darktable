# Task: Implement Module Injection Logic

## Description
Implement the logic to inject new processing modules into an XMP's history stack. This involves adding new `rdf:li` elements with the correct attributes (`operation`, `enabled`, `params`, `modversion`).

## Background
Darktable reads the history stack sequentially. For our AI variations, we need to append (or insert) the AI-driven modules like Exposure and Color Balance at the end of the existing history.

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement `add_history_item(root, operation, params, modversion, enabled=True)`.
2. Generate unique `darktable:num` values for each history item (sequential integer).
3. Automatically call `sync_history_end` after every injection.
4. Set safe defaults for `blendop_version` and `blendop_params` (often empty or standard bypass).

## Dependencies
- XMP Sync (Step 4).
- Hex Mapping (Tasks 5-01, 5-02).

## Implementation Approach
1. Locate the `rdf:Seq` element in the root.
2. Append a new `rdf:li` with all required `darktable:*` attributes.
3. Ensure the `darktable:num` is incremented based on the current list size.

## Acceptance Criteria

1. **Successful Injection**
   - Given an XMP with 2 modules
   - When `add_history_item` is called for 'exposure'
   - Then the history stack has 3 modules and `history_end` is `3`.

2. **Attribute Correctness**
   - Given an injected module
   - Then it contains all 9+ required attributes: `operation`, `enabled`, `modversion`, `params`, `multi_name`, `multi_priority`, `blendop_version`, `blendop_params`.

## Metadata
- **Complexity**: Medium
- **Labels**: XML, Logic, Workflow
- **Required Skills**: Python, XML
