# Neurons · .

refreshed 2026-10-11 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/` (now 27 domains, up from 22), generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged. Both new imports this refresh (`board.proto`, `canvas.proto` into `events.proto`/`realtime.proto`) mean those four files now break together.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. Plugin pins mirror `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel; it was already missing 8 of 22 domains before this refresh and the 5 added this round (board, books, canvas, remediation, security) are absent too. Deep imports (`./tank/board/v1/board_pb.js`) are the primary path for anything not in the barrel.
- `README.md`'s consumer table is in the same state: it lists 12 packages and was not touched when board/books/canvas/remediation/security/admin's `EndMemberSessions` landed. Read `proto/` itself for what exists, not the README.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` is the real check.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain is installed in this agent sandbox, so `make build` / `go build ./...` cannot be run here; CI's `go build ./...` step is the only place it is proven. Do not claim it locally.
- `make` itself is also absent from this sandbox (no `/usr/bin/make`): every target above has to be run as the raw command it wraps (e.g. `npx --yes @bufbuild/buf lint` for `make lint`) or `open_pull_request` here fails before pushing anything with `spawn make ENOENT`.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed with no output. `make build` / `go build ./...` not run: no `go` on PATH here.
