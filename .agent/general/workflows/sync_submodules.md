---
description: Workflow to ensure that all core submodules are in sync
---

# Sync Submodules Workflow

This workflow ensures that the `ai-agents-core` repository correctly manages its dependencies.

## 1. Check Submodule Status
// turbo
```zsh
git submodule status
```

## 2. Update Submodules 
Run this if submodules are out of date.
// turbo
```zsh
git submodule update --init --recursive
```

## 3. Propagation
If core rules are updated, ensure that you let the user know they need to run `git submodule update --remote` in their consumer projects.
