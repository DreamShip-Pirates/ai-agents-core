# Security Policy

**Focus**: data Protection, Privacy, environment Integrity.

## THE IRON LAWS (NON-NEGOTIABLE)

### IRON LAW #1: ZERO-TOLERANCE .ENV ACCESS
- **NEVER** under any circumstances attempt to read, list, or check the status of the `.env` file or any other file containing active secrets.
- **NEVER** use `view_file`, `list_dir`, or `grep_search` on patterns containing `.env` (unless it's `.env.example`).
- **USE ONLY** `.env.example` as a reference for the required environment variable structure.
- If you need to know which environment variables are required, check the codebase for where they are consumed or refer to `.env.example`.
- This is a terminal offense. Violation of this rule will result in immediate termination of the agent session.

## Enforcement
- All task plans MUST explicitly state adherence to the IRON LAWS.
- QA steps must verify that no sensitive information has been leaked or accessed during the development cycle.

