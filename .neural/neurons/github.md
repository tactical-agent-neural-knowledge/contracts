# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (`check` + `publish-ts`) and `security.yml` (secret scanning). `ci.yml` calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: a wire break "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone. `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — gated on `github.event_name == 'push'`.
- `security.yml` is a deliberate inlined duplicate of `workflows/.github/workflows/secret-scan.yml`, not a `uses:` call — GitHub refuses a reusable workflow from a private repo (`workflows`) to a public caller (this repo) before any job is scheduled, which looked like a silent always-green gate. The file's own header comment is the record of that trap; keep the duplicated rules in step by hand if the source workflow changes.
- `security.yml` gitleaks is a pinned release binary (`VERSION: "8.30.1"`, downloaded via curl, never the Action — that asks organisations for a licence key). It always runs with `--exit-code 0`; the separate `report` step reads `gitleaks.sarif` and decides pass/fail, so a scanner crash can't masquerade as a clean run, and a missing SARIF file is itself a failure.
- `security.yml` scans the working tree on every PR/push (`fetch-depth: 1`) and the full git history only on the Monday 06:17 UTC cron (`fetch-depth: 0`, `HISTORY=true`) — a credential committed and reverted still leaked in a public repo, so history gets walked weekly regardless of what's in HEAD now.
- A false positive in `security.yml` is silenced with a dated entry in `.gitleaksignore`, never by dropping the check (stated in the workflow's own comment block).
- Permissions are least-privilege: `ci.yml` declares `contents: read` at the top, only `publish-ts` adds `packages: write`; `security.yml` declares `contents: read` only. `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks from `ci.yml` reproducible outside Actions; both passed. Neither workflow was executed, and gitleaks was not run locally.
