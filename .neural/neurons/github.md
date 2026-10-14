# Neurons · .github

refreshed 2026-10-14 · 3b1cc8caafe7

- Two workflows now: `ci.yml` (`check` + `publish-ts`, unchanged in shape since 2026-10-03) and the new `security.yml` (secret scanning). Both call `buf`/`gitleaks` directly, never `make` — a `Makefile`-only change is exercised by neither.
- `security.yml` runs gitleaks on every PR, every push to main, and a weekly full-history scan (Monday 06:17 UTC cron) — the history scan exists because "a credential committed and reverted is still a credential that leaked," and in a public repo it leaked to everybody.
- `security.yml`'s own header comment is the load-bearing fact: its rules are copy-pasted from a private `workflows` repo's reusable workflow, not called via `uses:`, because GitHub refuses a reusable workflow from a private repo to a public caller — that silent refusal was "red forever, scanning nothing" on every push until someone inlined it. If `workflows/.github/workflows/secret-scan.yml` changes, this file has to be hand-updated to match; there is no mechanism that keeps them in sync.
- The scanner (`gitleaks dir .` for PRs/push, `gitleaks git .` for the weekly cron) always exits 0; the separate `report` step reads `gitleaks.sarif` and decides pass/fail itself. No SARIF file at all is treated as a failure, never a pass — a crashed scanner must not look like a clean one.
- Findings are redacted (`--redact`) in both the log and the SARIF, because this repo is public and a run log is readable by anyone.
- `ci.yml`'s breaking check is still the point of the whole file (`buf breaking --against ".git#branch=main"`, PRs only) and still needs the explicit `git fetch --no-tags origin main:main` first — `actions/checkout` leaves a PR on a detached commit with no local `main` ref.
- `actions/checkout@v4` is `fetch-depth: 0` in `ci.yml` purely for the breaking check's history; `security.yml` instead varies `fetch-depth` per trigger (0 only on the scheduled history scan, 1 otherwise) since a tree scan needs no history at all.
- `publish-ts` is unchanged: canary (`0.0.0-canary.$SHA`) on push to main, real semver on `v*` tags, to GitHub Packages, gated on `github.event_name == 'push'` so PRs never publish.
- Permissions stay least-privilege and are now split across two files: `ci.yml` declares `contents: read` (plus `packages: write` on `publish-ts` only); `security.yml` declares only `contents: read`, no write permission anywhere in it.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` is `ci.yml` only; `security.yml` has no concurrency group, so overlapping PR pushes can run two scans at once.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow, including `security.yml`'s gitleaks step, was executed here.
