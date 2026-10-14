# Neurons · .github

refreshed 2026-10-14 · 6e371811ddb2

- Two workflows now: `ci.yml` (lint/breaking/gen-staleness/build, plus `publish-ts`) and the new `security.yml` (secret scanning). `ci.yml` itself is unchanged this cycle.
- `ci.yml`'s `check` job calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI. `actions/checkout@v4` uses `fetch-depth: 0` so `buf breaking --against ".git#branch=main"` has history; a PR run must first `git fetch --no-tags origin main:main` since checkout leaves it on a detached merge commit with no local `main`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}`. PRs never publish (`github.event_name == 'push'` gate).
- `security.yml` is the secret scan, and it is **inlined rather than calling a reusable workflow** — this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow call from private to public *before any job is scheduled*. The symptom was a nought-second failure with no job and no log, on every push, since the gate was adopted: "red forever, scanning nothing, indistinguishable from a working gate." If a scan ever looks like that again, check for exactly this.
- `security.yml` triggers: `pull_request`, `push` to `main`, `workflow_dispatch`, and a weekly `schedule` (Monday 06:17 UTC) that scans **full git history** (`gitleaks git .`) rather than the working tree (`gitleaks dir .`), because a credential committed-then-reverted in a public repo already leaked.
- gitleaks is fetched as a pinned release binary (`VERSION: "8.30.1"`, curl from GitHub releases) rather than via the Action, because the Action gates on an organisation licence key.
- The scan step always exits 0 (`--exit-code 0`); a separate `report` step (`if: always()`) decides pass/fail by reading the SARIF and counting results — a missing SARIF file is itself a hard failure ("an unknown result is a failure, never a pass"), so a crash in the scan step cannot read as green.
- Findings are redacted in the SARIF and in the job summary (`--redact`), because this repo is public and anyone can read the run log. A false positive is silenced with a dated entry in `.gitleaksignore`, never by relaxing the workflow.
- `permissions: contents: read` only; `publish-ts` is the sole job that adds `packages: write`. `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` means a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks reproducible outside Actions; both passed. Neither workflow file itself was executed.
