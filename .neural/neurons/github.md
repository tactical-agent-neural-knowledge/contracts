# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (unchanged since the last refresh — lint/breaking/gen-staleness/go build/tsc on PRs and main, npm publish on push) and the new `security.yml`, which runs the secret scan.
- `security.yml` is deliberately self-contained, and the comment at its top says why: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled — a nought-second failure with no log. The gate had been silently red on every push since it was adopted. Any future attempt to switch this back to `uses: owner/workflows/.github/workflows/secret-scan.yml@...` will reproduce that exact failure.
- `security.yml` triggers on `pull_request`, `push` to `main`, a weekly `schedule` (Monday 06:17 UTC), and `workflow_dispatch`. Only the scheduled run scans full git history (`fetch-depth: 0`, `gitleaks git .`); PR/push runs scan the working tree only (`fetch-depth: 1`, `gitleaks dir .`) — a credential committed and reverted is only ever caught by the weekly run.
- gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a release binary, not the GitHub Action — the Action requires an org licence key, the binary doesn't.
- The scanner step always runs `--exit-code 0`; a separate `report` step (`if: always()`) is what actually fails the job, by counting `gitleaks.sarif` results with `jq`. A missing `.sarif` file is treated as a failure, never a pass — "no report" and "clean report" are not the same thing.
- A false positive is silenced with a dated entry in `.gitleaksignore`, never by disabling or skipping this workflow.
- CI calls `buf` directly via `bufbuild/buf-setup-action@v1` and gitleaks via a pinned curl download, never `make` — a change to the `Makefile` alone is not exercised by either workflow.
- The breaking check (`ci.yml`) runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` — the same applies on a fresh clone, which is why `make breaking` needs that fetch too.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` in `ci.yml` purely so the breaking check has history to compare against.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. It never runs on a PR (`github.event_name == 'push'` gate).
- Permissions are least-privilege: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group of its own.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file itself was executed (no Actions runner here).
