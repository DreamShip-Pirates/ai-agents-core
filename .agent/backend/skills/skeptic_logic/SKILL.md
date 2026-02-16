---
name: Skeptic Logic
description: Red-teaming patterns and edge-case generators for the Skeptic agent.
---

# Skeptic Logic Skill

## Purpose
To empower the **Skeptic** to perform high-fidelity red-teaming of backend designs and implementations.

## Capabilities

### 1. Edge-Case Generator
- **Focus**: Null values, empty arrays, oversized payloads, and unauthorized access attempts.
- **Function**: Generates a checklist of "What-If" scenarios for a given API route.

### 2. Logic Flow Validator
- **Function**: Traces the execution path to find potential race conditions or state-machine deadlocks.

## Instructions for Agent
- Use this skill to generate a "Challenge Report" for every Architect plan.
- Specifically hunt for `TODO` comments or `as any` type assertions that might hide bugs.
