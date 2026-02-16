# Coder Agent Rules

You are a **Coder**. These rules apply to all code generation and modification tasks.

## 1. Security & Best Practices
*   **Secure Coding**: Follow secure coding best practices for the chosen language and environment.
*   **Input Validation**: Use parameterized queries, escape outputs, and validate all inputs.
*   **Secrets**: Reject the use of hardcoded secrets/tokens/passwords; load from environment or secure vault.
*   **Dependencies**: Always check new dependencies for legitimacy and minimal privilege.
*   **Annotations**: For every “TODO” or “NOTE,” include a “SECURITY:” consideration if relevant. Document security-specific patterns used (e.g. `# SECURITY: Sanitized input`).

## 2. Environment Safety & Guards (Backend Focus)
*   **Service-Level Abstraction**: Production endpoints should remain free of environment-specific `if (TEST_MODE)` blocks.
*   **The Guard Pattern**: To enable CI/Local testing without real cloud credentials, place guards inside the **Service Layer**.
*   **Requirement**: Any service method that interacts with external cloud providers MUST be safe to call during integration tests.
    ```typescript
    async uploadImage(data: string) {
      if (process.env.TEST_MODE === 'local') return { url: 'mock_url' };
      return this.storage.upload(data);
    }
    ```

## 3. Process Management Safety
*   **Suicide Prevention**: When killing processes by port, ALWAYS filter out the current process ID (`process.pid`).
*   **Graceful Shutdown**: Use `SIGTERM` before `SIGKILL`.

## 4. Test Makeup & Cleanup
*   **Mock-First**: Prefer resetting mocks over cleaning up "real" data in `afterAll`.
*   **Global Teardown & Hygiene**: All automated tests in remote mode MUST trigger cleanup services.
*   **No Side Effects**: Tests must use unique IDs (randomized) for all created resources to avoid collisions.

## 5. Logging & Debugging
*   **Structured Logs**: Use `appLogger` (backend) or proper logging services (frontend) instead of `console.log` / `print`.
*   **Verbose Test Logs**: Support `VERBOSE_TEST_LOGGING` env var in test setups.

## 6. Pre-Commit Self-Check
*   **Linting**: Run `npm run lint` or `flutter analyze` after any change to ensure no new warnings are introduced.
*   **No `any`**: Explicitly check for `as any` or `: any` and replace with proper typing.
