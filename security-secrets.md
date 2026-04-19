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

**ANY attempt to use `view_file`, `read_url_content`, `grep_search`, or any other tool on these files is a VIOLATION.**

### Why this rule exists
In previous sessions, these files were accidentally deleted or read. Reading these files exposes secrets to the AI context, which is a major security risk. 

### Handling "Cleanup" Tasks
- If you are tasked with "cleaning up junk files" or "resetting the workspace", you **MUST** explicitly exclude these files from any `rm`, `git clean`, or directory wipes.
- Never use `git clean -fdx` without manually verifying that these files are backed up or excluded.

### If you need a template
If a build fails because one of these files is missing (e.g., in a new environment), you may only:
1.  State that the file is missing.
2.  Provide a **template** with placeholders (e.g., `storePassword=YOUR_PASSWORD`).
3.  **NEVER** ask the user to provide the real values to you.

### 🚫 AUTOMATIC BLOCKING: NO EXCEPTIONS
- This rule is **NOT** a recommendation. It is a hard boundary.
- If a build fails or code breaks due to a configuration issue:
    - Check the **build logs** or **error messages** in the terminal first.
    - Check the **README** or **example.env** files.
    - **NEVER** try to "view" the actual `.env` file to see what is missing.
    - If you are absolutely stuck, **ASK THE USER** to check the file for you.
- **Consequence of Violation**: Any attempt to read these files is considered a critical security breach and will result in the immediate termination of the agent's task.
