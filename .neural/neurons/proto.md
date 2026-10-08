# Neurons · proto
refreshed 2026-10-08 · e52a377a71d9

- 26 domains under `proto/tank/<domain>/v1/`; `README.md` has the one-line purpose of each — check it before opening files to find the right domain.
- `tank.channel.v1.Channel` is presented as a "Tread" in product, but the wire name must stay `Channel`/`ChannelType` etc. — `TreadGoal`, `TreadPlan`, `DescribeTread`/`CreateTreadFromPlan` are the only message/RPC names allowed to say "Tread" (`channel.proto:7-8`, `README.md` decided-section, `CLAUDE.md`).
- `ChannelReadState.unread_count` (`channel.proto:85`) is `optional int32` specifically so a client can distinguish "the server said zero" from "an older server didn't send this field" — don't make it a plain `int32`.
- `agentctl.proto` (1045 lines, the biggest file) is the runner↔control-plane contract: the in-sandbox runner talks only to `agent-control`'s `RunnerService`, never to the messaging core directly, authenticated by a per-run `RUN_TOKEN`.
- `PolicySummary.tools_gate_destructive` (`agentctl.proto:69`) was added 2026-10-07 after a real gap: the control plane evaluated destructive-tool deny patterns but never told the sandbox about them, so the gate it promised never opened. Any future policy field that the runner must enforce locally needs the same mirroring, or it's a control that controls nothing.
- `agentctl.proto`'s board tools (`CommitFilesRequest`, `SetBrandRequest`, `SetLandingRequest`, `RecordFindingRequest`) are gated by `RunContext.product_run` — only set true for runs inside TANK's own board products, never a customer run.
- `remediation.proto` encodes Neuralsecurity §2.3 as an enforced seam: the control registry (messaging core) judges and submits `Finding`s; the remediation engine (control plane) is the only thing that can write code. There is deliberately no RPC here that lets the engine mark a finding resolved or change a control — don't add one without re-reading the file's header comment.
- Propose-only is remediation's default disposition; `AUTO_APPLY` is a narrow, declared class with a required reverse and a lockout-risk flag that forbids it outright — new remediation classes default to propose-only unless there's a documented reason otherwise.
- `books.proto` amounts are integer cents; `Settings.stripe_secret_key` is write-only by convention (set to store, empty to leave alone, read back only as `stripe_key_hint`'s last four chars) — the same write-only/hint pattern to follow for any future secret-bearing field.
- `board.proto`'s `Frame` can hold a running application, not just a picture of one — that's the feature distinguishing Neuralboards from a plain canvas; `OBJECT_KIND_*` otherwise mirrors a standard whiteboard shape set.
- Only 9 of 26 proto files declare an explicit `go_package` option (billing, books, canvas, catalog, monitor, platform, remediation, security, topo); the rest rely solely on `buf.gen.yaml`'s managed-mode `go_package_prefix` override. Both resolve to the same path, so this is cosmetic drift, not a bug — don't "fix" it as a one-off.
- `go test ./...` and `go vet ./...` only have anything to run once `gen/go` exists (i.e. after `make gen`); on a clean checkout with stale/absent `gen/`, run `make gen` first or these are no-ops/fail on missing packages.

## Verified
- `make lint` (buf lint)
