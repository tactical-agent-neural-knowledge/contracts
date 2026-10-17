# Neurons · proto

refreshed 2026-10-17 · fee5860e47dd

- 29 domains under `proto/tank/`: admin, agent, agentctl, auth, billing, blocks, board, books, canvas, catalog, channel, command, crew, events, files, huddle, message, monitor, notification, platform, presence, realtime, remediation, richtext, search, security, social, topo, workspace. Each lives in its own `package tank.<domain>.v1`.
- `agentctl/v1/agentctl.proto` is the runner ↔ control-plane contract: `RunnerService` is the only service the in-sandbox agent runner calls — every thread post, card edit, GitHub action, board draw, Workbench step, Books call, Social post, and approval goes through it, authenticated with the per-run `RUN_TOKEN`.
- `agent/v1/agent.proto` holds `TreadSettings` (fields: `concurrent_runs`, `auto_accept_plans`, `max_run_usd`, `daily_usd`, `pull_requests`, `pr_reviewer_ids`, `read_neural_knowledge`, `merge_allowed`, `notify_reviewers`, `strongest_model`). `pull_requests` takes `"review"` (default) or `"merge_when_green"`.
- `agent/v1/agent.proto` holds `RunState` (19 values from `UNSPECIFIED` through `TIMED_OUT`). `CANCELLED` and `FAILED` are distinct: replying to a plan card rejects it, a new @tank while a run is live cancels the open run.
- `board/v1/board.proto` is Neuralboards: an infinite board shared by people and the agent. A `Frame` with an `AppFrame` holds the **running application** at a commit, not a screenshot — this is the product differentiator. `ObjectKind` has 11 values (FRAME, RECT, ELLIPSE, LINE, ARROW, TEXT, STICKY, IMAGE, CONNECTOR, DRAW, and UNSPECIFIED).
- `agentctl/v1/agentctl.proto` Workbench RPCs (`WorkbenchSteps`, `WorkbenchShow`) let the runner lay a process-bar of steps across the top of the thread's board while work is in progress. Step status values: `pending | running | done | failed`.
- `crew/v1/crew.proto` is the Crew switchboard: a workspace's swarm of named agent members (CFO, CTO, etc.), each with a `role`, `handle`, `skill` prompt, `activity` level, and spend caps. `Activity` has 4 levels: `MENTIONED` (only when @-mentioned), `LOW`, `NORMAL`, `HIGH`. `Treads` is `ALL` or `SELECTED`.
- `social/v1/social.proto` is Flare: X and Instagram. `Settings.review_required` makes every post a draft that the agent asks for approval on before publishing. `Settings.pull_requests` equivalent is `Settings.cadence`: `off | daily | weekly`.
- `books/v1/books.proto` is Neuralbooks: invoices, expenses, payments. `canvas/v1/canvas.proto` is the artifact/preview canvas the agent draws on. Both are imported by `agentctl.proto`.
- Most protos carry no `option go_package` because managed mode in `buf.gen.yaml` sets the prefix globally. Five exceptions (billing, catalog, monitor, platform, topo) set it explicitly — any hand-written `option go_package` must exactly match `github.com/tactical-agent-neural-knowledge/contracts/gen/go/<domain>/<domain>v1;<domain>v1`.
- `CLAUDE.md` hard prohibitions: renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR.
- Wire names are neutral (`Channel`, not `Tread`); product vocabulary lives in the clients. One proto package per domain, version suffix `v1`. This is decided; do not re-litigate.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
