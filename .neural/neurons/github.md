# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now: `ci.yml` (`check` + `publish-ts`, unchanged in shape) and the new `security.yml` (secret scanning). Both declare `permissions: contents: read` at the top.
- `ci.yml` calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`, after `git fetch --no-tags origin main:main` (checkout leaves a PR on a detached merge commit with no local `main`).
- `actions/checkout@v4` in `ci.yml` is pinned to `fetch-depth: 0` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` against GitHub Packages. PRs never publish (`github.event_name == 'push'` gate).
- `security.yml` is inlined rather than calling a reusable workflow, and its header comment explains why: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow call from private to public *before any job is scheduled* — the prior setup failed silently (a zero-second run with no job and no log) on every push since it was adopted. The rules are duplicated here on purpose rather than referenced.
- `security.yml` runs gitleaks v8.30.1 fetched as a release binary (not the Action, which asks orgs for a licence key) on PRs, pushes to main, a weekly Monday-06:17-UTC cron, and `workflow_dispatch`. Tree scan (`gitleaks dir .`, `fetch-depth: 1`) on PR/push; full history scan (`gitleaks git .`, `fetch-depth: 0`) only on the weekly cron — because a credential committed and reverted is still leaked in a public repo's history.
- `security.yml`'s scan step always exits 0 (`--exit-code 0`); a separate `report` step (`if: always()`) parses the SARIF and decides pass/fail. Absence of `gitleaks.sarif` is itself a failure (`"an unknown result is a failure, never a pass"`), and any finding count > 0 fails the job — so a scanner crash cannot masquerade as a clean scan.
- Findings are redacted (`--redact`) in `security.yml` because the run log and the uploaded SARIF artifact are both readable by anyone — the repo itself is public. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; gitleaks itself was not run here.
