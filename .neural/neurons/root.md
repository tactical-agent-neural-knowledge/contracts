# Neurons · .
refreshed 2026-10-07 · 572da952c512

- This repo is only the wire contracts: `proto/tank/<domain>/v1/*.proto` in, generated `gen/go` + `gen/ts` + `gen/python` out, committed on purpose — never generated at build time by consumers (README.md).
- `make check` = `lint` + `gen` + `build`, then fails if regenerating changed anything under `gen/` — this is how CI catches hand-edited or stale generated code (Makefile).
- `make gen`/`lint`/`breaking` all shell out to `npx --yes @bufbuild/buf`; no local buf binary is expected or required.
- Plugin versions are pinned per-language in `buf.gen.yaml` (protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3, python 29.3); bumping any one without regenerating everything in the same PR is a hard prohibition (CLAUDE.md, buf.gen.yaml).
- `buf.yaml` lint excludes `PACKAGE_VERSION_SUFFIX` deliberately — the repo's own convention is one proto package per domain with a `v1` suffix, just not the linter-enforced form of it (buf.yaml).
- `buf.yaml` breaking is set to `FILE` level and runs via `make breaking` / `buf breaking --against '.git#branch=main'` — this is the check that makes the polyrepo safe instead of a monorepo build.
- Hard prohibitions (CLAUDE.md): never renumber or reuse a field number, never remove a field before every client has shipped without it, never edit `gen/` by hand.
- Wire names stay product-neutral by decision: `Channel` not `Tread` — product vocabulary belongs in the clients, not here (CLAUDE.md, README.md).
- Go module is `github.com/tactical-agent-neural-knowledge/contracts` on Go 1.26 (go.mod); npm package is `@tactical-agent-neural-knowledge/contracts`, built with `tsc` (gen/ts/package.json).
- Changes are additive-first across the whole repo: add a field, ship every client, wait for mobile to land, then remove — `buf breaking` only enforces the wire half of that discipline (README.md).

## Verified
- `npx --yes @bufbuild/buf lint` (clean, no findings)
