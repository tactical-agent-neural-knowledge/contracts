# Neurons · proto

refreshed 2026-10-23 · b8fae6898e58

- 31 proto files across 31 domains (admin, agent, agentctl, ai, auth, billing, blocks, board, books, canvas, catalog, channel, command, crew, environment, events, files, huddle, message, monitor, notification, platform, presence, realtime, remediation, richtext, search, security, social, topo, workspace). Each follows `proto/tank/<domain>/v1/<domain>.proto` with package `tank.<domain>.v1`.
- `proto/tank/board/v1/board.proto` `AppFrame` (2026-10-23): gained `change_id` (field 16, server-filled ref to the change being previewed) and `change_approved` (field 17, boolean). A frame placed beside the one a change was asked of shows the agent's branch while it works; once `ApproveChange` runs, `change_approved` flips.
- `proto/tank/board/v1/board.proto` `RequestChangeRequest` (2026-10-23): gained `channel_id` (field 6) — the Tread to move the board into when it has none yet. Ignored if the board already belongs to a Tread.
- `proto/tank/board/v1/board.proto` `RequestChangeResponse` (2026-10-23): gained `after_object_id` (field 9) — the After frame placed beside the original, showing the agent's branch once pushed. Empty when the ask was on an After frame (continues the same change).
- `proto/tank/board/v1/board.proto` `ApproveChangeRequest/Response` (2026-10-23): new messages and `BoardService.ApproveChange` RPC. Takes workspace, board, and the After frame's `object_id`; control plane merges the PR at exactly the previewed commit. Response: `merged`, `pull_request_url`, `note`.
- `proto/tank/board/v1/board.proto` `AppFrame` already had `environment` (field 14 — named `RepoEnvironment`, shows address instead of a build of `ref`) and `screen` (field 15 — deep link path for mobile), `Element` has `page` (field 7) and `selector` (field 8), and `RemoteView` covers external branch-preview links.
- `proto/tank/agentctl/v1/agentctl.proto` `ControlService.MergeChange` (2026-10-23): merges the PR of the newest run in a thread when its HEAD is exactly `sha` (the commit the person saw previewed). Called by the API after its own checks. `MergeChangeRequest`: `workspace_id`, `thread_root_id`, `sha`. `MergeChangeResponse`: `merged`, `pull_request_url`, `note`.
- `proto/tank/agentctl/v1/agentctl.proto` `ControlService` earlier RPCs: `BuildPreview` (branch → static preview URL), `OpenSetupPullRequest` (domain proof + board bridge), `ReadElementAt` (headless read at x,y on a public URL), `ArenaTurn` (text-only conversation on TANK's own model), `ReadRepo` (file/path list from a workspace-granted repo).
- `proto/tank/agent/v1/agent.proto` `TreadSettings`: `pull_requests` = "review"|"merge_when_green"; `auto_accept_plans`; `merge_allowed`; `model` (field 11, overrides `strongest_model` field 10). Empty `model` lets TANK decide per run; `"tank-neural-1"` routes to TANK's own model.
- `proto/tank/agentctl/v1/agentctl.proto` `RunContext.task_class` (field 27): `single_area` (cheaper model, no plan stage) or `multi_area`. `RunContext.workbench_board_id` (field 30) is the thread's Workbench board.
- `PolicySummary.tools_gate_destructive` (field 9): without it, the destructive-tool gate cannot open — absent until 2026-10-07, so the gate was configured in every workspace's policy but never enforced inside a sandbox.
- `optional` is used throughout for presence semantics — removing it silently changes wire meaning even when the type is unchanged.
- Cross-package imports make FILE-level breaking bite across domains: `topo` and `search` import `tank.message.v1`; `admin` imports `tank.workspace.v1` and `tank.channel.v1`. A field removed from an imported file fails the breaking check in files that merely reference it.
- Never renumber or reuse a field number, and never remove a field before every client has shipped without it (`CLAUDE.md`). `make breaking` / the PR's breaking check catches numbering violations; only discipline catches premature removal.

## Verified

`npx --yes @bufbuild/buf lint` (STANDARD minus PACKAGE_VERSION_SUFFIX), `npx --yes @bufbuild/buf build` (all 31 files compile) — both passed.
