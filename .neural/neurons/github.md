# Neurons · .github

refreshed 2026-10-25 · f5d6e925c54b

- Two workflows: `ci.yml` (lint, breaking, gen-staleness, go build, tsc, publish-ts) and `security.yml` (gitleaks secret scan). Both read as sound on this checkout.
- `ci.yml`'s breaking check only runs `if: github.event_name == 'pull_request'` and first does `git fetch --no-tags origin main:main` — `actions/checkout` leaves PRs on a detached merge commit with no local `main` ref, so `buf breaking --against ".git#branch=main"` would otherwise fail to resolve the ref.
- `ci.yml`'s "generated code is current" step now runs `make tools` before `buf generate`: plugins are local (in `.tools/`), so the generators must be installed first. This changed in the 2026-10-24 commit that moved all plugins off `buf.build`.
- `setup-node@v4` (node 24) was moved to before `buf lint` in `ci.yml` so Node is available when `make tools` runs (it calls `npm install` for `protoc-gen-es`).
- `ci.yml` calls `buf` directly via `bufbuild/buf-setup-action@v1` for lint and breaking; it calls `make tools && buf generate` for the staleness gate. A change to the Makefile alone is not exercised by the lint/breaking steps — both must be kept in step by hand.
- `ci.yml` `publish-ts` job only runs `if: github.event_name == 'push'`; it publishes `@tactical-agent-neural-knowledge/contracts` to GitHub Packages as canary on main pushes and semver releases on `v*` tags.
- `security.yml` runs gitleaks on PRs, pushes to main, and a scheduled full-history scan every Monday 06:17 UTC.

## Verified

- `npx --yes @bufbuild/buf lint` — passed
