# Neurons · .

refreshed 2026-10-10 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH. `make` itself is not installed in the agent sandbox — run the `npx --yes @bufbuild/buf <cmd>` the Makefile wraps directly (`lint`, `build`, `generate`, `breaking --against '.git#branch=main'`).
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. Plugin pins mirror `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and now covers only 15 of 27 proto packages: the five domains added this refresh (board, books, canvas, remediation, security) are absent from it, same as the eight that were already missing (admin, billing, catalog, command, huddle, monitor, platform, topo). Deep imports (`./tank/message/v1/message_pb.js`) are the documented primary path; adding a domain to `proto/` does not add it here.
- `gen/go`, `gen/ts/src` and `gen/python` already carry generated code for all 27 domains including the five new ones — `buf build`/`lint`/`breaking` and the committed tree agree, so `gen/` is current as of this commit.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` (CI only — no Go toolchain here) is the real check.
- `README.md` names the consumers each language serves — Go: api, agent-control; TS: sdk-ts, web, mobile, agent-runner; Python: knowledge — and states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- `.neural/LICENSE` is TANK's own boilerplate on the generated layer, not a repo license; it is regenerated with everything else and not a place to record project facts.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed against main at `e52a377`. `make build` / `go build ./...` not run: no `go` on PATH here.
