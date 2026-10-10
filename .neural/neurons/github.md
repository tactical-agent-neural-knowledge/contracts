# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen/build/tsc, then publish) and `security.yml` (secret scanning), added this refresh window.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source". It runs only `if: github.event_name == 'pull_request'`, and `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it — same trap locally on a fresh clone.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.`
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. Publishes to GitHub Packages with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed. `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` means a second push to the same ref kills a half-finished publish.
- `security.yml` is the secret scan, and it is *inlined* rather than calling a shared `workflows/.github/workflows/secret-scan.yml` — the comment at the top of the file explains why: this repo is public, the shared workflow lives in a private repo, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled. The gate had been red on every push since adoption (nought-second failure, no job, no log) until `b57522e` inlined the rules.
- `security.yml` runs gitleaks fetched as a pinned release binary (`VERSION: "8.30.1"`), never the Action, because the Action asks for an organisation licence key. Findings are always redacted (`--redact`) because the log is world-readable on a public repo.
- The scanner is invoked with `--exit-code 0` always, and a separate `report` step (`if: always()`) decides pass/fail by counting SARIF results — a crashed scanner producing no `gitleaks.sarif` is itself treated as a failure (`::error::gitleaks produced no report — an unknown result is a failure, never a pass`), never silently as a pass.
- Tree scan (`gitleaks dir`, `fetch-depth: 1`) on push/PR/dispatch; full history scan (`gitleaks git`, `fetch-depth: 0`) only on the Monday 06:17 UTC cron — a credential committed and reverted is still leaked in a public repo's history.
- A false positive is silenced with a dated entry in `.gitleaksignore`, never by dropping the check — stated directly in the step summary output.
- Permissions are least-privilege: `ci.yml` declares `contents: read` at top, `publish-ts` alone adds `packages: write`; `security.yml` is `contents: read` only, even though it uploads a SARIF artifact.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow was executed here (no Actions runner, no gitleaks binary fetch attempted).
