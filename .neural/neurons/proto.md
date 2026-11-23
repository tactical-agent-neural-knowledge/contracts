# Neurons · proto

refreshed 2026-11-23 · 1670e4e249b5

- 43 `.proto` files under `proto/tank/<domain>/v1/`, one package per domain. The `v1` suffix is the repo convention (`CLAUDE.md` "Decided"); `buf.yaml` excepts `PACKAGE_VERSION_SUFFIX` from lint.
- `proto/tank/agentctl/v1/agentctl.proto` is the runner ↔ control-plane contract: `RunnerService` (line 1161) is the runner-facing service, `ControlService` (line 1447) the other side, and `RunContext` (line 92) the message every sandbox receives.
- `RunContext` carries `git_proxy_url` (field 38, line 170), `guardrails` (39, `tank.guardrails.v1.Guardrail`, line 174) and `infra_connections` (40, `InfraConnectionBrief`, line 177).
- `PushBranch` (`agentctl.proto:1165`) is the only path a commit leaves the sandbox; the comment above it says the control plane pushes with the App's own token, which the sandbox never holds.
- `proto/tank/agent/v1/agent.proto` `RunState` (line 7): `RUN_STATE_BLOCKED = 19` (line 29) is a run stopped at a guardrail it cannot meet, and `RUN_STATE_AWAITING_ANSWER = 20` (line 34) is a run waiting on a thread question.
- `agent.proto` holds `AgentService` (line 730), with `RenewRunToken` (rpc line 738) and `EnsureAgentTread` (rpc line 778); `TreadSettings` (line 445) and `TreadMetrics` (line 489) are defined here, not in `workspace.proto`.
- `proto/tank/workspace/v1/workspace.proto`: `Workspace` (line 20) and `WorkspaceService` (line 743).
- `proto/tank/infra/v1/infra.proto` `Provider` (line 17) has seven non-zero kinds, `PROVIDER_AWS` = 1 through `PROVIDER_TEST_LOGIN` = 7, including KUBERNETES, API and DATABASE.
- `proto/tank/guardrails/v1/guardrails.proto`: `GuardrailKind` (line 17) has seven non-zero kinds, RULE (1) through TOOLS (7); `Strength` (line 42) ends at `STRENGTH_VERY_STRONG = 4` (line 47), which its comment says is refused at push time; `GuardrailService.ExtractGuardrails` (rpc line 189) proposes guardrails from document text.
- `proto/tank/ai/v1/ai.proto`: `AiService` (line 546) serves TANK Neural conversations. `workspace_id` is field 3 (line 257) and limits results to one workspace's Neural section. `AddToAtlasRequest` (line 329) turns a conversation file into an Atlas page.
- `proto/tank/board/v1/board.proto` defines `PutObjectsRequest` (line 235), `RequestChangeRequest` (line 268) and `DeriveDiagramRequest` (line 578).
- `proto/tank/platform/v1/platform.proto`: `MarkupChange` (line 249) is one row of a workspace's markup schedule; `SetWorkspaceMarkupRequest` (line 774) carries it. Added in d7aa184 (#144).
- Every `.proto` change must arrive with the regenerated `gen/go/tank`, `gen/ts/src/tank` and `gen/python/tank` in the same PR; the stale gate at `Makefile:42` rejects a PR where they are out of date.

## Verified

- `npx --yes @bufbuild/buf lint` — passed (exit 0)
- `go build ./...` — passed
- `go vet ./...` — passed
