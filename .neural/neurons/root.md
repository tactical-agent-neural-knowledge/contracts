# Neurons · .
refreshed 2026-10-06 · fb6e2ffe6678

- `gen/` (go, ts, python) is committed on purpose, generated via remote buf plugins pinned in `buf.gen.yaml` — never hand-edit it (CLAUDE.md hard prohibition); `make check` fails the build if `gen/` is stale vs proto/.
- Plugin versions are pinned exactly: protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3 (TS), protobuf/pyi python 29.3 — bump and regenerate everything in the same PR, never partially.
- `make check` = `lint gen build` + a `git diff --exit-code --stat gen/` staleness check; this is exactly what CI's "generated code is current" step runs, so `make check` locally predicts CI.
- `make breaking` runs `buf breaking --against '.git#branch=main'`; this is the check that makes the polyrepo safe — a wire break here would otherwise surface as a prod incident in web/mobile/agent-runner.
- Hard prohibitions (CLAUDE.md): no renumbering/reusing field numbers, no removing a field before every client has shipped without it, no editing `gen/` by hand, no changing plugin versions without regenerating in the same PR.
- Decided, do not re-litigate: wire names stay neutral (`Channel`, not `Tread` — product vocabulary lives in the clients); one proto package per domain, version suffix `v1`.
- `buf.yaml` lints with STANDARD minus `PACKAGE_VERSION_SUFFIX` (the `v1` suffix is intentional, see above) and breaking-checks at `FILE` granularity.
- `Makefile`'s `BUF` var defaults to `npx --yes @bufbuild/buf` — no local buf binary is assumed or required.
- `README.md` has a table of every `tank.*.v1` package and its purpose — read it before opening individual `.proto` files to find which package owns a concept.
- Three consumers of `gen/`: Go module `github.com/tactical-agent-neural-knowledge/contracts/gen/go`, npm `@tactical-agent-neural-knowledge/contracts` (GitHub Packages), and a Python package for `knowledge`.

## Verified
- `buf lint` (clean, no findings)
