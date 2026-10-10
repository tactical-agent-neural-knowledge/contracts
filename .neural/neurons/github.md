# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (`check` + `publish-ts`) and the new `security.yml`, added because a secret-scan gate had been failing on every push since it was adopted.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so that breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in the workflow: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`. `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` kills a half-finished publish on a second push.
- `security.yml` exists only because reusable workflows cannot cross the public/private boundary: this repo is public, the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow call from private to public *before any job is scheduled* — a nought-second failure with no job and no log, which is why the gate was red on every run since it was adopted and nobody noticed. The fix is duplication, not a call: the rules of `workflows/.github/workflows/secret-scan.yml` are reproduced inline in `security.yml` and must be kept in step by hand if that source ever changes.
- `security.yml` runs gitleaks fetched as a pinned release binary (`VERSION: "8.30.1"`), not the GitHub Action, because the Action asks organisations for a licence key. It always exits 0 from the scan step; a separate `report` step reads `gitleaks.sarif` and decides pass/fail — a missing report file is treated as a failure (`::error::gitleaks produced no report`), never a silent pass. Findings are redacted in the summary because this repo is public and its Action logs are readable by anyone.
- `security.yml` triggers on `pull_request`, `push: [main]`, `workflow_dispatch`, and a weekly cron (`17 6 * * 1`) that scans full git history (`gitleaks git .` with `fetch-depth: 0`) instead of just the tree (`gitleaks dir .`, `fetch-depth: 1`) — a credential committed and reverted is still leaked in a public repo, so history is swept weekly even though PRs only need the tree.
- Permissions are least-privilege and deliberate in both workflows: `contents: read` at the top, and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read`.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step was not run here.
