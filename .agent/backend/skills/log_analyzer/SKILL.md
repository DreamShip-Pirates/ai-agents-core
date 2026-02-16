---
name: Log Analyzer
description: Analyze server and CI logs for patterns of errors.
---

# Log Analyzer Skill

This skill guides the agent in diagnosing complex CI and server failures.

## 1. Analysis Protocol
When provided with a log file (e.g., `Failed test.txt`):

1.  **Check Exit Code First**: Scroll to the VERY END of the file.
    *   **Exit Code 1 w/ No Visible Error**: Indicates "Process Suicide" or silent crash during cleanup.
    *   **Exit Code 137**: Out of Memory (OOM).

2.  **Scan for Fatal Patterns**: Use `grep` or `Select-String` for these high-priority keywords:
    *   `Could not load the default credentials` -> **Action**: Check `NODE_ENV` / `TEST_MODE` guards.
    *   `EADDRINUSE` -> **Action**: Check process cleanup logic (orphan processes).
    *   `AggregateError` -> **Action**: Network stack failure, often caused by previous unhandled promise rejections.

3.  **Enable Verbose Mode**:
    *   If logs are unclear, request a re-run with: `$env:VERBOSE_TEST_LOGGING='true'; npm run ...`

## 2. Common Root Causes (Reference)

| Symptom | Probable Cause | Fix Strategy |
| :--- | :--- | :--- |
| `Process completed with exit code 1` (no other error) | Cleanup script killed the runner | Filter `process.pid` in `killProcessOnPort` |
| `Could not load default credentials` | Unguarded Google Cloud/Firebase init | Add `if (process.env.TEST_MODE === 'local') return;` |
| Tests pass but build fails | Post-test cleanup (globalTeardown) failure | Check `globalTeardown.ts` logic |

## 3. Tools
*   **Repo-Specific Script**: `python .agent/skills/log_analyzer/analyze_logs.py` (if available)
*   **Native Tools**: `grep`, `Select-String`
