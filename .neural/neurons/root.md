# Neurons · .
refreshed 2026-10-08 · a887d51f4d82

- `gen/` is committed on purpose (CLAUDE.md, README.md): consumers pull the Go module / npm package straight from
  this repo's tree, nothing is generated at their build time.
- `make check` (Makefile) = lint + gen + build, then `git diff --exit-code --stat gen/` — if `buf generate` changes
  anything, check fails with "generated code is stale"; this is the same gate CI runs.
- `make breaking` (Makefile) only compares against `main` (`buf breaking --against '.git#branch=main'`); it is a
  no-op if your local `main` ref is stale or missing, so fetch it first.
- Hard prohibitions (CLAUDE.md): never renumber/reuse a field number, never remove a field before every client has
  shipped without it, never hand-edit `gen/`, never bump a plugin version in `buf.gen.yaml` without regenerating
  everything in the same PR.
- Decided, not open for debate (CLAUDE.md): wire names stay neutral — `Channel`, never `Tread` — product vocabulary
  lives only in clients; one proto package per domain, version suffix `v1`.
- `buf.yaml`: lint is `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (packages are plain `tank.<domain>.v1`, not
  `v1`-as-suffix style); breaking rules are `FILE`-level.
- README.md's package table is the fastest map from a domain name to its proto file — 11 packages, one line each,
  with what each owns and who consumes it.
- This sandbox has no `make` and no `go` binary; `npx --yes @bufbuild/buf <cmd>` works directly (network-fetched,
  pinned via `buf.gen.yaml`), so drop straight to the underlying `buf lint` / `buf breaking` / `buf generate` calls
  instead of the Makefile wrappers here.
- `make clean` only removes `gen/go/tank`, `gen/ts/src/tank`, `gen/python/tank` — the `gen/*/package.json` etc.
  scaffolding around them is not regenerated and must stay hand-maintained.

## Verified
- `npx --yes @bufbuild/buf lint` (passed, no findings)
