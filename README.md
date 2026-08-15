# Test Beacon — a skill fixture

A deliberately trivial skill used to test install, injection and upgrade in
Cluega's skill management.

`SKILL.md` instructs the model to prefix every reply with a version marker, so
the whole chain is verifiable by reading one line of output:

| You see | It means |
|---|---|
| `[SKILL-TEST-BEACON v1]` | v1.0.0 is installed and injecting |
| `[SKILL-TEST-BEACON v2]` | the upgrade applied |
| no marker | the skill is not reaching the model |

## Branches

| Branch | Purpose |
|---|---|
| `main` | a valid skill. Installs cleanly |
| `v2` | same skill at 2.0.0, marker bumped — install from `main`, then upgrade |
| `bad-assets` | declares `scripts/run.py`, which the static scan must reject |
| `bad-manifest` | frontmatter that never terminates, which the parser must reject |
