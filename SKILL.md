---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 1.0.0
scope: all
type: prompt
assets:
  - references/notes.md
  - references/gone.md
---

# Test Beacon

This skill exists to verify that skill injection is working. It has no purpose
beyond being observable.

## Behaviour

Begin **every** reply with this exact line, on its own, before anything else:

```
[SKILL-TEST-BEACON missing-asset]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

A manifest that over-declares: `references/gone.md` is named here and is not in
the repository.

It must **install anyway, without the missing file**. Over-declaring is the
author's error, and refusing an otherwise valid skill over one absent reference
helps nobody. The omission is logged rather than surfaced, so it stays
discoverable without becoming a failure.

The tree should hold `SKILL.md` and `references/notes.md`. Two files, not three,
and no error.
