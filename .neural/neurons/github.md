# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (`check` + `publish-ts`) and `security.yml` (the secret scan), added since the last refresh. CI still calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- `security.yml` is a secret scan with gitleaks, and its header comment explains why it is a full file instead of `uses: tactical-agent-neural-knowledge/workflows/.github/workflows/secret-scan.yml@...`: this repo is public, the reusable workflow lives in a private repo, and GitHub refuses that call before any job is even scheduled — a nought-second failure with no log. The rules are duplicated here by hand and "must not drift" per the comment.
- `security.yml` always exits the scan step 0 (`--exit-code 0`) and lets a separate `report` step decide pass/fail from the SARIF: a scanner crash must not read as a clean run, and "no report at all is a failure, never a pass" — `if [ ! -f gitleaks.sarif ]` is itself a hard failure.
- Findings are redacted (`--redact`) because this repo is public and a run log is world-readable; a false positive is silenced with a dated `.gitleaksignore` entry (none exists yet), never by weakening the gate.
- `security.yml` scans the tree (`gitleaks dir .`) on PR/push/dispatch, and the full git history (`gitleaks git .`) only on the Monday 06:17 UTC cron — a credential committed and reverted is still leaked in a public repo, hence the periodic deep scan.
- gitleaks is fetched as a pinned release binary (`VERSION: "8.30.1"`, downloaded from GitHub releases) rather than via the Action, because the Action's licence-key requirement doesn't fit a public repo.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top, and only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` only.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed here (no `gh`/Actions runner in this sandbox).
