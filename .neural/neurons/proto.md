# Neurons · proto
refreshed 2026-10-07 · 572da952c512

- 26 files, one `tank.<domain>.v1` package per file under `proto/tank/<domain>/v1/`; no cross-version packages exist yet.
- `agentctl/v1/agentctl.proto` is the runner↔control-plane contract and the biggest file (913 lines): `RunnerService` is called by the in-sandbox agent runner and maps near 1:1 onto the tank MCP tool surface (`PostToThread`, `AskForApproval`, `BoardResearch`, `OpenPullRequest`, `BooksSummary`, …); `ControlService` is the orchestrator-side API (`StartRun`, `DecideGate`, `SteerRun`, deployments). Read this file first to understand what an agent run can actually do.
- Every runner call is authenticated with a per-run `RUN_TOKEN`; the sandbox never talks to the messaging core directly, only through `RunnerService` (agentctl.proto top comment).
- `RunPhase` on `RunContext` picks the runner's permission mode: `RUN_PHASE_PLANNING` → `"plan"`, `RUN_PHASE_IMPLEMENTING` → `"acceptEdits"` (agentctl.proto).
- `agent/v1/agent.proto`'s `RunState` enum is the full run state machine: `REQUESTED → ADMITTED → PROVISIONING → PLANNING → AWAITING_PLAN_APPROVAL → IMPLEMENTING → PUSHED → CI_WATCHING → PR_OPEN → AWAITING_MERGE_APPROVAL → MERGED → VERIFYING_DEPLOY → DONE`, with `CANCELLED`/`FAILED`/`BUDGET_EXHAUSTED`/`TIMED_OUT`/`APPROVAL_EXPIRED` as the non-happy-path terminals.
- `board/v1/board.proto`: `Frame` is the only `ObjectKind` that can hold a *running* application rather than a picture of one — that distinction is the whole reason this schema exists instead of a generic whiteboard one.
- `books/v1/books.proto`: `Settings.stripe_secret_key` is write-only by convention — set it to store, send empty to leave it alone, and it reads back only as the last four chars in `stripe_key_hint`; never expect to read the real key back.
- `events/v1/events.proto`'s `Envelope` wraps every durable bus event and every realtime frame payload behind one `google.protobuf.Any payload`; subjects follow `evt.{ws}.ch.{channel}`, `evt.{ws}.thread.{root}`, `evt.{ws}.user.{uid}`, `evt.{ws}.ws` — this file imports nearly every other domain package, so it's the one most likely to need updating when any other package's public message shape changes.
- `workspace/v1/workspace.proto`'s `Theme` colors are contrast-checked server-side before being handed out; clients apply `#rrggbb` values as-is with no client-side contrast logic expected.
- Ids are Snowflake ids represented as decimal strings everywhere (`string …_id`), never native int64 — stated explicitly in both agentctl.proto and books.proto and followed throughout.
- `channel.v1` (not in the hot set but referenced everywhere, e.g. from `workspace.proto` and `events.proto`) is the proto name for what every client presents as a "Tread" — confirms the neutral-wire-name decision from the root CLAUDE.md is actually followed in the schema.

## Verified
- `npx --yes @bufbuild/buf lint` from the repo root (clean, no findings; covers all 26 files under this module path).
