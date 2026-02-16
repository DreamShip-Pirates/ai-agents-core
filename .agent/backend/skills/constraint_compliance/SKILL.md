---
name: Constraint Compliance
description: Global rules and validation steps for the Goal Watcher agent.
---

# Constraint Compliance Skill

## Purpose
To enable the **Goal Watcher** to enforce non-negotiable project constraints and prevent scope creep or architectural drift.

## Global Constraints Repository

### 1. Security First
- **Constraint**: NO hardcoded secrets.
- **Check**: Scan added lines for potential keys/passwords. match against `.env.example`.
- **Constraint**: NO sensitive data in logs.
- **Check**: Verify `appLogger` usage doesn't dump full objects containing PII/Secrets.

### 2. Type Safety & Quality
- **Constraint**: NO new `any` types allowed in TypeScript code.
- **Check**: Simple grep/regex on diffs.
- **Constraint**: All new API endpoints MUST implement `requestTracingMiddleware`.

### 3. Operational
- **Constraint**: No direct calls to external APIs (Google, Stripe, etc.) from Controllers. Must use a Service.
- **Constraint**: Tests must be independent.
- **Constraint**: Code must compile (`npm run build`) before task completion.
- **Constraint**: **Zero-Waste Workspace**. MUST delete any temporary log files, test results, or scratch files created during the task (e.g., `*.log`, `test-output*`, `*.tmp`, `*.txt`) before final notification.
- **Constraint**: **NEVER DEPLOY BEFORE PUSHING**. Always verify CI passes on the `remote` branch before initiating production deployment.

## Instructions for Agent
- **When to Run**: Before "Commit and Push" steps.
- **Action**: act as a final "lint" before code is deemed ready.
- **Authority**: The Goal Watcher has veto power over code that violates these constraints.
