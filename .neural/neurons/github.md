# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now, not one: `ci.yml` (lint/breaking/gen/build/tsc) and `security.yml` (secret scan), added this refresh cycle. Both declare `permissions: contents: read` at top.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by either workflow — keep them in step by hand.
- `ci.yml`'s breaking check is the point of the whole file: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so `ci.yml` must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. Same on a fresh clone locally. `fetch-depth: 0` on checkout exists purely for this.
- `ci.yml`'s staleness gate is `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` A different buf/plugin version than `buf.gen.yaml`'s pins trips it.
- `security.yml` runs gitleaks as a pinned release binary (`VERSION: "8.30.1"`, fetched by curl), never the Action — the comment at `.github/workflows/security.yml:5` explains why: this repo is public, `workflows` (holding the reusable secret-scan job) is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled. The rules are duplicated here by necessity and must be kept in sync with `workflows/.github/workflows/secret-scan.yml` by hand, not by reference.
- `security.yml` trap: the scanner step always `exit-code 0`; the separate `report` step (`if: always()`) is what actually fails the job, by counting `gitleaks.sarif` results with `jq`. A missing sarif file is treated as a failure too ("an unknown result is a failure, never a pass") — a crashed scanner cannot pass as clean.
- `security.yml` triggers on `pull_request`, `push` to main, a weekly Monday 06:17 UTC cron, and `workflow_dispatch`. Only the scheduled run sets `fetch-depth: 0` and scans `git` history (`gitleaks git .`); PR/push runs scan only the working tree (`gitleaks dir .`) for speed. There is no `.gitleaksignore` file in the repo yet — false positives are meant to be silenced there with a dated entry, never by dropping the check.
- A dependency-scanning gate was added and then deliberately narrowed back to secrets-only (`572da95`, "while the call is diagnosed") — `security.yml` currently has exactly one job, `secrets`. Don't assume a dependency scanner runs here.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `ci.yml`'s TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- `publish-ts` (in `ci.yml`) versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. Gated on `github.event_name == 'push'`, so PRs never publish.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed; gitleaks was not run here.
