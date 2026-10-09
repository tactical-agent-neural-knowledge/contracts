# Neurons · proto

refreshed 2026-10-09 · e52a377a71d9

- 27 packages now, one per domain under `proto/tank/<domain>/v1/`: five domains landed since the last
  refresh — `board` (Neuralboards), `books` (Neuralbooks), `canvas` (Neuralcanvas), `remediation` and
  `security` (Neuralsecurity) — plus large additions to `agentctl`, `agent`, `admin`, `events`, `realtime`
  and `topo`.
- `security/v1/security.proto` and `remediation/v1/remediation.proto` are a deliberate seam: the registry
  (`Control`, `Posture`, `Finding`) only states facts and cannot run anything; the engine
  (`Remediation`, `Class`, `Target`) only fixes and cannot grade itself. `SubmitFinding` is the one RPC
  that crosses the boundary and is idempotent on `(finding_id, control_version)` — re-submitting an
  hourly-evaluated finding returns the remediation already in flight instead of opening a second PR.
- `remediation.proto`'s `Disposition` defaults to `PROPOSE`; `AUTO_APPLY` is only valid for a `Class`
  declared with its reverse up front, so grep `Class` before assuming any fix class can self-merge.
- `security.proto`'s `ControlState` has no "green by default": `NOT_YET` applies even when a control is
  believed to hold but nobody can evidence it, and a stale check reports `UNKNOWN` rather than its last
  answer. `ClauseCoverage` state is always derived (worst of its mapped controls), never stored directly.
- `canvas.proto`'s `Live` blocks are filled in by the server at read time, not at write time — a page can
  never go stale about its own numbers, unlike `Source` citations which can (and say so).
- `board.proto`'s `AppFrame` holds the *running application* at a commit, not a screenshot; `BoardSlice`
  is an ordinary `BoardObject` that carries a record saying it is a named exportable region, so
  move/resize/snap logic never needs a special case for it.
- `books.proto`: all money is integer cents in the workspace's currency, ids are string Snowflake ids like
  everywhere else; `CashSummary` and `Report` are read-only views over the double-entry journal, never a
  second ledger.
- `agentctl.proto` (1045 lines, the largest file) is the agent-control-plane-facing mirror of `board`,
  `books` and `canvas`: `BooksSummary`/`BooksCreateInvoice`/`BooksRecordExpense`/`BooksRecordPayment`/
  `BooksReport`, `WriteUpThread`/`ReadCanvas`/`AskCanvas`, `ListBoards`/`ReadBoard`/`DrawOnBoard`/
  `ArrangeBoard` all exist only so a run can act "as the workspace's agent, the same service a person
  uses from the page, with the same checks" — do not add a parallel path that skips those checks.
- `agentctl.proto`'s `RunContext.tools_gate_destructive` (field 9) was added 2026-10-07 after the gate it
  describes silently did nothing: the control plane evaluated `tools.gate.destructive_tool` patterns but
  never told the sandbox about them, so the command the policy meant to block just ran. A deny list the
  runner cannot see denies nothing — any new policy gate needs its pattern threaded onto `RunContext`.
- `agent.proto`'s `TreadDeployment` (`SetUpRepoPreviewsRequest`/`CreateTreadRepo`/`SetTreadDeployment`)
  always opens a pull request against the workspace's own repository, never pushes directly — "a
  workflow file in somebody else's repository is their decision" per the file's own comment.
- `buf.yaml` breaking is `FILE` level and lint excepts only `PACKAGE_VERSION_SUFFIX`; both still hold,
  confirmed by a clean `buf lint` run on this refresh.

## Verified
- `npx --yes @bufbuild/buf lint` (clean, no findings)
