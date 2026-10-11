# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen/build/tsc, publish) and `security.yml` (gitleaks secret scan), added since the last refresh.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone. `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, to GitHub Packages (`@tactical-agent-neural-knowledge` scope, `NODE_AUTH_TOKEN: ${{ github.token }}`). PRs never publish — gated on `github.event_name == 'push'`.
- `security.yml` is gitleaks, inlined rather than called as a reusable workflow — the file's own header explains why: this repo is public and the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller *before any job is scheduled*. That produced a nought-second failure with no job and no log, red on every push since the gate was adopted — the trap that looks identical to a working gate.
- `security.yml` rules that must not drift (duplicated from `workflows/.github/workflows/secret-scan.yml`, not referenced): gitleaks is a pinned release binary (`VERSION: "8.30.1"`), not the Action (which asks orgs for a licence key); findings are redacted since this repo is public; the scanner step always runs with `--exit-code 0` and a separate `report` step decides pass/fail, so a scanner crash can't masquerade as clean; and **no SARIF file at all is treated as a failure**, never a pass.
- `security.yml` triggers: PR and push-to-main scan the working tree (`fetch-depth: 1`); a weekly `schedule` (Mon 06:17 UTC) scans full git history (`fetch-depth: 0`) because a committed-then-reverted credential in a public repo already leaked.
- Permissions are least-privilege and deliberate in both workflows: `ci.yml` declares `contents: read` at top-level, only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` only.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here (no `gitleaks` binary fetch, no Actions runner).
