# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen-staleness/build/publish, unchanged in shape since the last refresh) and the new `security.yml` (gitleaks secret scan). They are independent — `security.yml` is not `needs:` by anything and doesn't gate `ci.yml`.
- `security.yml` exists only because this repo is **public** while the org's shared `workflows` repo is **private**: GitHub refuses a reusable workflow call from private to public before any job is even scheduled, so the call was a nought-second failure with no log — "red forever, scanning nothing, and indistinguishable from a gate that is working" (security.yml:9-13). The fix was to inline the rules, not fix the call; keep the inlined copy in step with `workflows/.github/workflows/secret-scan.yml` by hand, there is no automation that does it.
- `security.yml` trigger shape: `pull_request` and `push: main` scan only the working tree (`gitleaks dir .`); the Monday 06:17 UTC `schedule` run walks the **full git history** (`gitleaks git .`, `fetch-depth: 0`) because "a credential committed and reverted is still a credential that leaked... in a public repository it leaked to everybody." `workflow_dispatch` is also wired for an ad hoc run.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step (`if: always()`) is what actually fails the job, by counting `.sarif` results with `jq`. A missing `gitleaks.sarif` is treated as a hard failure ("an unknown result is a failure, never a pass"), not a pass — a crash in the scan step can't silently go green.
- Findings are redacted (`--redact`) because this is a public repo and the Actions log is world-readable; a false positive is silenced with a dated `.gitleaksignore` entry, never by removing the step.
- `ci.yml` still calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is still not exercised by CI, keep them in step by hand.
- The breaking check (`ci.yml`, PR-only) still needs `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` because `actions/checkout` leaves PRs on a detached merge commit with no local `main` — same trap applies on a fresh local clone.
- `publish-ts` is unchanged: canary (`0.0.0-canary.${GITHUB_SHA::12}`) on push to main, release (`${GITHUB_REF_NAME#v}`) on a `v*` tag, PRs never publish, `GITHUB_TOKEN` is the only credential used (`packages: write`, scoped to that one job).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` still applies only to `ci.yml`; `security.yml` has no concurrency group, so a scheduled scan and a push-triggered scan can run side by side.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file itself was executed (`security.yml`'s gitleaks step and `ci.yml`'s Actions-only steps are unverifiable here).
