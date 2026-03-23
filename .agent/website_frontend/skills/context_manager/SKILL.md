# Context Manager Skill

This skill is used by **Goalkeeper** to manage and compress the task context, preventing token bloat in long-running tasks.

## Purpose
Maintain a high-level summary of the current task, key decisions, and pending actions in `brain/context_state.md`.

## Workflow
1. **Identify Triggers**:
   - Every 10 tool calls in a single task.
   - Upon completion of a major milestone in `task.md`.
   - When the agent logic detects recursive or repetitive loops.
2. **Compress**:
   - Read the current conversation logs and `task.md`.
   - Distill into the `context_state.md` template.
3. **Notify**:
   - Inform the **Orchestrator** that the state has been updated.

## Template (`brain/context_state.md`)
```markdown
# Compressed Task Context: [Task Name]

## Primary Coal
[Concise statement of what we are trying to achieve]

## Current State
- [Finished major step A]
- [Currently working on B]

## Key Technical Decisions
- [Decision 1]: [Reasoning]

## Pending Actions
1. [Next step]
2. [Blockers if any]

## History (Condensed)
[Bullet points of old iterations that are no longer active but relevant for context]
```
