# Neurons · .github

refreshed 2026-10-14 · 6e371811ddb2

- Two workflows now, not one: `ci.yml` (unchanged shape: `check` on PR/main/`v*` tags, `publish-ts` on push only, `needs: check`) and a new `security.yml` (secret scanning).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` ref — same trap applies on a fresh local clone.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` to GitHub Packages.
- `security.yml` is a **secret scan reproduced inline on purpose**, not called as a reusable workflow: the comment at the top explains a reusable workflow from a private `workflows` repo cannot be called by this public repo (GitHub refuses it pre-scheduling, a nought-second failure with no job and no log — it had silently failed on every push since adoption before this was noticed).
- `security.yml` rules that must not drift if ever resynced from the source: gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a release binary, never the Action (licence key required for orgs); findings are redacted in the log because this repo is public; the scanner runs `--exit-code 0` always, and the separate `report` step decides pass/fail by counting the sarif — a crash in the scan step cannot silently pass; no sarif file at all is itself a failure (`exit 1`), never treated as clean.
- `security.yml` triggers on PR, push to main, a weekly `schedule` (Monday 06:17 UTC) that walks full git history (`fetch-depth: 0`, `gitleaks git .`) because a committed-then-reverted credential is still leaked in a public repo, and `workflow_dispatch`. Normal PR/push runs are a tree-only scan (`fetch-depth: 1`, `gitleaks dir .`).
- A false positive in `security.yml` is silenced with a dated entry in `.gitleaksignore`, never by dropping or weakening the check.
- Permissions are least-privilege and deliberate across both workflows: top-level `contents: read`; `publish-ts` alone adds `packages: write`. `ci.yml`'s `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here (no GitHub Actions runner, no gitleaks binary fetch attempted).
