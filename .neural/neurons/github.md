# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged this refresh: `check` + `publish-ts`) and the new `security.yml`, the secret scan.
- `security.yml` is deliberately inlined rather than calling a reusable workflow from the org's private `workflows` repo: GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled, which this repo hit as a silent, log-less, nought-second failure "on every push since the gate was adopted" — read the file's header comment in full before touching it, since it explains why the duplication is intentional, not an oversight.
- `security.yml` runs gitleaks as a pinned release binary (`VERSION: "8.30.1"`, fetched by `curl` + `tar`, never the Action) because the Action asks organisations for a licence key this repo doesn't have.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step decides pass/fail by reading `gitleaks.sarif` with `jq` — a crashed scanner must not look like a clean one, and a missing `gitleaks.sarif` is treated as a failure (`::error::gitleaks produced no report`), never a pass.
- Findings are redacted (`--redact`) because this repo is public and a run log is world-readable; a false positive is silenced with a dated `.gitleaksignore` entry, never by removing or weakening the check.
- `security.yml` scans the working tree on every PR/push (`fetch-depth: 1`) but the full git history on the Monday 06:17 UTC cron (`fetch-depth: 0`, `HISTORY: ${{ github.event_name == 'schedule' }}`) — a credential committed and reverted is still treated as leaked in a public repo.
- CI calls `buf` and `gitleaks` directly, never `make`. A change to the `Makefile` alone is not exercised by CI — the two must be kept in step by hand.
- The breaking check (`ci.yml`) is the point of the `check` job: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason that step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so it must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — the job is gated on `github.event_name == 'push'`.
- Permissions are least-privilege and deliberate in both workflows: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read` throughout.
- `ci.yml`'s `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; gitleaks was not run locally.
