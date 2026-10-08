# Neurons · .

refreshed 2026-10-08 · a887d51f4d82

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. A handful do anyway (billing, catalog, monitor, platform, topo, security, remediation); a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and still trails the proto tree: five new domains landed this refresh (board, books, canvas, remediation, security) on top of the earlier gap (admin, billing, catalog, command, huddle, monitor, platform, topo). Its own comment says deep imports (`./tank/message/v1/message_pb.js`) are the primary path; adding a domain does not add it here.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext, `@bufbuild/protobuf` as a peer dep). The es plugin is configured with `import_extension=js`, so every generated import ends in `.js` and must stay that way for NodeNext to resolve.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` is the real check.
- The proto tree grew from 22 to 27 packages since the last refresh (`.neural/map.yaml` `proto` area now lists 27 files): `board`, `books`, `canvas`, `remediation` and `security` were added whole. `README.md` and `CLAUDE.md` were not touched by any of that work — `README.md`'s package table still only names the original 13 domains it always chose to list, not an exhaustive index.
- `README.md` names the consumers each language serves — Go: api, agent-control; TS: sdk-ts, web, mobile, agent-runner; Python: knowledge — and states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain is installed in this agent sandbox, so `make build` / `go build ./...` cannot be run here; CI's `go build ./...` step is the only place it is proven. Do not claim it locally.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make build` / `go build ./...` not run: no `go` on PATH here.
