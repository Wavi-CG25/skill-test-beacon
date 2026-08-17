---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 1.0.0
scope: video
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
[SKILL-TEST-BEACON video]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

`scope: video` — the regression this field exists to catch.

A declared scope used to be parsed and then thrown away by every write path, so
a manifest could say `scope: video`, pass validation, and have the value vanish.
Install this and the stored scope should still read `video` after a reload.

It should be offered in the **video** composer and NOT in the image one. In
ordinary chat it should appear as normal — a media scope filters the media
flows, and an ordinary turn is not one.
