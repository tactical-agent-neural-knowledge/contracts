# Neurons · .

refreshed 2026-10-08 · a887d51f4d82

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. Nine now set it by hand (billing, books, canvas, catalog, monitor, platform, remediation, security, topo — four more than the last refresh); a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained barrel and is badly stale: it exports only 14 of the 27 domains (missing, among others, the four newest — `board`, `books`, `canvas`, `remediation`, `security` — plus older ones like `admin`, `billing`, `topo`). Adding a `.proto` file never updates it; a consumer wanting one of the missing packages must use the deep import (`./tank/<domain>/v1/<domain>_pb.js`) documented in the barrel's own comment.
- Root `CLAUDE.md`'s CI table and plugin-version line are still accurate as written; no root config file (`Makefile`, `buf.yaml`, `buf.gen.yaml`, `CLAUDE.md`, `README.md`, `go.mod`) changed since the last refresh — this refresh's root changes are additions under `proto/` and `.github/` only, which is why `root`'s hash moved while its hot files did not.
- `README.md`'s package table is a second source of truth for what each `tank.<domain>.v1` package holds; it lists only the original ~11 domains and has not been extended for `board`, `books`, `canvas`, `remediation`, `security`, `agentctl`'s growth, or the others added since — read the proto files themselves for anything newer, do not trust the table as exhaustive.
- `go.mod` pins `go 1.26` with exactly two deps (`connectrpc.com/connect`, `google.golang.org/protobuf`); there is no third-party Go dependency to go stale.

## Verified

`npx --yes @bufbuild/buf lint` (clean, STANDARD minus PACKAGE_VERSION_SUFFIX), `npx --yes @bufbuild/buf build -o /dev/null` (all files compile).
