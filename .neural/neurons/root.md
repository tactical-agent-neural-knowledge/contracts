# Neurons · .
refreshed 2026-10-07 · d58208d52ddc

- This repo is only the wire contract: `proto/` in, `gen/go` + `gen/ts` + `gen/python` out, committed on purpose — never hand-edit `gen/` (Makefile:20, CLAUDE.md).
- `make check` (Makefile:24) is exactly what CI runs: lint, gen, build, then a `git diff --exit-code --stat gen/` — a PR fails if generated code is stale, so always run `make gen` after touching any `.proto` and commit the diff.
- `make breaking` (Makefile:14-15) runs `buf breaking --against '.git#branch=main'`; CI only runs it on pull_request events, so a direct push to main skips it — don't rely on CI to catch a wire break outside a PR.
- `buf.yaml` lints with `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (buf.yaml:6-8) and breaking-checks at `FILE` granularity (buf.yaml:9-11) — field renumbering across any file is a breaking-check failure, not just a style nit.
- Plugin versions are pinned in `buf.gen.yaml` (protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3, python 29.3); bumping one without regenerating everything in the same PR is a hard prohibition (CLAUDE.md).
- `go.mod` requires Go 1.26 and pins `connectrpc.com/connect v1.18.1` / `google.golang.org/protobuf v1.36.4` to match `buf.gen.yaml` exactly — these two must move together.
- No `.proto` file in this repo uses `reserved` yet (checked via grep) — when a field is finally removed after every client ships without it, add the `reserved` number/name instead of letting a number go silently unused.
- Wire names stay neutral — `Channel` not `Tread`, `Board` not whatever the product calls it elsewhere — product vocabulary belongs in the clients only (CLAUDE.md, README.md).
- One proto package per domain with a `v1` suffix (`tank.<domain>.v1`); `README.md`'s package table is the map of what lives where and is usually faster to check than grepping `proto/`.
- Changes are additive-first: add the field, ship every consumer (Go `api`/`agent-control`, TS `sdk-ts`/`web`/`mobile`/`agent-runner`, Python `knowledge`), then remove — never remove a field before every client has shipped without it (README.md:25, CLAUDE.md).
- `gen/ts` publishes to GitHub Packages as `@tactical-agent-neural-knowledge/contracts`: canary (`0.0.0-canary.<sha12>`) on every push to main, real semver on `v*` tags (.github/workflows/ci.yml:68-75).

## Verified
- `make lint` (buf lint via npx @bufbuild/buf)
