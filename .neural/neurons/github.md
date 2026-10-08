# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now: `ci.yml` (buf lint/breaking/gen/build/tsc) and `security.yml` (gitleaks secret scan). `ci.yml` is unchanged since the last refresh; `security.yml` is new.
- `security.yml`'s own header comment explains why its rules are duplicated here rather than calling a shared one: this repo is **public**, the org's reusable `workflows/.github/workflows/secret-scan.yml` is **private**, and GitHub refuses a private reusable workflow to a public caller before any job is even scheduled — a nought-second failure with no log, which had been silently red on every push since the gate was adopted.
- `security.yml` trap for whoever next touches it: `gitleaks` is fetched as a pinned release binary (`VERSION: "8.30.1"`, curl from `gitleaks/gitleaks` releases), not the Action, because the Action asks organisations for a licence key.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step is what decides pass/fail by reading `gitleaks.sarif` with `jq`. A missing SARIF file is treated as a failure (`::error::...an unknown result is a failure, never a pass`), so a crash in the scan step cannot silently pass as clean.
- `security.yml` findings are redacted in the log and step summary on purpose — a run log is readable by anyone who can read a public repo. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing the check.
- `security.yml` runs a tree scan (`gitleaks dir`, `fetch-depth: 1`) on PRs and pushes to main, and a full history scan (`gitleaks git`, `fetch-depth: 0`) on the Monday 06:17 UTC cron — because a credential committed and reverted is still leaked in a public repo's history.
- `ci.yml` is still the only workflow calling `make`-equivalent steps directly: two jobs, `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make`, so a `Makefile`-only change is not exercised by CI.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` in `ci.yml` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate in `ci.yml` is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` against GitHub Packages. PRs never publish.
- Both workflows declare `contents: read` at the top and widen only where needed: `ci.yml`'s `publish-ts` adds `packages: write`; neither needs more.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed; `security.yml`'s gitleaks step was not run here.
