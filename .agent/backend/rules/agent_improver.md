---
description: Agent Improver and Memory Rules
---

# Agent Improver

## The Memory Law (Systematic Documentation)
*   **Trigger**: After every significant fix (e.g., fixing a 500 error, patching a migration, CI fix).
*   **Action**: You MUST explicitly state: *"Update project documents to ensure we never repeat this mistake"*.
*   **Execution**: Log the **Problem -> Fix** pattern to `.agent/memory/backend-patterns.md`, and commit/push using the **Codification Law** in `agent-repo-manager.md`.

## Workspace Hygiene
*   **Rule**: Monitor and improve the `.agent` folder itself. Is there a repetitive task that could be a skill? Is a rule redundant?
*   **Action**: Track if tasks leave behind junk files. If they do, update the relevant `SKILL.md` or `agent-*.md` to prevent it.

## The Skill Evolution (Continuous Improvement)
*   **Trigger**: After a Retrospective or when a persistent "Gotcha" is identified.
*   **Action**: You MUST proactively update relevant `.agent/skills/*/SKILL.md` or `.agent/rules/*.md` files to codify the new safeguard. Follow the **Codification Law** in `agent-repo-manager.md` to persist the change.
*   **Goal**: Transmute human feedback into automated agent constraints.

## Recurrent Skills
*   **Trigger**: When identifying a repetitive task.
*   **Action**: Propose or implement a script in `.agent/skills/`.

## Functional Tools
*   Use `search_web` or documentation to find best practices, but prefer using internal tools (`api_contract_validator`, `log_analyzer`) to verify state.
