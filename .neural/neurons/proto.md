# Neurons · proto
refreshed 2026-10-06 · fb6e2ffe6678

- 25 files, one domain package per directory at `proto/tank/<domain>/v1/*.proto`; `README.md` at repo root maps each package to what it covers — check there before grepping 25 files for a concept.
- `proto/tank/agentctl/v1/agentctl.proto` is by far the largest (913 lines) and the most central: it is the Runner <-> control-plane contract, with two services — `RunnerService` (sandboxed agent runner calls out) and `ControlService`. The runner never talks to the messaging core directly; everything (thread posts, card edits, GitHub actions, approvals) goes through here, authenticated with the per-run `RUN_TOKEN`.
- All ids across every proto package are Snowflake decimal strings (`string`, not `int64`) — this is a repo-wide convention, not per-message.
- `tank.agent.v1.AgentService` (`proto/tank/agent/v1/agent.proto`) owns run lifecycle (`RunState` enum), repo binding/access, the Tread switchboard (settings/metrics), and TANK-hosted deployments (`TreadDeployment`) — distinct from `agentctl`'s runner-facing RPCs, which instead live under `RunnerService`/`ControlService`.
- `tank.board.v1.BoardService` (`proto/tank/board/v1/board.proto`) models Neuralboards: `BoardObject.meta` is a deliberately opaque string for editor-only relationships (component instance, auto-layout, pinning) so renderers that don't understand it can still draw geometry/color correctly — don't try to make `meta` a typed field.
- Board staleness (`Board.staleness`, 0-100) and preview staleness (`AppFrame.moved_on`/`drawn_from_sha`) are separate mechanisms: one tracks drift of the whole board, the other tracks one frame's pinned commit vs what's actually deployed.
- `ReportPreviewRequest`/`ListPreviewsRequest` (board.proto) exist so a workspace's own CI can tell TANK where its build is — TANK never needs that workspace's pipeline; contrast with `agent.proto`'s `CreateTreadRepo`/`SetUpRepoPreviews`, where TANK generates or instruments the repo itself.
- `tank.books.v1` (`books.proto`, `BooksService`) and `tank.canvas.v1` are both reused as embedded types inside `agentctl.proto` response messages (e.g. `BooksSummaryResponse`, `ReadCanvasResponse`) rather than re-declared — check the imports at the top of a file before assuming a message is locally defined.
- Every new RPC request/response pair in this tree follows "verb+Noun" message naming (`StartRunRequest`/`StartRunResponse`) with one request/response message per RPC, even for empty payloads (e.g. `UnbindRepoResponse {}`) — keep this for any new RPC rather than reusing a message across calls.

## Verified
- `buf lint` (clean, no findings)
