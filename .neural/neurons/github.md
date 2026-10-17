# Neurons · .github

refreshed 2026-10-17 · fee5860e47dd

- Two workflows: `ci.yml` (lint, breaking, gen-staleness, go build, tsc, publish-ts) and `security.yml` (gitleaks secret scan). Both read as sound on this checkout.
- `ci.yml` calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make`. A change to the Makefile alone is not exercised by CI — both must be kept in step by hand.
- `ci.yml`'s breaking check only runs `if: github.event_name == 'pull_request'` and first does `git fetch --no-tags origin main:main` — `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref, so `buf breaking --against ".git#branch=main"` would otherwise fail to resolve the ref.
- `ci.yml`'s "generated code is current" step runs `buf generate` then `git diff --exit-code --stat gen/` — same gate as `make check`. A stale gen/ fails the PR.
- `ci.yml` has a `publish-ts` job that runs only on `push` (main and `v*` tags), publishes `@tactical-agent-neural-knowledge/contracts` as a canary (main) or semver release (tag) to GitHub Packages.
- `security.yml` is the gitleaks secret scan, inlined rather than called from a private reusable workflow because GitHub refuses a private reusable workflow called from a public repo — a lesson learned from a gate that was red on every push while scanning nothing.
- `security.yml` runs on PR, push to main, and a scheduled full-history walk every Monday 06:17 UTC. The scheduled run uses `fetch-depth: 0` to walk all history; PR/push uses depth 1 (tree scan only).
- `security.yml` always exits 0 from the scan step; the `report` step decides pass/fail. A missing SARIF report is a failure — a crash can never masquerade as a clean scan.
- Secret findings are redacted in logs because this repo is public and run logs are readable by anyone who can read the repo.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
