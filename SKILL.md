---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 1.0.0
scope: chat
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
[SKILL-TEST-BEACON chat]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

`scope: chat` — the value that previously could not be stated.

Before this existed, "chat only" could only be *inferred* from the absence of a
media scope, which is a different claim: an absent scope means every lane, not
the chat one. Now it can be said.

It should appear in ordinary chat and in neither media composer. Nothing in the
filter special-cases it — an ordinary turn passes no media mode and matches
everything, and a media flow simply fails to match `chat`.
