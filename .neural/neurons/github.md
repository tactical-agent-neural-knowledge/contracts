# Neurons · .github

refreshed 2026-10-08 · b57522e4f7aa

- Two workflows now, not one: `ci.yml` (lint/breaking/gen/build/tsc, then `publish-ts`) and a new `security.yml` (secret scanning). Both still call `buf` / tools directly, never `make`; a `Makefile`-only change is not exercised by CI.
- `security.yml` exists, and is a full duplicate of another repo's reusable workflow, only because this repo is **public** and the org's shared `tactical-agent-neural-knowledge/workflows` repo is **private** — GitHub refuses a reusable workflow call from private to public *before scheduling any job*, so the original two-line `uses:` call failed with zero jobs and no log (`.github/workflows/security.yml`'s own header comment explains this in full; read it before "simplifying" this file back to a `uses:` call).
- That failure mode cost real time: `6b1c4b7` (appending the calls to `ci.yml` was rejected pre-schedule, sending contracts and sdk-ts red on main), `572da95` (split to one scanner to isolate which call GitHub rejected), `b57522e` (inlined gitleaks's own rules rather than calling them). A `deps-scan` equivalent was dropped in the same narrowing and has not come back.
- The rules reproduced from `workflows/.github/workflows/secret-scan.yml` and marked "must not drift" in the header comment: gitleaks pinned as a release binary (not the Action, which asks orgs for a licence key); findings redacted in the SARIF and the log (this repo is world-readable); the scan step always exits 0 and a separate `report` step decides pass/fail; **no SARIF file at all is a failure**, never treated as a clean scan.
- `security.yml` triggers on PR, push to main, `workflow_dispatch`, and a weekly cron (`17 6 * * 1`) that walks full git history (`fetch-depth: 0`, `gitleaks git .`) because a credential committed and reverted is still leaked in a public repo; PR/push runs scan only the working tree (`fetch-depth: 1`, `gitleaks dir .`).
- A finding is silenced only with a dated entry in `.gitleaksignore`, per the report step's own text — never by relaxing `exit-code` or skipping the job.
- `ci.yml`'s breaking check still needs `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it (detached merge commit on PRs has no local `main`); same trap locally on a fresh clone.
- `ci.yml`'s staleness gate: `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed or used.
- Permissions stay least-privilege per job: `ci.yml` top-level `contents: read`, only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` throughout, including its SARIF upload.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks from `ci.yml` reproducible outside Actions; both passed. Neither workflow file was executed (no `gitleaks` binary here, no Actions runner).
