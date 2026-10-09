# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (lint/breaking/gen/build/tsc, publish-ts) and the new `security.yml` (gitleaks secret scan). They are independent — `security.yml` never gates `ci.yml` or vice versa.
- `security.yml` is a secret scan inlined rather than called as a reusable workflow, and the file's own header comment explains why: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled — a nought-second failure with no log. The rules are reproduced here by hand, so a change to the canonical `workflows/.github/workflows/secret-scan.yml` does not propagate; drift must be caught by a human.
- `security.yml` gitleaks is fetched as a pinned release binary (`VERSION: "8.30.1"`), not the Action, because the Action asks organizations for a license key.
- `security.yml` scan step always exits 0 (`--exit-code 0`); the separate `report` step is what decides pass/fail by reading `gitleaks.sarif` and counting results. A crash before the report step still fails the job because `if [ ! -f gitleaks.sarif ]` in `report` treats a missing report as a failure, never a pass.
- `security.yml` fetch-depth is conditional: `0` only on the Monday 06:17 UTC `schedule` run (full history walk — a credential committed and reverted in a public repo still leaked to everybody), `1` otherwise (tree-only, on every PR and push to main).
- A `security.yml` false positive is silenced with a dated entry in `.gitleaksignore`, never by dropping the check — stated in the report step's own summary text.
- `ci.yml` itself is unchanged since the last refresh: two jobs, `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`); CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make`, so a `Makefile`-only change is not exercised by CI.
- `ci.yml` breaking check trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main` ref, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it — true locally on a fresh clone too.
- `ci.yml` staleness gate is `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `ci.yml publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` against GitHub Packages.
- Both workflows declare `permissions: contents: read` at top and widen only the one job that needs more (`publish-ts` adds `packages: write`).

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks reproducible outside Actions; both passed. Neither workflow file itself was executed.
