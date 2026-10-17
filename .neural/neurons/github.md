# Neurons · .github

refreshed 2026-10-17 · fee5860e47dd

- Two workflows: `ci.yml` (lint, breaking, gen-staleness, go build, tsc, then `publish-ts`) and `security.yml` (gitleaks secret scan on PR, push to main, and a scheduled full-history walk every Monday 06:17 UTC).
- CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make`. A change to the Makefile alone is not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:32` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap in the breaking step: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` so the breaking check has history; shallowing it breaks the comparison.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` trips it.
- Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile only, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`; a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish.
- Publishing goes to GitHub Packages (`registry-url: https://npm.pkg.github.com`, `npm publish --access restricted`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed.
- `security.yml` is inlined rather than called from a reusable workflow because this repo is public and GitHub refuses a reusable workflow from a private caller. The comment at `security.yml:4-18` explains the history.
- `security.yml` design: gitleaks runs with `--exit-code 0` (scanner never fails the step); a separate report step reads the SARIF and exits non-zero if findings exist. No report at all is a failure — `security.yml:66-70`. Findings are redacted because the run log is public.
- gitleaks is pinned at v8.30.1 and fetched as a release binary, not via the Action (which requires a licence key for organisations).
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish.
- Permissions are least-privilege: `contents: read` at the workflow level; only `publish-ts` adds `packages: write`.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — both passed. Workflows not executed.
