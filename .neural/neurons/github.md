# Neurons · .github

refreshed 2026-10-14 · 3b1cc8caafe7

- Two workflows now: `ci.yml` (buf/go/ts checks, unchanged since the last refresh) and the new `security.yml` (secret scanning). They are independent — `security.yml` never calls `make` or `buf`.
- `ci.yml` is still the only place the schema is proven: `check` (PRs, main, `v*` tags) runs buf lint, breaking (PRs only), the gen-is-current diff, `go build ./...`, then a `gen/ts` tsc compile; `publish-ts` (`needs: check`, push-only) ships the npm package.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves PRs on a detached merge commit with no local `main` — the same applies on a fresh clone, and `fetch-depth: 0` exists solely to make that comparison possible.
- `security.yml` is inlined gitleaks rather than a reusable workflow, and its own header comment explains why: GitHub refuses a reusable workflow from the private `workflows` repo to this public caller, which made the check fail silently (zero-second run, no job scheduled, no log) on every push since it was adopted — "the worst shape a security gate can take: red forever, scanning nothing." The rules are duplicated from `workflows/.github/workflows/secret-scan.yml` and must not drift.
- `security.yml` trap: the scan step always exits 0 (`--exit-code 0`); a separate `report` step (`if: always()`) parses the SARIF and decides pass/fail. "No report at all" is treated as a failure, never a pass — `gitleaks.sarif` missing triggers `::error::` and `exit 1` before the finding count is even checked.
- `security.yml` runs two scan depths from one job: `pull_request`/`push` get a tree-only scan (`fetch-depth: 1`, `gitleaks dir .`), the Monday 06:17 UTC `schedule` trigger gets a full-history scan (`fetch-depth: 0`, `gitleaks git .`) — "a credential committed and reverted is still a credential that leaked, and in a public repository it leaked to everybody."
- Findings are redacted (`--redact`) because this repo is public and a run log is readable by anyone; a false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — gated on `github.event_name == 'push'`.
- Permissions are least-privilege and per-workflow: `ci.yml` declares `contents: read` and only `publish-ts` adds `packages: write`; `security.yml` declares `contents: read` only (it never writes, only uploads a SARIF artifact).
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file was executed here (`security.yml`'s gitleaks step and `ci.yml`'s Actions runners are not available in this sandbox).
