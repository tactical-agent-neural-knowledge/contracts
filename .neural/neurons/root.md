# Neurons · .

refreshed 2026-10-15 · 37e79eff8520

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR touching a proto also carries the regenerated files.
- `Makefile` is the one documented entry point (`make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate), but `make` is **not installed in the agent sandbox**. Run the underlying buf commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`. A stale `.neural/map.yaml` that still lists `make ...` as the runner's command makes `open_pull_request` fail before anything is pushed (`spawn make ENOENT`).
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, so every target shells out to npx and the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- A Go 1.26 toolchain **is** present in the agent sandbox (`/usr/local/go/bin/go`) and `go build ./...` succeeds here, downloading `connectrpc.com/connect v1.18.1` and `google.golang.org/protobuf v1.36.4` on a cold module cache — don't assume a toolchain is missing without checking `command -v go` first.
- `buf generate`'s remote plugins (protoc-gen-es, python/pyi) depend on buf's remote plugin service; it can be down (`Failure: the server hosted at that remote is unavailable`) even when lint/breaking/local Go generation all work — a `make gen` failure isn't necessarily a code problem.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix`, which is why most protos carry no `option go_package`. 10 of 28 domain files set it explicitly anyway (billing, books, canvas, catalog, monitor, platform, remediation, security, social, topo) — a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never hand-written files like `gen/ts/src/index.ts`.
- `README.md`'s package table only lists the original 13 domains (auth, workspace, channel, search, richtext, message, blocks, presence, files, events, realtime, agent, admin) — it is stale against the actual 28-domain `proto/` tree and should not be trusted as the domain list.
- `README.md` ends with a stray `x` / `y` / `z` after the Security section — looks like leftover test content, left as-is since this refresh only touches `.neural/` and `AGENTS.md`.

## Verified
- `npx --yes @bufbuild/buf lint` (clean, no output)
- `git fetch --no-tags origin main:main && npx --yes @bufbuild/buf breaking --against ".git#branch=main"` (clean, no output)
- `go build ./...` (succeeds after downloading `connectrpc.com/connect` and `google.golang.org/protobuf`)
