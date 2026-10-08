# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- Two workflows now: `ci.yml` (check + publish-ts, unchanged this refresh) and the new `security.yml` (secret scanning). Both are gated the same way: `permissions: contents: read` at top, a per-ref `concurrency` group with `cancel-in-progress: true`.
- `ci.yml`'s `check` job (PRs, main, `v*` tags) runs `buf lint`, `buf breaking` (PRs only, after `git fetch --no-tags origin main:main` since checkout leaves a detached merge commit), `buf generate` + `git diff --exit-code --stat gen/` (the staleness gate), `go build ./...`, then a `gen/ts` tsc compile on node 24. `publish-ts` (`needs: check`, push only) versions with `npm version --no-git-tag-version` and publishes to GitHub Packages: `0.0.0-canary.${GITHUB_SHA::12}` under `canary` on main, `${GITHUB_REF_NAME#v}` under `latest` on a `v*` tag.
- `security.yml`'s header comment is load-bearing, read it before touching the file: this repo is **public**, a sibling `workflows` repo is **private**, and GitHub refuses a reusable workflow call from private to public *before any job is scheduled* — the failure is a nought-second run with no job and no log. So `security.yml` duplicates `workflows/.github/workflows/secret-scan.yml`'s rules by hand rather than calling it; the duplication is deliberate and is the cost of being public. Keep both in step by hand if either changes.
- `security.yml` runs gitleaks (pinned version in `env.VERSION`, fetched as a release tarball, never the Action — the Action asks orgs for a licence key) on three triggers: PR and push-to-main do a tree scan (`gitleaks dir .`, `fetch-depth: 1`), the Monday 06:17 UTC cron does a full history scan (`gitleaks git .`, `fetch-depth: 0`) because a committed-then-reverted credential in a public repo already leaked to everybody.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step (`if: always()`) is what decides pass/fail by counting `.runs[].results[]` in the SARIF — a crash in the scan step must not read as a clean scan, and no SARIF file at all is treated as a failure (`::error::gitleaks produced no report`), never a silent pass.
- Findings are always `--redact`ed, in both the SARIF and the step summary: this repo is public and a run log is readable by anyone. A false positive is silenced with a dated `.gitleaksignore` entry, never by removing or weakening this check.
- `publish-ts` publishes `@tactical-agent-neural-knowledge/contracts` authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed; `security.yml` needs no credential either, since gitleaks is a release binary, not an Action requiring a licence key.
- `actions/checkout@v4` with `fetch-depth: 0` is required in two unrelated places for two different reasons: `ci.yml`'s breaking check needs `main` reachable, `security.yml`'s scheduled scan needs full history to walk.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks from `ci.yml` reproducible outside Actions; both passed. Neither workflow file itself was executed (no gitleaks binary fetch, no Actions runner here).
