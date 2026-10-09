# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen-is-current/build/tsc) and `security.yml` (secret scan), both triggered on PR and push to main.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: a wire break "would be a production incident in web/mobile/agent-runner, so it is caught at the source" (`ci.yml:31`). It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. `fetch-depth: 0` on checkout exists purely for this. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`. The TypeScript check is `npm install --no-audit --no-fund && npm run build` in `gen/ts` on node 24 — a tsc compile of the generated sources, no tests.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. Publishes to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed. `packages: write` is scoped to that one job only.
- `security.yml` is a secret scan **inlined rather than called** (`security.yml:1-18`): this repo is public and the org's reusable workflow lives in a private repo, and GitHub refuses a reusable workflow from a private caller to a public repo before any job is even scheduled. It had been failing silently on every push — a nought-second, job-less failure — until this was noticed, which is the worst shape a security gate can take. Any edit to the org's canonical `workflows/.github/workflows/secret-scan.yml` must be hand-mirrored here; there is no other link between them.
- `security.yml` pins gitleaks as a release binary (`VERSION: "8.30.1"`, fetched from `gitleaks/gitleaks` releases) rather than using the Action, which asks organisations for a licence key.
- The scanner always runs with `--exit-code 0` and `--redact`; a separate `report` step (`if: always()`) reads `gitleaks.sarif` and is what actually fails the job — `n=$(jq '[.runs[].results[]] | length' ...)`. No report file at all is treated as a failure, never a pass (`::error::gitleaks produced no report`), so a crash in the scan step cannot masquerade as "clean".
- `security.yml` scans the working tree (`gitleaks dir .`, `fetch-depth: 1`) on PR and push, and the full git history (`gitleaks git .`, `fetch-depth: 0`) on the Monday 06:17 UTC cron — a credential committed and reverted is still a leak in a public repo, so the history scan exists even though the tree scan is cheaper and runs far more often.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step was not run here (no network fetch of the binary attempted).
