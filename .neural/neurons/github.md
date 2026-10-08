# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now: `ci.yml` (unchanged this refresh) and `security.yml`, new this refresh. `ci.yml` still has the only two jobs that touch this repo's own build: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- `security.yml` is a secret scan (gitleaks) **inlined** rather than called as a reusable workflow, and the file's own header comment explains why: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — the prior setup failed silently on every push, a nought-second run with no job and no log. Keep the duplicated rules (pinned gitleaks release binary, redacted output, scanner always exits 0 so the report step decides, no report at all is a failure) in step with `workflows/.github/workflows/secret-scan.yml` by hand; nothing enforces that they match.
- `security.yml` triggers on `pull_request`, `push: [main]`, a weekly `schedule` (Monday 06:17 UTC) and `workflow_dispatch`. Only the scheduled run does `fetch-depth: 0` and scans `git` history (`HISTORY=true`); PR/push runs scan the working tree only (`fetch-depth: 1`). The reasoning in the file: "a credential committed and reverted is still a credential that leaked."
- The `report` step in `security.yml` is the actual gate, not the scan: it treats a missing `gitleaks.sarif` as a hard failure ("an unknown result is a failure, never a pass") before it ever counts findings, so a gitleaks crash cannot read as clean.
- `ci.yml` calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` in `ci.yml` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- Permissions are least-privilege and deliberate across both files: both declare `contents: read` at the top; only `ci.yml`'s `publish-ts` adds `packages: write`.
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed (no `gitleaks` run here).
