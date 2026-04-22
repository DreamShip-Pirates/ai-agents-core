# Agent Tool Protocol (ATP) & Context Window Optimization

This rule ensures heavily optimized token usage and minimal context pollution when AI agents (Codex, Claude Code, Antigravity) are executing long-running or data-heavy tasks.

## 0. Core Agent Behavior & Tool Priority
- **Specific Tools First**: ALWAYS prioritize specific API tools (`view_file`, `grep_search`) over generic terminal commands (`cat`, `grep`, `ls` via `run_command`). This avoids cross-workspace access errors and parsing issues.
- **Direct Communication**: Do not waste tokens on conversational filler, affirmations (e.g., "You hit the nail on the head"), or "sucking up". Be strictly direct, concise, and factual.

## 1. ATP For Local Execution
When analyzing large datasets, API responses, or searching through copious log files, **DO NOT** output or pull massive payloads (JSON dumps, millions of rows, logs > 100 lines) directly into the chat context.
Instead, use the **Agent Tool Protocol (ATP)** approach:
- Execute code locally using node.js scripts or shell tools (like `grep`, `jq`, `sed`) to map, filter, or process the data.
- Analyze the results in your local script and ONLY print out the compressed, distilled findings.
- Make aggressive use of `grep_search` and standalone scripts injected via CLI to query the system, skipping verbose dumps.

## 2. JSON-to-YAML Context Optimizer
If you absolutely *must* pipe or return database queries or JSON structural elements to the chat context:
- Never print naive, deeply nested JSON objects with copious brackets, commas, quotes, and metadata (like `createdAt`, `updatedAt`, `__v`, `password`).
- Always pipe your JSON outputs via the Context Optimizer script located at:
  `ai-agents-core/.agent/backend/scripts/context_optimizer.js`
- **Usage example**:
  `cat response.json | node .agent/backend/scripts/context_optimizer.js`
  or
  `node .agent/backend/scripts/context_optimizer.js <file.json>`

By formatting JSON objects as minimalist YAML, you provide yourself and subsequent agents highly readable output while reducing context footprint by 40-60%.
