# Neurons · .github

refreshed 2026-10-15 · 37e79eff8520

- Two workflows: `ci.yml` (lint, breaking, gen-is-current, go build, tsc, then `publish-ts`) and `security.yml` (gitleaks secret scan) — both read as sound on this checkout.
- `ci.yml`'s breaking check only runs `if: github.event_name == 'pull_request'` and first does `git fetch --no-tags origin main:main`, because `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref — without that fetch `buf breaking --against '.git#branch=main'` can't resolve `main`.
- `ci.yml`'s "generated code is current" step runs `buf generate` then `git diff --exit-code --stat gen/` — this is the actual enforcement of "`gen/` is committed, not fetched at build time"; a PR with a stale `gen/` fails CI even if the proto itself is fine.
- `publish-ts` only runs `if: github.event_name == 'push'` (not on PRs) and `needs: check` — so merging to `main` always publishes a canary (`0.0.0-canary.<sha12>`) to GitHub Packages scope `@tactical-agent-neural-knowledge`; a `v*` tag publishes a real semver release instead. Merging to `main` is already a publish, not a passive event.
- `security.yml` is deliberately **inlined**, not a reusable-workflow call, because this repo is public and the sibling `workflows` repo is private — GitHub refuses a reusable workflow from a private repo to a public caller before scheduling any job, producing a silent zero-second failure with no log. The rules are duplicated here on purpose; see the file's own header comment before "fixing" the duplication.
- `security.yml` runs gitleaks `8.30.1` as a downloaded release binary, not the Action, to avoid an org licence-key requirement.
- `security.yml` always scans with `--exit-code 0`; a separate `report` step parses `gitleaks.sarif` with `jq` and fails the job — "no report at all is a failure, never a pass" (`if [ ! -f gitleaks.sarif ]; then ... exit 1`). A crash in the scan step can't silently read as green.
- `security.yml` does a tree-only scan (`fetch-depth: 1`) on PRs/pushes but a full-history scan (`fetch-depth: 0`) on the weekly `17 6 * * 1` (Mon 06:17 UTC) schedule — a secret committed-then-reverted only surfaces on the weekly run.
- Findings are redacted (`--redact`) because the repo is public and the Action log is world-readable; false positives are silenced via a dated `.gitleaksignore` entry, never by dropping the check.

## Verified
- Read both workflow files in full; no commands executed specific to this area beyond the root-level buf/go checks in `.neural/neurons/root.md`.
