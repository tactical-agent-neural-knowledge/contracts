# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now, not one: `ci.yml` (lint/breaking/gen-staleness/build/tsc, then publish) and a new `security.yml` (secret scanning). They are independent — `security.yml` does not gate `ci.yml`'s jobs or vice versa.
- `.github/workflows/ci.yml` still has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref (same trap locally on a fresh clone).
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, to GitHub Packages (`registry-url: https://npm.pkg.github.com`, `scope: "@tactical-agent-neural-knowledge"`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}`. PRs never publish.
- `security.yml` inlines gitleaks rather than calling a reusable workflow, and says why in its own header comment: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow call from private to public *before any job is scheduled* — the earlier setup failed silently (a nought-second run, no job, no log). The rules are duplicated here on purpose and must not drift from `workflows/.github/workflows/secret-scan.yml`.
- `security.yml`'s scan step always runs gitleaks with `--exit-code 0` and a separate `report` step decides pass/fail from the SARIF; this is deliberate — a gitleaks *crash* must not read as a clean scan, and "no `gitleaks.sarif` at all" is treated as a failure (`::error::gitleaks produced no report`), never as a pass.
- `security.yml` scan depth depends on trigger: `HISTORY: ${{ github.event_name == 'schedule' }}` — PRs and pushes get `fetch-depth: 1` / `gitleaks dir .` (tree only); the Monday 06:17 UTC cron gets `fetch-depth: 0` / `gitleaks git .` (full history), because a credential committed and reverted is still a credential that leaked in a public repo. A false positive is silenced with a dated `.gitleaksignore` entry, never by weakening the check.
- Findings are redacted in both the job log and the step summary (`--redact`) — a run log here is readable by anyone, since the repo is public.
- Permissions stay least-privilege in both files: `ci.yml` declares `contents: read` and only `publish-ts` adds `packages: write`; `security.yml` declares `contents: read` only.
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow file itself was executed (no gitleaks binary fetched, no Actions runner here).
