---
name: Migration Safety Check
description: Verify migration scripts for dangerous operations.
---

# Migration Safety Check

Ensures database operations don't accidentally cause data loss or table locks.

## Script: `check_migrations.py`
Usage: `python .agent/skills/migration_safety_check/check_migrations.py --dir scripts`

Features:
- Scans for `DROP TABLE`, `DELETE`, `TRUNCATE`.
- Scans for expensive operations (like adding a column with default value on large tables, though this is harder to detect statically).

## 2. Infrastructure Configuration Validation
*   **Rule**: Files like `firestore.indexes.json` and `firestore.rules` MUST be validated before deployment.
*   **Protocol**:
    *   **JSON Validation**: Ensure no trailing commas or missing braces in `firestore.indexes.json`. Use a standard linter or `node -e "JSON.parse(fs.readFileSync('...'))"`.
    *   **Index Structure**: Verify that composite indexes match the query structure (fields and sort order) exactly as defined in the Service layer.
*   **Checklist for Architect**:
    *   [ ] Does the new query require a composite index?
    *   [ ] Is the index defined in the `firestore.indexes.json` file?
    *   [ ] Is the JSON valid?
