# Neurons · .github

refreshed 2026-10-08 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (lint/breaking/gen/build/tsc, publish-ts) and `security.yml` (gitleaks secret scan), added 2026-10-05..07.
- `security.yml`'s own header comment explains why it is a full copy rather than a call to a shared workflow: this repo is **public**, the org's `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — the failure is a nought-second run with no log. That silent-red state is why the rules are reproduced here instead of referenced; keep `.github/workflows/security.yml` and `workflows/.github/workflows/secret-scan.yml` in step by hand if either changes.
- `security.yml` runs gitleaks as a pinned release binary (`VERSION: "8.30.1"`, fetched over `curl` from GitHub releases), never the Action — the Action asks organisations for a licence key.
- The scan always exits 0 (`--exit-code 0`); the separate `report` step is what decides pass/fail by counting `gitleaks.sarif` results with `jq`. A missing `gitleaks.sarif` is itself a hard failure (`::error::gitleaks produced no report`) — unknown is never treated as clean.
- Tree scan (`fetch-depth: 1`, `gitleaks dir .`) runs on every PR and push to main; a full-history scan (`fetch-depth: 0`, `gitleaks git .`) runs only on the Monday 06:17 UTC cron, because a credential committed and reverted in a public repo has still leaked.
- Findings are redacted (`--redact`) in both the log and the SARIF upload: this repo is public, so an unredacted finding would publish the secret a second time. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check.
- `.github/workflows/ci.yml` is unchanged since the last refresh: two jobs, `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}`.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read` throughout.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow file itself was executed (no `gitleaks` binary fetched here).
