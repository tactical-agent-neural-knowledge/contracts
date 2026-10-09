# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (unchanged since the last refresh — `check` on PRs/main/`v*` tags, `publish-ts` on pushes, `needs: check`) and the new `security.yml`.
- `security.yml` runs gitleaks on `pull_request`, `push: [main]`, a weekly `schedule` ("17 6 * * 1"), and `workflow_dispatch`. Tree scan (`gitleaks dir .`, `fetch-depth: 1`) on PR/push; full-history scan (`gitleaks git .`, `fetch-depth: 0`) only on the weekly cron — "a credential committed and reverted is still a credential that leaked" in a public repo (security.yml:24-26).
- Trap already hit once: `security.yml` *inlines* the gitleaks rules instead of calling the org's reusable `workflows/.github/workflows/secret-scan.yml`, because GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — that failed silently (0-second run, no job, no log) on every push since the gate was adopted. Keep the two files' rules in step by hand; there is no other way to share them.
- gitleaks is pinned (`VERSION: "8.30.1"`) and fetched as a release binary, not the Marketplace Action — the Action requires an org licence key this setup doesn't have.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step (`if: always()`) is what actually fails the job by counting `.sarif` results with `jq` — so a gitleaks crash doesn't read as a clean scan, and a missing `.sarif` file is treated as a failure, never a pass (security.yml:67-70).
- Findings are redacted (`--redact --no-banner`) because this repo is public and a run log is readable by anyone; a false positive is silenced only with a dated entry in `.gitleaksignore`, never by dropping the check.
- `ci.yml`'s breaking check remains the point of that file: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source," gated `if: github.event_name == 'pull_request'`.
- Same trap as before applies to both workflows: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the breaking-check step must `git fetch --no-tags origin main:main` first — true locally on a fresh clone too.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): `v*` tag → `${GITHUB_REF_NAME#v}` under dist-tag `latest`; push to main → `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish (`if: github.event_name == 'push'`).
- Permissions stay least-privilege and are now split across two files: `ci.yml` declares `contents: read` (only `publish-ts` adds `packages: write`); `security.yml` declares only `contents: read` — neither needs anything more.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` only; `security.yml` has no concurrency group, so a scheduled full-history scan can overlap a PR's tree scan without being cancelled.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks reproducible outside Actions; both passed. Neither workflow file itself was executed (no local Actions runner).
