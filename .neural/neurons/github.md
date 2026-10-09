# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `.github/workflows/ci.yml` (the contract gates) and `.github/workflows/security.yml` (the secret scan, added 2026-10-08). `ci.yml` itself has not changed since the last refresh.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of the whole file: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so that breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- Publishing goes to GitHub Packages (`registry-url: https://npm.pkg.github.com`, `scope: "@tactical-agent-neural-knowledge"`, `npm publish --access restricted`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` throughout.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first ci run, including a half-finished publish. `security.yml` declares no concurrency group, so its runs are not cancelled by a newer push.
- Why `security.yml` inlines the scan instead of calling the shared one, in its own header: this repository is **public** and `workflows` is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller *before scheduling any job* — so the failure was a nought-second run with no job in it and no log to read. It had been red on every push since the gate was adopted. A nought-second workflow failure with no job is this signature, not a flaky runner.
- The four rules of that scan that must not drift when it is edited: gitleaks is pinned (`VERSION: 8.30.1`) and fetched as a release tarball rather than via the Action, which asks organisations for a licence key; findings are `--redact`ed because a public repo's run log is readable by anyone; the scanner always runs with `--exit-code 0` and a separate `report` step decides, so a crashed scanner cannot pass as a clean one; and a missing `gitleaks.sarif` is an error, never a pass.
- `security.yml` triggers on PRs, pushes to main, `workflow_dispatch`, and `cron: "17 6 * * 1"`. Only the schedule sets `HISTORY=true`, which switches `gitleaks dir .` to `gitleaks git .` and `fetch-depth` from 1 to 0: the weekly run walks the whole history because a credential committed and reverted still leaked. The SARIF is uploaded as an artifact for 30 days.
- A false positive is silenced with a dated entry in `.gitleaksignore` — never by dropping or narrowing the check. No `.gitleaksignore` exists yet.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed, and gitleaks was not run here.
