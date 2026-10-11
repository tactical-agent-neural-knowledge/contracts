# Neurons · .github

refreshed 2026-10-11 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (unchanged this round — `check` + `publish-ts`) and the new `security.yml`, which runs the secret scan (gitleaks) on PR, push to main, a weekly full-history cron (Monday 06:17 UTC), and `workflow_dispatch`.
- `security.yml`'s own header comment explains why it's a ~90-line inlined workflow instead of a one-line `uses:` reference to a shared one: this repo is **public**, the org's shared `workflows` repo is **private**, and GitHub refuses a reusable workflow call from private to public *before scheduling a job* — so the call was a nought-second failure with no log, red on every push since the gate was adopted, indistinguishable from a working gate. The rules are reproduced here by hand and must be kept in step with `workflows/.github/workflows/secret-scan.yml` manually; there is no dependency that would catch drift.
- `security.yml` trap for anyone re-pinning gitleaks: it's fetched as a raw release binary from `github.com/gitleaks/gitleaks/releases`, not the `gitleaks/gitleaks-action`, specifically because the Action gates organisations behind a licence key. Version is pinned in `env.VERSION` at the top of the job, not in a tag reference.
- `security.yml`'s scan step always exits 0 (`--exit-code 0`); the separate `report` step (`if: always()`) is what actually fails the job, by reading the SARIF and checking the finding count. A missing SARIF file is itself a hard failure (`::error::gitleaks produced no report`) — a crashed scanner must never read as a clean one.
- `security.yml` redacts every finding (`--redact`) because this repo and its Actions logs are both public; a real secret found here still means rotate-then-purge, documented in the job summary itself, not a note anyone has to go find.
- `ci.yml` is still the only workflow that calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a `Makefile`-only change is still not exercised by CI.
- The breaking check (`ci.yml:31`) is still PR-only, still needs the three-line `git fetch --no-tags origin main:main` dance before `buf breaking --against ".git#branch=main"` can see `main` (actions/checkout leaves PRs on a detached merge commit), and `fetch-depth: 0` is there purely for this comparison.
- The staleness gate is still `buf generate` + `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` — this round added 2363 lines of hand-written `.proto` and ~45,500 lines of generated code in the same commits, so a partial regen (one language but not all three) would have tripped this immediately.
- `go-version-file: go.mod` for `actions/setup-go@v5`, `npm run build` in `gen/ts` on node 24 for the TS check (a tsc compile only, no tests) — both unchanged.
- `publish-ts` is still push-only (`v*` tags → semver/`latest`, push to main → `0.0.0-canary.${GITHUB_SHA::12}`/`canary`), authenticated with the ambient `github.token`, `packages: write` scoped to just that job.
- `concurrency: group: ci-${{ github.ref }}` + `cancel-in-progress: true` on `ci.yml` only — `security.yml` has no concurrency group, so a scheduled run and a push-triggered run of the secret scan can overlap; that's fine since it only reads the tree.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. `security.yml`'s gitleaks scan was not run here (no network fetch of the release binary attempted); neither workflow was executed by Actions.
