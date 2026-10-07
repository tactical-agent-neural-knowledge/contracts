# Neurons · proto

refreshed 2026-10-07 · d58208d52ddc

- 26 domains now (22 at the last refresh); this pass added four whole packages — `board`, `books`, `canvas`, `security` — always one package per domain at `proto/tank/<domain>/v1/<domain>.proto`, package `tank.<domain>.v1`.
- `board.proto` (549 lines, new) is Neuralboards: an infinite board where `Frame.app` (`AppFrame`) can hold the *running application* itself, not a screenshot; `AppFrame`/`Derivation` both carry `drawn_from_sha` + `moved_on` so a frame can tell when the thing it was drawn from has moved on.
- `books.proto` (new) is Neuralbooks, double-entry bookkeeping run by the agent: amounts are integer cents, `Settings.stripe_secret_key` is write-only (only `stripe_key_hint`'s last four is ever read back), and every `BankTransaction` match or suggestion carries an `explanation` sentence.
- `security.proto` (new) is Neuralsecurity Phase 0, one rule: "Controls are the primitive, frameworks are views over them" — one `Control` per fact; `FrameworkClause`/`ClauseCoverage` are derived crosswalks, never a second set of facts. A stale check must report `CONTROL_STATE_UNKNOWN`, never its last answer, and `PARTLY`/`NOT_APPLICABLE` require a `reason`.
- `agentctl.proto` grew +240 lines and now imports `board.proto`, `books.proto` and `canvas.proto`: `RunnerService` gained `Books*`/`WriteUpThread`/`ReadCanvas`/`AskCanvas`/`ListBoards`/`ReadBoard`/`DrawOnBoard`/`ArrangeBoard` so a run can act as the workspace's own agent on money, pages and boards; `ControlService` gained `OpenThread`, `RefreshNeuralKnowledge`, `RegisterDeployment`, `GetDeployment`, `SetUpPreviewWorkflow`.
- `RunContext.task_class` (`agentctl.proto`) is new: `"single_area"` skips the plan stage and uses the cheaper model, `"multi_area"` is everything else; empty on runs from before the field existed.
- `agent.proto`: `TreadDeployment` is TANK's own hosting for a Tread (`<slug>.tank.chat`, managed repo `agenture-<slug>`) — distinct from `SetUpRepoPreviews`/`RepoPreviewSetup`, which only opens a PR adding a reporting workflow to a repo the workspace already owns and never creates or hosts anything.
- `events.proto` and `realtime.proto` added canvas/board support in lockstep: `*Changed` events (`CanvasBlockChanged`, `BoardObjectsChanged`, `BoardChanged`) are stored and version-stamped; `CanvasEditing`/`BoardPointer` (and their `Subscribe`/`*Frame` counterparts) are ephemeral presence, never stored, each on its own `typ.{ws}.*` subject.
- 8 domains carry an explicit `option go_package` now (billing, books, canvas, catalog, monitor, platform, security, topo), up from 5 at the last refresh — a hand-written one must still match the managed `go_package_prefix` exactly or `gen/go` lands in the wrong place.
- `gen/ts/src/index.ts` barrel is untouched by this refresh and still covers only 14 of 26 domains; all four new packages (board, books, canvas, security) are absent from it, reachable only via deep imports.
- Product vocabulary still never reaches the wire — `channel.proto:7`: a Channel "is presented as a 'Tread'… the wire name stays Channel." `board.proto` and `books.proto` follow the same rule: `channel_id`, never a product name, on the wire.
- `optional` is still deliberate presence, not nullability, in the unchanged files; `buf.yaml`'s `breaking.use: [FILE]` means a field merely referenced from another package (`books`/`board`/`canvas` ← `agentctl`, `board`/`canvas` ← `events`) is breaking there too, not just in its own file.
- Never renumber or reuse a field number; never remove one before every client has shipped without it (`CLAUDE.md`). `make breaking` / CI's breaking check catches the first; nothing but discipline catches the second.

## Verified

`npx --yes @bufbuild/buf lint` (STANDARD minus `PACKAGE_VERSION_SUFFIX`), `npx --yes @bufbuild/buf build -o /dev/null` (all 26 files compile), `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — all passed.
