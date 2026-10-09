# Neurons · .github
refreshed 2026-10-09T02:51:01Z · e52a377a71d9

- `ci.yml` has two jobs: `check` (buf lint, buf breaking against main on PRs only, `buf generate` + `git diff` to catch stale `gen/`, `go build ./...`, then `npm install && npm run build` in `gen/ts`) and `publish-ts` (push-only, needs `check` to pass first).
- The breaking-change job only runs `if: github.event_name == 'pull_request'` and first runs `git fetch --no-tags origin main:main` — `actions/checkout`'s default checkout has no local `main` ref on a PR's detached merge commit, so skipping that fetch makes `buf breaking --against '.git#branch=main'` compare against nothing meaningful.
- `publish-ts` versions with `npm version --no-git-tag-version`: `0.0.0-canary.<first 12 chars of GITHUB_SHA>` on every push to main (tag `canary`), or the tag name minus leading `v` on a `v*` tag push (tag `latest`) — this is the only place the release version is decided, not in `package.json`.
- `security.yml` is a full secret-scan workflow inlined here rather than calling a reusable one — see the long comment at the top of the file: a private org workflow cannot be called from this public repo (GitHub refuses that reusable-workflow call before scheduling any job), so this repo was silently red-with-no-job on every run until it was copied in verbatim. Keep it in sync with `workflows/.github/workflows/secret-scan.yml` by hand; there is no automation doing that.
- `security.yml`'s gitleaks step always exits 0; the separate `report` step is what actually decides pass/fail by reading `gitleaks.sarif` and checking the finding count — if `gitleaks.sarif` doesn't exist at all, that's treated as a failure, never a silent pass.
- History scan (`gitleaks git .`, full git log) only runs on the Monday 06:17 UTC cron; PR/push runs are tree-only (`gitleaks dir .`, `fetch-depth: 1`) — a secret committed and reverted between two Monday runs would only surface on the next scheduled scan, not on the PR that reverted it.
- A false-positive secret finding is silenced with a dated entry in `.gitleaksignore`, never by weakening or skipping this check (stated directly in the workflow's own comments).

## Verified
- Read only; no runnable command for this area (YAML workflow files, not executed locally).
