# Backend Patterns & Lessons Learned

## CI/CD
### Firebase Initialization in CI
*   **Problem**: CI pipeline fails because it lacks real Firebase credentials.
*   **Fix**: Modify `FirebaseInit.ts` (or equivalent) to verify the environment. If `NODE_ENV === 'test'` or similar, use dummy credentials/suppress errors to allow the server to start for testing.
*   **Context**: Conversation fc86f011 (Jan 2026).

## API Development
### API V2 -> V3 Migration
*   **Problem**: 404 errors when tests hit V3 endpoints that are not yet registered or have typos in paths.
*   **Fix**: Always verify `routes.ts` or `app.ts` includes the new router *before* running tests. Use `api_contract_validator` to check consistency.
*   **Context**: Conversation 4f11ba1e & e92bc578.

## Build System
### Android R8/ProGuard
*   **Problem**: Release builds fail due to missing classes (e.g., `com.google.android.play.core`).
*   **Fix**: Add specific `-keep` rules in `proguard-rules.pro` when adding new native dependencies.
*   **Context**: Conversation fdbee606.

## Testing
### Integration Testing
*   **Problem**: Tests hitting real backend instead of mocks, causing 404s or 500s.
*   **Fix**: Ensure `globalSetup.ts` or test config points to the local test server or correctly mocked services. Verify API endpoints exist in the code being tested.

### Mocking Services
*   **Problem**: Runtime crashes (`TypeError: Cannot read properties of undefined`) in services during testing when external dependencies (Firebase) invoke callbacks on uninitialized objects.
*   **Fix**: When catching initialization errors in `test` mode, **you MUST provide a mock implementation** of the service object (`firestore`, `auth`), not just set a `successful` flag.
*   **Robust Mocking**: When initialization errors are caught in `test` mode, provide a functional mock for `firestore` and `auth` to prevent runtime crashes.
*   **Stateful Mocking**: Use `Map` objects within mocks to persist data (like users or documents) during a test session. This allows "create then get" flows (common in registration/login) to work even without a real database.
*   **Global vs Local Access**: If using `firebase-admin` directly (e.g., `getFirestore()`), it will expect an initialized app. Use `FirebaseInit.getFirestore` instead, which can return a mock if initialization fails.
*   **Chainable Mocks**: Use a chainable mock for Firestore to handle multiple `.where().where().limit().orderBy()` calls, rather than a rigid nested structure.
*   **Transaction Mocking**: Mock `runTransaction` and `batch` to allow services using complex operations to run during tests without crashing.
*   **Context**: Conversation fc86f011 (Feb 2026).

