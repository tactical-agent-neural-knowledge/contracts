# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflow files now: `ci.yml` (lint/breaking/gen-staleness/build/tsc, then npm publish) and `security.yml` (gitleaks secret scan), added since the last refresh.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone. `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, gated on `github.event_name == 'push'`. Publishes to GitHub Packages (`registry-url: https://npm.pkg.github.com`, `scope: "@tactical-agent-neural-knowledge"`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed.
- `security.yml` secret-scans with gitleaks, pinned to a fetched release binary (not the Action, which requires an org licence key) — the rules are reproduced inline rather than calling the org's private reusable workflow, because **a public repo cannot invoke a reusable workflow from a private one**: that call fails with a zero-second, job-less run before anything schedules, which is exactly how this repo's gate went red on every push until the duplication was made (see `security.yml:3-18`).
- `security.yml` triggers on PR, push to main, a weekly Monday 06:17 UTC cron, and `workflow_dispatch`. Only the cron does a full-history scan (`fetch-depth: 0`, `gitleaks git`); PR/push scan the working tree only (`gitleaks dir`, `fetch-depth: 1`).
- `security.yml` always exits 0 from the scan step and lets the `report` step decide pass/fail from the SARIF file — a crashed scanner must not read as a clean one. No SARIF file at all is treated as a failure, never a pass. Findings are redacted in the summary and the log because the repo is public and readable by anyone.
- A false positive in the secret scan is silenced with a dated `.gitleaksignore` entry, never by dropping or weakening the workflow.
- Permissions are least-privilege and deliberate in both workflows: `contents: read` at top, and only `ci.yml`'s `publish-ts` adds `packages: write`.
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`. The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here (gitleaks binary fetch and Actions runtime are not available in this sandbox).
