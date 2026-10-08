# Neurons · .

refreshed 2026-10-08 · b57522e4f7aa

- This repo is input + output: hand-written `.proto` under `proto/` (27 domains now, up from 22), generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2, single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` pins are unchanged across this whole wave of new domains: protoc-gen-go v1.36.4, connect-go v1.18.1, protoc-gen-es v2.2.3, python v29.3, mirrored in `go.mod` (`google.golang.org/protobuf v1.36.4`, `connectrpc.com/connect v1.18.1`). `CLAUDE.md` forbids moving one side without regenerating everything in the same PR.
- Managed mode sets `go_package_prefix`, so most protos carry no `option go_package`. Nine now set it explicitly anyway (billing, books, canvas, catalog, monitor, platform, remediation, security, topo) — a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory. `board.proto` is the one new domain that *doesn't* set it, inconsistent with its four new siblings; see `.neural/neurons/proto.md`.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and now covers only 14 of 27 proto packages (admin, billing, board, books, canvas, catalog, command, huddle, monitor, platform, remediation, security, topo absent). Its own comment says deep imports (`./tank/message/v1/message_pb.js`) are the primary path; a new domain — `board`, `books`, `canvas`, `remediation`, `security` all included — does not get added here automatically.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never the hand-written `gen/ts/src/index.ts`.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext, `@bufbuild/protobuf` as a peer dep). The es plugin runs with `import_extension=js`, so every generated import ends in `.js` and must stay that way for NodeNext to resolve.
- `go test ./...` appears in `.neural/map.yaml` but there is not one `_test.go` file in the repo: the Go module is generated code only; `go build ./...` is the real check.
- `README.md`'s package table is now stale against the proto tree: it documents 10 of the 27 packages and has not been updated for `board`, `books`, `canvas`, `remediation`, `security` or the other domains added before them (admin, billing, catalog, command, huddle, monitor, notification, platform, topo). Don't trust it as a domain inventory; read `proto/tank/*/v1/*.proto` instead.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain is installed in this agent sandbox, so `make build` / `go build ./...` cannot be run here; CI's `go build ./...` step is the only place it is proven. Do not claim it locally.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build -o /dev/null`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make build` / `go build ./...` not run: no `go` on PATH here.
