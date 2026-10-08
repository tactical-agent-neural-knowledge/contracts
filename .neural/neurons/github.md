# Neurons · .github
refreshed 2026-10-08 · a887d51f4d82

- `ci.yml` `check` job order: `buf lint` → breaking check (PR only) → `buf generate` + `git diff --stat gen/`
  staleness check → `go build ./...` → `npm run build` (tsc) in `gen/ts`. Any step failing fails the whole job.
- The breaking check step runs `git fetch --no-tags origin main:main` before `buf breaking` — `actions/checkout`
  leaves a PR on a detached merge commit with no local `main` ref, so buf has nothing to diff against without this.
- `publish-ts` only runs on `push` (main or `v*` tags), after `check` passes: canary version on main is
  `0.0.0-canary.<12-char sha>` tagged `canary`; a `v*` tag publishes the literal semver tagged `latest`.
- `security.yml`'s gitleaks scan is **inlined**, not a `uses:` call to the org's reusable
  `workflows/.github/workflows/secret-scan.yml` — a public repo cannot call a reusable workflow from a private repo
  (scheduling fails before any job starts, a silent 0-second red run). Don't "fix" this by switching back to a
  reusable-workflow call; the duplication is intentional and documented in the file's own header comment.
- gitleaks always exits 0 (`--exit-code 0`); the `report` step is what decides pass/fail by counting
  `.runs[].results[]` in the sarif. A missing sarif file is treated as a failure, never a pass — a crashed scanner
  must not look like a clean one.
- Secret-scan triggers: PR and push-to-main do a tree-only scan (`fetch-depth: 1`); a weekly Monday 06:17 UTC cron
  does a full-history scan (`fetch-depth: 0`, `gitleaks git` instead of `gitleaks dir`) because a reverted commit
  still leaked the credential in a public repo.
- A gitleaks false positive is silenced with a dated entry in `.gitleaksignore`, never by disabling the workflow.
- Both workflows set `permissions: contents: read` at the top level; `publish-ts` elevates to `packages: write` only
  inside its own job block.

## Verified
- Read both workflow files in full; no YAML linter available in this sandbox (no `actionlint`, no `pyyaml`), so
  syntax was checked by inspection only, not executed.
