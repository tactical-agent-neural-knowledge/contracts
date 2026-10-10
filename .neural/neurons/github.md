# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (lint/breaking/gen/build/tsc, plus npm publish) and `security.yml` (gitleaks secret scan). They are independent — `security.yml` does not gate `ci.yml` or `publish-ts`.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so that breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- `security.yml` is inlined rather than calling a reusable workflow, and the file's own header comment says why: this repo is public, `workflows` (holding the real reusable scan) is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — a nought-second failure with no log. The duplication here is the price of being public; the rules that must not drift between the two copies are listed in the comment at `.github/workflows/security.yml:12-18`.
- `security.yml` runs gitleaks (pinned version in `env.VERSION`, fetched as a release binary, never the Action — orgs are asked for a licence key) on PRs and pushes to main (tree scan, `fetch-depth: 1`) and on a Monday 06:17 UTC cron (full history scan, `fetch-depth: 0`, `HISTORY=true`). Findings are redacted in the summary because the run log is world-readable on a public repo.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step is what decides pass/fail by reading `gitleaks.sarif` and counting findings. A missing sarif file is treated as failure, never a pass — "no report at all is a failure, never a pass" (`.github/workflows/security.yml:67-69`). A silencer for a false positive is a dated `.gitleaksignore` entry, never dropping the check.
- Permissions are least-privilege and deliberate across both workflows: `contents: read` at the top of each, and only `ci.yml`'s `publish-ts` adds `packages: write`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group of its own.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks that can be reproduced outside Actions; both passed. Neither workflow was executed here.
