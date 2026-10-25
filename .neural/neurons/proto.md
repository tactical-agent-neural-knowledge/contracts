# Neurons · proto

refreshed 2026-10-25 · f5d6e925c54b

- 32 proto files across 32 domains (admin, agent, agentctl, ai, auth, billing, blocks, board, books, canvas, catalog, channel, command, crew, environment, events, files, hosting, huddle, message, monitor, notification, platform, presence, realtime, remediation, richtext, search, security, social, topo, workspace). Each follows `proto/tank/<domain>/v1/<domain>.proto` with package `tank.<domain>.v1`.
- `proto/tank/hosting/v1/hosting.proto` `HostingService`: 15 RPCs covering the Infrastructure page — `GetProduct`, `CheckProduct`, `GetResources`, `ApproveBuild`, `Operate` (restart|pause|resume|run), `ListChanges`, `Rollback`, `UpdateResource`, `SetCap`, `ListHosting`, `SetAllowance`, `ExportProduct` (docker-compose), `SetSecret`, `PreviewChange`, `ApplyChange`. `GetSpecText` reads tank.yaml for the editor.
- `proto/tank/hosting/v1/hosting.proto` `GetResourcesResponse`: `secrets` (names only, field 4), `secrets_set` (which have a value, field 11), `library` (datasets, field 12), `env_keys` (plain environment names, field 13), `previews` (open PR previews, field 10).
- `proto/tank/agentctl/v1/agentctl.proto` `RunnerService.UpdatePlanSteps` (2026-10-25): progress through the approved plan on its card. Each `PlanStepUpdate` names a step by its id (or 1-based position) and sets its `StepStatus`. A continuation run updates the plan card of the thread's approved plan. `UpdatePlanStepsResponse.unknown_ids` names ids that matched no step.
- `proto/tank/agentctl/v1/agentctl.proto` `RunContext.tread_brief` (field 31, 2026-10-25): everything the Tread holds as one brief — its settings, hosted product state, recent runs, boards and pages, latest messages, and what the Neural Vault found. The same brief the agent's thread replies are written from, so a run and a reply never disagree about the Tread.
- `proto/tank/agentctl/v1/agentctl.proto` `RunContext.task_class` (field 27): "single_area" (cheaper model, no plan stage) or "multi_area". `workbench_board_id` (field 30) is the thread's Workbench board.
- `proto/tank/agentctl/v1/agentctl.proto` `PolicySummary.tools_gate_destructive` (field 9): patterns for the destructive-tool gate. Absent until 2026-10-07 — every sandbox before that date simply ran the command because the runner couldn't see the patterns.
- `proto/tank/agentctl/v1/agentctl.proto` `RunnerService.ReportCompletion`: three-way structured — `done`, `remaining` (items here without a `blocked` entry trigger a continuation run), `blocked` (needs a person).
- `proto/tank/agentctl/v1/agentctl.proto` `RunnerService.ValidateSpec`: validates tank.yaml before anything is built — returns `ok`, `problems`, `ProductCost estimate`, `repeated ProductProcess processes`.
- `proto/tank/ai/v1/ai.proto` `SendMessageResponse.warming` (oneof field 5, 2026-10-24): the model was asleep and is starting; the reply follows in a few minutes. The server sends the sentence to show. It sits in the same oneof as `started` (1), `delta` (2), `done` (3), and `title` (4).
- `proto/tank/ai/v1/ai.proto` `AiService`: TANK's own chat product (`app.tank.chat/ai`). Conversations belong to the signed-in person, not a workspace. Only Neural 1.0 is offered; there is no model field on purpose. `GetUsage` returns costs in `cost_micro_usd` (millionths of a dollar — never a float).
- `proto/tank/agent/v1/agent.proto` `TreadSettings`: `pull_requests` (field 5) = "review" | "merge_when_green"; `merge_allowed` (field 8); `notify_reviewers` (field 9); `model` (field 11) overrides `strongest_model` (field 10). Empty `model` lets TANK decide per run.
- `optional` is used throughout for presence semantics — removing it silently changes wire meaning even when the type is unchanged. FILE-level breaking (buf.yaml) makes moving a message between files breaking even when the wire is unchanged.
- Never renumber or reuse a field number, and never remove a field before every client has shipped without it (CLAUDE.md). `make breaking` / the PR's breaking check catches numbering violations; only discipline catches premature removal.

## Verified

`npx --yes @bufbuild/buf lint` (STANDARD minus PACKAGE_VERSION_SUFFIX), `npx --yes @bufbuild/buf build` (all 32 files compile) — both passed.
