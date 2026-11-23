# Neurons · .

refreshed 2026-11-23 · 1670e4e249b5

- `Makefile:1` sets `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, so every target shells out to npx and needs the network on a cold cache. Pass `BUF=buf` when a buf binary is on PATH.
- `make check` (`Makefile:41`) runs `lint gen build`, then `git diff --exit-code --stat gen/` (`Makefile:42`); that stale-generated-code gate is the one CI enforces.
- `make gen` depends on `tools` (`Makefile:23`), which installs the pinned generators into `.tools/bin/` and `.tools/node_modules/.bin/` (`Makefile:10–20`). Run `make tools` before calling `buf generate` directly.
- Pins: protoc-gen-go v1.36.4 (`Makefile:12`), protoc-gen-connect-go v1.18.1 (`Makefile:14`), protoc-gen-es v2.2.3 (`Makefile:16`), protoc 29.3 for the Python and pyi builtins (`Makefile:3`). `buf.gen.yaml:14–36` runs every plugin locally from `.tools/`, not on buf.build.
- Output lands in `gen/go/tank` (`paths=source_relative`), `gen/ts/src/tank` (`target=ts`, `import_extension=js`) and `gen/python/tank`. Generated sources are tracked on purpose; `.gitignore` excludes only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` and `.tools/`.
- `buf.gen.yaml:3–7` enables managed mode and overrides `go_package_prefix` to `github.com/tactical-agent-neural-knowledge/contracts/gen/go`; the `go_package` values in 24 `.proto` files sit under `gen/go/tank/<domain>/v1`.
- `buf.yaml` is v2 with one module at `proto`; `lint.use: [STANDARD]` except `PACKAGE_VERSION_SUFFIX`; `breaking.use: [FILE]`, so moving a message between files is breaking even when field numbers are unchanged.
- `make breaking` (`Makefile:31`) runs `buf breaking --against '.git#branch=main'`, which needs a local `main`; CI fetches `origin main:main` before the breaking step in `.github/workflows/ci.yml` because PR checkouts have none.
- `README.md` states the compatibility rule: additive-first (add fields, ship every client, then remove). `buf breaking` enforces the wire half; the stale-gen gate enforces the generated half.

## Verified

- `npx --yes @bufbuild/buf lint` — passed (exit 0)
- `go build ./...` — passed
- `go vet ./...` — passed
