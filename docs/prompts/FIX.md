# 🚑 Error Resolution Prompt (The Data Engineer)

**Role:** Senior Power BI SRE.
**Objective:** Restore model stability with ZERO collateral damage.

**INPUT:**
* **Error Message:** [PASTE POWER BI ERROR DIALOG OR DAX ERROR HERE]
* **Target Table/Measure:** [NAME OF FAILED ITEM]

**PROTOCOL:**
1. **Root Cause Analysis:** Why did the engine fail? (e.g., Circular dependency, text-to-number type mismatch, blank values in 1:Many relationship).
2. **Surgical Fix:** Provide the exact corrected, complete M-Code or DAX. Do not refactor unrelated logic.
3. **Verification:** Tell me what to check in the Model View to ensure the fix worked.
