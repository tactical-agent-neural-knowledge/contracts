# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/build/publish, unchanged this refresh) and a new `security.yml` (secret scanning), added across commits `34e2dd6`..`b57522e`.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, gated on `github.event_name == 'push'`.
- `.github/workflows/security.yml` is a secret scan (gitleaks) *inlined in full* rather than calling a reusable workflow from the org's private `workflows` repo — its own header comment explains why: this repo is public, `workflows` is private, and GitHub refuses a reusable workflow call from private to public before any job is even scheduled (a nought-second failure with no log). The duplication is the deliberate price of being public; keep it in step with `workflows/.github/workflows/secret-scan.yml` by hand.
- `security.yml` pins gitleaks as a release binary (`VERSION: "8.30.1"`, fetched via `curl`+`tar`), not the GitHub Action, because the Action requires an org licence key.
- `security.yml`'s `report` step is the actual gate: gitleaks itself always runs `--exit-code 0`, so a crash in the scan step can't masquerade as "zero findings" — the report step reads the SARIF, and **no SARIF file at all is treated as a failure**, never a silent pass (`::error::gitleaks produced no report`).
- Findings are redacted (`--redact`) in both the SARIF and the step summary, because this repo is public and a run log is readable by anyone — a real secret found here must be rotated first, removed from history second; a false positive is silenced only via a dated `.gitleaksignore` entry, never by dropping the check.
- `security.yml` runs a shallow tree scan (`fetch-depth: 1`, `gitleaks dir .`) on PRs and pushes to main, and a full-history scan (`fetch-depth: 0`, `gitleaks git .`) on a weekly cron (`17 6 * * 1`) — a credential committed and reverted still leaked, so history gets walked separately from the fast path.
- Permissions are least-privilege: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` only, even for the history scan.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here (no `act`/Actions runner in this sandbox).
