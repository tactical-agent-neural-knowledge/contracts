# Neurons · .github

refreshed 2026-10-08 · b57522e4f7aa

- Two workflows now, not one: `ci.yml` (lint/breaking/build/publish) and `security.yml` (secret scanning), added this cycle. `ci.yml` is unchanged in shape: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. Publishing goes to GitHub Packages, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed.
- `security.yml` runs gitleaks as a pinned release binary (`VERSION: "8.30.1"`, curl + tar, never the Action), because this repo is **public** and the org's reusable `workflows/.github/workflows/secret-scan.yml` is in a **private** repo — GitHub refuses a reusable workflow from private to public *before scheduling any job*, so the failure was a nought-second run with no log. The rules are reproduced by hand instead of referenced; that duplication is the documented price of being public.
- `security.yml`'s scan step always exits 0 (`--exit-code 0`); a separate `report:` step (`if: always()`) parses the SARIF and decides pass/fail. If `gitleaks.sarif` is missing, the report step fails outright — `::error::gitleaks produced no report — an unknown result is a failure, never a pass`. A crash in the scan step cannot silently read as green.
- `security.yml` scan depth depends on trigger: `HISTORY: ${{ github.event_name == 'schedule' }}` — PRs and pushes get `fetch-depth: 1` and `gitleaks dir .` (tree scan only); the Monday 06:17 UTC cron gets `fetch-depth: 0` and `gitleaks git .` (full history, because a committed-then-reverted credential already leaked in a public repo).
- A gitleaks false positive is silenced with a dated entry in `.gitleaksignore`, per the workflow's own comment — never by dropping the check.
- Permissions are least-privilege and deliberate in both workflows: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` is `contents: read` only, even for the artifact upload.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed; gitleaks itself was not run here.
