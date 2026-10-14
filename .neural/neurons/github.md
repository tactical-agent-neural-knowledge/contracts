# Neurons · .github

refreshed 2026-10-14 · 3b1cc8caafe7

- Two workflows now: `ci.yml` (unchanged since the last refresh) and the new `security.yml`, added this cycle for the gitleaks secret scan.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` ref — the same applies locally on a fresh clone.
- `ci.yml`'s staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, gated on `github.event_name == 'push'`. Publishes to GitHub Packages, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed.
- `security.yml` is a secret scan (`gitleaks`) inlined rather than called as a reusable workflow, and `security.yml:1-18` explains why in a comment that is itself load-bearing: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled — a nought-second failure with no job and no log. It had been red on every push since adoption until this file replaced the `uses:` call with the rules reproduced inline.
- `security.yml` triggers on PR, push to main, a weekly cron (`17 6 * * 1`, Monday), and `workflow_dispatch`. Only the weekly cron scans full git history (`gitleaks git .`); PR/push scan the working tree only (`gitleaks dir .`) — a credential committed and reverted between two weekly runs is still caught, just not immediately.
- `security.yml`'s scan step always exits 0 (`--exit-code 0`); the separate `report` step reads `gitleaks.sarif` and decides pass/fail. A crash before the report step means no SARIF file, which `report` treats as a failure, never a silent pass — "no report at all is a failure, never a pass" (`security.yml:18`).
- Findings are redacted in `security.yml`'s report (`--redact`) because the run log is world-readable on a public repo. A false positive is silenced with a dated entry in `.gitleaksignore`, never by removing the check (`security.yml:80-81`).
- gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a release binary rather than via the GitHub Action, because the Action asks organisations for a licence key.
- Permissions stay least-privilege: both workflows declare `contents: read` at the top; only `ci.yml`'s `publish-ts` adds `packages: write`. `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed; gitleaks itself was not run here.
