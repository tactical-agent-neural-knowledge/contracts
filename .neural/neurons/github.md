# Neurons · .github

refreshed 2026-10-16 · 96c9e69403fd

- Two workflows: `ci.yml` (lint, breaking, gen-staleness, go build, tsc, then `publish-ts`) and `security.yml` (gitleaks secret scan). Both read as sound on this checkout.
- `ci.yml`'s breaking check only runs `if: github.event_name == 'pull_request'` and first does `git fetch --no-tags origin main:main` — `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref, so `buf breaking --against ".git#branch=main"` would otherwise fail to resolve the ref.
- `ci.yml`'s "generated code is current" step runs `buf generate` then `git diff --exit-code --stat gen/` in CI itself — the same gate `make check` runs locally, so a PR with stale `gen/` fails even if the author never ran `make check`.
- `publish-ts` only runs `if: github.event_name == 'push'` (so never on PRs) and is gated on `needs: check`. It versions as `0.0.0-canary.<12-char sha>` on every push to `main`, or the tag's semver on a `v*` tag, then `npm publish` to GitHub Packages under `@tactical-agent-neural-knowledge`.
- `security.yml` is **inlined**, not a `uses:` call to a reusable workflow — the comment block at the top of the file explains why: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses to let a private reusable workflow run for a public caller (a nought-second failure with no job and no log). Any change to the shared secret-scan rules has to be hand-copied here; there's no automatic sync.
- `security.yml` fetches a pinned gitleaks release binary (`VERSION: "8.30.1"`) directly from GitHub releases rather than using the gitleaks Action, because the Action asks for an org licence key this repo doesn't have.
- The scan step always passes `--exit-code 0`; the separate `report` step (`if: always()`) is what fails the job by reading the SARIF and checking the finding count — so a gitleaks crash that leaves no `gitleaks.sarif` is caught explicitly ("no report is a failure, never a pass") rather than silently passing.
- `security.yml` runs a tree-only scan (`fetch-depth: 1`, `gitleaks dir .`) on push/PR, and a full-history scan (`fetch-depth: 0`, `gitleaks git .`) on its Monday 06:17 UTC cron — a credential committed and reverted is still a leak in a public repo, so the weekly run checks history the fast path skips.
- A false positive is silenced with a dated entry in `.gitleaksignore`, never by disabling or loosening this workflow — that rule is in the workflow's own comments, enforce it in review.

## Verified
- Read both workflow files for internal consistency (no executable command specific to `.github/`; verification is the root-level buf lint/breaking above, which both workflows also run).
