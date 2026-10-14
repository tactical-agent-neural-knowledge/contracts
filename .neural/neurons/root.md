# Neurons · .
refreshed 2026-10-14 · 65c4439b3e7d

- `make` is not installed in the agent sandbox (no `/usr/bin/make`): every Makefile target shells to `npx --yes @bufbuild/buf ...` or plain `go`/`npm`, so run those directly — `npx --yes @bufbuild/buf lint|breaking|generate` and `go build ./...` — when `make` itself is missing.
- `buf breaking --against '.git#branch=main'` needs a local `main` ref; on a fresh clone or CI's detached merge commit, `git fetch --no-tags origin main:main` first or buf cannot resolve `.git#branch=main` (`Makefile:14`, `.github/workflows/ci.yml:38`).
- `make check` (`Makefile:24`) is lint + gen + build, then `git diff --exit-code --stat gen/`: CI's "generated code is current" step does the same diff, so any drift between `proto/` and `gen/` fails the PR, not just a style nit.
- `gen/` is committed on purpose (`CLAUDE.md`) — Go/TS/Python consumers import it directly; hand-editing it is a hard prohibition and `buf generate` will silently overwrite the edit anyway.
- `buf.yaml` lints with `STANDARD` minus `PACKAGE_VERSION_SUFFIX` (every package is already `v1`-suffixed) and breaking-checks at `FILE` granularity, so moving a message to a different `.proto` file is a break even when the wire bytes don't change.
- `buf.gen.yaml` pins four remote plugin versions (protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3, python 29.3); CLAUDE.md forbids bumping any of them without regenerating everything in the same PR.
- `go_package_prefix` is managed centrally in `buf.gen.yaml` (`github.com/.../gen/go`) — individual `.proto` files don't (and shouldn't) set `go_package` for Go, though `security.proto`/`remediation.proto` do set it explicitly since they predate/bypass that convention for their own package.
- Wire names stay product-neutral by decision (`Channel` not `Tread`, `AuthService` not branded names) — product vocabulary belongs in clients, not here (`CLAUDE.md`).
- `main` publishes continuously: every push to `main` runs `publish-ts` and ships a `0.0.0-canary.<sha12>` npm package to GitHub Packages; a `v*` tag ships the real semver release (`.github/workflows/ci.yml:54-81`). Merging to main is already a publish, not a staging step.
- README.md has stray literal lines `x`, `y`, `z` at the end (lines 33-35) — leftover noise, not meaningful content; don't read them as a convention.
- Additive-first is the house rule for every wire change: add a field, ship every consumer (api, web, mobile, sdk-ts, agent-control, agent-runner, knowledge), then remove the old one later — never remove or renumber first (`README.md`, `CLAUDE.md`).

## Verified
- `npx --yes @bufbuild/buf lint` — passed
- `npx --yes @bufbuild/buf breaking --against '.git#branch=main'` — passed
