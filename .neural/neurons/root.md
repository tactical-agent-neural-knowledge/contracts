# Neurons · .

refreshed 2026-10-17 · fee5860e47dd

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one documented entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `make` itself is often **absent in agent sandboxes** (`command -v make` fails with no `/usr/bin/make`). Run underlying commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...`. `.neural/map.yaml`'s `commands:` block is what `open_pull_request`'s pre-check runs — a stale map that still lists `make ...` fails every PR with `spawn make ENOENT` before anything is pushed.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. The few that do (billing, catalog, crew, monitor, platform, social, topo) must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel; adding a new domain does not add it here — deep imports (`./tank/message/v1/message_pb.js`) are the primary path.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext). The es plugin uses `import_extension=js` — every generated import ends `.js` and must stay that way for NodeNext resolution.
- `go test ./...` is listed in `.neural/map.yaml` but there are no `_test.go` files: the Go module is generated code only and `go build ./...` is the real check.
- `README.md` states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove." Go consumers: api, agent-control; TS consumers: sdk-ts, web, mobile, agent-runner; Python consumer: knowledge.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."

## Verified

`npx --yes @bufbuild/buf lint` — passed.
