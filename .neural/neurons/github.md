# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged since the last refresh) and the new `security.yml` secret scan.
- `.github/workflows/ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- `security.yml` is a secret scan **inlined rather than called**, and its header comment explains why: this repo is public, a sibling `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — the run was a nought-second failure with no log, red on every push since the gate was adopted, "the worst shape a security gate can take". The rules are duplicated from `workflows/.github/workflows/secret-scan.yml` by hand; keeping them in step is on whoever edits either side.
- `security.yml` runs gitleaks (pinned `VERSION: "8.30.1"`, fetched as a release binary, not the Action — avoids the org licence-key requirement) on `pull_request`, `push: main`, a weekly `schedule` (Monday 06:17 UTC), and `workflow_dispatch`.
- Scan depth depends on trigger: `fetch-depth` is `0` only on `schedule` (full git history — "a credential committed and reverted is still a credential that leaked"), `1` otherwise (`gitleaks dir .`, tree only vs `gitleaks git .`).
- `security.yml`'s `scan` step always runs gitleaks with `--exit-code 0`; the separate `report` step (`if: always()`) is what decides pass/fail by reading `gitleaks.sarif` — a missing report file is itself a failure (`::error::gitleaks produced no report — an unknown result is a failure, never a pass`), so a scanner crash can never silently read as clean.
- A false positive in the secret scan is silenced with a dated `.gitleaksignore` entry, never by dropping the check (stated directly in the workflow's own summary text).
- `ci.yml`'s breaking check (`.github/workflows/ci.yml:35`) only runs `if: github.event_name == 'pull_request'`; `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so it must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it — same trap applies on a fresh local clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` in `ci.yml` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- `ci.yml`'s staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf/plugin version than `buf.gen.yaml`'s pins will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — gated on `github.event_name == 'push'`.
- Permissions are least-privilege on both workflows: `contents: read` at the top of each; `ci.yml`'s `publish-ts` adds `packages: write`, `security.yml` adds nothing.
- Both workflows use `concurrency: cancel-in-progress: true` (`ci.yml` keyed on `ci-${{ github.ref }}`) — a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow file was executed; gitleaks was not run locally.
