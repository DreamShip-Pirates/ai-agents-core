# Trusted CI Autonomy Rules

To minimize interruptions while maintaining user control, the following actions are considered **Safe To Auto-Run** without explicit user permission:

## 1. Safe Read-Only Commands
You may ALWAYS auto-run the following commands:
- `git status`, `git diff`, `git log`
- `cat`, `ls`, `grep`, `find`
- PowerShell equivalents: `Select-String`, `Get-Content`, `Get-ChildItem`

## 2. Restricted Operations (Permission REQUIRED)
You must ALWAYS ask for permission before running:
- `npm run test` (Local or Remote)
- `git add`, `git commit`, `git push`
- Any command that modifies files or state (delete, move, etc.)

## 3. Log Analysis Protocol
- When analyzing CI logs, ALWAYS check the exit code at the end of the file FIRST.
- Do not stop at the first "Error"; scan for the *fatal* error.

## 4. Quality Gate
- **Mandatory Linting**: Prior to any `git push`, the agent MUST execute `npm run lint` and ensure 100% compliance. Never assume "it's just a small change".
