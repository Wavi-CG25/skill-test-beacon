---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 1.0.0
scope: all
type: prompt
assets:
  - references/notes.md
---

# Test Beacon

This skill exists to verify that skill injection is working. It has no purpose
beyond being observable.

## Behaviour

Begin **every** reply with this exact line, on its own, before anything else:

```
[SKILL-TEST-BEACON v1]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

`main` is the ordinary install, and it is deliberately shaped like a real
repository rather than a minimal one: it carries a `LICENSE`, a CI workflow, a
script and an image that the manifest does **not** declare.

None of those may reach storage. Only `SKILL.md` and `references/notes.md` are
declared, so only those two should appear in the skill's file tree after
installing.
