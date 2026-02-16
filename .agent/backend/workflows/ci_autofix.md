---
description: CI Fix Cycle (Semi-Autonomous)
---

This workflow guides the agent through a cycle of diagnosing, fixing, and verifying CI failures.
Note: Test execution and Git operations require user permission.

// turbo-all
1.  **Diagnosis (Fast Fail)**
    *   Read the last 100 lines of `Failed test.txt` to check the exit code.
    *   If exit code is 1 but no errors are visible, check for process termination issues.
    *   Grep for "Error", "FAIL", "Timeout".

2.  **Reproduction**
    *   Propose a local test command: `npm run test:local <failing_test_file>`.
    *   **WAIT** for user approval to run the test.

3.  **Fix Implementation**
    *   Modify code to address the root cause.
    *   Verify the fix using the SAME reproduction command (Ask permission again).

4.  **Verification (Comprehensive)**
    *   Propose running the full local test suite: `npm run test:local`.
    *   **WAIT** for user approval.

5.  **Push**
    *   If verify passes, propose:
        *   `git add .`
        *   `git commit -m "fix(ci): <description>"`
        *   `git push origin dev`
    *   **WAIT** for user approval.
