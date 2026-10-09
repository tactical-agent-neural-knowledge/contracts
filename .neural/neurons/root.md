# Neurons · .
refreshed 2026-10-09T15:24:11Z · e52a377a71d9

- This repo is only `proto/` + generated `gen/`: Go module `github.com/tactical-agent-neural-knowledge/contracts` (go.mod), npm package `@tactical-agent-neural-knowledge/contracts` (gen/ts/package.json). No server code lives here.
- `buf.gen.yaml` managed mode sets `go_package` for every file from `go_package_prefix` + the proto path; an explicit `option go_package = ...` in a .proto (books, billing, canvas, catalog, monitor, platform, remediation, security, topo) is redundant but harmless — don't copy it into new domains, managed mode already does it.
- `make check` = `lint gen build` + `git diff --exit-code --stat gen/`: it fails if `gen/` is stale after a fresh `buf generate`, so always run `make gen` and commit the diff after touching any `.proto`.
- `make breaking` runs `buf breaking --against '.git#branch=main'`; CI only runs it on pull_request (ci.yml `breaking change check` step) and needs `git fetch origin main:main` first because checkout leaves no local `main` ref.
- `buf.yaml` lints with `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (package names are `tank.<domain>.v1`, not `tank.<domain>v1`), and breaking-detects at `FILE` granularity.
- Hard rule from CLAUDE.md: never renumber/reuse a field number, never remove a field before every client shipped without it, never hand-edit `gen/`, never bump a plugin version in `buf.gen.yaml` without regenerating everything in the same PR.
- Decided, not up for debate (CLAUDE.md): wire names stay neutral — `Channel` not `Tread`, `TreadGoal`/`TreadPlan` are the only product-named wire types and that's deliberate (see channel.proto comments); one package per domain, suffix `v1`; `gen/` is committed, never fetched at build time.
- `gen/ts` is a real npm package built with `tsc -p tsconfig.json`; CI publishes it from `publish-ts` on every push to main (canary `0.0.0-canary.<sha12>`) and on `v*` tags (the tag's semver), to GitHub Packages.
- README.md's package table is the fastest map from a wire package (`tank.auth.v1`, `tank.admin.v1`, ...) to what it covers — read it before grepping `proto/` for a feature.
- `.gitleaksignore` doesn't exist yet; if gitleaks ever flags a false positive in this repo, add a dated entry there rather than touching `.github/workflows/security.yml`.

## Verified
- `buf lint` (clean)
