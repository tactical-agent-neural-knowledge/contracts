# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now, not one: `ci.yml` (`check` + `publish-ts`) and `security.yml` (the secret scan), added this cycle.
- `ci.yml` calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it (same applies locally on a fresh clone). `fetch-depth: 0` exists purely for this comparison.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` against GitHub Packages. PRs never publish (`if: github.event_name == 'push'`, `needs: check`).
- `security.yml:1-18` is a documented workaround, not a reusable call: this repo is public and the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow from a private repo to a public caller *before any job is scheduled* — a nought-second failure with no job and no log. It had been failing on every push silently, "red forever, scanning nothing, and indistinguishable from a gate that is working" (`security.yml:9-10`). The fix was to inline the rules rather than reference them; keep both copies in step by hand if `workflows/.github/workflows/secret-scan.yml` ever changes.
- gitleaks is fetched as a pinned release binary (`VERSION: "8.30.1"`, `gitleaks_${VERSION}_linux_x64.tar.gz`), not the Action — the Action requires an org licence key this repo doesn't have.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step is what decides pass/fail by reading `gitleaks.sarif` with `jq`. A missing report file is treated as a failure, never a pass (`security.yml:67-69`) — the scanner crashing silently must not look like a clean run.
- Findings are redacted (`--redact`) because a run log is readable by anyone who can read this repo, and the repo is public. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check (`security.yml:80-81`).
- Trigger-dependent depth: `fetch-depth: ${{ github.event_name == 'schedule' && 0 || 1 }}` — the weekly cron (`17 6 * * 1`, Monday) walks full git history because "a credential committed and reverted is still a credential that leaked" in a public repo; PR/push scans only the working tree.
- Both workflows declare `contents: read` and add nothing beyond it except `publish-ts`'s `packages: write` — least-privilege, checked per job not per workflow.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; `gitleaks` is not installed in this sandbox.
