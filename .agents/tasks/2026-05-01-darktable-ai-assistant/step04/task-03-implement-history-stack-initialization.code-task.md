# Task: Implement History Stack Initialization

## Description
Ensure that newly created AI variations have a properly initialized history stack. This includes setting the `history_end` pointer and preparing the `history` section to receive module injections.

## Background
Darktable's history stack is an ordered list. Even an "empty" edit should have a base state (often just the 'raw preparation' steps if cloned from a base XMP).

## Reference Documentation
**Required:**
- Design: .agents/planning/2026-05-01-darktable-ai-assistant/design/detailed-design.md

**Note:** You MUST read the detailed design document before beginning implementation. Read additional references as needed for context.

## Technical Requirements
1. Implement logic to count modules in the `darktable:history` list.
2. Automatically update `darktable:history_end` to match the count.
3. If cloning an existing XMP, ensure the new version's history starts with the parent's history.
4. Implement a helper to clear existing AI-injected modules if re-running on the same version (optional but recommended for idempotency).

## Dependencies
- XMP Skeleton (Task 4-01).
- Version Naming (Task 4-02).

## Implementation Approach
1. Add methods to the XMP management class to manipulate the `history` list.
2. Ensure the XML structure remains valid after every insertion.

## Acceptance Criteria

1. **History End Consistency**
   - Given an XMP with 5 history items
   - When updated
   - Then `darktable:history_end` is exactly `5`.

2. **Inherent History (Cloning)**
   - Given a base XMP with 2 modules
   - When a new version is created
   - Then the new XMP contains those 2 modules in its history.

## Metadata
- **Complexity**: Medium
- **Labels**: XML, Logic, Darktable
- **Required Skills**: Python, XML
