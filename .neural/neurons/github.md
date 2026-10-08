# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now: `ci.yml` (buf lint/breaking/gen-staleness/go build/tsc, since before this refresh) and `security.yml`, added this cycle (the secret scan).
- `security.yml` is a full secret-scan workflow *inlined* rather than called from the org's shared `workflows` repo, because that repo is private and this one is public — GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled, which previously produced a nought-second failure with no job and no log, red on every push since the gate was adopted. The file's own header comment says the duplication is deliberate and names the rules that must not drift if `workflows/.github/workflows/secret-scan.yml` changes.
- `security.yml` runs gitleaks v8.30.1 fetched as a pinned release binary (not the Action, which asks orgs for a licence key), triggered on `pull_request`, `push` to `main`, a weekly `schedule` (Monday 06:17 UTC) and `workflow_dispatch`.
- The scan step always exits 0 (`--exit-code 0`); a separate `report` step (`if: always()`) decides pass/fail by reading the SARIF and failing if the file is missing at all — "no report at all is a failure, never a pass" is the file's own comment, so a crashed scanner cannot look like a clean one.
- `HISTORY=${{ github.event_name == 'schedule' }}` switches both the checkout depth (`fetch-depth: 0` only for the scheduled run) and the gitleaks mode (`git .` walking all history vs `dir .` on the working tree) — a push/PR scan is tree-only and cheap, the weekly cron is the one that catches a secret that was committed and reverted.
- Findings are redacted in both the SARIF and the step summary (`--redact`), because a run log on this public repo is readable by anyone, and a false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- `ci.yml` is otherwise unchanged from the last refresh. Two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI, the two must be kept in step by hand.
- The breaking check (`ci.yml`) is the point of the whole file, `if: github.event_name == 'pull_request'` only. Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it — true locally on a fresh clone too.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` in `ci.yml` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, gated on `github.event_name == 'push'`.
- Permissions are least-privilege and deliberate in both files: `contents: read` at the top of each; `publish-ts` alone adds `packages: write`, and `security.yml` never needs more than `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group, so a scheduled scan and a push-triggered one can run side by side.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed here (no Actions runner, and `security.yml`'s gitleaks download is a release-binary fetch not exercised in this sandbox).
