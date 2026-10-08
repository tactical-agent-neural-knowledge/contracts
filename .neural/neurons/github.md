# Neurons · .github

refreshed 2026-10-08 · a887d51f4d82

- `.github/workflows/ci.yml` `check` job is the whole CI contract in one job: `buf lint` → `buf breaking --against ".git#branch=main"` (PRs only) → regenerate and diff `gen/` → `go build ./...` → `npm install && npm run build` in `gen/ts`. `fetch-depth: 0` on checkout is required so buf has `main` to diff against; the breaking step additionally does `git fetch --no-tags origin main:main` because a PR's checkout leaves a detached merge commit with no local `main` ref.
- `publish-ts` (push to `main` or a `v*` tag) runs only after `check` passes (`needs: check`) and only on `push`, never on `pull_request`. It versions `gen/ts` with `npm version --no-git-tag-version`: `0.0.0-canary.<12-char sha>` on `main`, the tag's own semver (`v1.2.3` → `1.2.3`) on a `v*` tag, then `npm publish` to GitHub Packages (`registry-url: npm.pkg.github.com`, scope `@tactical-agent-neural-knowledge`) tagged `canary` or `latest` respectively.
- `.github/workflows/security.yml` is new since the last refresh: a secret scan (gitleaks) that duplicates rather than calls a reusable workflow from the org's private `workflows` repo, because GitHub refuses a reusable workflow from a private repo to a public caller before any job is scheduled — this repo is public. The file's own header comment is the reason this duplication exists and that it must not silently drift from `workflows/.github/workflows/secret-scan.yml`.
- `security.yml` runs a tree scan (`gitleaks dir .`) on every PR and push to `main`, and a full-history scan (`gitleaks git .`, `fetch-depth: 0`) on a weekly schedule (`17 6 * * 1`, Monday). `gitleaks` is pinned (`VERSION: "8.30.1"`) and fetched as a release binary rather than via the Action, because the Action gates on an organisation licence key.
- `security.yml`'s scan step always exits 0 (`--exit-code 0`); the `report` step is what decides pass/fail by reading `gitleaks.sarif` with `jq` and failing if the finding count isn't 0 — and it fails hard if the sarif file is missing entirely, on the principle that an unknown result must never read as a pass. A false positive is silenced with a dated `.gitleaksignore` entry, never by touching this gate.
- Neither workflow needs secrets beyond the default `GITHUB_TOKEN`; `publish-ts` uses `${{ github.token }}` as `NODE_AUTH_TOKEN`, so no PAT is configured here. `permissions: contents: read` is the default on both files, with `packages: write` added only on the `publish-ts` job.
- The two workflows never call each other and have independent triggers; `ci.yml`'s `concurrency` group (`ci-${{ github.ref }}`, cancel-in-progress) has no equivalent in `security.yml`, so overlapping security scans on rapid pushes are not cancelled.

## Verified

Read both workflow files; no runnable command for `.github/` itself (`make lint`/`make check` cover `proto/` and `gen/`, not workflow YAML) — see `root.md` for the commands actually run this refresh.
