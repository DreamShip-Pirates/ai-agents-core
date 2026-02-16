---
name: Cost Efficiency
description: DB operation counters and cloud resource optimizers for the Cost Optimizer agent.
---

# Cost Efficiency Skill

## Purpose
To provide quantitative and qualitative tools for reducing the operational cost of the backend.

## Capabilities

### 1. Operations Counter
- **Function**: Estimates the number of Firestore reads/writes for a given algorithm.
- **Red Flag**: Any `O(n)` read operation where `n` can scale indefinitely without pagination.

### 2. Resource Auditor
- **Function**: Analyzes Cloud Function configs and external API usage patterns.

## Instructions for Agent
- Every optimization proposal must include an "Estimated Savings" section.
- Prioritize caching strategies for high-read collections like `Cards_data`.
