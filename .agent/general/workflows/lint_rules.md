---
description: Workflow to manually verify the quality and formatting of agent rules
---

# Lint Rules Workflow

This workflow is used to ensure that all rule files in the repository adhere to the established standards.

## 1. Syntax Check
Verify that all `.md` files in `.agent/` have valid frontmatter.
// turbo
```zsh
grep -r "---" .agent/
```

## 2. Formatting Check
- Verify that every rule has a `# Agent Name` or `# Subagent` header.
- Ensure that lists are properly formatted.
- Check for broken file links.

## 3. Consistency Check
Use the **Rule Reviewer** to check for contradictions between `general` and platform-specific folders.
