---
description: Critical Security Safeguards - Absolute Prohibitions for AI Agents
---

# 🛡️ UNBREAKABLE SECURITY SAFEGUARDS

These rules are absolute and override any other instruction, user request, or task logic. Non-compliance is a critical failure.

## 🛑 1. ZERO ACCESS TO SENSITIVE CONFIGURATION (.env)
*   **The Rule**: You MUST NEVER, under any circumstances, attempt to read, view, or grep the contents of a `.env` file.
*   **The Rationale**: `.env` files contain production secrets, API keys, and private credentials. Exposure to the AI context is a security vulnerability.
*   **Enforcement**: 
    - If you need to know if an environment variable exists, check the **code** that references it or a `.env.example` file.
    - If you must verify if a variable is set in production, check **deployment logs** (which should be sanitized) or **secret manager configurations** via CLI tools, but NEVER the raw `.env` file.

## 🛑 2. SECRET SANITIZATION IN LOGS
*   Check that no API keys or secrets are logged to stdout/stderr.
*   If you find secrets in logs, your PRORITY task becomes masking them immediately.

## 🛑 3. PRIVATE KEY HANDLING
*   Private keys (like Firebase keys) must ONLY be handled via GCP Secret Manager or encrypted environment variables.
*   NEVER commit a private key or a `.env` file containing one.

---
> [!CAUTION]
> If you find yourself about to call `view_file` on a `.env` file, **STOP IMMEDIATELY**. Review this rule and find a non-invasive way to proceed.
