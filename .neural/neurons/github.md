# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (`check` + `publish-ts`, unchanged in shape since the last refresh) and the new `security.yml` (secret scanning).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". Runs only `if: github.event_name == 'pull_request'`, and needs `git fetch --no-tags origin main:main` first because `actions/checkout` leaves a PR on a detached merge commit with no local `main` — true locally too, on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}`. PRs never publish (`github.event_name == 'push'` gate). `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means a second push to the same ref kills the first run, including a half-finished publish.
- `security.yml` is a secret scan (gitleaks) **inlined rather than referenced** from the org's shared `workflows` repo, and the file's own header comment explains why: this repo is public, `workflows` is private, and GitHub refuses a reusable workflow call from a private repo into a public caller before any job is even scheduled — the run used to fail in zero seconds with no job and no log, silently, on every push, which is the worst shape a security gate can take. So the rules are duplicated here on purpose; keep them in step with `workflows/.github/workflows/secret-scan.yml` by hand.
- `security.yml` runs on `pull_request`, `push: [main]`, `workflow_dispatch`, and a weekly `schedule` (`17 6 * * 1`) that scans full git history (`gitleaks git .`) instead of just the tree (`gitleaks dir .`), because a credential committed and reverted is still leaked in a public repo. `HISTORY` is derived from `github.event_name == 'schedule'`, which also sets `fetch-depth: 0` only for that run.
- gitleaks is fetched as a pinned release binary (`VERSION: "8.30.1"`, `curl` + `tar`), not the Action — the Action asks organisations for a licence key.
- The scan step always runs with `--exit-code 0`; the **report step** decides pass/fail by counting `.runs[].results[]` in the SARIF with `jq`, so a scanner crash can't silently read as "clean". No report file at all (`! -f gitleaks.sarif`) is itself a hard failure: `::error::gitleaks produced no report — an unknown result is a failure, never a pass`.
- Findings are redacted in the job summary (`--redact`) because the run log is world-readable on a public repo; a false positive is silenced only with a dated `.gitleaksignore` entry, never by removing the check. No `.gitleaksignore` file exists in the repo yet.
- `permissions: contents: read` at the top of both workflows; `publish-ts` is the only job anywhere that adds `packages: write`.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here.
