# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now: `ci.yml` (build/publish) and `security.yml` (secret scanning), added since the last refresh.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone. `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` A different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `actions/setup-go@v5` takes `go-version-file: go.mod` — the Go version is never written in the workflow, so bumping Go means editing `go.mod`. TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24, a tsc compile only, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish (gated on `github.event_name == 'push'`). Publishing goes to GitHub Packages, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish.
- `security.yml` runs gitleaks on PRs, pushes to main, a weekly schedule (Monday 06:17 UTC, full git history) and `workflow_dispatch` (tree only). Its own header comment explains why it is inlined rather than calling a reusable workflow: this repo is **public** and the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo into a public caller before any job is scheduled — the gate had silently zero-second-failed on every push since it was adopted.
- `security.yml` always exits the scanner with `--exit-code 0` and lets the `report` step decide pass/fail from the SARIF file, so a scanner crash cannot masquerade as a clean run; no SARIF file at all is treated as a failure, never a pass (`gitleaks.sarif` missing → `::error::gitleaks produced no report`).
- Findings are redacted in both the step output and the job summary (`--redact`) because the run log is world-readable on a public repo. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- `security.yml` permissions are `contents: read` only — no `packages: write`, unlike `ci.yml`'s `publish-ts` job.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; gitleaks itself was not run here.
