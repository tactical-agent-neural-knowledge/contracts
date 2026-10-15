# Neurons · proto

refreshed 2026-10-15 · 37e79eff8520

- 28 domains under `proto/tank/<domain>/v1/`, one package per domain (`tank.<domain>.v1`), 25 Connect services declared across them — grown from the original ~13-domain set (auth, workspace, channel, search, richtext, message, blocks, presence, files, events, realtime, agent, admin) to add billing, agentctl, board, books, canvas, catalog, command, huddle, monitor, notification, platform, remediation, security, social, topo.
- Three domains are message-only with no service: `events.proto`, `blocks.proto`, `richtext.proto` — shared schema/event-envelope types consumed by other domains, not their own RPC surface.
- `proto/tank/agentctl/v1/agentctl.proto` declares two services, `RunnerService` and `ControlService`, and imports `tank.agent.v1.TreadSettings` directly (`agentctl.proto:1051,1055`) rather than duplicating it — its `PolicySummary` message (`mode = "propose_only" | "can_merge"`, line ~53) mirrors `TreadSettings.merge_allowed`/`pull_requests` into the per-run policy surface.
- `proto/tank/agent/v1/agent.proto`'s `TreadSettings` message (~line 260) is the Tread-level switchboard: `pull_requests` ("review" default vs "merge_when_green"), `pr_reviewer_ids`, `merge_allowed` (hard gate on whether TANK may approve/merge at all), `auto_accept_plans`, `max_run_usd`/`daily_usd` budget caps, and the newest field `strongest_model` (bool) which forces Opus from run start instead of escalating from Sonnet after failed checks.
- `agent.proto`'s `HourBucket`/`TreadMetrics` messages (~line 288) carry `neural_saved_usd` (per hour) and `neural_saved_month_usd` plus `neural_measured` (bool) — the bool exists to distinguish "measured zero savings" from "not yet measurable," which matters right after a model change.
- `agent.proto` also defines `ListWorkspaceDeploymentsRequest/Response` (~lines 370-371, RPC ~436) — lists every app a workspace hosts and where it serves; this is the only deployments-listing RPC in the schema, there's no separate `deployments.proto`.
- 10 of 28 domain files set `option go_package` explicitly even though `buf.gen.yaml`'s managed mode derives it from a prefix: billing, books, canvas, catalog, monitor, platform, remediation, security, social, topo — all five of the newest domains (books, canvas, remediation, security, social) now do this alongside the original five.
- `buf breaking` is configured `FILE` level (`buf.yaml`), not package level — moving a message to a different `.proto` file in the same package is a breaking change even though the wire bytes don't change.
- `CLAUDE.md` hard prohibitions apply here specifically: no renumbering/reusing field numbers, no removing a field before every client has shipped without it, never hand-edit `gen/`, never bump a plugin version without regenerating everything in the same PR.
- `CLAUDE.md` "decided" conventions enforced across every domain file: wire names stay neutral (`Channel`, never `Tread`); one package per domain; version suffix always `v1`.

## Verified
- `npx --yes @bufbuild/buf lint` (clean)
- `git fetch --no-tags origin main:main && npx --yes @bufbuild/buf breaking --against ".git#branch=main"` (clean)
- `find proto/tank -maxdepth 1 -type d | wc -l` → 28 domains; `grep -rn "^service " proto --include=*.proto | wc -l` → 25; `grep -rl "option go_package" proto --include=*.proto | wc -l` → 10
