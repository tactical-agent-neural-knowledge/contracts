# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- `security.yml` is new this cycle: a secret scan via gitleaks, inlined rather than called as a reusable workflow. Its own header comment explains why — this repo is public and the org's shared `workflows` repo is private, and GitHub refuses a reusable workflow call from a private repo into a public caller before any job is even scheduled, so the shared version failed silently on every push (a nought-second run, no job, no log). The rules here are a deliberate duplicate of `workflows/.github/workflows/secret-scan.yml` and must not drift from it.
- `security.yml` runs a tree scan (`gitleaks dir`) on every PR and push to main, and a full-history scan (`gitleaks git`, `fetch-depth: 0`) on a Monday 06:17 UTC cron — a credential committed and reverted is still leaked in a public repo, hence the periodic deep scan.
- The scan step always exits 0 (`--exit-code 0`); the separate `report` step is what actually fails the job, by checking the sarif file exists and counting findings. This is deliberate: a crashed scanner must not read as "no secrets found". A missing `gitleaks.sarif` is itself treated as a failure.
- Findings are redacted in the summary and the log (`--redact`) because this is a public repo and the Action run log is world-readable. A false positive is silenced only with a dated entry in `.gitleaksignore`, never by weakening or dropping the job.
- `gitleaks` is pinned by version (`8.30.1`) and fetched as a release binary over `curl`, not via the marketplace Action — the marketplace Action now asks organisations for a licence key.
- `ci.yml`'s `check` job is the one PR gate for proto changes: `buf lint` → breaking check (PRs only, materializes `main` locally first since a PR checkout is a detached merge commit with no local `main` ref) → `buf generate` + `git diff --exit-code gen/` (gen must already be current) → `go build ./...` → `npm install && npm run build` in `gen/ts`.
- `ci.yml`'s `publish-ts` job only runs on `push` (not PRs), needs `check` to pass first, and picks the npm dist-tag from the ref: `0.0.0-canary.<12-char sha>` tagged `canary` on every push to `main`, or the tag's own version tagged `latest` on a `v*` tag.
- Both workflows set `permissions: contents: read` at the top level and grant `packages: write` only on the one job (`publish-ts`) that needs it — least privilege per job, not per workflow.

## Verified

Read-only review of both workflow files; no runnable lint/test target exists for `.github/` itself (YAML syntax is exercised by GitHub Actions on push, not locally).
