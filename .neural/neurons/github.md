# Neurons · .github

refreshed 2026-10-09 · e52a377a71d9

- Two workflows now: `ci.yml` (lint/breaking/gen-is-current/build/tsc, unchanged in shape since the last
  refresh) and `security.yml`, added since then — the secret scan.
- `security.yml` exists as a standalone file, not a call to the org's shared `workflows` repo, because
  this repo is **public** and `workflows` is **private** — GitHub refuses a reusable workflow from a
  private repo to a public caller before any job is scheduled, which showed up as a nought-second run with
  no job and no log. It had been silently red on every push since the gate was adopted. The workflow's own
  top comment says the duplication is the price of being public; do not "simplify" it back into a call to
  the shared workflow without checking that restriction still holds.
- `security.yml` gitleaks rules that must not drift (from the file's own comment): gitleaks is pinned and
  fetched as a release binary, not the Action, because the Action asks orgs for a licence key; findings
  are redacted in the log and summary because this repo is public and any reader can see CI output; the
  scanner is always invoked with `--exit-code 0` and the separate `report` step decides pass/fail, so a
  gitleaks crash can't masquerade as "no findings"; and a missing `gitleaks.sarif` is itself a failure —
  "no report at all is a failure, never a pass."
- `security.yml` runs three ways: on every PR and push to `main` as a tree scan (`fetch-depth: 1`,
  `gitleaks dir .`), and weekly (Monday 06:17 UTC cron) as a full history scan (`fetch-depth: 0`,
  `gitleaks git .`) — "a credential committed and reverted is still a credential that leaked."
- A false positive is silenced with a dated entry in `.gitleaksignore` (not present in the repo yet, so
  there have been none), never by weakening or dropping the step.
- `ci.yml`'s breaking-check comment still applies: `actions/checkout` leaves PRs on a detached merge
  commit with no local `main` ref, so it runs `git fetch --no-tags origin main:main` before `buf breaking`.
- `publish-ts` is unchanged: canary (`0.0.0-canary.<sha12>`) on every push to `main`, real semver on a
  `v*` tag, both gated on `check` passing first.

## Verified
- Read both workflow files in full; no YAML tooling invoked (no lint config targets `.github/`).
