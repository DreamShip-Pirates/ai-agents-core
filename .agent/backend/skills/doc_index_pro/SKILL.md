---
name: Doc Index Pro (Backend)
description: A library of verified Backend patterns for the Knowledge Seeker and Coder.
---

# Doc Index Pro Skill

## Purpose
To provide the agents with high-quality, pre-verified code snippets for the backend, reducing common errors in Firestore transactions, API versioning, and middleware setup.

## Capabilities

### 1. Snippet Library
- **Structure**: `.agent/snippets/**/*.ts`
- **Function**: Contains "Golden Verification" snippets for:
    - `firestore_transaction_idempotent.ts`
    - `express_v3_router_setup.ts`
    - `error_middleware_traceable.ts`

### 2. Dependency Tracker
- **Function**: Monitors `package.json` to ensure snippets stay compatible with current library versions.

## Instructions for Agent
- Before implementing complex Firestore logic, check the `Snippet Library`.
- If a relevant snippet exists, use it as the primary source of truth.
