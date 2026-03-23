---
name: Knowledge Base Curator
description: Processes for updating and maintaining the agent's memory and knowledge base.
---

# Knowledge Base Curator Skill

## Purpose
To guide the **Agent Improver** in codifying lessons learned, ensuring the "Brain" of the operation grows smarter over time.

## Capabilities

### 1. Pattern Extraction
- **Role**: Analyze completed tasks to find reusable patterns.
- **Target**: `memory/project-patterns.md`, `memory/backend-patterns.md`.
- **Examples**:
    - "How we fixed the Firebase Init race condition".
    - "The correct way to mock `SecretManagerService`".

### 2. Memory Updates
- **Context**: `task.md` and `walkthrough.md`.
- **Action**: Ensure these are kept up-to-date.
- **Rule**: Documentation is NOT optional. It is part of the "Definition of Done".

### 3. Anti-Hallucination Guard
- **Verify**: Check `Active Document` context.
- **Correction**: If the agent "imagined" a file or function that doesn't exist, Create a rule in `rules/` to prevent recurrence.

## Instructions for Agent
- **Trigger**: Run this skill at the end of every comprehensive `task_boundary` (e.g., after Verifying a major feature).
- **Input**: The chat history and file diffs.
- **Output**: Updates to `.agent/memory/` files.
