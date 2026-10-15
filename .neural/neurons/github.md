# Neurons · .github

refreshed 2026-10-15 · 09478439316a

- Two workflows now, not one: `ci.yml` (buf lint/breaking/gen-is-current/go build/tsc, unchanged since the last refresh) and the new `security.yml` (gitleaks secret scan).
- `security.yml`'s own header comment explains why it is a full file instead of a call to a reusable workflow: this repo is **public** and the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — the secret-scan gate had been failing on every push since it was adopted, a nought-second red run with no job and no log, which is the worst shape a security gate can take (looks like it's working, scans nothing).
- `security.yml` runs on `pull_request`, `push` to `main`, a weekly `schedule` (Mon 06:17 UTC, full git-history scan because a committed-then-reverted credential still leaked in a public repo), and `workflow_dispatch`. Only the scheduled run sets `fetch-depth: 0`; PR/push scans are tree-only (`fetch-depth: 1`).
- gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a release binary rather than via the gitleaks Action, because the Action asks organisations for a licence key. Findings are redacted in the job summary and log (SARIF is still uploaded as an artifact) because this repo is publicly readable.
- The scan step always `exit-code 0`; the separate `report` step is what actually fails the job (reads the SARIF finding count with `jq`, exits 1 if non-zero). A missing SARIF file is also treated as failure ("an unknown result is a failure, never a pass"), never a silent pass.
- README.md says the security gate also checks "fixable critical or high dependency vulnerabilities" and reports a `neuralsecurity` check — but `security.yml` only runs gitleaks; no dependency-scan job exists in this repo yet. Either the dependency half lives in a workflow not yet added here, or the README is ahead of what's actually wired — don't assume parity between the two without checking again.
- `ci.yml` is still the only workflow with `check` (PRs, main, `v*` tags) and `publish-ts` (push only, `needs: check`); neither job changed in this refresh.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — consistent with `make` being absent from the agent sandbox too (see root neurons). A change to the `Makefile` alone is not exercised by CI.
- The breaking check (`ci.yml`) only runs `if: github.event_name == 'pull_request'` and needs `git fetch --no-tags origin main:main` first, since `actions/checkout` leaves a PR on a detached merge commit with no local `main` ref — same trap applies on a fresh local clone.
- `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping the Go version used in CI means editing `go.mod`, not the workflow.
- `publish-ts` publishes to GitHub Packages (`registry-url: https://npm.pkg.github.com`) with `${{ github.token }}`; a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under dist-tag `canary`, a `v*` tag publishes the stripped tag version under `latest`. PRs never publish (`github.event_name == 'push'` gate).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file was executed here (no `act`/Actions runner in this sandbox).
