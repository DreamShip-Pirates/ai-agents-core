---
name: Clean Code Linter
description: Guidelines and automated checks for the Code Reviewer agent.
---

# Clean Code Linter Skill

## Purpose
To provide the **Code Reviewer** agent with objective criteria for assessing code quality, ensuring maintainability and readability.

## Capabilities

### 1. Complexity Guards
- **Function Length**: Flag functions > 50 lines. Suggest breaking them down.
- **Nesting**: Flag nesting levels > 3 (Callback Hell). Suggest `async/await` or early returns.
- **Cyclomatic Complexity**: Watch for excessive `if/else` or `switch` statements.

### 2. Architecture Enforcement ("Service Layout")
- **Rule**: `src/routes/` files (Controllers) MUST NOT contain business logic or direct DB calls.
- **Rule**: Controllers MUST delegate to classes in `src/services/`.
- **Violation**:
    ```typescript
    // BAD
    router.get('/users', async (req, res) => {
        const users = await firestore.collection('users').get(); // DIRECT DB CALL
        res.json(users);
    });
    ```
- **Correction**:
    ```typescript
    // GOOD
    router.get('/users', async (req, res) => {
        const users = await UserService.getAllUsers();
        res.json(users);
    });
    ```

### 3. Naming Conventions
- **Variables**: `camelCase`.
- **Classes/Interfaces**: `PascalCase`.
- **Constants**: `UPPER_SNAKE_CASE`.
- **Booleans**: Should implement `isX`, `hasX`, `canX`.

### 4. Type Safety
- **No `any`**: Flag usage of `any`. Suggest specific interfaces or `unknown`.
- **No Implicit Any**: Ensure function parameters have explicit types.

## Instructions for Agent
- **Review Protocol**: detailed review of PRs/Changes against these pillars.
- **Tone**: Constructive and educational. Explain *why* a change is requested.
