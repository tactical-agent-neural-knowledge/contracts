# Neurons · .github
refreshed 2026-10-14 · 65c4439b3e7d

- `ci.yml`'s `check` job is the only required gate: `buf lint`, `buf breaking --against ".git#branch=main"` (PRs only), `buf generate` + `git diff --exit-code gen/` (gen must already be committed current), `go build ./...`, then `npm run build` in `gen/ts`.
- The breaking check only runs `if: github.event_name == 'pull_request'` and first does `git fetch --no-tags origin main:main`, because `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref for buf to diff against.
- `publish-ts` runs only `on: push` after `check` passes: canary version `0.0.0-canary.<12-char sha>` on every main push, real semver from the tag on `v*` pushes, published to GitHub Packages under `@tactical-agent-neural-knowledge` with `packages: write` permission.
- `security.yml` (gitleaks secret scan) is hand-inlined, not called as a reusable workflow, and the file's own top comment explains why: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a private reusable workflow to a public caller — that call used to fail with a zero-second, logless run on every push until it was inlined here.
- Rules that must not drift out of `security.yml` if it's ever reunified with the private original: gitleaks is pinned and fetched as a release binary (not the Action, which asks orgs for a licence key); findings are redacted (`--redact`) because run logs are public; the scanner is invoked with `--exit-code 0` and the separate `report` step decides pass/fail, so a scanner crash can't silently read as clean; and `report` treats a missing `gitleaks.sarif` as a hard failure, never a pass.
- `security.yml` runs a working-tree-only scan (`fetch-depth: 1`, `gitleaks dir .`) on push/PR, and a full-history scan (`fetch-depth: 0`, `gitleaks git .`) only on the Monday 06:17 UTC cron — a secret committed and reverted still leaked in a public repo, hence the periodic deep scan.
- A gitleaks false positive is silenced with a dated entry in `.gitleaksignore`, never by disabling or loosening the workflow.
- Both workflows set `permissions: contents: read` at the top level; `publish-ts` escalates to `packages: write` only inside its own job block, not repo-wide.

## Verified
- read-through of .github/workflows/ci.yml and .github/workflows/security.yml (no executable change in this area; no CI-only command can be run locally)
