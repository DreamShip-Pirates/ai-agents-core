---
description: How to manage development, staging, and production environments
---

# Environment Management Workflow

## Environment Structure

### **Dev** Environment (`dev` branch)
- **Purpose**: Active development and feature work
- **Branch Name**: `dev`
- **Usage**: All new features, bug fixes, and experiments start here
- **Testing**: Run full test suite before merging to staging

### **Staging** Environment (`staging` branch)  
- **Purpose**: QA and pre-production testing
- **Branch Name**: `staging` (to be created)
- **Usage**: Merge from `dev` when ready for QA review
- **Testing**: Comprehensive testing, including manual QA and UAT

### **Production** Environment (`main` branch)
- **Purpose**: Live production code
- **Branch Name**: `main`
- **Usage**: Merge from `staging` after successful QA approval
- **Releases**: Tag with version numbers (e.g., `v2.1.0`)

## Workflow

```
dev → staging → main (production)
 ↓        ↓         ↓ 
test   → QA    →  deploy
```

## Commands

### Switch to development
```bash
git checkout dev
```

### Create staging branch (when needed)
```bash
git checkout -b staging
git push -u origin staging
```

### Promote dev to staging
```bash
git checkout staging
git merge dev
git push origin staging
```

### Promote staging to production
```bash
git checkout main
git merge staging
git tag -a v2.1.0 -m "Release version 2.1.0"
git push origin main --tags
```

## Best Practices

1. **Always test** before promoting between environments
2. **Use pull requests** for staging → main merges
3. **Tag production releases** with semantic versioning
4. **Keep dev updated** with latest from main periodically
5. **Document breaking changes** before promoting to staging

## Testing Requirements

- **Dev**: `flutter test` must pass
- **Staging**: Full test suite + manual QA + integration tests
- **Production**: Staging approval + final smoke tests

## Current Status

- ✅ `dev` branch created from `v2`
- ⏳ `staging` branch - to be created when needed
- ✅ `main` production branch exists

## Notes

- The `v2` branch contains the latest development code
- Session loss and crash issues have been resolved via test isolation fixes
- All ValueKeys in pages are functional requirements, not test-specific
