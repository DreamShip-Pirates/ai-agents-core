---
name: Security Threat Modeler
description: Security checklists and validation tools for the Architect agent.
---

# Security Threat Modeler Skill

## Purpose
To empower the **Architect** agent to identify security risks early in the design phase and enforce security best practices in the implementation.

## Capabilities

### 1. OWASP Top 10 (API Focus) Checklist
- **Injection**: Verify inputs are validated and sanitized. No direct SQL/NoSQL query concatenation.
- **Broken Object Level Authorization (BOLA)**: Ensure resource IDs in URLs are checked against the authenticated user's permissions.
- **Excessive Data Exposure**: Verify that APIs return only necessary data. Use DTOs or response shaping.
- **Lack of Resources & Rate Limiting**: Check if endpoints have rate limiting or resource quotas.
- **Security Misconfiguration**: Verify `helmet` usage and proper error handling (no stack traces in production).

### 2. Middleware & Configuration Validation
- **Server Setup Checks (`src/server.ts`):**
    - Verify `helmet()` is the first or very early middleware.
    - Verify `cors()` configuration does NOT allow `*` in production.
    - **Rule**: `allowedOrigins` must be configurable via ENV and stricter than `localhost`.
    - Verify `morgan` connects to a secure logging pipeline (not just stdout in prod).

### 3. Scheduler & Background Task Review
- **File**: `src/services/securityScheduler.ts`
- **Check**: Ensure background tasks (like `SecurityScheduler`) handle errors gracefully and don't crash the main process.
- **Check**: Verify that scheduled tasks do not run with elevated privileges unnecessarily.

### 4. AuthZ & AuthN Patterns
- **User IDs**: Ensure all user-scoped data access uses the UID from the decoded ID token (not from the request body).
- **Secrets**: Scan for hardcoded API keys or secrets. All secrets must use `dotenv` or `SecretManagerService`.

## Instructions for Agent
- **When Designing**: Run through the OWASP checklist for every new endpoint.
- **When Reviewing**: Check `src/server.ts` for accidental weakening of security middleware.
- **Output**: Create an `ARCH_SECURITY` note in the implementation plan if risks are found.
