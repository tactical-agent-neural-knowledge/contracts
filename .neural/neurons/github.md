# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen-staleness/build/tsc, then publish) and `security.yml` (gitleaks secret scan), added this refresh.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it — same on a fresh local clone. `fetch-depth: 0` on checkout exists purely for this.
- The staleness gate is `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` A different buf/plugin version than the `buf.gen.yaml` pins will trip it even with no proto change.
- `actions/setup-go@v5` takes `go-version-file: go.mod`, so the Go version is never written in the workflow — bumping Go means editing `go.mod`. The TS check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24, a tsc compile with no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}`. PRs never publish (`github.event_name == 'push'` gate). `concurrency: group: ci-${{ github.ref }}` + `cancel-in-progress: true` means a second push to the same ref kills a half-finished publish.
- `security.yml` is a full secret-scan workflow reproduced inline rather than called from the org's shared `workflows` repo, because that repo is private and this one is public — GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled, so a call produces a nought-second failure with no log. The duplication is deliberate and documented at the top of the file; keep the two in step by hand if the shared version changes.
- `security.yml` rules that must not drift (file's own header comment): gitleaks is pinned and fetched as a release binary, not the Action, because the Action asks orgs for a licence key; findings are redacted in the log because this repo is public and readable by everyone; the scanner always runs with `--exit-code 0` and the separate `report` step decides pass/fail, so a scanner crash cannot masquerade as a clean run; and a missing `gitleaks.sarif` is itself a failure (`report` step: "an unknown result is a failure, never a pass").
- `security.yml` triggers: PRs and pushes to main do a tree-only scan (`fetch-depth: 1`, `gitleaks dir .`); a weekly Monday-06:17-UTC cron does a full-history scan (`fetch-depth: 0`, `gitleaks git .`) because a committed-then-reverted credential in a public repo has still leaked. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check.
- Permissions stay least-privilege: both workflows declare `contents: read` at top; only `publish-ts` adds `packages: write`.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step was not run here.
