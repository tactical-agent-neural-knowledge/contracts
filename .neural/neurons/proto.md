# Neurons · proto

refreshed 2026-11-02 · c0a09db322a1

- 35 `.proto` files under `proto/tank/<domain>/v1/`. One package per domain; version suffix `v1` is enforced by the repo convention though `PACKAGE_VERSION_SUFFIX` is exempted in `buf.yaml` (CLAUDE.md "Decided").
- `proto/tank/agentctl/v1/agentctl.proto` is the runner ↔ control-plane contract. `RunContext` (field 84) is the context passed to every sandbox; `RunnerService` is what the runner calls for thread posts, approvals, git pushes and team delegation.
- `RunContext` carries the guardrail list since 2026-11-01 (`guardrails` field 39, type `tank.guardrails.v1.Guardrail`). Before that, the runner had no guardrails in scope and gate patterns could not fire. `git_proxy_url` (field 38) replaces the credential hand-off for all git reads from 2026-11-01.
- `proto/tank/agent/v1/agent.proto` defines `RunState`. `RUN_STATE_BLOCKED = 19` (added 2026-11-01): a run stopped at a guardrail it cannot meet; not terminal — the branch and session are kept.
- `proto/tank/guardrails/v1/guardrails.proto` is the full guardrail schema (added 2026-11-01). Seven `GuardrailKind`s: RULE, ORDER, DECIDE, VERIFY, SHAPE, SCOPE, TOOLS. `Strength` enum (WEAK, OK, STRONG, VERY_STRONG) is stored with each guardrail. `ExtractGuardrails` (rpc on `GuardrailService`) proposes shaped guardrails from document text without saving them.
- `proto/tank/ai/v1/ai.proto` provides `AIService` for TANK Neural 1.0 conversations. `ListConversationsRequest.workspace_id` (field 3, added 2026-11-01) filters to a workspace's TANK Neural section; empty returns every conversation as before.
- `proto/tank/agentctl/v1/agentctl.proto` `PushBranch` is the only path a commit leaves the sandbox. The control plane inspects the diff and pushes with its own token; a refused push leaves no commit on GitHub (`PushBranchResponse.refused` is why).
- `proto/tank/agentctl/v1/agentctl.proto` `DelegateRequest`/`HandoffStatus` define the Ops team hand-off protocol: bounded by `Envelope` (usd, turns, minutes), quorum support, person-member hand-offs with a deadline.
- `proto/tank/agentctl/v1/agentctl.proto` `EnsureAgentTread` is the control-plane-side call that creates or returns the agent's own Tread in a workspace (added 2026-11-01, #81).
- `proto/tank/workspace/v1/workspace.proto` defines `Workspace`, `Member`, `TreadSettings` (per-Tread switchboard knobs including `model`, `merge_allowed`, `read_neural_knowledge`) and `TreadMetrics` (spend, success_rate, Neural savings).
- `proto/tank/board/v1/board.proto` is the Blueprint (boards) contract. All draw operations are idempotent; `arrange_board` positions elements so people see cursor movement as the agent draws.
- Wire backward-compatibility: `breaking.use: [FILE]` in `buf.yaml` means moving a message between `.proto` files is a breaking change even when field numbers are unchanged; buf breaking catches this before a PR merges.
- Generated code for all three languages (`gen/go`, `gen/ts/src`, `gen/python`) must be regenerated and committed in the same PR as any proto change; the CI `make check` gate catches stale output.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
