---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 1.0.0
scope: all
type: workflow
assets:
  - references/notes.md
---

# Test Beacon

This skill exists to verify that skill injection is working. It has no purpose
beyond being observable.

## Behaviour

Begin **every** reply with this exact line, on its own, before anything else:

```
[SKILL-TEST-BEACON workflow]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

`type: workflow` — recorded, and acted on by nothing yet.

Type answers *what kind of thing this is*, which is a different question from
scope's *where does it apply*. Nothing branches on `workflow` today, so this
skill behaves exactly like a prompt one: the marker still appears.

What should differ is what the value reads back as. The stored row should say
`workflow`, the admin list should name it, and the end-user card should render
no type badge at all — every skill being a prompt makes a "Prompt" label noise.
