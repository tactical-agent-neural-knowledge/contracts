# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged this refresh — lint/breaking/gen-staleness/go-build/tsc, plus `publish-ts`) and the new `.github/workflows/security.yml`, the secret scan.
- `security.yml` is inlined rather than calling a reusable workflow on purpose: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow call from private to public before any job is even scheduled — the prior setup failed every push as a nought-second run with no job and no log, "red forever, scanning nothing, and indistinguishable from a gate that is working." Keeping the rules in step with `workflows/.github/workflows/secret-scan.yml` by hand is the price of being public.
- `security.yml` runs gitleaks pinned to a release binary (not the Action, which asks orgs for a licence key), on `pull_request`, `push: [main]`, `workflow_dispatch`, and a weekly `schedule` (Mon 06:17 UTC) that walks full git history (`fetch-depth: 0`) because "a credential committed and reverted is still a credential that leaked" in a public repo. Non-scheduled runs scan only the working tree (`fetch-depth: 1`, `gitleaks dir .`).
- Trap: the scan step always exits 0 (`--exit-code 0`) and a separate `report` step (`if: always()`) decides pass/fail from the SARIF — "a crash cannot pass as a clean scan." If `gitleaks.sarif` is missing entirely, `report` fails with `::error::gitleaks produced no report` rather than passing: "no report at all is a failure, never a pass." A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- Findings are redacted (`--redact`) in both the log and the uploaded SARIF artifact, because the run log is readable by anyone who can read this (public) repo.
- `ci.yml`: two jobs, `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI, the two must be kept in step by hand.
- The breaking check (`ci.yml:31`) only runs `if: github.event_name == 'pull_request'`; it needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` — same trap on a fresh local clone. `actions/checkout@v4` is pinned `fetch-depth: 0` purely for this comparison.
- The staleness gate is `buf generate` + `git diff --exit-code --stat gen/`, failing `::error::gen/ is stale. Run 'make gen' and commit the result.` — regenerating with a buf/plugin version other than `buf.gen.yaml`'s pins will trip it.
- `actions/setup-go@v5` takes `go-version-file: go.mod`; the Go version is never written in the workflow itself.
- TS check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile only, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` as `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` as `canary`. Permissions are least-privilege: `contents: read` at top level, `packages: write` only on `publish-ts`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed here (no gitleaks binary fetched, no Actions runner).
