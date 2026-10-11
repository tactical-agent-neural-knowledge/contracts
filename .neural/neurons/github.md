# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged this refresh: `check` on PRs/main/`v*` tags, `publish-ts` on pushes, `needs: check`) and the new `security.yml` — a standalone gitleaks secret scan, not called from `ci.yml`.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so that breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- Publishing goes to GitHub Packages (`registry-url: https://npm.pkg.github.com`, `scope: "@tactical-agent-neural-knowledge"`, `npm publish --access restricted`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top, and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.
- `security.yml` reproduces (does not call) a reusable workflow from a private sibling repo `workflows`, because GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled — this repo is public. Keep the two in step by hand; the duplication is deliberate, per the file's own header comment.
- `security.yml` runs gitleaks as a pinned release binary (`VERSION: "8.30.1"`, downloaded via `curl`, never the Action, which asks orgs for a licence key). It always exits 0 from the scan step; the separate `report` step reads `gitleaks.sarif` and decides pass/fail, so a scanner crash can't masquerade as "no findings" — and a missing report file is itself a hard failure (`::error::gitleaks produced no report`).
- `security.yml` scans the working tree (`fetch-depth: 1`, `gitleaks dir .`) on `pull_request`/`push`/`workflow_dispatch`, but the Monday 06:17 UTC `schedule` trigger sets `HISTORY=true`, fetches full history (`fetch-depth: 0`) and runs `gitleaks git .` instead — a credential committed and reverted still leaked, especially in a public repo.
- Findings are redacted in the log and the job summary on purpose (`--redact`, plus the report step never prints raw values) because this repo's Actions logs are world-readable. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step cannot be reproduced here (no network fetch of the release binary attempted).
