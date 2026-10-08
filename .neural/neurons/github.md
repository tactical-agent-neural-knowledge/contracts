# Neurons · .github

refreshed 2026-10-08 · 572da952c512

- Two workflows now: `ci.yml` (build/lint/breaking/publish, unchanged in shape) and a new `security.yml` for scanning gates — they were split apart mid-week, see below.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so that breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- `security.yml` is mid-incident, don't take its current shape as settled: it was first appended as two extra jobs (`secrets-scan`, `deps-scan`) directly onto `ci.yml` (34e2dd6), which GitHub rejected outright — workflow-file error, zero jobs scheduled, main went red for several minutes with nothing to point at. Moved to its own file (6b1c4b7), still calling both reusable workflows (`tactical-agent-neural-knowledge/workflows/.github/workflows/secret-scan.yml@main` and `.../deps-scan.yml@main`) — still a workflow-file error with zero jobs. 572da95 narrowed it to the `secrets` job alone to bisect which call GitHub rejects; `deps-scan` is not currently running here. Check whether that bisection has concluded before assuming scanning coverage matches what `CLAUDE.md`/the thread expects.
- Unlike `ci.yml`, `security.yml` runs on `push: branches: [main]` (no tags) plus `workflow_dispatch`, and has no `concurrency` block of its own.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` likewise declares `contents: read` only.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow file was executed; the `security.yml` workflow-file rejection is read from commit history, not reproduced here.
