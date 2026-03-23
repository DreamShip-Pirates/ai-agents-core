# Skill: Migration Safety Check

**Purpose**: Identifying destructive DB operations before execution.

## Checklist
- [ ] Will this operation lock the table?
- [ ] Is there a rollback script?
- [ ] Does it maintain backward compatibility with the FE?
- [ ] Has it been tested on a staging environment?

## Usage
Mandatory for the **Migration Guardian**.
