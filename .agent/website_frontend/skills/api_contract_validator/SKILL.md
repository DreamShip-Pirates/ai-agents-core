# Skill: API Contract Validator

**Purpose**: Ensure frontend implementation matches Backend/OpenAPI specifications.

## Logic
1. Retrieve the latest `openapi.json` or `swagger.json` from the backend source.
2. Compare the request body and response types in `crud.js` against the spec.
3. Throw a warning if a property is missing, misspelled, or has an incorrect type.

## Usage
Activate during `API_BUILD` intent to prevent breaking changes.
