# Neurons · proto
refreshed 2026-10-07 · d58208d52ddc

- 26 files, one package per domain at `proto/tank/<domain>/v1/*.proto`; `README.md`'s package table is the fastest way to find which domain owns a type before grepping all 26 files.
- `board.proto` (549 lines) is the largest and most active domain: boards/objects/templates (board:106-291), export as raster/slice/embed (board:297-359), CI-sourced preview and build-source reporting (board:361-493), and `DeriveDiagramRequest`/`Derivation` for diagrams drawn from what CI reports rather than hand-drawn (board:495-526) — read this one first when a board feature changes.
- `agentctl.proto` (913 lines) is the agent's own RPC surface back into TANK (post to thread, post plan, attach artifact, ask for approval/question, report status, read thread, board research, commit files, set brand/landing, record finding) — this is the file to check before adding any new agent-callable action, not `agent.proto`.
- `agent.proto` (380 lines) models runs/states/scoped session tokens and the preview-serving relationship: "TANK serves previews of the applications it builds; a workspace that builds its own [CI]..." (agent.proto:201) — the two files split by direction: `agent.proto` is TANK's view of an agent run, `agentctl.proto` is the agent's own callback API.
- `security.proto` (263 lines, newest domain) has one governing rule stated in its own file header: controls are the primitive, frameworks (SOC 2 etc.) are views over them via `FrameworkClause`/`ClauseCoverage` — never add a framework-specific message, only crosswalk rows onto existing `Control`s (security.proto:9-22, 104-113).
- In `security.proto`, `ControlState.UNKNOWN` and `Evidence.stale` are load-bearing: a check that hasn't run recently must report UNKNOWN rather than replay its last answer (security.proto:38-41, 83-85) — a future edit that lets a stale evidence resolve to MET would silently defeat the whole model.
- `workspace.proto` (721 lines) and `agentctl.proto` (913 lines) are the two largest files after `board.proto`; `workspace.proto` owns the single-call `GetBootstrap` plus Armor Mode preferences — check there before adding another "get everything for app boot" RPC.
- No file in `proto/` uses the `reserved` keyword (verified by grep) — this codebase hasn't yet hit its first field removal; when one happens, it must add `reserved` rather than just deleting the field number, per the hard prohibition in CLAUDE.md.
- `buf.yaml` lints at `STANDARD` minus `PACKAGE_VERSION_SUFFIX` and breaking-checks at `FILE` granularity (buf.yaml:4-11) — moving a message between files in the same package is a breaking-check failure even though the wire format is unchanged.
- Managed mode in `buf.gen.yaml` overrides only `go_package_prefix` (buf.gen.yaml:4-7); every `.proto` file still declares its own explicit `go_package = ".../gen/go/tank/<domain>/v1;<domain>v1"` option, so a new file must not skip that line even though managed mode is on.

## Verified
- `buf lint` (via `npx --yes @bufbuild/buf lint`) — passed clean, no findings
