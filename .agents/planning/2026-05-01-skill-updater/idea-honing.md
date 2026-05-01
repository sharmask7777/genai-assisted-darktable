# Idea Honing: Skill Updater

This document tracks the requirements clarification process for the `MAINTAIN_PARITY_WITH_LATEST_DARKTABLE` skill.

## Questions & Answers

### Question 1
Should the `MAINTAIN_PARITY_WITH_LATEST_DARKTABLE` skill be a *read-only* advisor that suggests changes, or should it have the authority to *directly modify* the codebase (prompts, Python logic, XMP schemas) when it detects a discrepancy?

**Answer:** Hybrid approach—it should propose changes that require user approval before being applied to the codebase.

### Question 2
How should the skill "look at" or discover the latest Darktable industry trends and schema changes? Should it rely on specific URLs (e.g., Darktable GitHub, development blogs), a general web search, or an internal "knowledge base" provided by the user?

**Answer:** General web search, Darktable blogs, and GitHub.

### Question 3
Since the skill needs to analyze the "existing implementation", should it perform a full codebase scan every time it's invoked to ensure total consistency, or should it focus its analysis on specific "high-impact" modules like `dt_ai/xmp.py` (schemas) and `dt_ai/ai.py` (prompts)?

**Answer:** Full codebase scan, motivated by the `codebase-summary` skill approach.

### Question 4
When the skill identifies that an update is needed, how should it present its findings? Should it produce a structured "Parity Audit" report (e.g., `PARITY_REPORT.md`) that compares the current implementation against industry standards before proposing code changes, or should it proceed directly to proposing the modifications in the conversation?

**Answer:** Use a hidden progress directory (starting with `.`) with a time-stamped unique name. Generate a Parity Report within this directory and use it to drive a Test-Driven Development (TDD) implementation of the changes, motivated by the `code-assist` skill.

### Question 5
Do you have any specific requirements for how the "Parity Report" should be structured (e.g., specific sections for prompts vs. code vs. schemas), or should I design it based on standard industry auditing patterns?

**Answer:** Use standard industry auditing patterns.

### Question 6
Is `MAINTAIN_PARITY_WITH_LATEST_DARKTABLE` the final name you'd like for this skill, or should it be something more concise (e.g., `darktable-parity-sync`)? Also, do you feel we have sufficient detail to proceed to the research phase?

**Answer:** A concise name is better (e.g., `darktable-parity-sync`). Requirements clarification is complete.
