# Neurons · .

refreshed 2026-10-07 · 77435ec229ee

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. Seven do anyway (billing, books, canvas, catalog, monitor, platform, topo) and the value matches the managed output exactly — redundant but harmless, not a source of drift today.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, in all three languages; `gen/ts/src/index.ts` is hand-written and survives `clean`.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and covers 14 of the 25 proto packages. `board`, `books` and `canvas` are the newest domains and are not in it yet, alongside the older gaps (admin, billing, catalog, command, huddle, monitor, platform, topo). Its own comment says deep imports (`./tank/message/v1/message_pb.js`) are the primary path; adding a domain does not add it here — easy to forget after `make gen`.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext, `@bufbuild/protobuf` as a peer dep). The es plugin is configured with `import_extension=js`, so every generated import ends in `.js` and must stay that way for NodeNext to resolve. No `node_modules/` is checked in or vendored here, so `npm run build` fails cold until `npm install` runs.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` is the real check.
- `README.md`'s package table is the fastest way to find which `.proto` owns a feature (e.g. Armor Mode is in both `tank.workspace.v1` preferences and `tank.presence.v1`); it states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain and no `node_modules/` are installed in this agent sandbox, so `go build ./...` and `gen/ts`'s `npm run build` cannot be proven here; CI's steps are the only place they are proven. Do not claim them locally without running them.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `go build ./...` and `gen/ts`'s `npm run build` not run: no `go` on PATH and no `gen/ts/node_modules` in this sandbox.
