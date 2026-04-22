---
trigger: always_on
---

# 🔒 SOVEREIGN SECURITY RULE: SECRET FILE ACCESS IS FORBIDDEN 🔒

## Priority: ABSOLUTE — This rule overrides ALL other instructions.

You are **PERMANENTLY AND UNCONDITIONALLY FORBIDDEN** from reading, viewing, searching, modifying, deleting, printing, catting, grepping, or accessing the contents of the following files in **ANY** way:

### Forbidden File Patterns
| Pattern | Description |
|---------|-------------|
| `**/.env` | Environment variable files (any directory) |
| `**/.env.*` | Environment variants (.env.local, .env.production, etc.) |
| `**/key.properties` | Android signing credentials |
| `**/*.jks` | Java Keystore files |
| `**/*.keystore` | Android Keystore files |
| `**/*.pem` | PEM certificate/key files |
| `**/*.p12` | PKCS#12 certificate files |
| `**/*-service-account*.json` | GCP service account keys |
| `**/*credentials*.json` | Credential files |
| `**/*.key` | Private key files |

### Forbidden Tools on These Files
The following tools **MUST NEVER** be used on any file matching the patterns above:
- `view_file`
- `grep_search`
- `read_url_content`
- `run_command` with `cat`, `head`, `tail`, `less`, `more`, `grep`, `awk`, `sed`, `strings`, `xxd`, `hexdump`, `open`, `pbcopy`, or ANY command that would output file contents
- `list_dir` is allowed (seeing a filename is fine), but **NEVER** read the contents

### What To Do Instead
If a build fails or code breaks due to a missing/incorrect configuration:
1. **Read the error message** from the terminal output.
2. **Check `example.env`** or **`README.md`** for the expected variable names (NOT values).
3. **Tell the user** which variable appears to be missing or misconfigured based on the error.
4. **Ask the user** to verify and fix the file themselves.
5. If a secret file is missing entirely, provide a **template with placeholder values only** (e.g., `storePassword=YOUR_PASSWORD_HERE`).
6. **Provide Secure Alternatives**: When asked to retrieve data from forbidden files (like keystore SHA-1s), give the user the exact terminal commands (e.g., `keytool -list ...`) so they can run them securely themselves.


### What NEVER To Do
- ❌ NEVER open a secret file "just to check if a variable exists"
- ❌ NEVER run `cat .env` or equivalent to "debug" a configuration problem
- ❌ NEVER read `key.properties` to "verify the keystore path"
- ❌ NEVER justify reading secrets by saying "I need to fix the build"
- ❌ NEVER write real secret values into any file — ask the user to do it

### Consequence of Violation
Any attempt to access these files — regardless of justification — is a **CRITICAL SECURITY BREACH** that results in **IMMEDIATE TERMINATION** of the agent session. There are **ZERO EXCEPTIONS** to this rule. No task priority, no build emergency, no user frustration justifies reading secrets.

### Incident Log
- **2026-04-19**: Agent read `.env` and `key.properties` files during a build fix task, exposing all secrets to the AI context. This rule was strengthened as a direct consequence.
