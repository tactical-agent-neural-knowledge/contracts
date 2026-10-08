# Neurons · .github

refreshed 2026-10-08 · b57522e4f7aa

- Two workflows now, not one: `ci.yml` (unchanged this window) and `security.yml`, new. `ci.yml` is still `check` (PRs, main, `v*` tags) plus `publish-ts` (pushes only, `needs: check`), calling `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI.
- `security.yml` runs gitleaks and is **inlined rather than calling a reusable workflow**, because this repo is public and the org's shared `workflows` repo is private: GitHub refuses a private reusable workflow to a public caller before any job is scheduled, which is a nought-second failure with no log. The rules are duplicated here on purpose (`security.yml:11-18`) and must not drift from `workflows/.github/workflows/secret-scan.yml`.
- `security.yml` triggers on `pull_request`, `push: [main]`, a weekly `schedule` (Monday 06:17 UTC) and `workflow_dispatch`. Only the schedule does a full-history scan (`gitleaks git .`, `fetch-depth: 0`); PR and push scans are tree-only (`gitleaks dir .`, `fetch-depth: 1`) — a secret committed and reverted between two scheduled runs is only caught on Monday.
- gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a release binary from GitHub, not the Action, because the Action now asks organisations for a licence key.
- The scanner always runs with `--exit-code 0`; the `report` step (`if: always()`) is what actually fails the job, by counting `.sarif` results with `jq` and checking the file exists at all. No report file is itself a failure (`gitleaks produced no report — an unknown result is a failure, never a pass`) — a crash in the scan step cannot silently pass as clean.
- Findings are redacted in the summary (`--redact`) because the run log is world-readable on a public repo. A false positive is silenced with a dated `.gitleaksignore` entry, never by weakening this workflow.
- The breaking check is still the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner". It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves PRs on a detached merge commit with no local `main` — `fetch-depth: 0` on `actions/checkout@v4` exists purely for this.
- The staleness gate in `ci.yml` is `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`. TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile only, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed.
- Permissions are least-privilege per workflow: `ci.yml` declares `contents: read` at top, only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read` throughout, including the `upload-artifact` step.
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}, cancel-in-progress: true`; `security.yml` has no concurrency group, so overlapping pushes can run two scans at once (harmless, since it's read-only).

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step was not run here.
