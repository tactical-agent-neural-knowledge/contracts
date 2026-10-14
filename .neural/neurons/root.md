# Neurons · .

refreshed 2026-10-14 · 6e371811ddb2

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. Generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one entry point. `make check` = `lint gen build` plus `git diff --exit-code --stat gen/`, the stale-generated-code gate CI also enforces. `Makefile:1` is `BUF ?= npx --yes @bufbuild/buf` — buf is not vendored, every target shells out to npx. Override with `make lint BUF=buf` when a real buf binary is on PATH.
- No `make` and no Go toolchain in this agent sandbox: run `npx --yes @bufbuild/buf lint|build|generate|breaking --against '.git#branch=main'` directly — this is what the Makefile shells out to, and it is also what `open_pull_request`'s pre-check runner reads from `.neural/map.yaml`'s `commands:` block (not the Makefile), so a stale map entry can fail a PR before anything is pushed.
- `buf.yaml` is v2, single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml`/plugin pins (protoc-gen-go v1.36.4, connect-go v1.18.1) mirror `go.mod`; `CLAUDE.md` forbids moving one without regenerating everything in the same PR. Five domains carry an explicit `option go_package` (billing, catalog, monitor, platform, topo) — a hand-written one must match the managed `go_package_prefix` exactly.
- `gen/ts/src/index.ts` is a hand-maintained barrel covering 14 of the now-27 proto packages; adding a domain (board, books, canvas, remediation, security are the newest five) does not add it there automatically.
- 27 proto files now, five added this cycle: `board` (Neuralboards — infinite board, a frame can hold the running app), `books` (Neuralbooks — invoices/payments/expenses/cash), `canvas` (Neuralcanvas — pages that cite what they were written from), `remediation` and `security` (Neuralsecurity's two halves: the registry that judges, the engine that fixes, kept as separate services on purpose).
- `README.md` now has a `## Security` section: every push/PR is scanned by Neuralsecurity from inside a sandbox whose only way out is the egress proxy; the verdict is the `neuralsecurity` check on the commit.
- `README.md:33-35` carries three stray lines (`x`/`y`/`z`) after the Security section — not proto-generated, looks like leftover test content, left alone since this refresh only touches `.neural/` and `AGENTS.md`.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- `TreadSettings` (agent.proto) now has `pull_requests` ("review" default | "merge_when_green") and `merge_allowed` — this is the on-the-wire answer to "can TANK merge its own PRs for a Tread", sitting next to `auto_accept_plans`.

## Verified

`npx --yes @bufbuild/buf lint`, `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — all passed. `make build` / `go build ./...` not run: no `make` or `go` on PATH here.
