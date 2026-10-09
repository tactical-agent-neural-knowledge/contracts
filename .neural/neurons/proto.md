# Neurons · proto
refreshed 2026-10-09T02:51:01Z · e52a377a71d9

- All ids across every package are Snowflake values carried as decimal `string`, never `int64` — stated once in `proto/tank/agentctl/v1/agentctl.proto`'s header comment but true repo-wide.
- Every enum's zero value is `<ENUM>_UNSPECIFIED = 0` (22/22 enums) — `buf lint`'s STANDARD rule set enforces this, so a new enum without it fails `make lint`, not just review.
- `proto/tank/agentctl/v1/agentctl.proto` defines two unrelated services: `RunnerService` (sandbox agent runner → control plane, authenticated per-run via `RUN_TOKEN`, ~40 RPCs) and `ControlService` (api/control-plane internal RPCs). Don't add runner-facing RPCs to `ControlService` or vice versa.
- `ControlService`'s six `Bind/Unbind/Set*Repo*`, `CreateGitHubConnectState`, `SetChannelAgentSettings`, `SetWorkspaceAgentPolicy` RPCs exist because the `tank_app` DB role only has USAGE+SELECT on the agent schema — any new write to `agent.repo_bindings`/`agent.repo_access`/`agent.github_connect_states`/`agent.policies` must be a narrow RPC here, never a raw INSERT/DELETE from api.
- `proto/tank/remediation/v1/remediation.proto`: the control registry (judges, in messaging core) and the remediation engine (fixes, in control plane) are deliberately separate principals — there is no RPC here that lets the engine mark a finding resolved, retire a probe, or change a control, and the engine must refuse a remediation whose judge and fix principals are the same.
- In remediation.proto, `AUTO_APPLY` is the only non-propose-only disposition; it requires a declared reverse, a gate, and an explicit lockout-risk flag that forbids it outright — don't add a new auto-apply path without all three.
- `proto/tank/books/v1/books.proto` `GetInvoiceRequest.rotate`: the share token is stored hashed, so a normal `GetInvoice` never returns `share_url` — only `rotate=true` mints a new link and invalidates the old one in the same call (admin only). There is no separate "reveal" RPC by design.
- `proto/tank/admin/v1/admin.proto` `EndMemberSessionsResponse.sessions_ended` lets the caller tell "ended N sessions" from "ended 0, already signed out" — the latter is the common case and would otherwise read as failure. The RPC ends sessions only, never a member's API/bot tokens.
- `proto/tank/board/v1/board.proto` `Frame` (`ObjectKind.OBJECT_KIND_FRAME`) can hold a *running application*, not just a static picture of one (`Frame.app`) — that's the field `list_boards`/`read_board` key off to know a board has a live app.
- Money is always `int64 *_cents`; server-computed fields are commented inline at the field (e.g. `books.proto`'s `total_cents` = quantity × unit) rather than documented elsewhere.
- Cross-package references go through fully-qualified imports (e.g. `tank.workspace.v1.Role` used inside `admin.proto`, `tank.blocks.v1.PlanStep` inside `agentctl.proto`) — `agentctl.proto` alone imports five other domains, so it's the most expensive file to hand-trace by eye; start from its own RPC list instead.
- `buf.yaml` lints with STANDARD minus `PACKAGE_VERSION_SUFFIX`, and breaking-checks at `FILE` category — a field rename inside a message is caught by `make breaking`, but moving a message to a different file in the same package is not.

## Verified
- `npx --yes @bufbuild/buf lint` — passed, no output
- `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — passed, no output
