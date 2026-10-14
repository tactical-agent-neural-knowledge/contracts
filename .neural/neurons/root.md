# Neurons · .

refreshed 2026-10-14 · 6e371811ddb2

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point, but **`make` itself is not installed in the agent sandbox** (`spawn make ENOENT`). Every target is one line shelling to `npx --yes @bufbuild/buf`; run that directly (`npx --yes @bufbuild/buf lint|build|generate|breaking --against '.git#branch=main'`) when `make` is missing.
- The pull-request runner's pre-open verification reads its lint/build/check commands from `.neural/map.yaml`'s `commands:` block, not from the Makefile directly — keep that block's commands runnable without `make` or opening a PR fails before anything is pushed.
- `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate; it prints "ERROR: generated code is stale. Run 'make gen' and commit." and is the same gate CI enforces.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`, which is why most protos carry no `option go_package`. The five new-ish domains that set it explicitly (billing, catalog, monitor, platform, topo) now have company: books, canvas, remediation, security also declare it — a hand-written one must match the managed prefix exactly or `gen/go` lands in the wrong directory.
- Plugin pins in `buf.gen.yaml` mirror the runtime pins in `go.mod`: protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`. `CLAUDE.md` forbids changing a plugin version without regenerating everything in the same PR; moving one side alone desynchronises them.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` — the `tank` subtree only, never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained namespaced barrel and only covers 15 of the 27 proto packages now (admin, billing, board, books, canvas, catalog, command, huddle, monitor, platform, remediation, security, topo absent). Its own comment says deep imports (`./tank/message/v1/message_pb.js`) are the primary path; a new domain (board, books, canvas, remediation, security all landed since the last refresh) does not add itself here.
- `gen/ts` is its own npm package (`@tactical-agent-neural-knowledge/contracts`, `"type": "module"`, tsc NodeNext, `@bufbuild/protobuf` as a peer dep). The es plugin is configured with `import_extension=js`, so every generated import ends in `.js` and must stay that way for NodeNext to resolve.
- `go test ./...` appears in `.neural/map.yaml` but there is not a single `_test.go` file in the repo: the Go module is generated code only, and `go build ./...` is the real check.
- `README.md` names the consumers each language serves and states the change discipline: "Changes are additive-first: add fields, ship every client, wait for the mobile build to land, then remove." It also now documents the `neuralsecurity` scan gate (every push and PR, verdict is the `neuralsecurity` check, sandbox egress only through the proxy) — and carries three stray lines (`x`/`y`/`z`) at the very end that look like an accidental leftover, not content.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- No Go toolchain is installed in this agent sandbox, so `make build` / `go build ./...` cannot be run here; CI's `go build ./...` step is the only place it is proven. Do not claim it locally.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make build` / `go build ./...` not run: no `go` on PATH here, and `make` itself is absent.
