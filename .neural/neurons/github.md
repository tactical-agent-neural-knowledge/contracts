# Neurons · .github

refreshed 2026-10-10 · e52a377a71d9

- Two workflows now: `ci.yml` (buf lint/breaking/gen-check/build/tsc) and `security.yml` (gitleaks secret scan), added this cycle. `ci.yml` still calls `buf` directly via `bufbuild/buf-setup-action@v1`, never `make` — a Makefile-only change is not exercised by CI.
- `security.yml` is the whole secret-scan workflow of another, private repo (`workflows`) copied in by hand, not referenced — its own header comment explains why: a public repo cannot call a reusable workflow hosted in a private one (GitHub refuses it before any job is scheduled, a nought-second failure with no log). The duplication is deliberate and "the price of this repository being public"; drift between the two copies is a real risk the comment calls out.
- `security.yml` rules that must not drift (per its own header): gitleaks is pinned and fetched as a release binary, never the Action (orgs need a licence key for that); findings are redacted since the run log is public; the scanner always exits 0 and the `report` step decides, so a crash can't masquerade as a clean scan; **no report at all is a failure, never a pass**.
- `security.yml` scans the working tree (`fetch-depth: 1`) on every push/PR, and the full git history (`fetch-depth: 0`, `gitleaks git .`) only on the Monday 06:17 UTC cron — "a credential committed and reverted is still a credential that leaked... in a public repository it leaked to everybody."
- A gitleaks false positive is silenced with a dated entry in `.gitleaksignore`, never by dropping the check — stated directly in `security.yml`'s report step.
- The breaking check is the point of `ci.yml`: line 31 says a wire break here "would be a production incident in web/mobile/agent-runner, so it is caught at the source." It runs only `if: github.event_name == 'pull_request'`.
- Trap, and the reason the step has three lines instead of one: `actions/checkout` leaves a PR on a detached merge commit with no local `main`, so the step must `git fetch --no-tags origin main:main` before `buf breaking --against ".git#branch=main"` can read it. The same applies locally on a fresh clone.
- `actions/checkout@v4` is pinned to `fetch-depth: 0` in `ci.yml` purely so the breaking check has history; shallowing it breaks the comparison, not the build.
- The staleness gate is `buf generate` followed by `git diff --exit-code --stat gen/`, failing with `::error::gen/ is stale. Run 'make gen' and commit the result.` Regenerating with a different buf or plugin version than the pins in `buf.gen.yaml` will trip it.
- The Go version is never written in `ci.yml`: `actions/setup-go@v5` takes `go-version-file: go.mod`, so bumping Go means editing `go.mod`.
- `publish-ts` versions without committing (`npm version --no-git-tag-version`): a `v*` tag publishes `${GITHUB_REF_NAME#v}` under dist-tag `latest`, a push to main publishes `0.0.0-canary.${GITHUB_SHA::12}` under `canary`. PRs never publish — gated on `github.event_name == 'push'`.
- Permissions are least-privilege and deliberate in both files: `contents: read` at the top of each, and only `ci.yml`'s `publish-ts` adds `packages: write`. `ci.yml` also sets `concurrency: group: ci-${{ github.ref }}` with `cancel-in-progress: true` — a second push to the same ref kills the first run, including a half-finished publish.

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — the two checks `ci.yml` runs that can be reproduced outside Actions; both passed. Neither workflow itself was executed (no Actions runner here).
