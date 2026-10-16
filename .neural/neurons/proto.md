# Neurons · proto

refreshed 2026-10-16 · 96c9e69403fd

- 29 `.proto` files, one domain per directory under `proto/tank/<domain>/v1/`, package `tank.<domain>.v1` — `README.md`'s package table at the top is the fastest index of what each domain owns; read it before grepping 29 files cold.
- Snowflake ids as strings is the universal convention — called out explicitly in file-header comments (e.g. `crew.proto`, `social.proto`) and true across every domain; don't introduce a numeric or UUID id type.
- Wire names stay neutral: the channel domain is `tank.channel.v1` / `Channel` in the wire even though the product calls it "Tread" everywhere else (`CLAUDE.md`'s "Decided — do not re-litigate"). Same pattern elsewhere — check a domain's product name against its proto package name before assuming they match.
- `tank.agent.v1.TreadSettings` (`agent.proto:263`) is the per-Tread agent policy message: `concurrent_runs`, `auto_accept_plans`, `max_run_usd`/`daily_usd`, `pull_requests` ("review" | "merge_when_green"), `pr_reviewer_ids`, `read_neural_knowledge`, `merge_allowed`, `notify_reviewers`, `strongest_model`. This is the one message to read when a thread asks "is there a setting for X" about agent run behavior.
- `tank.agentctl.v1` (`agentctl.proto`, 1074 lines — the largest file in the repo) carries `TreadSettings` by reference at lines 1056/1060 (`SetTreadSettings` request/response) — it's the control-plane RPC surface, `tank.agent.v1` owns the data shape.
- The newest domains (added since the 2026-10-03 refresh): `board` (Neuralboards, 549 lines, second largest file), `books` (Neuralbooks), `canvas` (Neuralcanvas), `remediation`, `security`, `crew` (agent swarm switchboard, `Treads`/`Activity` enums control where and how often a member speaks), `social` (Flare: X/Instagram). Treat any neuron or doc older than this refresh as silent on all seven.
- 10 files carry an explicit `option go_package` overriding the managed prefix from `buf.gen.yaml` (billing, books, canvas, catalog, crew, monitor, platform, remediation, security, social, topo — verify with `grep -rl "option go_package" proto/` since this list grows with new domains); a new hand-written override must match `github.com/tactical-agent-neural-knowledge/contracts/gen/go/tank/<domain>/v1;<domain>v1` exactly.
- `breaking.use: [FILE]` in `buf.yaml` means moving a message to a different `.proto` file is a breaking-change failure even with zero wire changes — don't "clean up" by relocating a message across files without expecting `make breaking` to flag it.
- Hard prohibitions from `CLAUDE.md` apply repo-wide but are proto-authored: never renumber or reuse a field number, never remove a field before every client has shipped without it, never hand-edit anything under `gen/`.
- A proto change and its regenerated `gen/` output must land in the same commit — `make check` / CI's "generated code is current" step diffs `gen/` after a fresh `buf generate` and fails on any drift.

## Verified
- npx --yes @bufbuild/buf lint
- npx --yes @bufbuild/buf breaking --against '.git#branch=main'
