# Neurons · proto

refreshed 2026-10-18 · 88b93f57c9fd

- 29 proto files across 29 domains (admin, agent, agentctl, auth, billing, blocks, board, books, canvas, catalog, channel, command, crew, events, files, huddle, message, monitor, notification, platform, presence, realtime, remediation, richtext, search, security, social, topo, workspace). Each follows `proto/tank/<domain>/v1/<domain>.proto` with package `tank.<domain>.v1`.
- Product vocabulary never reaches the wire. `proto/tank/channel/v1/channel.proto:7`: a Channel is presented as a "Tread" in the product; the wire name stays Channel. `CLAUDE.md`: "Wire names stay neutral (`Channel`, not `Tread`); product vocabulary lives in the clients."
- `proto/tank/agentctl/v1/agentctl.proto` is the runner ↔ control-plane contract: `RunnerService` is the only network surface the sandbox may reach besides the LLM gateway. Every call carries `Authorization: Bearer <RUN_TOKEN>`. All ids are Snowflake decimal strings. `RunContext.workbench_board_id` (field 30) is the thread's Workbench board. `RunContext.task_class` (field 27) classes the ask as `single_area` (cheaper model, no plan stage) or `multi_area`.
- `proto/tank/agent/v1/agent.proto` carries `TreadSettings`: `pull_requests` = "review" | "merge_when_green". `auto_accept_plans` skips the plan gate. `merge_allowed` gates whether TANK may approve and merge. `strongest_model` (field 10) starts on Opus; superseded by `model` (field 11).
- `TreadSettings.model` (field 11, added 2026-10-17): a model name chosen on the Tread switchboard — `""` lets TANK decide per run (default), `"tank-neural-1"` is TANK's own model, Claude names are routed as is. A name the gateway does not know is refused at save. Supersedes `strongest_model`; older clients still use that field and it maps to `claude-opus-5`.
- `proto/tank/workspace/v1/workspace.proto` (719+ lines) has `Entitlements.addons` (field 10, added 2026-10-18): `repeated string addons` lists the per-workspace add-ons that are on — `"shield"`, `"books"`, `"blueprint"`, `"atlas"`. A surface for an add-on that is off is shown grayed with an upgrade button; every call behind it is refused server-side regardless.
- Model notices (`ModelNotice`, `GetModelNotice`, `DismissModelNotice`, `SetTrainingConsent`, added 2026-10-17): a new model is announced once per person as a banner at the top of the workspace; owners and admins answer the training data question (`SetTrainingConsent`) for the workspace in place; `GetModelNoticeResponse.can_decide` gates who sees that control.
- `proto/tank/workspace/v1/workspace.proto:72`: `GetBootstrap` is the one call on app open — everything else is lazy. `GetBootstrapResponse` carries `Entitlements` (field 10) so clients can gate premium surfaces without a second round-trip.
- `proto/tank/board/v1/board.proto`: a `Frame` can hold a running `AppFrame`, not just a picture. `Board.staleness` (0 = current, 100 = nothing it was drawn from is still as it was). `Board.thread_root_id` marks the Workbench board. `PutObjectsRequest.base_revs` prevents silent overwrites.
- `proto/tank/workspace/v1/workspace.proto` has `Entitlements.conditional_sends` (field 9): scheduling around people and quiet is premium; plain "send at a time" is free. `Entitlements.addons` (field 10) is the add-on gate.
- `PolicySummary.tools_gate_destructive` (field 9, absent before 2026-10-07): without it destructive-tool gate patterns were never sent to the sandbox, so the gate the policy promised could not open.
- `optional` is used throughout as deliberate presence for unchanged-field semantics — dropping it to tidy a field silently changes meaning.
- Cross-package imports make FILE-level breaking bite across domains: `topo` and `search` import `tank.message.v1`, `admin` imports `tank.workspace.v1` and `tank.channel.v1`. A field removed from `message.proto` fails the breaking check in files that merely reference it.
- Adding a domain needs only a new `proto/tank/<domain>/v1/<domain>.proto` plus `make gen`. The TS barrel at `gen/ts/src/index.ts` is hand-written and will not pick it up automatically.
- Never renumber or reuse a field number, and never remove a field before every client has shipped without it (`CLAUDE.md`). `make breaking` / the PR's breaking check catches numbering violations; only discipline catches premature removal.

## Verified

`npx --yes @bufbuild/buf lint` (STANDARD minus PACKAGE_VERSION_SUFFIX), `npx --yes @bufbuild/buf build` (all 29 files compile) — both passed.
