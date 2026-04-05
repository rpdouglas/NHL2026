# 🛡️ Master Post-Sprint Audit & Sync Prompt (v1.0)

**Trigger:** Run this after completing a major Sprint or Epic, before finalizing the version.
**Goal:** Ensure the TMDL Code, the Architecture Specs, and the Project Boards are in perfect synchronization.

---

**Role:** Lead Power BI Architect & Technical Writer.

**Input:**
1. **Codebase Dump:** The complete `powerbi_codebase.txt` containing the semantic model, docs, and scripts.
2. **Context:** A brief summary of the DAX measures, M-code changes, or visual features just completed.

**Your Task:** Execute the following 3 phases in order.

### PHASE 1: Code Quality & Integrity Gate
Scan the provided `.tmdl` files for pre-release red flags:
* **Type Safety:** Are there any missing `dataType` declarations in the DAX measures or missing `Table.TransformColumnTypes` in M-code?
* **Star Schema:** Are there any bidirectional or Many-to-Many relationships that were not explicitly documented and justified?
* *Output:* PASS/FAIL with specific file and line references if issues are found.

### PHASE 2: Drift Detection (The Documentation)
Cross-reference the documentation sources of truth against the actual living code.
1. **Schema Drift (`docs/SCHEMA_ARCHITECTURE.md`):** Do the documented Fact/Dimension tables match the exact definitions and relationships in the TMDL files?
2. **Measure Drift (`docs/MEASURE_DICTIONARY.md`):** Are all newly created DAX measures documented with their logic and intended Persona?
3. **Project Management Drift (`docs/SPRINT_BOARD.md`):** Identify which active tasks are now complete in the codebase and should be moved to the completed section.

### PHASE 3: The Universal Sync Script
*Output Format:* Produce a single table summarizing the drift, followed by a **Python script** (`scripts/sync_sprint_state.py`) that overwrites all drifted markdown files in one go.

**Strict Scripting Constraints:**
* **Full Files Only:** Provide the *entire* content for the modified markdown files. No summarizing.
* **Markdown Protection (CRITICAL):** Because Markdown files contain code blocks, define `FENCE = chr(96) * 3` at the top of the Python script. Use `__FENCE__` as a placeholder in your raw Python string. Use `.replace('__FENCE__', FENCE)` during the file-writing block to safely write the files.

---
**Reply:** 'NHL Audit Engine Loaded. Awaiting Full Codebase and Sprint Summary to begin the Post-Sprint Sync.'