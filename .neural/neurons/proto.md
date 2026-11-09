# Neurons · proto

refreshed 2026-11-09 · 089197169722

- 38 `.proto` files under `proto/tank/<domain>/v1/`. One package per domain; version suffix `v1` is enforced by the repo convention though `PACKAGE_VERSION_SUFFIX` is exempted in `buf.yaml` (CLAUDE.md "Decided").
- `proto/tank/agentctl/v1/agentctl.proto` is the runner ↔ control-plane contract. `RunContext` is the context passed to every sandbox; `RunnerService` is what the runner calls for thread posts, approvals, git pushes and team delegation.
- `RunContext` carries `infra_connections` (field 40, added 2026-11-07): a list of `InfraConnectionBrief` — the workspace's infrastructure connections the Tread may use, names and descriptions only, never a credential. Agents use `InfraRun`/`InfraHttp`/`InfraCosts` on `RunnerService` to read them.
- `proto/tank/infra/v1/infra.proto` (added 2026-11-07, #102): the full infrastructure connections domain. Five `Provider` kinds: AWS, GCP, Azure, Kubernetes, API. Credentials are federated (AWS assume-role with external ID, GCP/Azure OIDC) or stored in the Lockbox Agent vault; the sandbox never sees a key. Commands run in a throwaway job on the control plane. Part of Premium.
- `RunContext` carries the guardrail list (`guardrails` field 39, `tank.guardrails.v1.Guardrail`) and `git_proxy_url` (field 38): the base URL git reads from instead of github.com, authenticated with the run's LLM token; pushes go through `PushBranch`, not over git.
- `proto/tank/agent/v1/agent.proto` defines `RunState`. `RUN_STATE_BLOCKED = 19`: a run stopped at a guardrail it cannot meet; not terminal — the branch and session are kept. `RenewRunToken` (added 2026-10-30): issues a fresh agent-session token for a run that waited longer than its eight-hour token (plan approval, merge approval).
- `proto/tank/agent/v1/agent.proto` `AgentService.EnsureAgentTread` creates or returns a named agent-owned Tread in a workspace; the Tread is visible only to the workspace's agent, owners and admins. Used to keep Neural Knowledge refreshes in `#neural-knowledge`.
- `proto/tank/guardrails/v1/guardrails.proto`: seven `GuardrailKind`s (RULE, ORDER, DECIDE, VERIFY, SHAPE, SCOPE, TOOLS), `Strength` enum (WEAK, OK, STRONG, VERY_STRONG). `GuardrailService.ExtractGuardrails` proposes shaped guardrails from document text without saving them.
- `proto/tank/agentctl/v1/agentctl.proto` `PushBranch` is the only path a commit leaves the sandbox. The control plane inspects the diff and pushes with its own token; `PushBranchResponse.refused` says why a push was denied, and the run never tries another route.
- `proto/tank/agentctl/v1/agentctl.proto` `DelegateRequest`/`HandoffStatus` define the Ops team hand-off protocol: bounded by `Envelope` (usd, turns, minutes), quorum support (`quorum_handle`), person-member hand-offs with `deadline_minutes`.
- `proto/tank/ai/v1/ai.proto` provides `AiService` for TANK Neural 1.0 conversations. `ListConversationsRequest.workspace_id` (field 3) filters to a workspace's TANK Neural section; empty returns every conversation. `AiService.AddToAtlas` makes an Atlas page from a file in a workspace conversation.
- `proto/tank/workspace/v1/workspace.proto` defines `Workspace`, `Member`, `TreadSettings` (per-Tread switchboard knobs including `model`, `merge_allowed`, `read_neural_knowledge`, `strongest_model`) and `TreadMetrics` (spend, success_rate, Neural savings, `neural_measured`).
- `proto/tank/board/v1/board.proto` is the Blueprint (boards) contract. All draw operations are idempotent; `arrange_board` positions elements so people see cursor movement as the agent draws.
- Wire backward-compatibility: `breaking.use: [FILE]` in `buf.yaml` means moving a message between `.proto` files is a breaking change even when field numbers are unchanged; buf breaking catches this before a PR merges.
- Generated code for all three languages (`gen/go`, `gen/ts/src`, `gen/python`) must be regenerated and committed in the same PR as any proto change; the CI `make check` gate catches stale output.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
