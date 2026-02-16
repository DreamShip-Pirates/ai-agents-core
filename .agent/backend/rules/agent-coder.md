# Coder Agent Rules

These rules apply to all code generation and modification tasks.

## 1. Environment Safety & Guards
*   **Service-Level Abstraction**: Production endpoints (Controllers) should remain free of environment-specific `if (TEST_MODE)` blocks. 
*   **The Guard Pattern**: To enable CI/Local testing without real cloud credentials, place guards inside the **Service Layer** (e.g., `FirebaseUserService`, `MailgunService`).
*   **Requirement**: Any service method that interacts with external cloud providers MUST be safe to call during integration tests. If real credentials aren't available, they must either return mock data or skip the operation gracefully.
*   **Example (Service Layer)**:
    ```typescript
    async uploadImage(data: string) {
      if (process.env.TEST_MODE === 'local') return { url: 'mock_url' };
      return this.storage.upload(data);
    }
    ```
*   **Test Utilities**: All code in `tests/utils/` MUST be strictly guarded against accidental cloud initialization.

## 2. Process Management Safety
*   **Suicide Prevention**: When killing processes by port, ALWAYS filter out the current process ID (`process.pid`).
*   **Graceful Shutdown**: Use `SIGTERM` before `SIGKILL`.

## 3. Test Makeup & Cleanup
*   **Mock-First**: Prefer resetting mocks (`FirebaseInit.resetMockData()`) over cleaning up "real" data in `afterAll`.
*   **Global Teardown & Hygiene**: All automated tests in remote mode MUST trigger `FirebaseCleanupService.cleanupTestData()` via `globalTeardown.ts`.
*   **No Side Effects**: Tests must use unique IDs (randomized) for all created resources to avoid collisions.

## 4. Logging & Debugging
*   **Structured Logs**: Use `appLogger` instead of `console.log` in backend code.
*   **Verbose Test Logs**: Support `VERBOSE_TEST_LOGGING` env var in test setups to print full request/response details for debugging.

## 5. Pre-Commit Self-Check
*   **Linting**: Run `npm run lint` after any change to ensure no new warnings are introduced.
*   **No `any`**: Explicitly check for `as any` or `: any` and replace with proper typing.

