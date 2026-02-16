---
name: Silent Failure Hunter
description: Detects swallowed exceptions and non-traceable error handlers in the backend.
---

# Silent Failure Hunter Skill

## Purpose
To ensure that all errors are properly logged and return meaningful responses to the client, preventing "silent" failures where the system breaks without warning.

## Capabilities

### 1. Swallowed Catch Hunter
- **Regex Pattern**: `catch\s*\(e\)\s*\{\s*\}` or `catch\s*\(err\)\s*\{\s*console\.log\(.*\);?\s*\}` (without rethrowing or reporting).
- **Goal**: Identify and fix `try...catch` blocks that don't satisfy traceability requirements.

### 2. Transaction Rollback Auditor
- **Function**: Checks Firestore transaction blocks to ensure that all logical branches result in a proper finish or error.

## Instructions for Agent
- Run this hunter during the **QA** phase of any coding task.
- Flag any catch block that lacks a unique error ID or fails to log to the centralized monitoring service.
