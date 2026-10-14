# Neurons · .

refreshed 2026-10-14 · 65c4439b3e7d

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, which is the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and therefore to the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. Several newer domains (board, books, canvas, remediation, security, plus the older billing, catalog, monitor, platform, topo) set it explicitly anyway; a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and still only covers a subset of proto packages (board, books, canvas, remediation, security and others are absent, same gap as before this refresh). Its own comment says deep imports (`./tank/message/v1/message_pb.js`) are the primary path; adding a domain does not add it here.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext, `@bufbuild/protobuf` as a peer dep). The es plugin is configured with `import_extension=js`, so every generated import ends in `.js` and must stay that way for NodeNext to resolve.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` is the real check.
- `README.md` now has a `## Security` section: every push to main and every PR is scanned by Neuralsecurity (secrets, fixable critical/high dependency vulns) from inside a TANK sandbox whose only way out is the egress proxy; the verdict is the `neuralsecurity` check on the commit. See `.github/neurons.md` for how that gate is actually wired (the reusable-workflow call was replaced by an inlined one).
- Trap: `README.md`'s current tail is three stray lines — literal `x`, `y`, `z` — left by a sequence of "docs: nudge" commits (#41). They read as test artifacts, not content; do not treat them as meaningful and do not copy them into anything that quotes the README.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain is installed in this agent sandbox, so `make build` / `go build ./...` cannot be run here; CI's `go build ./...` step is the only place it is proven. Do not claim it locally.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make build` / `go build ./...` not run: no `go` on PATH here.
