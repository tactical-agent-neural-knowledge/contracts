# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now, not one: `ci.yml` (buf lint/breaking/gen-staleness, go build, tsc, npm publish) and the new `security.yml` (secret scanning). They are independent — `security.yml` does not gate `ci.yml` or vice versa.
- `ci.yml` is unchanged this cycle. Two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is not exercised by CI and the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: a wire break "would be a production incident in web/mobile/agent-runner, so it is caught at the source" (`ci.yml:31`). It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. Same on a fresh local clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. Gated on `github.event_name == 'push'`, so PRs never publish.
- `security.yml` is inlined rather than calling a reusable workflow in the private `workflows` repo, because GitHub refuses a reusable workflow from a private repo into a public caller before any job is scheduled — the failure mode was a nought-second run with no job and no log, silently red on every push until noticed. The rules are reproduced by hand and must not drift from `workflows/.github/workflows/secret-scan.yml`.
- `security.yml` fetches gitleaks as a pinned release binary (`VERSION: "8.30.1"`), never the Action, because the Action asks organizations for a licence key. Findings are redacted in the job summary and log since this repo is public and readable by anyone.
- Scan depth depends on trigger: `fetch-depth: ${{ github.event_name == 'schedule' && 0 || 1 }}` — the Monday 06:17 UTC cron walks full git history (a reverted secret still leaked), PR/push runs scan only the working tree.
- `security.yml` always runs gitleaks with `--exit-code 0`; the `report` step, not the scanner, decides pass/fail by reading `gitleaks.sarif` with `jq`. Missing `gitleaks.sarif` is itself a failure ("an unknown result is a failure, never a pass") — a crash cannot silently pass as a clean scan.
- A false positive in `security.yml` is silenced with a dated entry in `.gitleaksignore`, never by weakening the `exit-code` check; there is no `.gitleaksignore` in the repo yet.
- Permissions are least-privilege: both workflows declare `contents: read` at the top; only `ci.yml`'s `publish-ts` adds `packages: write`. `ci.yml` has `concurrency: group: ci-${{ github.ref }}` / `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file nor `security.yml`'s gitleaks step was executed here.
