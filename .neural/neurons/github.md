# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged since the last refresh) and `security.yml` (new). `ci.yml` has jobs `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- `security.yml` is a secret scan (gitleaks) inlined rather than called as a reusable workflow, and the file's own header comment explains why: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a private reusable workflow to a public caller before any job is scheduled — a silent nought-second failure with no log. It had been red on every push since the gate was adopted. Keep this file's rules in sync with `workflows/.github/workflows/secret-scan.yml` by hand; there is no other link between them.
- `security.yml` triggers on PR, push to main, `workflow_dispatch`, and a weekly cron (`17 6 * * 1`) that scans full git history (`gitleaks git .`) instead of the working tree (`gitleaks dir .`), because a credential committed and reverted in a public repo already leaked.
- `security.yml`'s scan step always runs with `--exit-code 0`; the `report` step (`if: always()`) is what actually decides pass/fail by reading the SARIF — a missing SARIF file is treated as a failure, never a silent pass. Findings are redacted in the log and the job summary on purpose, since this repo's Actions logs are world-readable.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone, and to `security.yml`'s own checkout defaults (`fetch-depth: 1` except on the weekly history run).
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- Permissions are least-privilege and deliberate in both files: `ci.yml` and `security.yml` each declare `contents: read` at the top; only `ci.yml`'s `publish-ts` adds `packages: write`.
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here (no `gitleaks`/Actions runner in this sandbox).
