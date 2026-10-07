# Neurons · .github
refreshed 2026-10-07 · d58208d52ddc

- Single workflow file `.github/workflows/ci.yml` runs two jobs: `check` (every PR, every push to main, every `v*` tag) and `publish-ts` (push events only, `needs: check`) — there is no separate lint-only or test-only workflow to edit.
- `check` does `buf lint` → breaking check (PRs only) → `buf generate` + `git diff --exit-code --stat gen/` → `go build ./...` → `npm install && npm run build` in `gen/ts`, in that exact order (ci.yml:30-52); a local `make check` reproduces lint+gen+build but not the TS compile step.
- The breaking check only runs `if: github.event_name == 'pull_request'` (ci.yml:36) — a direct push to main bypasses `buf breaking` entirely, so wire breaks pushed straight to main are not caught by CI at all, only by review.
- `actions/checkout` leaves PR runs on a detached merge commit with no local `main` ref, so the workflow does `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` (ci.yml:33-39) — reproducing the breaking check locally with a stale/missing local `main` branch will give a false pass or a buf error, not a false failure.
- `concurrency: group: ci-${{ github.ref }}, cancel-in-progress: true` (ci.yml:12-14) means pushing twice quickly to the same branch cancels the first run's `check` job mid-flight rather than queuing it.
- `publish-ts` versions `gen/ts` with `npm version --no-git-tag-version` right before publish: canary `0.0.0-canary.<sha:12>` + `--tag canary` on main, semver from the tag name + `--tag latest` on `v*` tags (ci.yml:68-75) — the published version is never the one committed in `gen/ts/package.json`.
- `publish-ts` needs `packages: write` (ci.yml:58-60) in addition to the default `contents: read` (ci.yml:9-11); if publishing ever starts failing with a permissions error, check this block first, not the npm token.
- Go setup uses `go-version-file: go.mod` (ci.yml:26-29), so bumping the Go version only requires editing the repo's `go.mod`, not this workflow.

## Verified
- (no command in map.yaml targets `.github` directly; workflow syntax was read, not executed — nothing to run here beyond what `.` already verifies with `buf lint`)
