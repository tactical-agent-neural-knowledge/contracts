# Neurons · .

refreshed 2026-10-09 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose.
- `proto/tank/` now holds 27 domains (`ls proto/tank | wc -l`), up from 22 at the last refresh: `board`, `books`, `canvas`, `remediation`, `security` are new since then (`topo` was added just before the last refresh and is now fully documented in `proto.md`).
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate; same gate CI's `check` job enforces, unchanged this refresh.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells to npx and the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2, single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, `breaking.use: [FILE]` — FILE-level, so moving a message between files breaks even when the wire is unchanged. Unchanged this refresh.
- `buf.gen.yaml` turns managed mode on, sets `go_package_prefix` to `github.com/.../contracts/gen/go`. Plugin pins mirror `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and now covers only 14 of 27 proto packages — 13 absent, including every domain added since the last two refreshes (`admin`, `billing`, `catalog`, `command`, `huddle`, `monitor`, `platform`, `topo`, plus this refresh's `board`, `books`, `canvas`, `remediation`, `security`). Its own comment says deep imports are the primary path; new domains are never added here automatically.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext, `@bufbuild/protobuf` peer dep). The es plugin uses `import_extension=js`; every generated import ends in `.js` and must stay that way for NodeNext.
- `go test ./...` is listed in `.neural/map.yaml` but there is not one `_test.go` file in the repo: the Go module is generated code only, `go build ./...` is the real check, and it has no Go toolchain in this sandbox — only CI proves it.
- `README.md`'s package table lists only about a third of the actual 27 domains (it was never updated for `board`/`books`/`canvas`/`remediation`/`security`/`topo`/etc.) — don't treat it as the authoritative domain list; `ls proto/tank` is.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain is installed in this agent sandbox, so `make build` / `go build ./...` cannot be run here; CI's `go build ./...` step is the only place it is proven. Do not claim it locally.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed, no output. `make build` / `go build ./...` not run: no `go` on PATH here.
