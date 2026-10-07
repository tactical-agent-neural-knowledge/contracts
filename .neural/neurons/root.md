# Neurons · root

refreshed 2026-10-07 · d58208d52ddc

- 26 domains under `proto/tank/<domain>/v1/` now (was 22 at the last refresh): `board`, `books`, `canvas`, `security` are new packages; `agent`, `agentctl`, `events`, `realtime`, `topo`, `workspace` grew in place. `README.md`'s package table only lists 11 — it is stale and should not be trusted for the current domain list.
- `gen/ts/src/index.ts` is hand-written and is missing **12 of the 26** domains from its barrel: `admin`, `billing`, `board`, `books`, `canvas`, `catalog`, `command`, `huddle`, `monitor`, `notification`'s sibling `platform`, `security`, `topo` have no namespaced export. Consumers of those must deep-import `./tank/<domain>/v1/<domain>_pb.js`; adding a barrel line is a manual step `make gen` does not do.
- Newer domain files (`billing`, `books`, `canvas`, `catalog`, `monitor`, `platform`, `security`, `topo`) set `option go_package` explicitly; older ones (`agent`, `agentctl`, `board`, plus the original 2026-10-03 set) rely on `buf.gen.yaml`'s `managed.override.file_option: go_package_prefix` alone. Both land at the same import path today — `buf lint`/`buf build` don't flag the inconsistency — but a domain that sets it explicitly stops tracking a future prefix change.
- `make check` (lint → gen → build, then `git diff --exit-code --stat gen/`) is the one command that proves `gen/` is current; CI runs the same four steps directly with `buf`, not through `make` (see `.neural/neurons/github.md`).
- `make clean` only removes `gen/{go,ts/src,python}/tank` — it does not touch `gen/ts/package.json`, `gen/ts/tsconfig.json` or `dist/`, so a clean build still needs `npm install` in `gen/ts` afterward.
- `gen/ts/package.json` pins `@bufbuild/protobuf` as a peer dependency (`^2.2.3`) matching the `protoc-gen-es` plugin version in `buf.gen.yaml`; bumping one without the other is a version the TS build won't catch until a consumer installs it.
- `go.mod` requires Go 1.26 and pins `connectrpc.com/connect v1.18.1` / `google.golang.org/protobuf v1.36.4` — exactly the plugin versions in `buf.gen.yaml`. `CLAUDE.md`'s prohibition on "changing plugin versions without regenerating everything in the same PR" means these three version strings move together.
- `BUF ?= npx --yes @bufbuild/buf` in the `Makefile` means every `make` target resolves and runs buf fresh each time (no local binary cached by default); set `BUF=buf` to use one already on `PATH`.
- No `_test.go` files exist anywhere in this repo; `go test ./...` (listed in `.neural/map.yaml`) passes vacuously. Correctness here is proven by `buf lint`, `buf breaking` and the committed-`gen/`-matches-source check, not by tests.
- There is no `.github/workflows` step or `Makefile` target that runs `buf format` — formatting is not enforced, only `STANDARD` lint rules (minus `PACKAGE_VERSION_SUFFIX`, per `buf.yaml`).

## Verified

`npx --yes @bufbuild/buf lint`, `npx --yes @bufbuild/buf build` (all 26 files compile), `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `npm install && npm run build` in `gen/ts` (tsc compiles) — all passed. `go build ./...` was not run: no Go toolchain in this sandbox.
