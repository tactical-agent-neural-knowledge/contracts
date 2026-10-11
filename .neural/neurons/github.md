# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now: `ci.yml` (`check` + `publish-ts`, unchanged in shape since the last refresh) and a new `security.yml` that runs the gitleaks secret scan.
- `security.yml`'s own header comment is the fact worth keeping: its rules are a reproduction of `workflows/.github/workflows/secret-scan.yml`, not a call to it, because GitHub refuses a reusable workflow from a private repository (`workflows`) called by a public one (this repo) — before any job is even scheduled, so the failure was a nought-second run with no log. It had failed on every push since the gate was adopted until this file replaced the call with a copy.
- Anyone editing `security.yml` must keep it in step with `workflows/.github/workflows/secret-scan.yml` by hand — there is no mechanism enforcing the two stay identical, only the comment saying they must.
- Rules that must not drift out of `security.yml`, per its own comment: gitleaks is pinned and fetched as a release binary (not the Action, which asks orgs for a licence key); findings are redacted in the log, because this repo is public and readable by anyone; the scanner always exits 0 and a separate `report` step decides pass/fail, so a scanner crash cannot be mistaken for a clean run; and no SARIF report at all is itself a failure, never a pass.
- `security.yml` triggers on PR, push to main, a weekly `schedule` (Monday 06:17 UTC), and `workflow_dispatch`. Only the scheduled run sets `fetch-depth: 0` and scans `gitleaks git .` (full history); PR/push scan `gitleaks dir .` (working tree only) — "a credential committed and reverted is still a credential that leaked."
- `ci.yml` is still the only workflow that gates merges to main on wire safety. Two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, gated on `github.event_name == 'push'`.
- Permissions are least-privilege per workflow: `ci.yml` declares `contents: read` at top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read` throughout, even for the SARIF upload step.
- `ci.yml` has `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed with no output. Neither workflow file itself was executed (gitleaks was not run here).
