# Neurons · .github

refreshed 2026-10-07 · 572da952c512

- Two workflows now: `ci.yml` (lint/breaking/build/publish, unchanged this refresh) and a new `security.yml` that runs a single reusable job.
- `security.yml` triggers on `pull_request`, `push` to `main`, and `workflow_dispatch`, and declares only `contents: read` — it has no jobs of its own, just a `secrets` job that calls `uses: tactical-agent-neural-knowledge/workflows/.github/workflows/secret-scan.yml@main`.
- That reusable workflow lives in a different repository (`tactical-agent-neural-knowledge/workflows`) pinned to its `@main`, not a tag or SHA — a breaking change there changes this repo's CI without a commit here. Recent repo history (`ci: narrow the security workflow to one scanner while the call is diagnosed`) shows it was cut back from more scanners/jobs after failures; the full intended shape is not yet in this file.
- `ci.yml` is still the only workflow that gates merges in practice: `check` (PRs, main, `v*` tags) and `publish-ts` (pushes only, `needs: check`). `security.yml`'s `secrets` job is not referenced by `ci.yml` and branch-protection status isn't visible from this repo, so whether it actually blocks a merge can't be confirmed by reading the file.
- CI calls `buf` directly from `bufbuild/buf-setup-action@v1`, never `make`. A change to the `Makefile` alone is therefore not exercised by CI — the two must be kept in step by hand.
- The breaking check is the point of `ci.yml`: `.github/workflows/ci.yml:31` says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish, because the job is gated on `github.event_name == 'push'`.
- Publishing goes to GitHub Packages (`registry-url: https://npm.pkg.github.com`, `scope: "@tactical-agent-neural-knowledge"`, `npm publish --access restricted`) authenticated with `NODE_AUTH_TOKEN: ${{ github.token }}` — no external npm credential exists or is needed.
- `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` on `ci.yml` — a second push to the same ref kills the first run, including a half-finished publish. `security.yml` has no concurrency group.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two `ci.yml` checks reproducible outside Actions; both passed. Neither workflow file itself was executed (the `secret-scan.yml` reusable workflow is in another repository and unreachable from here).
