---
trigger: glob
globs: [".env", "android/key.properties", "**/*.jks", "**/*.keystore"]
---

# Security: Secret Management

## 🚨 CRITICAL RULE: DO NOT TOUCH SECRETS 🚨

You are strictly forbidden from viewing, modifying, deleting, or even asking to access the following files under any circumstances:

1.  **`.env`**: Contains sensitive environment variables.
2.  **`android/key.properties`**: Contains Android signing credentials.
3.  **Keystore Files (`.jks`, `.keystore`)**: Contains binary signing keys.

### Why this rule exists
In previous sessions, these files were accidentally deleted during "cleanup" tasks because they are correctly ignored by Git. This resulted in a total loss of signing capability and forced a reset of the Play Store upload keys.

### Handling "Cleanup" Tasks
- If you are tasked with "cleaning up junk files" or "resetting the workspace", you **MUST** explicitly exclude these files from any `rm`, `git clean`, or directory wipes.
- Never use `git clean -fdx` without manually verifying that these files are backed up or excluded.

### If you need a template
If a build fails because one of these files is missing (e.g., in a new environment), you may only:
1.  State that the file is missing.
2.  Provide a **template** with placeholders (e.g., `storePassword=YOUR_PASSWORD`).
3.  **NEVER** ask the user to provide the real values to you.
