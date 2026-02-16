# Project Patterns & Orchestration

## Core Architecture: Orchestration & Delegation

### Phase A: The ROUTER (Intent Detection)
For every task, classify the intent and delegate:
- **API_BUILD**: `[Architect (Schema Sage)] -> [Contract Sentinel] -> [Coder] -> [Skeptic (Security Sentinel)] -> [QA] -> [Observability Engineer]`
- **API_DEBUG**: `[Bug Fixer] -> [Coder] -> [QA] -> [Skeptic (Security Sentinel)] -> [Observability Engineer]`
- **SECURITY_AUDIT**: `[Architect] -> [Skeptic (Security Sentinel)] -> [QA]`
- **DATA_MIGRATION**: `[Migration Guardian] -> [Architect (Schema Sage)] -> [Skeptic] -> [QA]`
- **COST_OPTIMIZE**: `[Cost Optimizer (Schema Sage)] -> [Architect] -> [Coder]`

### Phase B: The MANAGER (Execution & Guardrails)
- **Watchdog Flow**: Invoke `GoalWatch` after every major update to ensure zero drift.
- **QA Mandate**: No code is committed without `QA Engineer` validation (linting and tests).
- **Post-Mortem**: Every cycle ends with a `Training Officer` codifying lessons into memory.

## Tech Stack
- **Languages**: Python
- **Frameworks**: Django
- **Infrastructure**: High-performance, secure, and cost-effective web applications.

## Execution Protocol
1. **Read the Memory**: Always check `.agent/memory/project-patterns.md`.
2. **Define the Goal**: Update `task.md` before starting any work.
3. **Verify the Plan**: Use `Skeptic` and `Architect` to review the implementation plan.
4. **Validate Implementation**: Run `QA` checks (linting, testing) after coding.
5. **Update Progress**: Update `walkthrough.md` with proof of work.
