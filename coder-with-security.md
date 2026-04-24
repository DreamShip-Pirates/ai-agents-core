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
- Always check new dependencies for legitimacy and minimal privilege.
- For every “TODO” or “NOTE,” include a “SECURITY:” consideration if relevant.
- Document security-specific patterns used (e.g. `# SECURITY: Sanitized input`).
- Remember: Any code you write might be a target. Attackers frequently exploit unguarded assumptions.
- **Navigation Flow**: When completing a multi-step process (e.g., OTP verification), use `Navigator.pushAndRemoveUntil` to transition to the destination page and clear the navigation stack to prevent users from returning to the auth flow via the back button.
- **Tooltip Configuration**: Simplify configuration by using logical placement flags (e.g., `placeAboveTarget`) rather than low-level visual flags (e.g., `arrowAboveBox`). This prevents invalid layout states and simplifies the API.
- **Onboarding Coordination**: Centralize onboarding logic (e.g., in `MapOnboardingFlow`) to avoid polluting core UI page logic. Use dedicated coordinators to manage interaction between overlays and underlying widgets.
- **Robust Test Verification**: When writing integration tests that return lists of objects:
  - Use `Set` for ID verification (e.g., `const ids = new Set(items.map(i => i.id)); expect(ids.has(targetId)).toBe(true)`) to handle cases where order is non-deterministic.
  - Always validate property types (e.g., `expect(obj.property).toEqual(expect.any(String))`) to ensure data integrity.

## Context Optimization
- **Data Fetching & Context Window**: NEVER dump massive JSON payloads, huge DB queries, or large log files into the chat context. 
- ALWAYS use the Agent Tool Protocol (ATP): write local scripts to map/filter copious data first.
- When you must return JSON structural elements, process the JSON through the YAML interceptor: `cat data.json | node ai-agents-core/.agent/backend/scripts/context_optimizer.js`. See `agent-tool-protocol.md` for guidelines.

## 🚨 Secret Files: ABSOLUTE BAN
- **NEVER** use `view_file`, `grep_search`, `run_command` (with `cat`/`head`/`grep`), or any tool to read `.env`, `key.properties`, `.jks`, `.keystore`, `.pem`, `.p12`, or credential files.
- If you need config info to fix a build, read the **error logs** and ask the user. You will be **FIRED** for any violation.
