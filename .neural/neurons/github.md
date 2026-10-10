# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (unchanged since the last refresh) and the new `security.yml` secret scan.
- `ci.yml` has two jobs: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). CI calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a change to the `Makefile` alone is not exercised by CI, so keep the two in step by hand.
- `.github/workflows/ci.yml:31`: the breaking check "would be a production incident in web/mobile/agent-runner, so it is caught at the source"; it runs only `if: github.event_name == 'pull_request'` and needs `git fetch --no-tags origin main:main` first, because `actions/checkout` leaves a PR on a detached merge commit with no local `main`. `fetch-depth: 0` on checkout exists purely for this.
- The staleness gate is `buf generate` then `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a buf/plugin version other than the pins in `buf.gen.yaml` will trip it.
- `security.yml` exists only because this repo is **public** and the org's reusable `workflows` repo is **private** — GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled, so the gate had been a nought-second failure with no log on every push since it was adopted. The fix was to inline the rules rather than call them; the file's header comment says this duplication is "the price of this repository being public."
- `security.yml` runs gitleaks (pinned release binary, not the Action, to avoid a licence-key prompt) on `pull_request`, `push` to main, a weekly `schedule` (Mon 06:17 UTC, full `git` history scan because "a credential committed and reverted is still a credential that leaked"), and `workflow_dispatch`. Non-schedule runs scan the working tree only (`fetch-depth: 1`).
- The scan itself always exits 0 (`--exit-code 0`); the separate `report` step (`if: always()`) decides pass/fail by reading the SARIF and failing if findings > 0 **or** if the SARIF file is missing at all — "an unknown result is a failure, never a pass." Findings are redacted in the log because the repo is public and readable by everyone.
- A false positive in the secret scan is silenced with a dated entry in `.gitleaksignore`, never by dropping the check (per the workflow's own comment).
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — gated on `github.event_name == 'push'`.
- Publishing targets GitHub Packages (`registry-url: https://npm.pkg.github.com`, scope `@tactical-agent-neural-knowledge`, `npm publish --access restricted`), authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential needed.
- Permissions are least-privilege: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read`.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group of its own.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks from `ci.yml` that are reproducible outside Actions; both passed. Neither workflow was executed directly.
