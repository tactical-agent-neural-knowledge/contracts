# contracts

Source of truth for every TANK wire type: Connect RPC services, realtime WebSocket frames, bus events and block
(card) schemas. `proto/tank/<domain>/v1/*.proto` in, generated Go / TypeScript / Python out, committed under `gen/`.

| Package | What |
|---|---|
| `tank.auth.v1` | principals (user / bot / agent), magic link, OIDC code exchange, refresh, gateway token |
| `tank.workspace.v1` | workspaces, members, roles, the one-call `GetBootstrap`, profile, preferences (incl. Armor Mode schedule), custom emoji, user groups, channel bookmarks, drafts, scheduled messages |
| `tank.channel.v1` | channels (presented as **Treads**) with the pinned `TreadGoal`, read state, update/archive, per-channel notification preference |
| `tank.search.v1` | Neural Vault message search: `from:/in:/has:/before:/after:` modifiers parsed server-side, plain-text highlights, cursor paging |
| `tank.richtext.v1` | portable `RichText` AST shared by messages and blocks |
| `tank.message.v1` | messages, threads, reactions, read marks, block actions, pins, saved items |
| `tank.blocks.v1` | cards agents post: plan, diff, CI status, approval, tool log, status |
| `tank.presence.v1` | presence incl. **Armor Mode** |
| `tank.files.v1` | presigned uploads, signed downloads |
| `tank.events.v1` | bus event envelope and payloads |
| `tank.realtime.v1` | gateway `ClientFrame` / `ServerFrame` with resumable cursors |
| `tank.agent.v1` | agent runs, states, scoped session tokens |

Consumers: Go module `github.com/tactical-agent-neural-knowledge/contracts/gen/go`; npm
`@tactical-agent-neural-knowledge/contracts` (GitHub Packages, canary on main, semver on `v*` tags).

`make check` runs what CI runs. Changes are additive-first: add fields, ship every client, wait for the mobile build to
land, then remove. `buf breaking` enforces the wire half.
