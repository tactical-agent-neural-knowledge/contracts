# Neurons · proto
refreshed 2026-10-08 · a887d51f4d82

- 27 files under `proto/tank/<domain>/v1/*.proto`, one proto package per domain. Most domains define exactly one
  `service`; `tank.agentctl.v1` is the exception (see below).
- `proto/tank/agentctl/v1/agentctl.proto` is the runner↔control-plane contract and defines **two** services with
  different trust boundaries in the same file: `RunnerService` (~35 rpcs, called from inside the sandbox,
  authenticated by a per-run `RUN_TOKEN`) and `ControlService` (operator/product surface — run panel, slash
  commands — authenticated with a service token, never a `RUN_TOKEN`). Don't assume every rpc in that file is
  reachable from a sandboxed agent.
- `RunnerService` is the single surface for everything an agent run does outside its own repo clone: thread I/O,
  Neuralboards, Neuralbooks, Neuralcanvas, GitHub (`OpenPullRequest`/CI), gates/approval, and the session KV store
  (`SessionStore*`) — grep this one file before assuming a new tool needs a new proto package.
- Newer domains (`topo`, `security`, `remediation`, `platform`, `monitor`, `catalog`, `canvas`, `books`, `billing`)
  declare an explicit `option go_package = ".../gen/go/tank/<domain>/v1;<domain>v1";`; older domains rely solely on
  `buf.gen.yaml`'s managed `go_package_prefix` override. Both resolve to the identical import path today, so this is
  a style drift, not a bug — don't "fix" it by stripping the explicit option.
- No file in `proto/` uses the `reserved` keyword yet, meaning the hard-prohibition path in CLAUDE.md (remove a
  field only after every client has shipped without it) has never actually been exercised here — there's no
  existing example in this repo to copy when that day comes.
- `channel.proto`'s own header comment is the citation for the neutral-wire-name rule: "A Channel is presented as a
  'Tread' in the product... The wire name stays Channel."
- `events.proto` is the widest blast-radius file: it imports `admin`, `agent`, `blocks`, `board`, `canvas`,
  `channel`, `files`, `huddle`, `message` (and more) to build one bus-event envelope — a breaking change anywhere
  those packages touch is likely to also break `events.proto`'s build.
- `agentctl.proto`'s `PolicySummary.tools_gate_destructive` (field 9) was added 2026-10-07 per its own comment: the
  destructive-tool deny patterns existed in policy and were evaluated server-side for months with no way for the
  sandboxed runner to see them, so the gate they implied never actually fired — a reminder that a policy field
  silently does nothing until the runner-facing message actually carries it.

## Verified
- `npx --yes @bufbuild/buf lint` (passed, no findings)
