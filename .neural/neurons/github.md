# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/build/publish, unchanged since the last refresh) and `security.yml` (new — the gitleaks secret scan).
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref — the same applies on a fresh local clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}`.
- `security.yml` is inlined rather than calling a reusable workflow, and the file's own header explains why: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow call from private to public before any job is even scheduled — so every push failed silently (a zero-second run, no job, no log) until the rules were copied in by hand. That duplication is a trap: the two copies (here and in `workflows/.github/workflows/secret-scan.yml`) will drift unless kept in sync deliberately.
- gitleaks is pinned by version (`VERSION: "8.30.1"`) and fetched as a release tarball, not via the GitHub Action — the Action asks organisations for a licence key this repo doesn't have.
- The scan step always passes `--exit-code 0`; a separate `report` step (`if: always()`) reads `gitleaks.sarif` and decides pass/fail by counting `.runs[].results[]` with `jq`. If the sarif file is missing entirely, that is treated as a failure, never a pass — `::error::gitleaks produced no report`. A crash in the scan step cannot masquerade as a clean scan.
- Tree scan on PRs and pushes (`fetch-depth: 1`); full-history scan on the Monday 06:17 UTC cron (`fetch-depth: 0`), because "a credential committed and reverted is still a credential that leaked" in a public repo. `workflow_dispatch` is also wired for an on-demand run.
- Findings are redacted (`--redact`) because the Actions log and job summary are world-readable on a public repo; a false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check.
- `actions/checkout@v4` with `fetch-depth: 0` in `ci.yml` is there purely so the breaking check has history; shallowing it breaks the comparison, not the build. `security.yml` sets its own independent `fetch-depth` per the tree-vs-history distinction above.
- Permissions are least-privilege throughout: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` only, even for the SARIF artifact upload.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` only — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow itself was executed (no `gitleaks` binary fetched, no Actions runner here).
