# Neurons · .

refreshed 2026-10-10 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/` (27 domains now, five new since the last refresh: board, books, canvas, remediation, security), generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- No `make` binary and no `go` toolchain exist in the agent sandbox — every documented command is a `make` target that shells to `go build`/`npx`. Run the underlying commands directly instead: `npx --yes @bufbuild/buf lint|build|generate|breaking --against '.git#branch=main'`. `go build ./...` cannot be reproduced here at all; CI is the only place it runs.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. A handful do anyway (billing, catalog, monitor, platform, topo); a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written and will not pick up a new domain on its own; it needs a manual export added.
- `README.md`'s package table (the one documenting each `tank.<domain>.v1` package) has not been updated for the five newest domains (board, books, canvas, remediation, security) — read `proto/` directly for those rather than trusting the table's completeness.
- `go.mod` declares `go 1.26`; `actions/setup-go@v5` in CI reads the version from `go-version-file: go.mod`, so bumping Go means editing that file, not the workflow.

## Verified

`npx --yes @bufbuild/buf lint`, `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (after `git fetch --no-tags origin main:main`) — all passed clean. `make`/`make check` could not be run (no `make` in this sandbox); `go build ./...` could not be run (no Go toolchain in this sandbox).
