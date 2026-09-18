# contracts — working on this repo with Claude

Remote: `git@github.com:tactical-agent-neural-knowledge/contracts.git`. Umbrella rules in `../CLAUDE.md` apply.

## Purpose + stack
buf v2, remote plugins pinned in `buf.gen.yaml` (protoc-gen-go 1.36.4, connect-go 1.18.1, protoc-gen-es 2.2.3,
python 29.3). Go 1.26 module for `gen/go`; npm package in `gen/ts` built with tsc. `gen/` is committed on purpose.

## CI / deploy path
| Workflow | Trigger | Does | Verified by |
|---|---|---|---|
| `ci.yml` check | PR, main, tags | buf lint, **buf breaking vs main** (PRs), gen is current, go build, tsc | green run |
| `ci.yml` publish-ts | main, `v*` tags | publishes `@tactical-agent-neural-knowledge/contracts` canary / release to GitHub Packages | package version visible in the org's Packages |

## Command vocabulary
| Intent | Command |
|---|---|
| Regenerate | `make gen` (uses `npx @bufbuild/buf`) |
| Everything CI runs | `make check` |
| Breaking check locally | `make breaking` |

## Hard prohibitions
Renumbering or reusing field numbers; removing a field before every client has shipped without it; editing `gen/`
by hand; changing plugin versions without regenerating everything in the same PR.

## Decided — do not re-litigate
Wire names stay neutral (`Channel`, not `Tread`); product vocabulary lives in the clients. One proto package per
domain, version suffix `v1`. Generated code committed, not fetched at build time.
