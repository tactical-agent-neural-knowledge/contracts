# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/build/publish, unchanged this refresh) and the new `security.yml` (secret scanning).
- `.github/workflows/ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check in `ci.yml` runs only `if: github.event_name == 'pull_request'`; `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone. `fetch-depth: 0` exists purely so this comparison has history.
- `security.yml` (`.github/workflows/security.yml:1-18`) is a secret scan **inlined rather than called**: this repo is public and the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled — so a `uses: org/workflows/.github/workflows/secret-scan.yml@...` call here fails with a nought-second run and no log, and did so on every push since it was first adopted (see `572da95`, `6b1c4b7`, `34e2dd6`). The fix was to duplicate the rules rather than reference them; that duplication is a deliberate, documented cost of being a public repo, not an oversight — don't "simplify" it back to a `uses:` call.
- `security.yml` pins gitleaks `8.30.1` as a release binary (not the Action, which asks orgs for a licence key), always exits 0 from the scan step, and lets a separate `report` step decide pass/fail from the SARIF — so a scanner crash can't look like a clean run, and "no report at all" is itself a failure (`if [ ! -f gitleaks.sarif ]` → `exit 1`).
- `security.yml` findings are redacted in the job summary (`--redact`): a run log on a public repo is readable by anyone, so a real secret is never echoed even to prove a match. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- `security.yml` scans the working tree (`gitleaks dir .`) on PRs and pushes, but the whole git history (`gitleaks git .`) on its Monday 06:17 UTC `schedule` cron — a credential committed and reverted is still leaked in a public repo, so the history scan exists specifically to catch that.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, gated on `github.event_name == 'push'`. Publishes to GitHub Packages, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed.
- Permissions are least-privilege per workflow: `ci.yml` and `security.yml` both declare `contents: read` at the top; only `publish-ts` adds `packages: write`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group of its own.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step was not run here.
