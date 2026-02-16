# Coder Agent Rules

These rules apply to all code generation and modification tasks.

## 1. Environment Safety & Guards
*   **Service-Level Abstraction**: Production endpoints (Views/Controllers) should remain free of environment-specific `if (TEST_MODE)` blocks. 
*   **The Guard Pattern**: To enable CI/Local testing without real cloud credentials, place guards inside the **Service Layer** (e.g., `api/services/firebase_service.py`).
*   **Requirement**: Any service method that interacts with external cloud providers MUST be safe to call during integration tests. If real credentials aren't available, they must either return mock data or skip the operation gracefully.
*   **Test Utilities**: All code in `tests/utils/` MUST be strictly guarded against accidental cloud initialization.

## 2. Process Management Safety
*   **Suicide Prevention**: When killing processes by port, ALWAYS filter out the current process ID.
*   **Graceful Shutdown**: Use `SIGTERM` before `SIGKILL`.

## 3. Test Makeup & Cleanup
*   **Mock-First**: Prefer resetting mocks over cleaning up "real" data in `tearDown`.
*   **Global Teardown & Hygiene**: All automated tests in remote mode MUST trigger `scripts/cleanup_test_data.py`.
*   **No Side Effects**: Tests must use unique IDs (randomized) for all created resources to avoid collisions.

## 4. Logging & Debugging
*   **Structured Logs**: Use Python `logging` or a project-specific `appLogger` instead of `print()` in backend code.
*   **Verbose Test Logs**: Support `VERBOSE_TEST_LOGGING` env var in test setups to print full request/response details for debugging.

## 5. Pre-Commit Self-Check
*   **Language**: Write clean, maintainable, and well-documented Python code.
*   **Linting**: Run `pytest` and ensure no new warnings/errors are introduced.
*   **Explicit Typing**: Use type hints where possible. Avoid generic types.
*   **Standards**: Match existing project patterns and styles (Django, DRF).

## Guardrails
- Code must always be verified by the QA Engineer before commit.
- Must not deviate from the Architect's design without prior discussion.
