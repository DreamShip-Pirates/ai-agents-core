# Project Patterns & Tribal Knowledge

This file contains codified knowledge, common pitfalls, and established patterns for this project.

## Established Patterns

- **UI Components**: Follow the existing structure in `js/` for new components.
- **Authentication**: Using `api/v4` for OTP authentication.
- **Context Management**: Use the **Goalkeeper** agent and `context_manager` skill to summarize task state in `brain/context_state.md` to prevent context bloat.

## Known Gotchas

- **Environment Variables**: Never read `.env` directly; use `.env.example` as a reference for required variables.

## Problem -> Fix Ledger

- **Problem**: Context window bloat in long tasks leading to high costs and drift. **Fix**: Implement the **Goalkeeper** role for proactive context compression and state tracking.
- **Problem**: Agent attempted to access `.env` file despite existing warnings. **Fix**: Implement **IRON LAW #1: ZERO-TOLERANCE .ENV ACCESS** in `security.md`, `orchestrator.md`, and `agent_improver.md`. Explicitly prohibit any `view_file`, `list_dir`, or `grep_search` on patterns containing `.env`.
<!-- Add new entries here -->

