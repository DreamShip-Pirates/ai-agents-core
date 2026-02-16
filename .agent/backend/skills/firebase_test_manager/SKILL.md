---
name: Firebase Test Manager
description: Testing protocols and environment management for the QA Engineer agent.
---

# Firebase Test Manager Skill

## Purpose
To enable the **QA Engineer** to reliably manage the Firebase Test Environment, ensuring clean state and avoiding flaky tests.

## 1. Test Environment Hygiene Protocols
### ❌ FORBIDDEN: `afterAll` Cloud Cleanup
*   **Do NOT** clean up cloud resources (Firestore/Storage) in `afterAll` or `afterEach` hooks of individual test files.
*   **Reason**: This runs after *every* file, often triggering "Unguarded Storage Initialization" errors in CI and causing intermittent failures.

### ✅ REQUIRED: Mock Reset Pattern
*   **Protocol**: Use in-memory mock resets for test cleanup.
    ```typescript
    // tests/utils/resetMocks.ts
    afterAll(() => {
      if (process.env.TEST_MODE === 'local') {
         FirebaseInit.resetMockData(); // Clears in-memory maps
      }
    });
    ```
*   **Global Teardown**: Heavy cleanup of *real* resources should only happen once in `globalTeardown.ts`.

## 2. Environment Guards (Service Layer)
*   **Rule**: Controllers/Endpoints should remain clean of test-specific logic.
*   **Implementation**: Place guards inside the **Service Layer** methods that call external APIs (Firestore, Storage, Auth).
*   **Requirement**: Any service interacting with the cloud MUST be "CI-Safe". It should either return a mock or skip the operation if `TEST_MODE === 'local'`.
*   **Code Pattern (Service)**:
    ```typescript
    if (process.env.TEST_MODE === 'local') return { success: true, mock: true };
    ```

## 3. Remote Environment Parity & Index Awareness
*   **Gap**: Local mocks do not enforce Firestore indexes. Tests passing locally may fail in production with `Code 9 (FAILED_PRECONDITION)`.
*   **Protocol**:
    *   **Index Sync**: When updating Firestore queries, verify if they require a composite index. Check existing `firestore.indexes.json`.
    *   **Validation**: Validate JSON syntax of index files before deployment.
    *   **Remote Verification**: Always run `npm run test:remote` after infrastructure changes (indexes, security rules) to confirm environment-specific configurations are correct.
*   **Best Practice**: If a query fails with `Database configuration error`, check the GCP/Firebase console for the "Create Index" link provided in the full error details.

## 4. Test Execution & debugging
*   **Verbose Logging**: To debug authentication flows, run:
    `$env:VERBOSE_TEST_LOGGING='true'; npm run test:local ...`
*   **Process Safety**: If tests exit with code 1 but no errors, it's likely "Process Suicide". Ensure `processCleanup.ts` ignores `process.pid`.
