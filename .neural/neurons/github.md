# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged in shape: `check` on PR/main/tags, `publish-ts` on push, `needs: check`) and the new `security.yml` (secret scanning).
- `security.yml` is a deliberate duplication, explained in its own header comment (lines 1-18): the real rules live in a private `workflows` repo's reusable `secret-scan.yml`, but GitHub refuses a reusable workflow call from a private repo into a public caller *before any job is scheduled* — so the call failed as a nought-second run with no job and no log, silently, on every push since it was adopted. That is why this file reproduces the rules instead of calling them.
- The failure mode `security.yml` exists to avoid — "red forever, scanning nothing, indistinguishable from a gate that works" — is the actual incident history of this repo's secret scanning, not a hypothetical in the comment.
- `security.yml` runs gitleaks v8.30.1 fetched as a release binary over `curl` (not the Action, which asks orgs for a licence key), always with `--exit-code 0`; the `report` step parses the SARIF and decides pass/fail itself, so a gitleaks crash cannot be mistaken for a clean scan, and "no report at all" is treated as a failure, never a pass (security.yml:63-71).
- Triggers: `pull_request` and `push: [main]` do a tree scan (`gitleaks dir .`, `fetch-depth: 1`); the Monday 06:17 UTC `schedule` does a full history scan (`gitleaks git .`, `fetch-depth: 0`) because a committed-then-reverted credential is still leaked, especially in a public repo.
- Findings are redacted (`--redact`) because this repo is public and the Actions log is readable by anyone who can read the repo. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing the step.
- `ci.yml` calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI. The breaking check (`ci.yml:31`) still runs only `if: github.event_name == 'pull_request'` and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves PRs on a detached merge commit with no local `main`.
- `actions/checkout@v4` uses `fetch-depth: 0` in `ci.yml` for the breaking check's history; `security.yml` instead sets fetch-depth per trigger (1 normally, 0 only for the scheduled history scan) since gitleaks' tree scan needs no history at all.
- The staleness gate is still `buf generate` + `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `publish-ts` is unchanged: versions without committing (`npm version --no-git-tag-version`), canary `0.0.0-canary.${GITHUB_SHA::12}` on push to main, release `${GITHUB_REF_NAME#v}` on `v*` tags, to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}`.
- Permissions stay least-privilege: `ci.yml` declares `contents: read` with `packages: write` only on `publish-ts`; `security.yml` declares only `contents: read` — it uploads a SARIF artifact, not a code-scanning alert, so it needs no `security-events: write`.
- `ci.yml` still has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true`; `security.yml` has no concurrency group, so overlapping pushes each get their own scan run.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. `security.yml` was read, not executed (gitleaks fetch/scan was not run here).
