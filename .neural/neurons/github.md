# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now, not one: `ci.yml` (lint/breaking/gen-staleness/build/publish, unchanged in shape) and `security.yml`, new this refresh.
- `security.yml` inlines a secret scan rather than calling a reusable workflow, and the comment at the top of the file states why: this repo is **public**, the org's `workflows` repo is **private**, and GitHub refuses a reusable workflow from a private repo to a public caller before any job is even scheduled — the result is a nought-second failure with no job and no log, which is indistinguishable from a passing gate unless you go looking. The rules are reproduced here, not referenced, and the duplication is the price of being public.
- The scanner is gitleaks v8.30.1, fetched as a release binary (not the Action, which asks orgs for a licence key), and is invoked with `--exit-code 0` always — the report step, not the scanner's exit code, decides pass/fail, so a scanner crash can't silently read as clean. No SARIF file at all (`gitleaks.sarif` missing) is treated as a hard failure, never a pass.
- `security.yml` runs three ways: on every PR and push to main (tree-only scan, `fetch-depth: 1`), and on a schedule (`17 6 * * 1`, Monday 06:17 UTC) that walks full git history (`fetch-depth: 0`, `gitleaks git .`) — because a credential committed and reverted is still leaked, and in a public repo it leaked to everyone. A false positive is silenced with a dated `.gitleaksignore` entry, never by dropping the check.
- `.github/workflows/ci.yml` is still the only workflow that runs `buf`; two jobs, `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`).
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand, and `make` itself isn't even installed in this agent sandbox (see root neuron).
- The breaking check is the point of `ci.yml`: a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source" (`ci.yml:31`). It runs only `if: github.event_name == 'pull_request'`.
- Trap: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the breaking step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. Same trap applies locally on a fresh clone. `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`, not the workflow.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — the job is gated on `github.event_name == 'push'`. Publishing goes to GitHub Packages, authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}`, no external npm credential needed.
- Permissions stay least-privilege and per-job: `ci.yml` declares `contents: read` at the top and only `publish-ts` adds `packages: write`; `security.yml` declares only `contents: read` throughout, even for the upload-artifact step.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed, no output. Neither workflow file itself, nor `security.yml`'s gitleaks step, was executed here.
