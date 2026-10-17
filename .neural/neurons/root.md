# Neurons · .

refreshed 2026-10-17 · fee5860e47dd

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and hits the network on a cold cache. Override with `make lint BUF=buf` when a real binary is on PATH.
- `make` is often **absent in agent sandboxes** (no `/usr/bin/make`). Run the underlying commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...`. `.neural/map.yaml`'s `commands:` block is what `open_pull_request`'s pre-check actually runs — a stale map that still lists `make ...` fails every PR with `spawn make ENOENT` before anything is pushed.
- `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate. Regenerating with a different buf/plugin version than `buf.gen.yaml` pins will dirty `gen/` and fail this check.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. Five domains carry one anyway (billing, catalog, monitor, platform, topo); a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml`: protoc-gen-go v1.36.4, connect-go v1.18.1, protoc-gen-es v2.2.3, python v29.3. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- A Go 1.26 toolchain is present in the agent sandbox (`/usr/local/go/bin/go`) and `go build ./...` succeeds here, downloading dependencies from the network on a cold module cache. Verify with `command -v go` rather than assuming.
- Wire names stay neutral (`Channel`, not `Tread`); product vocabulary lives in the clients. One proto package per domain, version suffix `v1`. This is decided; do not re-litigate.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
