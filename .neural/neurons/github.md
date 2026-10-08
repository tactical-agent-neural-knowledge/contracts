# Neurons · .github
refreshed 2026-10-07 · 572da952c512

- `ci.yml` `check` job is the single gate: `buf lint` → `buf breaking` (PRs only) → regenerate and `git diff --exit-code --stat gen/` for staleness → `go build ./...` → `npm run build` (tsc) in `gen/ts`.
- The breaking check needs a local `main` ref: `actions/checkout` leaves PRs on a detached merge commit, so the step runs `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` — without that fetch buf has nothing to diff against (ci.yml comment).
- `check` uses `fetch-depth: 0` specifically so the breaking check has history to compare against.
- `publish-ts` only runs on `push` (not PRs) and `needs: check`; on `main` it versions as `0.0.0-canary.<12-char-sha>` and publishes tag `canary`, on a `v*` tag it versions from the tag name and publishes tag `latest` — both go to GitHub Packages under `@tactical-agent-neural-knowledge`.
- `security.yml` currently runs only one job (`secrets`, calling the shared `tactical-agent-neural-knowledge/workflows` `secret-scan.yml`) — recent history (`ci: narrow the security workflow to one scanner while the call is diagnosed`) shows a dependency-scanning gate was pulled out while a call is being debugged; do not assume dependency scanning is active without checking this file first.
- Both workflows pin `permissions: contents: read` at the top level; `publish-ts` escalates to `packages: write` only inside its own job.
- Neither workflow file does its own module-path or domain checks — the actual wire-safety contract lives in `buf.yaml`/`buf.gen.yaml` at the repo root, not here; this directory only wires CI around those.

## Verified
- Read-only review of both workflow files; no runnable command lives in `.github` itself (the commands they invoke — `buf lint`, `go build`, `npm run build` — are verified from the repo root, see `.neural/neurons/root.md`).
