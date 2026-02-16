---
description: Run local tests, CI, deploy, and remote verify.
---

1. Run local tests
   ```bash
   pytest
   ```
2. If tests pass, commit and push to dev
   ```bash
   git add .
   git commit -m "Auto-commit from deploy workflow"
   git push origin dev
   ```
3. Wait for CI on dev (Manual Step or GitHub CLI)
   - Ensure the `Django CI` workflow passes on `dev` branch.

4. Merge dev into main and push
   ```bash
   git checkout main
   git merge dev
   git push origin main
   git checkout dev
   ```

5. Wait for CI on main (Manual Step or GitHub CLI)
    - Ensure the `Django CI` workflow passes on `main` branch.

6. Deploy to Production
   - Run the deployment script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts/deploy/deploy.ps1
   ```

7. Run remote tests
   - Replace `<YOUR_PRODUCTION_URL>` with your actual API base URL.
   ```bash
   python verify_api.py --url <YOUR_PRODUCTION_URL>
   ```

8. If any test fails
   - Fix the code and restart this workflow.
