# Neurons · .github

refreshed 2026-10-17 · fee5860e47dd

- Two workflows: `ci.yml` (lint, breaking, gen-staleness, go build, tsc, publish-ts) and `security.yml` (gitleaks secret scan). Both read as sound on this checkout.
- CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make`. A change to the Makefile alone is not exercised by CI — the two must be kept in step by hand.
- `ci.yml`'s breaking check only runs `if: github.event_name == 'pull_request'` and first does `git fetch --no-tags origin main:main` — `actions/checkout` leaves PRs on a detached merge commit with no local `main`, so `buf breaking --against ".git#branch=main"` would fail without this step. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` so the breaking check has full history; shallowing breaks the comparison.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf/plugin version than the pins in `buf.gen.yaml` will trip it.
- `actions/setup-go@v5` uses `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- `publish-ts` versions without committing: a `v*` tag publishes `${GITHUB_REF_NAME#v}` under `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish (job is gated on `github.event_name == 'push'`).
- Publishing goes to GitHub Packages (`registry-url: https://npm.pkg.github.com`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish.
- `security.yml` is inlined rather than calling a reusable workflow because this repo is public and GitHub refuses a reusable workflow from a private repo to a public caller. The scan runs on PR, push to main, and a scheduled full-history walk every Monday at 06:17 UTC.
- Gitleaks is pinned at v8.30.1 and fetched as a release binary (not the Action, which requires a licence key). The scanner always exits 0; the report step decides, so a crash cannot pass as a clean scan. No report = failure, never a pass.
- Security findings are redacted in logs because this is a public repo: a real secret is already leaked to everyone; rotate first, then remove from history. False positives are silenced with a dated `.gitleaksignore` entry.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — both passed. Workflow files themselves not executed.
