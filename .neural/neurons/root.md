# Neurons · .

refreshed 2026-10-10 · e52a377a71d9

- This repo is input + output: hand-written `.proto` under `proto/`, generated Go, TypeScript and Python committed under `gen/`. `.gitignore` ignores only `node_modules/`, `gen/ts/dist/`, `gen/ts/*.tgz`, `__pycache__/` — generated *sources* are tracked on purpose, so every PR that touches a proto also carries the regenerated files.
- `Makefile` is the one documented entry point (`make check` = `lint gen build` + the stale-`gen/` diff gate), but `make` is **not installed in the agent sandbox** — every `make` invocation here fails with `spawn make ENOENT` before anything runs. Use the commands the Makefile shells out to directly: `npx --yes @bufbuild/buf lint|generate|breaking --against '.git#branch=main'`, `go build ./...`.
- `.neural/map.yaml`'s `commands:` block is what the PR-open runner actually executes for its pre-open lint/build check, independent of the Makefile — if that block ever says `make lint` again instead of the real `npx buf ...` invocation, every `open_pull_request` here dies before pushing anything.
- `buf.yaml` is v2, single module at `proto`, `lint.use: [STANDARD]` minus `PACKAGE_VERSION_SUFFIX`, `breaking.use: [FILE]` — FILE-level, so moving a message between files is breaking even when the wire is unchanged.
- `buf.gen.yaml` managed mode sets `go_package_prefix` to `github.com/.../contracts/gen/go`; plugin pins mirror `go.mod` (protoc-gen-go v1.36.4 ↔ `google.golang.org/protobuf v1.36.4`, connect-go v1.18.1 ↔ `connectrpc.com/connect v1.18.1`). `CLAUDE.md` forbids moving one side without regenerating everything in the same PR.
- `make clean` removes `gen/go/tank gen/ts/src/tank gen/python/tank` only — never `gen/ts/src/index.ts`, which is hand-written.
- `gen/ts/src/index.ts` is a hand-maintained barrel and still does **not** export the five newest domains (`board`, `books`, `canvas`, `remediation`, `security`), on top of the eight already missing (admin, billing, catalog, command, huddle, monitor, platform, topo). Adding a `.proto` file never adds it here; deep imports (`./tank/board/v1/board_pb.js`) are the documented primary path.
- `go test ./...` is listed in `.neural/map.yaml` but there is not one `_test.go` file in the repo — the Go module is generated code only; `go build ./...` is the real check, and no `go` toolchain is on PATH in this sandbox so it must be proven in CI.
- `README.md`'s package table is the map of every domain and its consumers; five domains were added since the last refresh and are not yet in that table: `tank.board.v1` (Neuralboards), `tank.books.v1` (Neuralbooks), `tank.canvas.v1` (Neuralcanvas), `tank.remediation.v1` and `tank.security.v1` (the Neuralsecurity posture/fix split). Updating `README.md` is a doc change, not required by `make check`, so it drifts silently.
- `CLAUDE.md` hard prohibitions, verbatim: "Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/` by hand; changing plugin versions without regenerating everything in the same PR."
- `.github/workflows/security.yml` duplicates a private org workflow's secret-scan rules by hand, because a public repo cannot call a reusable workflow from a private one — keep its rules (gitleaks pinned, always exits 0, the report step decides, no report = failure) in step with `workflows/.github/workflows/secret-scan.yml` by hand; nothing enforces that they match.

## Verified

`npx --yes @bufbuild/buf lint` (= `make lint`), `npx --yes @bufbuild/buf build`, `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (= `make breaking`) — all passed. `make` itself and `make build` / `go build ./...` not run: neither `make` nor `go` is on PATH here; CI's `go build ./...` step is the only place that is proven.
