# Neurons · .

refreshed 2026-10-10 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `make` and `go` are not installed in the agent sandbox (no `/usr/bin/make`, no `go` on PATH) — every Makefile target and `go build ./...` fails before it starts. Run the underlying buf commands directly instead: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`. This is also why the Neural Knowledge refresh runner itself can die with `spawn make ENOENT` if its command list (`.neural/map.yaml`) ever points at a `make` target without an npx fallback.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`. Nine of 27 proto files now carry an explicit `option go_package` anyway (billing, books, canvas, catalog, monitor, platform, remediation, security, topo) — up from five at the last refresh, since books/canvas/remediation/security were added with it set from the start. A hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel; adding a new proto domain (board, books, canvas, remediation, security all arrived since the last refresh) does not add it to this file automatically — deep imports (`./tank/board/v1/board_pb.js`) are the documented primary path.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` (CI-only here, see above) is the real check.
- `README.md` names the consumers each language serves and states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- Five new domains landed since the 2026-10-03 refresh: `board` (Neuralboards), `books` (Neuralbooks), `canvas` (Neuralcanvas), `remediation` and `security` (Neuralsecurity's judge/fix split — see `proto.md`). `agentctl.proto` grew by over 300 lines wiring runner-side RPCs for the first three onto `RunnerService`.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make build` / `go build ./...` not run: no `go` or `make` on PATH here.
