# Neurons · .

refreshed 2026-10-09 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/` (27 domains, up from 22 at the last refresh — board, books, canvas, security and remediation were all added since), generated Go/TypeScript/Python committed under `gen/`. Every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." — the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells to npx and the network on a cold cache. Override with `make lint BUF=buf` when a real binary is on PATH.
- `buf.yaml` is v2, single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` managed mode sets `go_package_prefix`; most files carry no `option go_package`. Nine do anyway (billing, books, canvas, catalog, monitor, platform, remediation, security, topo) — the newest domains tend to set it explicitly even though it is redundant under managed mode.
- Plugin pins in `buf.gen.yaml` mirror `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids moving one side without regenerating everything in the same PR.
- `README.md`'s package table only documents 13 of the 27 domains (no billing, board, books, canvas, catalog, command, huddle, monitor, platform, remediation, security, topo) — do not trust it as a complete index of what `proto/` contains; `ls proto/tank` is.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and covers only 14 of 27 proto packages (auth, workspace, channel, richtext, message, blocks, presence, files, events, realtime, agent, agentctl, notification, search). A new domain's generated TS is reachable by deep import (`./tank/<domain>/v1/<domain>_pb.js`) long before anyone remembers to add it here — do not assume the barrel is current.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `go test ./...` is listed in `.neural/map.yaml` but there is not one `_test.go` file in the repo; `go build ./...` is the real Go check, and there is no Go toolchain in this agent sandbox — CI's `go build ./...` is the only place it is proven.
- `README.md` states the change discipline verbatim: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`, after `git fetch --no-tags origin main:main`) — all passed. `make build` / `go build ./...` not run: no `go` on PATH here.
