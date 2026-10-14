# Neurons · .github
refreshed 2026-10-14 · 65c4439b3e7d

- Two workflows only: `ci.yml` (lint/breaking/gen-is-current/build/tsc, plus npm publish on push) and `security.yml` (gitleaks secret scan) — there is no reusable/called workflow here anymore.
- `security.yml` inlines the entire gitleaks scan rather than calling a shared `workflows/.github/workflows/secret-scan.yml`, because this repo is **public** and that shared workflow lives in a **private** repo — GitHub refuses a reusable workflow from a private caller to a public repo before scheduling any job, producing a nought-second run with no log (`security.yml:5-17`). If the rules in the shared workflow change, they must be hand-ported here; there's no way to detect drift automatically.
- `security.yml` scan rules that must not drift if this file is ever touched: gitleaks is a pinned release binary (version `8.30.1` in `env.VERSION`), never the Action (orgs need a licence key for that); findings are redacted in the summary because the repo is public and the log is world-readable; the scan step always exits 0 and the separate "report" step decides pass/fail; **no SARIF report at all is treated as a failure**, never a silent pass (`security.yml:63-70`).
- `security.yml` runs a shallow tree scan (`gitleaks dir .`, `fetch-depth: 1`) on PRs/pushes but a full history scan (`gitleaks git .`, `fetch-depth: 0`) on the Monday 06:17 UTC cron — a credential committed and reverted still leaked in a public repo, so the weekly run exists specifically to catch that.
- A false positive in the secret scan is silenced with a dated `.gitleaksignore` entry, never by disabling or skipping the check (`security.yml:80-81`).
- `ci.yml`'s `check` job runs `buf lint`, then (PRs only) `git fetch --no-tags origin main:main` before `buf breaking` — `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref, so buf can't resolve `.git#branch=main` without that fetch (`ci.yml:34-39`).
- "generated code is current" in CI is `buf generate` followed by `git diff --exit-code --stat gen/` (`ci.yml:40-45`) — same check as `make check`'s last step, just inlined instead of calling make.
- `publish-ts` only runs `on: push` (main or `v*` tags) and depends on `check` passing first; it versions as `0.0.0-canary.<sha12>` on main or the tag's semver on `v*`, then `npm publish --tag canary|latest` to GitHub Packages scoped `@tactical-agent-neural-knowledge` (`ci.yml:54-81`).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means pushing again to the same branch/PR cancels the in-flight `ci.yml` run, including a publish already underway on main — a second push mid-publish race is possible in principle, though `needs: check` limits the window.

## Verified
- Read both workflow files in full; no executable change made, so no CI run to verify against.
