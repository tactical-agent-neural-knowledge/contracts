# Neurons · .github

refreshed 2026-10-15 · 6e371811ddb2

- Two workflows: `ci.yml` (lint/breaking/gen-staleness/build/tsc, then publish) and `security.yml` (secret scanning). No other workflow exists in `.github/`.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: line 31 says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` ref — the same trap applies on a fresh local clone.
- `security.yml` is a secret scan (gitleaks) **inlined rather than called** from a reusable workflow, and the file's own header comment explains why: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — the run used to fail at zero seconds with no job and no log, on every push, silently. The rules are reproduced here by hand and must not drift from `workflows/.github/workflows/secret-scan.yml`.
- `security.yml` runs on PR, push to main, a weekly Monday 06:17 UTC full-history scan, and `workflow_dispatch`. The weekly run sets `fetch-depth: 0` and scans `git` history (a credential committed and reverted is still leaked, especially in a public repo); every other trigger scans the working tree only (`fetch-depth: 1`).
- `security.yml`'s gitleaks is a pinned release binary (`VERSION: "8.30.1"`, fetched via `curl` from GitHub releases), not the GitHub Action — the Action requires an organisation licence key.
- `security.yml`'s scan step always exits 0 (`--exit-code 0`); the separate `report` step is what decides pass/fail by reading `gitleaks.sarif` with `jq`. A missing report file is treated as a failure, never a pass — "an unknown result is a failure, never a pass" — so a crash in the scan step cannot silently read as clean.
- Findings are `--redact`ed in `security.yml` because the Actions log and step summary are readable by anyone who can read the repo, and the repo is public. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check.
- `ci.yml`'s staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `${{ github.token }}` against GitHub Packages — no external npm credential needed.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no such concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here.
