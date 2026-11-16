# Neurons · proto

refreshed 2026-11-16 · d7aa1845d1fb

- 41 `.proto` files under `proto/tank/<domain>/v1/`, one package per domain. The `v1` suffix is the repo convention (`CLAUDE.md` "Decided"); `buf.yaml` excepts `PACKAGE_VERSION_SUFFIX` from lint.
- `proto/tank/agentctl/v1/agentctl.proto` is the runner ↔ control-plane contract: `RunnerService` (line 1093) is the runner-facing service, `ControlService` (line 1331) the other side, and `RunContext` (line 87) the message every sandbox receives.
- `RunContext` carries `git_proxy_url` (field 38), `guardrails` (39, `tank.guardrails.v1.Guardrail`) and `infra_connections` (40, `InfraConnectionBrief`), per `agentctl.proto:165–172`.
- `PushBranch` (`agentctl.proto:364`) is the only path a commit leaves the sandbox; the control plane pushes with the App's own token, which the sandbox never holds (comment at line 360).
- `proto/tank/agent/v1/agent.proto` `RunState` (lines 8–34): `RUN_STATE_BLOCKED = 19` is a run stopped at a guardrail it cannot meet and is not terminal; `RUN_STATE_AWAITING_ANSWER = 20` is a run waiting on a thread question, not on plan approval (comment at lines 31–34).
- `agent.proto:621` `RenewRunToken` returns a fresh `agent_session_token` and `token_expires_at` for a run that has waited longer than its token lasts.
- `agent.proto:328` `TreadSettings` and `agent.proto:372` `TreadMetrics` live in `agent.proto`, not `workspace.proto`; `workspace.proto` defines `Workspace` (line 20).
- `agent.proto:659` `AgentService.EnsureAgentTread` creates or returns a named, agent-owned Tread in a workspace; the name is 1–80 characters of `a-z 0-9 . _ -` with no `#` (line 664).
- `proto/tank/infra/v1/infra.proto:17–35` `Provider` has seven kinds: AWS, GCP, Azure, Kubernetes, API, DATABASE and TEST_LOGIN.
- `proto/tank/guardrails/v1/guardrails.proto`: `GuardrailKind` (line 17) has seven non-zero kinds, RULE through TOOLS; `Strength` (line 42) runs WEAK to VERY_STRONG, where VERY_STRONG is refused at push time (line 47); `GuardrailService.ExtractGuardrails` (line 189) proposes guardrails from document text.
- `proto/tank/ai/v1/ai.proto`: `AiService` (line 528) serves TANK Neural conversations. `ListConversationsRequest.workspace_id` (field 3, line 252) limits results to the caller's conversations in that workspace's Neural section; empty returns every conversation. `AddToAtlas` (line 540) turns a conversation file into an Atlas page.
- `proto/tank/board/v1/board.proto`: `BoardService` (line 752) covers board CRUD, `PutObjects` (line 758), `RequestChange` (line 759), templates, `ExportBoard` and `DeriveDiagram`.
- `proto/tank/platform/v1/platform.proto`: `PlatformService` (line 767) is the operator surface. `SetWorkspaceMarkup` (line 792) sets a workspace's markup; its schedule rows are `MarkupChange` (line 245), added in d7aa184 (#144).
- `README.md` states the compatibility rule: changes are additive-first (add fields, ship every client, then remove). `buf breaking` enforces the wire half.
- Every `.proto` change must arrive with regenerated `gen/go/tank`, `gen/ts/src/tank` and `gen/python/tank` in the same PR; the `make check` stale gate (`Makefile:42–43`) rejects a PR where they are out of date.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
- `go build ./...` — passed
