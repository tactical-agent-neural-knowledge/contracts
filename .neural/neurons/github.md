# Neurons · .github
refreshed 2026-10-08 · e52a377a71d9

- `ci.yml`'s `check` job is the only required gate for PRs: buf lint → breaking (PRs only) → regenerate and diff `gen/` for staleness → `go build ./...` → `gen/ts` tsc build.
- `publish-ts` only runs on `push` (not PRs) and `needs: check`; it versions canary (`0.0.0-canary.<sha12>`) on `main` or real semver on `v*` tags before `npm publish --tag canary|latest` (`ci.yml:68-81`).
- `security.yml` is a secret scan **inlined rather than called** from a reusable workflow: this repo is public and the org's `workflows` repo is private, and GitHub refuses a private reusable workflow to a public caller before any job is scheduled — a silent, logless nought-second failure. The duplication here is deliberate; keep it in sync with `workflows/.github/workflows/secret-scan.yml` by hand.
- gitleaks is fetched as a pinned release binary (`VERSION: 8.30.1`), not the Action, because the Action asks orgs for a licence key.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step is what actually fails the job by counting `.runs[].results` in the sarif. A missing sarif file is itself treated as a failure ("an unknown result is a failure, never a pass") — don't "fix" a crash by making the report step skip when the file is absent.
- Tree scan (`gitleaks dir .`) runs on PR/push; full-history scan (`gitleaks git .`) runs only on the Monday 06:17 UTC cron, because a credential committed-then-reverted is still leaked in a public repo.
- False positives are silenced with a dated entry in `.gitleaksignore`, never by disabling or weakening this workflow.
- Both workflows set `permissions: contents: read` at the top level; `publish-ts` escalates only its own job to `packages: write`.

## Verified
- (yaml-only area; no lint/build command applies — read for correctness against the comments' own stated invariants)
