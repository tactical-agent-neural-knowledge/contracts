# Neurons · .github

refreshed 2026-10-14 · 3b1cc8caafe7

- Two workflows now: `ci.yml` (unchanged since the last refresh — lint/breaking/gen-staleness/build/tsc, and npm publish) and the new `security.yml` (secret scanning).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. Publishing goes to GitHub Packages, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed.
- `security.yml` is a secret scan with gitleaks, *inlined* rather than called as a reusable workflow: the file's own header comment explains that a private `workflows` repo cannot be called by this public repo's reusable-workflow syntax (GitHub refuses it before any job is scheduled), so every push failed silently — "red forever, scanning nothing" — until the rules were copied in directly. If this repo's security gate ever needs to change, the source of truth to check against is `workflows/.github/workflows/secret-scan.yml`, and the two must be kept in step by hand, same as `ci.yml` vs `Makefile`.
- `security.yml` triggers are `pull_request`, `push: [main]`, a weekly `schedule` (Monday 06:17 UTC), and `workflow_dispatch`. Only the scheduled run does a full-history scan (`gitleaks git .` with `fetch-depth: 0`); PR/push runs are tree-only (`gitleaks dir .`, `fetch-depth: 1`) — a secret committed-then-reverted is only caught by the weekly run, because this repo is public and "leaked once" means "leaked to everybody".
- `security.yml`'s scan step always exits 0; the separate `report` step reads `gitleaks.sarif` and decides pass/fail. No report file at all is treated as a failure (`::error::gitleaks produced no report`), never as a pass — a crash in the scan step cannot silently look clean.
- Findings are redacted in both the log and the step summary (`--redact`), because this is a public repository and a run log is as public as the code. A false positive is silenced with a dated `.gitleaksignore` entry, never by disabling the check.
- Permissions are least-privilege and deliberate: `ci.yml` declares `contents: read` at the top, and only `publish-ts` adds `packages: write`; `security.yml` only ever declares `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow was executed here (no `gitleaks` binary fetched, no Actions runner).
