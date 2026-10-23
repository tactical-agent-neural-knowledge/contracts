# Neurons · .

refreshed 2026-10-23 · 8025748642c8

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one documented entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `make` itself is often **absent in agent sandboxes** (no `/usr/bin/make`). Run underlying commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...`. `.neural/map.yaml`'s `commands:` block is what `open_pull_request`'s pre-check runs — a stale map that still lists `make ...` fails every PR with `spawn make ENOENT` before anything is pushed.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`. Five domains carry an explicit `option go_package` (billing, catalog, monitor, platform, topo) plus crew, social, ai, and environment — all must match the managed prefix path exactly or generated code lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel; adding a domain does not add it here — update by hand if TS consumers need top-level imports from a new domain.
- A Go 1.26 toolchain is present in the agent sandbox (`/usr/local/go/bin/go`) and `go build ./...` succeeds; `go test ./...` is in the map but there are no `_test.go` files — `go build ./...` is the real check.
- `README.md` states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- Wire names stay neutral (`Channel`, not `Tread`); product vocabulary lives in the clients. One proto package per domain, version suffix `v1`. These are decided and must not be re-litigated.

## Verified

`npx --yes @bufbuild/buf lint` (STANDARD minus PACKAGE_VERSION_SUFFIX), `npx --yes @bufbuild/buf build` — both passed.
