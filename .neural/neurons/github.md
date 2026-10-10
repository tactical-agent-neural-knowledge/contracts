# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged since the last refresh) and the new `security.yml` secret scan.
- `ci.yml`: two jobs, `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` — `actions/checkout@v4` is pinned `fetch-depth: 0` for exactly this.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `security.yml` is a **secret scan reproduced by hand, not called**: `security.yml:3-18` explains why — this repo is public, the real rules live in the private `workflows` repo's `secret-scan.yml`, and GitHub refuses a reusable workflow call from a private repo into a public caller before any job is even scheduled (a nought-second failure, no job, no log). The duplication here is the price of being public; drift between the two copies is now a risk this repo owns alone.
- `security.yml` triggers: `pull_request`, `push` to `main`, a weekly `schedule` (`17 6 * * 1`, Monday 06:17 UTC), and `workflow_dispatch`. The weekly run walks full git history (`fetch-depth: 0`, `gitleaks git .`); PR/push runs scan only the working tree (`fetch-depth: 1`, `gitleaks dir .`) — "a credential committed and reverted is still a credential that leaked."
- gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a raw release binary, not the GitHub Action, because the Action asks organisations for a licence key.
- The scan step always runs with `--exit-code 0`; a separate `report` step (`if: always()`) is what decides pass/fail by counting `gitleaks.sarif` results with `jq`. This is deliberate: a scanner crash must not silently read as a clean pass. No SARIF file at all is treated as a failure (`::error::gitleaks produced no report`), never as a pass.
- Findings are redacted in the summary and log on purpose (`--redact`) — a run log is readable by anyone who can read this public repo. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- `security.yml` declares only `permissions: contents: read`; no `packages: write`, it never publishes anything.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` against GitHub Packages — no external npm credential needed. PRs never publish (`if: github.event_name == 'push'`).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` only — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed (no `gitleaks` binary fetch attempted here).
