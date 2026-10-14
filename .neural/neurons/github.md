# Neurons · .github

refreshed 2026-10-14 · 65c4439b3e7d

- Two workflows now: `ci.yml` (lint/breaking/gen-staleness/build/publish, unchanged this refresh) and the new `security.yml` (secret scanning).
- `ci.yml` is still called directly with `bufbuild/buf-setup-action@v1`, never `make`; a change to the `Makefile` alone is not exercised by CI.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason that step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `security.yml` history, worth knowing before touching it again: it started (34e2dd6) calling two reusable workflows in `tactical-agent-neural-knowledge/workflows` (secrets + deps); that two-job version failed with a workflow-file error and scheduled no jobs at all (572da95), so it was narrowed to one scanner to diagnose; the real cause (b57522e) is that **this repo is public and `workflows` is private**, and GitHub refuses a reusable workflow call from a private repo into a public caller before any job is scheduled — a nought-second failure with no log. The fix was to stop calling out and inline gitleaks directly in `security.yml` itself.
- `security.yml`'s own header comment states the rules that must not drift if it's ever split back out: gitleaks pinned and fetched as a release binary (not the Action, which asks for a licence key); findings redacted (the repo is public, a run log is readable by anyone); the scanner always exits 0 and a separate `report` step decides, so a crash can't pass as a clean scan; no SARIF report at all is itself a failure, never a pass.
- `security.yml` triggers: PR, push to main, `workflow_dispatch`, and a Monday 06:17 UTC cron that walks the **whole git history** (`gitleaks git .` with `fetch-depth: 0`) rather than just the working tree — because a credential committed and reverted in a public repo already leaked to everybody.
- `actions/checkout@v4` in `ci.yml` is pinned to `fetch-depth: 0` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top, `packages: write` only on `publish-ts`; `security.yml` declares `contents: read` only (gitleaks needs no write access).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file was executed (no Actions runner here, and gitleaks' release binary was not fetched).
