# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen-freshness/build/tsc, plus npm publish) and `security.yml`, new this refresh (gitleaks secret scan). Neither calls the other.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). It calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: line ~31 says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source," gated `if: github.event_name == 'pull_request'`. Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step runs `git fetch --no-tags origin main:main` first — the same is needed locally on a fresh clone. `fetch-depth: 0` on checkout exists purely for this.
- Staleness gate is `buf generate` then `git diff --exit-code --stat gen/`, failing `::error::gen/ is stale. Run 'make gen' and commit the result.` A different buf/plugin version than `buf.gen.yaml`'s pins will trip it even with no proto change.
- Go version is never written in the workflow — `actions/setup-go@v5` reads `go-version-file: go.mod` (currently go 1.26); bumping Go means editing `go.mod`, not the workflow.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` to dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` to `canary`. Goes to GitHub Packages, authenticated with the ambient `${{ github.token }}` — no external npm credential needed. PRs never publish (`if: github.event_name == 'push'`).
- `security.yml`'s own header comment is the key fact: it duplicates `workflows/.github/workflows/secret-scan.yml` by hand instead of calling it, because GitHub refuses a reusable workflow from a private repo (`workflows`) into a public caller (this repo) — that call used to fail as a nought-second run with no job and no log, "red forever, scanning nothing, and indistinguishable from a gate that is working."
- gitleaks is fetched as a pinned release binary (`VERSION: "8.30.1"`, curl + tar from GitHub releases), not the Action, because the Action asks organizations for a licence key.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step decides pass/fail by reading `gitleaks.sarif` with `jq`. No SARIF file at all is itself a failure (`::error::gitleaks produced no report — an unknown result is a failure, never a pass`) — a crash in the scan step cannot silently read as clean.
- Tree scan (`fetch-depth: 1`) on every PR and push to main; full-history scan (`fetch-depth: 0`, `gitleaks git .`) only on the Monday 06:17 UTC cron, because "a credential committed and reverted is still a credential that leaked" and this repo is public.
- Findings are always `--redact`ed, in the log and in the step summary, because run logs here are world-readable. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check — there is no `.gitleaksignore` in the repo yet.
- Permissions are least-privilege and explicit per workflow: `ci.yml` declares `contents: read` at top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read`. `ci.yml`'s `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means a second push to the same ref kills the first run, including a half-finished publish — `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks reproducible outside Actions; both passed. Neither workflow was executed here (no Actions runner, and gitleaks/npm publish need real credentials/registry access this sandbox doesn't have).
