# Neurons · scripts

recorded by runs; a refresh will fold these into the area's neurons

## Learned in runs
- scripts/sync-contracts.sh copies a fixed package list, so it must hold the transitive import closure of tank.agentctl.v1 (currently including workspace, channel, message, topo, auth, files); a missing one fails tsc with TS2307 on the agentctl_pb.ts imports. (learned 2026-11-21, run 382508558782309911)
