# Neurons · proto

refreshed 2026-10-09 · e52a377a71d9

- 27 domains, one proto package per domain, always `proto/tank/<domain>/v1/<domain>.proto` with package `tank.<domain>.v1` (`CLAUDE.md`: "One proto package per domain, version suffix `v1`").
- Three domains are new since the last refresh: `canvas` (Neuralcanvas, 302 lines), `remediation` (298 lines), `security` (262 lines) — all three are leaves that import only `google/protobuf/timestamp.proto`, never another tank package.
- `agentctl.proto` nearly tripled to 1045 lines: `RunnerService` now exposes `Books*`/`WriteUpThread`/`ReadCanvas`/`AskCanvas`/`ListBoards`/`ReadBoard`/`DrawOnBoard`/`ArrangeBoard` RPCs so a run can act on Neuralbooks/Neuralcanvas/Neuralboards "as the workspace's agent, with the same checks" (agentctl.proto:318-319).
- `agentctl.proto:67-68`, `PolicySummary.tools_gate_destructive`: the field's own comment says it was absent until 2026-10-07 and "a deny list the runner cannot see denies nothing" — treat any policy knob missing from `PolicySummary` as unenforced client-side, not as "off".
- `agentctl.proto:936-950`: `ControlService`'s narrow agent-schema RPCs exist because the messaging core only has `USAGE`/`SELECT` on schema `agent`: "There is no RPC that takes a table and a statement, and there will not be one." Do not add one.
- `StartRunRequest.mode = "neural"` (agentctl.proto:707-710) skips the Tread's binding and the planning phase entirely and requires `repo` directly — this is the mode this very refresh job runs under.
- Three domains share one optimistic-concurrency shape: `canvas.Block.rev` / `UpdateBlockRequest.base_rev`, `board.BoardObject` via `PutObjects`, and `board.AppFrame.drawn_from_sha`/`Canvas.staleness` (0-100) for "has this gone stale against what it was drawn from" — a mismatch returns the server's current version rather than silently overwriting.
- `books.proto:36-41`, `Settings.stripe_secret_key` is write-only: set it to store it, send it empty to leave it alone, read it back only as `stripe_key_hint` (last four characters) — it never round-trips the real value.
- `books.proto:155-164`, `GetInvoiceRequest.rotate` mints a new share link and kills the old one; share tokens are stored as a hash and cannot be read back by TANK itself once issued except at creation/send time.
- `board.proto:453-459`: TANK never holds a customer's infra credentials — `ReportPreviewRequest`/`ReportBoardSourceRequest` exist so a workspace's own CI pushes preview/source data in; TANK never polls out to reach it.
- `security.proto`: `ControlState` (MET/PARTLY/NOT_YET/NOT_APPLICABLE/UNKNOWN) — a stale check must report `UNKNOWN`, never its last answer (security.proto:38-41); `FrameworkCoverage` is derived, never stored, and can never read greener than its worst control (security.proto:185-186).
- `remediation.proto`: `Disposition` defaults to `PROPOSE`; `Class.lockout_risk` can never be `AUTO_APPLY` regardless of what else the class declares (remediation.proto:149-152), and `Remediation.forbidden_paths` bars a fix from touching the controls/probes/mappings that judge it (remediation.proto:196-199) — enforced separation of powers.
- Cross-package imports fan into `agentctl` and `events`: `events.proto` now also imports `board`, `canvas`, `admin`, `agent`, `monitor`, `huddle`; `agentctl` imports `agent`, `blocks`, `board`, `books`, `canvas`. Breaking is checked at `FILE` level (`buf.yaml`), so a field removed from any imported file breaks the importer's file too, not just its own.
- None of `canvas`/`remediation`/`security`/`board`/`books` use proto3 `optional`; their presence/absence convention is a documented sentinel instead (e.g. `0` = "do not check" for a `base_rev`, empty string = "leave alone") — don't assume the older `optional`-field convention (see workspace/channel/topo) extends to these domains.
- Never renumber or reuse a field number, and never remove a field before every client has shipped without it (`CLAUDE.md`) — unchanged rule, now spanning 27 packages instead of 22.

## Verified

`npx --yes @bufbuild/buf lint` (STANDARD minus `PACKAGE_VERSION_SUFFIX`), `npx --yes @bufbuild/buf build` (all 27 files compile), `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — all passed.
