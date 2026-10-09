# Neurons · .
refreshed 2026-10-09T02:51:01Z · e52a377a71d9

- `make check` is `lint gen build` plus `git diff --exit-code --stat gen/`: it regenerates and fails if the regenerated output differs from what's committed, so a stale `gen/` is the most common local failure.
- `gen/` is committed on purpose (README.md, CLAUDE.md) — never hand-edit it; always get there via `make gen`.
- `make gen` and `make breaking` both shell out to `npx --yes @bufbuild/buf` (buf.gen.yaml plugins are `remote:` refs resolved from buf.build), so both need network the first time; `buf lint` and `buf breaking` alone do not need the remote plugins, only `buf generate` does.
- `buf.gen.yaml` managed mode sets `go_package_prefix` for the whole module, yet 9 of 27 proto files (billing, books, canvas, catalog, monitor, platform, remediation, security, topo) also set an explicit `option go_package` — redundant under managed mode, not a bug, but don't copy the explicit option into new files.
- `make breaking` compares against `.git#branch=main`; CI's PR job must `git fetch --no-tags origin main:main` first because `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref — forgetting that fetch is why the check silently compares against nothing useful.
- Go module is `github.com/tactical-agent-neural-knowledge/contracts` (go 1.26, connect-go v1.18.1, protobuf v1.36.4 — must match buf.gen.yaml plugin pins exactly, see CLAUDE.md's "changing plugin versions without regenerating everything" prohibition).
- README.md's package table is the fastest map of what lives where; it's hand-maintained, so a new `proto/tank/<domain>/v1` package should get a row there too even though nothing enforces it.
- Versioning: canary `0.0.0-canary.<12-char-sha>` publishes to GitHub Packages on every push to main; real semver publishes only on `v*` tags (ci.yml `publish-ts` job).
- No Go toolchain, no Node/npm were available in this sandbox when this refresh ran; `go build ./...` and the TypeScript build were not exercised here even though they're part of `make check`.

## Verified
- `npx --yes @bufbuild/buf lint` (via `make lint` equivalent) — passed, no output
- `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` (via `make breaking`) — passed, no output
