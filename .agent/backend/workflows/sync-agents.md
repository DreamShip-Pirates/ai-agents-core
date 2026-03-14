---
description: Synchronize agent rules and skills with the authoritative .agent-source repository.
---

1. Fetch latest changes from the agent source repository.
// turbo
2. Run `git submodule update --remote --merge .agent-source`
3. Identify changed files in `.agent-source/.agent/backend/`.
4. Synchronize changes from `.agent-source/.agent/backend/` to `.agent/` using `rsync` or `cp`.
// turbo
5. Run `rsync -av --delete .agent-source/.agent/backend/ .agent/`
6. If local improvements were made to `.agent/`, synchronize them back to `.agent-source/.agent/backend/`.
// turbo
7. Run `rsync -av .agent/rules/ .agent-source/.agent/backend/rules/`
// turbo
8. Run `rsync -av .agent/skills/ .agent-source/.agent/backend/skills/`
9. Navigate to `.agent-source`, stage, and commit changes.
// turbo
10. Run `cd .agent-source && git add . && git commit -m "chore: sync agent improvements from website-backend"`
11. Return to the project root.
