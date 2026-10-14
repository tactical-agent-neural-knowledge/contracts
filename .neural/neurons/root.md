# Neurons · .
refreshed 2026-10-14 · 65c4439b3e7d

- This is the wire contract repo only: `proto/tank/<domain>/v1/*.proto` in, generated Go/TS/Python under `gen/` out, committed on purpose (README.md, CLAUDE.md).
- `make` is not installed in the agent sandbox (no `/usr/bin/make`) — every Makefile target fails with `spawn make ENOENT`; run the underlying `npx --yes @bufbuild/buf lint|build|generate|breaking --against '.git#branch=main'` directly instead.
- `make check` (= lint, gen, build, then `git diff --exit-code gen/`) is what CI runs; a stale `gen/` after editing proto is the most common break, fixed by `make gen` (or the buf invocation above) before committing.
- `buf.yaml` lints with `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (package names are `tank.<domain>.v1`, no extra suffix) and breaking-checks at `FILE` granularity against `main`.
- `buf.gen.yaml` pins three plugin families — protoc-gen-go 1.36.4 + connect-go 1.18.1 (`gen/go`), protoc-gen-es 2.2.3 (`gen/ts/src`), protobuf/pyi 29.3 (`gen/python`); bumping a version without regenerating everything in the same PR is a hard prohibition (CLAUDE.md).
- Hard prohibitions carried from CLAUDE.md: never renumber/reuse a field number, never remove a field before every client shipped without it, never hand-edit `gen/`.
- Decided, not open for relitigation: wire names stay neutral (`Channel` not `Tread`, `Agenture` not product vocabulary) — product vocabulary lives in the clients, not the wire.
- `README.md` carries a `## Security` section describing the Neuralsecurity scan on every push/PR; it also has three stray trailing lines (`x`/`y`/`z`) after that section — leftover noise, not a documented convention.
- Consumers: Go module `github.com/tactical-agent-neural-knowledge/contracts/gen/go` (this repo, go 1.26); npm `@tactical-agent-neural-knowledge/contracts` published from `gen/ts` (canary on every main push, semver on `v*` tags) — see `.github/workflows/ci.yml`'s `publish-ts` job.
- The repo is public while the org's CI reusable-workflow definitions live in a private `workflows` repo — GitHub refuses a private reusable workflow to a public caller, so CI logic that would otherwise be shared is inlined here instead (see `.neural/neurons/github.md`).

## Verified
- npx --yes @bufbuild/buf lint
