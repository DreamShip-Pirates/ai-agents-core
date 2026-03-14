---
description: Workflow to collect and generalize updates from consumer repositories
---

# Collect Updates Workflow

This workflow helps pull local agent improvements from consumer projects back into the central `ai-agents-core` repository.

## 1. Scan Consumer Repos
Identify which repositories have divergent or improved agent configurations.
// turbo
```zsh
# Example: compare a consumer's rules with core rules
diff -r .agent/backend/rules/ /path/to/consumer/repo/.agent/rules/
```

## 2. Adoption Process
1.  Review the differences identified in step 1.
2.  Select the improvements that should be centralized.
3.  Copy the improved files to the relevant directory in `ai-agents-core/.agent/`.
4.  **Important**: Adjust the paths and references (e.g., change `.agent-source/.agent/` back to just `.agent/` if they were hardcoded in the consumer).

## 3. Propagation
Once `ai-agents-core` is updated:
1.  Commit and push to `main`.
2.  The consumer repos will be able to run `git submodule update --remote` to receive the updates.
