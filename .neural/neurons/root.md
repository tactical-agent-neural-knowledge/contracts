# Neurons · .

refreshed 2026-11-16 · d7aa1845d1fb

- `Makefile:1` sets `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, so every target shells out to npx and needs the network on a cold cache. Use `make lint BUF=buf` when a buf binary is on PATH.
- `make check` (`Makefile:41`) runs `lint gen build`, then `git diff --exit-code --stat gen/`; that stale-generated-code gate is the one CI enforces.
- `make gen` depends on `tools` (`Makefile:23`), which installs the pinned generators into `.tools/bin/` and `.tools/node_modules/.bin/` (`Makefile:10–20`). Run `make tools` before calling `buf generate` directly.
- `buf.gen.yaml:9–13` runs every plugin locally from `.tools/`, not on buf.build: protoc-gen-go v1.36.4, protoc-gen-connect-go v1.18.1, protoc-gen-es v2.2.3, and protoc 29.3 for the Python and pyi builtins. The pins match `Makefile:3,12,14,16`.
- Generated output lands in `gen/go` (`paths=source_relative`), `gen/ts/src` (`target=ts`, `import_extension=js`) and `gen/python`. Generated sources are committed on purpose; `.gitignore` excludes only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` and `.tools/`.
- `buf.gen.yaml:3–7` enables managed mode with `go_package_prefix` `github.com/tactical-agent-neural-knowledge/contracts/gen/go`. 22 `.proto` files carry an explicit `option go_package`; all 22 match that prefix, so a drifting override would put generated code in the wrong directory.
- `buf.yaml` is v2 with one module at `proto`; `lint.use: [STANDARD]` except `PACKAGE_VERSION_SUFFIX`; `breaking.use: [FILE]`, so moving a message between files is breaking even when the wire is unchanged.
- `make breaking` (`Makefile:31–32`) runs `buf breaking --against '.git#branch=main'`, which compares against a local `main` branch.
- `CLAUDE.md` hard prohibitions: no renumbering or reusing field numbers; no removing a field before every client has shipped without it; no editing `gen/` by hand; no changing plugin versions without regenerating everything in the same PR.
- `make` is optional: each Makefile target wraps `npx --yes @bufbuild/buf` or `go`, so run those directly when make is missing.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
- `go build ./...` — passed
- `go vet ./...` — passed

## Learned in runs
- In the sandbox corepack's fetch ignores the egress proxy, so `pnpm` fails to download itself; run `NODE_USE_ENV_PROXY=1 corepack pnpm --version` once to seed the corepack cache, after which plain `pnpm` works (and open_pull_request's verification passes). (learned 2026-11-20, run 382149355898202234)
