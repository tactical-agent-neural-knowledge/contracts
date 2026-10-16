# Neurons · .github

refreshed 2026-10-16 · 96c9e69403fd

- Two workflows now, not one: `ci.yml` (lint/breaking/gen-staleness/go build/tsc/publish, unchanged in shape since the last refresh) and the new `security.yml` (gitleaks secret scan).
- `ci.yml`'s breaking check is PR-only (`if: github.event_name == 'pull_request'`) and must `git fetch --no-tags origin main:main` first — `actions/checkout` leaves PRs on a detached merge commit with no local `main`, so `buf breaking --against ".git#branch=main"` has nothing to read without it. `fetch-depth: 0` on checkout exists solely for this.
- The staleness gate (`ci.yml:40-45`) is `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` — regenerating with any plugin version other than `buf.gen.yaml`'s pins will trip it in CI even if it passed locally.
- Go version is never pinned in the workflow itself: `actions/setup-go@v5` reads `go-version-file: go.mod`, so bumping Go means editing `go.mod`, not `ci.yml`.
- `publish-ts` (push-only, `needs: check`) versions without a git commit via `npm version --no-git-tag-version`: canary `0.0.0-canary.${GITHUB_SHA::12}` on every push to main, real semver from the tag name on `v*` tags. Only this job gets `packages: write`; the rest of the file is `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` + `cancel-in-progress: true` — a second push to the same ref kills an in-flight run, including a half-finished publish.
- `security.yml` is inlined rather than calling a reusable workflow from a sibling private repo: GitHub refuses a public-repo call into a private reusable workflow before any job is even scheduled, so the scan logic lives directly in this file.
- Gitleaks (v8.30.1) is fetched as a raw GitHub release binary, not the official Action — avoids that Action's licence-key requirement.
- The scanner step always exits 0; a separate `report` step parses the produced `gitleaks.sarif` with `jq` and fails the job if findings > 0 **or if the sarif file is missing entirely** — an unknown result is treated as a failure, never a silent pass.
- Scan scope differs by trigger: PR/push scans the working tree only (`gitleaks dir`); a weekly cron (`17 6 * * 1`) runs `gitleaks git` across full history instead. Findings are redacted before upload since the repo is public, and the sarif is kept as a 30-day artifact.

## Verified

`npx --yes @bufbuild/buf lint`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks from `ci.yml` reproducible outside Actions; both passed. Neither workflow was executed directly.
