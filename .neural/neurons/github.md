# Neurons · .github
refreshed 2026-10-09T15:24:11Z · e52a377a71d9

- `ci.yml` `check` job is the whole contract: `buf lint` → `buf breaking` (PRs only) → `buf generate` + `git diff --exit-code --stat gen/` (gen must already be committed current) → `go build ./...` → `npm install && npm run build` in `gen/ts`.
- `publish-ts` only runs `if: github.event_name == 'push'` (main or a `v*` tag), after `check` passes; it bumps `gen/ts/package.json`'s version itself (`npm version --no-git-tag-version`), never edit that version by hand.
- Canary versions are `0.0.0-canary.<first 12 chars of GITHUB_SHA>`, published with npm dist-tag `canary`; tag pushes (`v*`) strip the leading `v` and publish as `latest`.
- `security.yml` (gitleaks) is a full copy of `workflows/.github/workflows/secret-scan.yml`, not a reusable-workflow call — GitHub refuses a reusable workflow from a private repo (`workflows`) into a public caller (this repo), which failed silently (0-second run, no job, no log) until someone noticed. If `workflows/`'s secret-scan rules change, this file has to be hand-synced; there is no automation keeping them aligned.
- gitleaks always exits 0 from the `scan` step; the separate `report` step is what fails the job (reads `gitleaks.sarif`, fails if the file is missing *or* if findings > 0). A missing sarif is treated as a failure, not a pass — don't "fix" a red run by making the scan step tolerant of errors.
- Only the Monday 06:17 UTC `schedule` trigger does a full-history gitleaks scan (`fetch-depth: 0`); `pull_request`/`push` runs scan only the working tree (`fetch-depth: 1`) for speed.
- A real secret ignore goes in `.gitleaksignore` with a dated entry — per security.yml's own comment, it must never be silenced by weakening the workflow.
- `ci.yml` pins `node-version: 24` for both the typecheck and publish steps; `go-version-file: go.mod` keeps Go version in sync with the repo's own `go.mod` (currently go 1.26) instead of a hardcoded version in the workflow.

## Verified
- (no runnable check for this area from this sandbox — reviewed ci.yml/security.yml by reading; buf lint for the repo's proto half passed, see root.md)
