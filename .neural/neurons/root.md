# Neurons · .

refreshed 2026-10-11 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- No `make` and no `go` binary in this agent sandbox. `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`, so every target normally shells to npx anyway; run `npx --yes @bufbuild/buf lint|build|breaking|generate` directly here and do not claim `make build` / `go build ./...` — only CI proves those.
- `buf.yaml` is v2, single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, `breaking.use: [FILE]` — FILE-level, so moving a message between files breaks even when the wire is unchanged.
- `buf.gen.yaml` managed mode sets `go_package_prefix` to `.../contracts/gen/go`, so most protos carry no `option go_package`. Nine now set it explicitly anyway — billing, books, canvas, catalog, monitor, platform, remediation, security, topo — one more than the last refresh (books and canvas and remediation and security are new since 2026-10-03, replacing the prior five with nine). A hand-written override must match the managed prefix exactly.
- Plugin pins in `buf.gen.yaml` mirror `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`, go 1.26 (`go.mod:3`). `CLAUDE.md` forbids moving a plugin version without regenerating everything in the same PR.
- `gen/ts/src/index.ts` is a hand-maintained barrel and now covers only 14 of 27 proto packages (admin, billing, board, books, canvas, catalog, command, huddle, monitor, platform, remediation, security, topo are absent — the repo grew from 22 to 27 domains since the last refresh and the barrel did not keep up). Deep imports (`./tank/<domain>/v1/<domain>_pb.js`) are the path for anything missing.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` only — never `gen/ts/src/index.ts`, which is hand-written and the thing most likely to go stale silently.
- `go test ./...` is listed in `.neural/map.yaml` but there is not one `_test.go` file in the repo: the Go module is generated code only, `go build ./...` (CI-only here) is the real check.
- `README.md` names consumers per language — Go: api, agent-control; TS: sdk-ts, web, mobile, agent-runner; Python: knowledge — and the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove."
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- A grant mismatch cost a production bug and taught the pattern to watch for: schema `agent` grants the application role USAGE + SELECT only, but api code issued INSERT/DELETE against it anyway and stayed green because the CI fixture grants itself DML the real role doesn't have (`agentctl.proto`, commit `a297744`). The fix was six narrow RPCs on `ControlService`, not a wider grant — when a proto adds a cross-schema write RPC instead of a field, that is usually this same discipline, not scope creep.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make build` / `go build ./...` not run: no `go` or `make` on PATH here.
