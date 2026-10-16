# Neurons · .

refreshed 2026-10-16 · 96c9e69403fd

- Input + output repo: hand-written `.proto` under `proto/`, generated Go/TypeScript/Python committed under `gen/` on purpose. `.gitignore` only excludes `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — the generated sources themselves are tracked, so a proto change and its regenerated output land in the same PR.
- `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf` — buf is not vendored; every target shells to npx and hits the network on a cold cache. Override with `make lint BUF=buf` if a real binary is on PATH.
- `make` itself is often **absent in agent sandboxes** (no `/usr/bin/make`), which fails every documented command with `spawn make ENOENT` before anything runs. Use the underlying commands directly: `npx --yes @bufbuild/buf lint|build|generate`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...`. `.neural/map.yaml`'s `commands:` block is what `open_pull_request`'s pre-check actually runs, so a stale map that still says `make ...` can block a PR before it's pushed.
- `make check` (Makefile) = `lint gen build` plus `git diff --exit-code --stat gen/`, the staleness gate: regenerating with a different buf/plugin version than `buf.gen.yaml` pins will dirty `gen/` and fail this.
- A Go 1.26 toolchain is present in this sandbox (`/usr/local/go/bin/go`); `go build ./...` succeeds, downloading `connectrpc.com/connect v1.18.1` and `google.golang.org/protobuf v1.36.4` on a cold module cache — these pin-match `buf.gen.yaml`'s plugin versions (`go.mod`).
- `buf.yaml`: v2, single module at `proto`, `lint.use: STANDARD` minus `PACKAGE_VERSION_SUFFIX` (domains use suffix `v1` on purpose), `breaking.use: FILE` — breaking is checked per-file, so moving a message between files is a break even with the wire unchanged.
- `buf.gen.yaml` managed mode sets `go_package_prefix: github.com/tactical-agent-neural-knowledge/contracts/gen/go`; plugins pinned at protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3 (→ `gen/ts/src`, ESM import extensions), protoc-gen-python/pyi 29.3.
- `README.md` documents a new "## Security" section: every push to main and every PR is scanned by Neuralsecurity for secrets and fixable critical/high dependency vulnerabilities, from inside a sandboxed runner whose only egress is a proxy — this is `security.yml`, see `.neural/neurons/github.md`.
- 29 proto domains now exist (not the 22 from the last refresh); newest is `crew` (`proto/tank/crew/v1/crew.proto`, "a workspace's swarm of agents… run from one switchboard"). See `.neural/neurons/proto.md` for the domain list and wire conventions.
- `CLAUDE.md` hard prohibitions (do not violate): renumbering/reusing field numbers, removing a field before every client has shipped without it, editing `gen/` by hand, changing plugin versions without regenerating everything in the same PR.
- `CLAUDE.md` decided-and-closed: wire names stay neutral (`Channel`, not `Tread` — product vocabulary lives in the clients), one proto package per domain with suffix `v1`, generated code is committed rather than fetched at build time.

## Verified

`npx --yes @bufbuild/buf lint`, `npx --yes @bufbuild/buf build -o /dev/null`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'`, `go build ./...` — all passed.
