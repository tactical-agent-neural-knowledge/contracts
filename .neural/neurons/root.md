# Neurons · .

refreshed 2026-10-16 · 96c9e69403fd

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one documented entry point (`make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate), but `make` is **not installed in the agent sandbox** (no `/usr/bin/make`). Run the underlying buf commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...`.
- `.neural/map.yaml`'s `commands:` block is what `open_pull_request`'s pre-check actually runs, not the Makefile — a stale map that still lists `make ...` fails every PR with `spawn make ENOENT` before anything is pushed.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`. 10 of the 29 proto files carry an explicit `option go_package` anyway (billing, books, canvas, catalog, crew, monitor, platform, remediation, security, social, topo — grep `option go_package` in `proto/` to get the current list); a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- A Go 1.26 toolchain is present in the agent sandbox (`go.mod` pins `go 1.26`) and `go build ./...` succeeds, downloading `connectrpc.com/connect` and `google.golang.org/protobuf` on a cold module cache.
- 29 domains under `proto/tank/*/v1/`; the newest are `crew` (switchboard for a workspace's agent swarm, `@handle` members with role/skill/activity) and `social` (Flare: X/Instagram posting, account connect stays human-only via OAuth). `README.md`'s package table is the map of what lives where — check it before assuming a concept needs a new package.
- `tank.agent.v1.TreadSettings` (`proto/tank/agent/v1/agent.proto:263`) is the per-Tread policy surface: `auto_accept_plans`, spend ceilings, `pull_requests` ("review" default vs "merge_when_green"), `merge_allowed`, `notify_reviewers`, `strongest_model`. Read this message directly rather than guessing at Tread behavior from the thread UI.
- README's package table (top of `README.md`) is the fastest way to find which `.proto` owns a concept — faster than grepping 29 files cold.

## Verified
- npx --yes @bufbuild/buf lint
- npx --yes @bufbuild/buf breaking --against '.git#branch=main'
