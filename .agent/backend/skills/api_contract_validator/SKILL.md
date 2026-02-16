---
name: API Contract Validator
description: Validate API routes against expectations or Swagger docs.
---

# API Contract Validator

This skill helps ensure implementation matches the spec.

## Script: `validate_routes.py`
Usage: `python .agent/skills/api_contract_validator/validate_routes.py`

Features:
- Scans `src/routes` for Express router definitions.
- Lists all found endpoints (Method + Path).
- (Future) Load `openapi.yaml` and compare.
