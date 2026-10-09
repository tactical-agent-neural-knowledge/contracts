# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (buf checks + npm publish) and `security.yml` (secret scan, new since the last refresh).
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`, and `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the comparison has history.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — the job is gated on `github.event_name == 'push'`.
- `security.yml` is a secret scan (gitleaks) reproduced inline rather than calling a reusable workflow, because the organization's `workflows` repo is **private** and this repo is **public**: GitHub refuses a reusable-workflow call from private to a public caller before any job is even scheduled, which previously showed up as a nought-second failure with no log (`.github/workflows/security.yml:5-10`). Keep the duplicated rules in sync with `workflows/.github/workflows/secret-scan.yml` by hand.
- `security.yml` triggers on PR, push to main, a weekly `17 6 * * 1` cron, and `workflow_dispatch`. Only the scheduled run does `fetch-depth: 0` and scans `git` history (`gitleaks git .`); PR/push runs scan the working tree only (`gitleaks dir .`) — a credential committed and reverted between two weekly runs is still caught, just not same-day.
- `security.yml` always exits gitleaks with `--exit-code 0` and lets the separate `report` step decide pass/fail from the SARIF file: a crash in the scan step can't be mistaken for "no secrets found." Missing SARIF is itself a failure (`.github/workflows/security.yml:67-69`) — "an unknown result is a failure, never a pass."
- Findings are always `--redact`ed because this repo is public and the Actions log is world-readable; a false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check (`.github/workflows/security.yml:80-81`).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.
- Permissions are least-privilege: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` only ever needs `contents: read`.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; gitleaks was not run locally.
