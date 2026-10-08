# Neurons · .
refreshed 2026-10-08 · e52a377a71d9

- This repo is the wire contract only: `proto/tank/<domain>/v1/*.proto` in, generated Go/TS/Python under `gen/` committed on purpose — never hand-edit `gen/`, run `make gen`.
- `make check` (`Makefile:24`) is exactly what CI's `check` job runs: lint, gen, go build, then fails if `gen/` is stale vs. the committed tree.
- `make breaking` (`Makefile:14`) compares against `.git#branch=main`; CI only runs it on PRs (`ci.yml:35`) after materializing a local `main` ref via `git fetch origin main:main`, since `actions/checkout` leaves PRs on a detached merge commit.
- `buf.gen.yaml` pins remote plugins per-language: protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3, python 29.3 — bumping any one requires regenerating everything in the same PR (hard prohibition in `CLAUDE.md`).
- `buf.yaml` lints with `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (package names are `tank.<domain>.v1`, suffix is already in the path) and breaking-checks at `FILE` granularity.
- Go module is `github.com/tactical-agent-neural-knowledge/contracts` (`go.mod:1`), go 1.26; `gen/go` is consumed by `api` and `agent-control` as a dependency, not this repo's own build target beyond `go build ./...`.
- `gen/ts` publishes to GitHub Packages as `@tactical-agent-neural-knowledge/contracts`: canary version `0.0.0-canary.<12-char-sha>` on every push to `main`, real semver on `v*` tags (`ci.yml:68-75`).
- Hard prohibitions (`CLAUDE.md`): no renumbering/reusing field numbers, no removing a field before every client has shipped without it, no hand-editing `gen/`, no silent plugin-version bumps.
- Decided and not up for re-litigation: wire names stay neutral (`Channel` not `Tread`, product vocabulary lives in clients only); one proto package per domain; generated code is committed, never fetched at build time.
- README's package table (`README.md:8-20`) is the fastest map from domain name to what it actually covers — check it before grepping 26 proto files for the right one.

## Verified
- `make lint` (buf lint via `npx @bufbuild/buf`)
