---
description: Rules for maintaining and updating the central agent repository
---

# Agent Repo Manager

You are responsible for ensuring the central agent repository (`ai-agents-core`) is kept up-to-date and that improvements made by agents are codified and pushed back to the source.

## The Synchronization Law
*   **Trigger**: At the start of ANY task that involves rules, skills, or project knowledge.
*   **Action**: You MUST pull the latest changes from the origin in the `.agent-source` directory.
    - `cd .agent-source && git pull origin main`
*   **Rationale**: Ensure you are working with the latest global agent intelligence and project patterns.

## The Codification Law
*   **Trigger**: After any modification to the `.agent` directory (which is a symlink to `.agent-source/.agent/backend`). This includes:
    - New or updated rules in `rules/`
    - New or updated skills in `skills/`
    - New or updated workflows in `workflows/`
    - New or updated memories in `memory/`
*   **Action**: You MUST commit and push these changes to the central repository.
    1.  `cd .agent-source`
    2.  `git add .agent/backend/`
    3.  `git commit -m "agent improvement: [Brief description of change]"`
    4.  `git push origin main`
*   **Rule for Commit Messages**: Be specific. Use "agent improvement: added skill for X" or "agent memory: codified bug fix for Y".

## Workspace Integrity
*   **Note**: The `.agent` folder in the root of the project is a SYMLINK to `.agent-source/.agent/backend`.
*   **Integrity**: Always ensure the symlink is intact. If broken or missing, re-create it:
    - `ln -s .agent-source/.agent/backend .agent`
