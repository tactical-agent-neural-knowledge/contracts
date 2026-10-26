# Neurons · .

refreshed 2026-10-26 · b36299acbfe8

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/`, and `.tools/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one documented entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate; same gate CI enforces.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf`: buf is not vendored, every target shells out to npx and hits the network on a cold cache. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- `make` itself is often **absent in agent sandboxes** (no `/usr/bin/make`). Run underlying commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...`. `.neural/map.yaml`'s `commands:` block is what `open_pull_request`'s pre-check runs — a stale map that still lists `make ...` fails every PR with `spawn make ENOENT` before anything is pushed.
- `buf.gen.yaml` runs all plugins **locally** from `.tools/`, not on `buf.build`. This changed on 2026-10-24 when the BSR started refusing CI's anonymous remote-plugin calls. The versions are unchanged (protoc-gen-go v1.36.4, connect-go v1.18.1, protoc-gen-es v2.2.3, python v29.3), so generated output is byte-for-byte identical.
- `make tools` installs those pinned generators into `.tools/bin/` and `.tools/node_modules/.bin/` (Go installs, npm install). `.tools/` is in `.gitignore` and must be built before `buf generate` runs — CI runs `make tools` in the gen-staleness step, and `gen` depends on `tools` in the Makefile.
- `buf.yaml` is v2 with a single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, and `breaking.use: [FILE]` — FILE-level means moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` turns managed mode on and sets `go_package_prefix` to `github.com/.../contracts/gen/go`. Five domains carry an explicit `option go_package` override; all must match the managed prefix path exactly or generated code lands in the wrong directory.
- Hard prohibitions (CLAUDE.md): never renumber or reuse field numbers; never remove a field before every client has shipped without it; never edit `gen/` by hand; never change plugin versions without regenerating everything in the same PR.
- Wire names stay neutral (`Channel`, not `Tread`); product vocabulary lives in the clients (CLAUDE.md "Decided").

## Verified

- `npx --yes @bufbuild/buf lint` — passed
