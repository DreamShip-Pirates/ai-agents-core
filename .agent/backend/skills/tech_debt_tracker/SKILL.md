---
name: Tech Debt Tracker
description: Tools for the Coder/Fixer agents to identify and reduce technical debt.
---

# Tech Debt Tracker Skill

## Purpose
To assist **Coder** and **Fixer** agents in maintaining a clean codebase by identifying legacy patterns, TODOs, and inconsistencies.

## Capabilities

### 1. Codebase Consistency Scanner
- **Filename Casing**:
    - Scan `src/services/`.
    - **Rule**: Enforce consistency. Current state is mixed (`MailgunService.ts` vs `cdnService.ts`).
    - **Action**: When creating new files, follow the dominant pattern (or Project Manager's directive).
- **Logging**:
    - **Hunt**: `console.log`, `console.error`.
    - **Fix**: Recommend replacing with `appLogger` from `src/utils/logger.ts`.

### 2. Orphaned & Legacy Code Hunter
- **Markers**: Grep for `TODO`, `FIXME`, `HACK`, `DEPRECATED`.
- **Firebase**: Check for deprecated `firebase-admin` methods or legacy initialization patterns not using `FirebaseInit.ts`.
- **Imports**: Check for unused imports (using `eslint` or `ts-unused-exports`).

### 3. Service Layer Hygiene
- **Check**: Verify that Controllers (`src/routes/`) are thin.
- **Anti-Pattern**: Business logic inside route handlers.
- **Fix**: Move logic to `src/services/`.

## Instructions for Agent
- **Proactive**: Before starting a task in a file, run a quick scan for local Tech Debt.
- **Reporting**: precise line numbers and the nature of the debt.
- **Refactoring**: If touching a file with "Low hanging fruit" debt (e.g., a simple `console.log` replacement), fix it as part of the task (Scout Rule).
