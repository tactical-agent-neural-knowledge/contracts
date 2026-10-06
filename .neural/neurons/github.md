# Neurons · .github
refreshed 2026-10-06 · fb6e2ffe6678

- One workflow, `.github/workflows/ci.yml`, two jobs: `check` (runs on PR, push to main, and `v*` tags) and `publish-ts` (push events only, `needs: check`).
- The breaking-change step only runs `if: github.event_name == 'pull_request'` — pushes to main have already passed that gate as a PR, so it isn't repeated there.
- `actions/checkout` leaves a PR run on a detached merge commit with no local `main` ref; the workflow explicitly runs `git fetch --no-tags origin main:main` before `buf breaking` reads `.git#branch=main`, or the breaking check would error on a missing ref.
- `fetch-depth: 0` is required on checkout for the same reason — buf needs real git history, not a shallow clone.
- The "generated code is current" step runs `buf generate` then `git diff --exit-code --stat gen/` directly (not `make check`) — keep both in sync if either changes.
- `publish-ts` versions the npm package as `0.0.0-canary.<12-char-sha>` (tag `canary`) on a push to main, or strips the leading `v` from the tag name as the semver (tag `latest`) on a `v*` tag push — this is the only place package version is set; it is not read from `package.json` in the repo.
- Publishing target is GitHub Packages (`npm.pkg.github.com`), scope `@tactical-agent-neural-knowledge`, authenticated with `github.token` — no separate npm token secret.
- Both jobs pin Node 24 via `actions/setup-node@v4`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a new push to the same ref cancels an in-flight run rather than queuing behind it.
- `permissions: contents: read` at the workflow level; `publish-ts` escalates to `packages: write` only within its own job.

## Verified
- (workflow YAML read only; no runnable command targets `.github` alone — covered by root's `buf lint`/`make check`)
