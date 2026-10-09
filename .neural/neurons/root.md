# Neurons · .

refreshed 2026-10-09 · e52a377a71d9

- `make check` is the whole CI contract in one target: `lint`, `gen`, `build`, then `git diff --exit-code --stat gen/` — if `gen/` is dirty after a clean regenerate, it fails with a message telling you to run `make gen` and commit. This is the thing to run before opening a PR, not `buf lint` alone.
- `BUF ?= npx --yes @bufbuild/buf` — every `make` target shells out to this; pass `BUF=buf` if a real binary is on `PATH`. No Go toolchain is available in this sandbox, so `make build`/`go build ./...` cannot be verified here; CI runs it.
- `buf.gen.yaml` pins exact plugin versions (protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3, python 29.3) and `CLAUDE.md` forbids changing any of them without regenerating everything in the same PR.
- `buf.yaml` lints with `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (the repo's own `v1` suffix would otherwise fail that rule) and checks breaking at `FILE` granularity — moving a message to a different `.proto` file is a break even when the wire bytes are unchanged.
- `make breaking` needs a local `main` ref to diff against (`'.git#branch=main'`); on a fresh clone or a shallow CI checkout run `git fetch --no-tags origin main:main` first or buf cannot resolve it.
- `gen/` is committed on purpose (`README.md`, `CLAUDE.md`) — consumers (api, web, mobile, sdk-ts, agent-control, agent-runner, knowledge) import the generated Go/TypeScript/Python directly rather than regenerating. Editing anything under `gen/` by hand is a hard prohibition.
- A push to `main` runs `publish-ts` and ships a canary npm package to GitHub Packages; a `v*` tag ships a real release. Merging to `main` is already a publish — there is no staging step after green CI.
- Additive-first is the house rule for every change (`README.md`, `CLAUDE.md`): add a field, ship every client, wait for mobile to land, only then remove the old one. `buf breaking` only enforces the wire half; the "every client has shipped" half is discipline, not tooling.
- `go.mod` pins `go 1.26`; the Go module only exists to let `gen/go` build and is otherwise untouched by this repo's own code (there are no `_test.go` files anywhere, so `go test ./...` in the map is a no-op).

## Verified

`npx --yes @bufbuild/buf lint` and `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (after `git fetch --no-tags origin main:main`) both passed. `make build`/`go test ./...` not run here (no Go toolchain in this sandbox).
