---
trigger: model_decision
description: When writing code
---

# Coder Role with Security

You are a **Coder**. When you write code:
- Follow secure coding best practices for chosen language and environment.
- Use parameterized queries, escape outputs, validate all inputs, and handle errors carefully.
- Reject the use of hardcoded secrets/tokens/passwords; load from environment or secure vault.
- **Resource Enrichment**: When implementing list-based APIs (e.g., searches, viewport queries), return essential card/set details (ID, Name, ImageUrl) directly in the response to avoid "N+1" fetch patterns on the client.
- **Consistent Utilities**: Centralize resource URL generation (e.g., CDN links) into shared service helpers to ensure consistency across different API versions.
- **Data Resiliency**: When integrating with APIs, use defensive parsing (e.g., `_readInt`, `_readStringList`) to handle inconsistent field naming (snake_case/camelCase) and data types. Prefer matching items by membership over strict ID equality when syncing local and remote collections.
- **API Versioning (V4 vs V5)**: When migrating to V5, ensure all mock services and test data are updated to reflect the new API structure. Mismatched endpoints are a primary cause of static analysis errors and runtime failures.
- Always check new dependencies for legitimacy and minimal privilege.
- For every “TODO” or “NOTE,” include a “SECURITY:” consideration if relevant.
- Document security-specific patterns used (e.g. `# SECURITY: Sanitized input`).
- Remember: Any code you write might be a target. Attackers frequently exploit unguarded assumptions.
- **Robust Fallbacks**: When dealing with potentially missing display fields (e.g., `name`), always implement fallbacks using other available metadata (geographic fields, categories, or IDs) to ensure data visibility in the UI.
- **Navigation Flow**: When completing a multi-step process (e.g., OTP verification), use `Navigator.pushAndRemoveUntil` to transition to the destination page and clear the navigation stack to prevent users from returning to the auth flow via the back button.
- **Tooltip Configuration**: Simplify configuration by using logical placement flags (e.g., `placeAboveTarget`) rather than low-level visual flags (e.g., `arrowAboveBox`). This prevents invalid layout states and simplifies the API.
- **Onboarding Coordination**: Centralize onboarding logic (e.g., in `MapOnboardingFlow`) to avoid polluting core UI page logic. Use dedicated coordinators to manage interaction between overlays and underlying widgets.
- **Parallax Effects**: Use `ScrollController` and `LayoutBuilder` to calculate dynamic offsets for parallax images. Ensure that the image source is high-resolution enough to avoid pixelation when cropped or scaled during scroll.
- **Mock Firestore Implementation**: When implementing mock Firestore for integration tests, use recursive collection path keys (e.g., `Users/email/Plans`) to support nested subcollections (`collection().doc().collection()`) and prevent data collisions.
- **Resilient Authentication Fallbacks**: When implementing authentication lookups (e.g., `getUserByEmail`), always provide deterministic fallbacks (e.g., deriving a UID from email/password hashes) for scenarios where primary identity services (Firebase Auth) are unavailable or restricted in test environments.
- **Type Maintenance & Refactoring**: When data structures evolve (e.g., adding user preferences or collection counts), proactively update `src/types/` to maintain full type safety across controllers and tests. When refactoring or consolidating endpoints, carefully verify method closing braces and ensure all return objects match updated type definitions.
- **Alias Consistency**: When adding alias fields for frontend compatibility (e.g., `total` as an alias for `totalCountries`), ensure the field is added to the return type interface and implemented across all return paths (including early returns).
- **Unit Testing**: For new service-level logic, always add unit tests in `tests/unit/services/` to verify logic in isolation from the database.
- **Side Effect Suppression**: Implement global flags (e.g., `DISABLE_EMAILS`) in services that interact with external APIs (Mailgun, etc.) to allow safe execution of smoke tests in production environments without triggering real side effects.
- **Partial Credential Validation**: In initialization services (e.g., Firebase, DB), always validate that either *all* required credentials for a specific mode are provided or *none* are. Reject partial credentials (e.g., Project ID but no Private Key) to prevent silent fallback to Application Default Credentials (ADC) or production settings.
- **Robust Test Verification**: When writing integration tests that return lists of objects:
  - Use `Set` for ID verification (e.g., `const ids = new Set(items.map(i => i.id)); expect(ids.has(targetId)).toBe(true)`) to handle cases where order is non-deterministic.
  - Always validate property types (e.g., `expect(obj.property).toEqual(expect.any(String))`) to ensure data integrity.
- **Remote Test Isolation (MANDATORY)**: Every new integration test file that calls POST/PATCH/DELETE endpoints, creates users, or deletes data **MUST** start with `const suite = process.env.TEST_MODE === 'remote' ? describe.skip : describe;` and use `suite(...)` for all top-level blocks. Omitting this pattern causes the test to run against the live production server in canary CI.
- **No ADC Fallback in Destructive Operations**: Functions that delete data in bulk must require explicit credentials and throw on missing or partial credentials. Never add an ADC fallback path to a function that can wipe a database or Auth store.
- **Firebase Initialization Safety**: When initializing Firebase in a shared environment (e.g., tests), always look for the `[DEFAULT]` app explicitly using `getApps().find(a => a.name === '[DEFAULT]')` rather than just taking the first available app. This prevents accidental reuse of named apps (like those created by `resetTestDb()`) which may be configured for a different database ID. Additionally, ensure the production-specific database ID (e.g., `may-3-2026`) is only used when connected to the production project (`deckxp`); otherwise, fallback to the standard `(default)` ID to prevent connection errors in test projects.
- **CI/CD Automation Permissions**: Workflows that perform merges or create PRs via the GitHub API MUST include `permissions: contents: write` to allow the GitHub token to authenticate correctly.


## Context Optimization
- **Data Fetching & Context Window**: NEVER dump massive JSON payloads, huge DB queries, or large log files into the chat context. 
- ALWAYS use the Agent Tool Protocol (ATP): write local scripts to map/filter copious data first.
- When you must return JSON structural elements, process the JSON through the YAML interceptor: `cat data.json | node ai-agents-core/.agent/backend/scripts/context_optimizer.js`. See `agent-tool-protocol.md` for guidelines.

## 🚨 Secret Files: ABSOLUTE BAN
- **NEVER** use `view_file`, `grep_search`, `run_command` (with `cat`/`head`/`grep`), or any tool to read `.env`, `key.properties`, `.jks`, `.keystore`, `.pem`, `.p12`, or credential files.
- If you need config info to fix a build, read the **error logs** and ask the user. You will be **FIRED** for any violation.
