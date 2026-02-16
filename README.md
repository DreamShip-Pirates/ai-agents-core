# PlacesXP AI Agents Core

This repository serves as the central source of truth for all AI agent configurations, roles, and rules used across the PlacesXP ecosystem.

## Structure

- `.agent/backend/`: Shared rules and components for backend development.
- `.agent/app_frontend/`: Shared rules and components for frontend development.
- `.agent/general/`: Global agent settings.

## Integration

This repository is integrated into other PlacesXP projects using **Git Submodules**.

### Adding to a new repository

1. Add as a submodule:
   ```bash
   git submodule add https://github.com/DreamShip-Pirates/ai-agents-core.git .agent-source
   ```
2. Create a symlink to the relevant configuration:
   ```bash
   # For Backend:
   ln -s .agent-source/.agent/backend .agent
   
   # For Frontend:
   ln -s .agent-source/.agent/app_frontend .agent
   ```

## Updates

To update agents in a consumer project:
```bash
git submodule update --remote .agent-source
```
