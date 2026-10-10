# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen-current/build/tsc, unchanged in shape since the last refresh) and `security.yml`, added since — the secret scan, inlined rather than called as a reusable workflow.
- `security.yml`'s own header comment explains why it is a full copy and not a `uses:` reference: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — that failure mode is a nought-second run with no job and no log, "red forever, scanning nothing, and indistinguishable from a gate that is working". Keep its rules in step with `workflows/.github/workflows/secret-scan.yml` by hand; nothing automated checks they still match.
- `security.yml` runs gitleaks fetched as a pinned release binary (`VERSION: 8.30.1`), never the Action, because the Action asks orgs for a licence key. It always passes `--exit-code 0` and lets the `report` step decide pass/fail from `gitleaks.sarif`, specifically so a scanner crash can't be mistaken for "no secrets found" — and a *missing* sarif file is treated as a hard failure for the same reason.
- `security.yml` triggers: PR (tree scan, `fetch-depth: 1`), push to main (tree scan), `workflow_dispatch`, and a weekly cron `17 6 * * 1` that does a **full history** scan (`fetch-depth: 0`, `gitleaks git .`) — a credential committed and reverted is still leaked in a public repo, so the tree-only scan on every push isn't enough on its own.
- A real finding is never silenced by disabling the check — only by a dated entry in `.gitleaksignore` for a confirmed false positive; findings are redacted in the log/summary because the run log of a public repo is public too.
- `ci.yml` calls `buf` and `npm`/`go` directly via setup actions, never `make` — a `Makefile`-only change is not exercised by CI; the two must be kept in step by hand.
- The breaking check (`ci.yml`, PR-only) is the whole point of the `check` job: `git fetch --no-tags origin main:main` first, because `actions/checkout` leaves a PR on a detached merge commit with no local `main` ref for `buf breaking --against ".git#branch=main"` to read.
- `actions/checkout@v4` uses `fetch-depth: 0` purely so the breaking check has history to diff against; shallowing it breaks the comparison, not the build.
- `go-version-file: go.mod` means the Go version is never written in the workflow — bumping Go means editing `go.mod`, nothing in `.github/`.
- `publish-ts` never commits a version bump (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` as `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` as `canary`; PRs never publish (`if: github.event_name == 'push'`). Auth is `NODE_AUTH_TOKEN: ${{ github.token }}` against GitHub Packages — no external npm credential involved.
- Both workflows are least-privilege: `contents: read` at the top level; `packages: write` only on `publish-ts`, `security.yml` adds nothing beyond `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group of its own.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow, nor the gitleaks steps in `security.yml`, was executed here.
