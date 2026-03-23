# Skill: Silent Failure Hunter

**Purpose**: Hunt for swallowed errors.

## Patterns
- `catch (e) {}` (Empty catch)
- `catch (e) { console.log(e); }` (Weak logging)
- `try { ... } finally { ... }` (No catch)

## Enforcement
All `catch` blocks must use a structured logger or re-throw the error with context.
