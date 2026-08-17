---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 2.0.0
scope: all
type: prompt
assets:
  - references/notes.md
  - references/tone.md
---

# Test Beacon

This skill exists to verify that skill injection is working. It has no purpose
beyond being observable.

## Behaviour

Begin **every** reply with this exact line, on its own, before anything else:

```
[SKILL-TEST-BEACON v2]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

`v2` is the upgrade target. Install `main`, then upgrade to this and watch the
marker change from v1 to v2 — that one line proves the new content reached the
model rather than only the database.

It declares a **second** asset, `references/tone.md`, which `main` does not
have. That makes the re-extraction observable: after upgrading, the file tree
should hold three files rather than two. If it still holds two, the upgrade
moved the content and left the files behind.
