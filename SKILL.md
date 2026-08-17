---
name: Test Beacon
description: A test fixture that makes skill injection visible — every reply opens with a fixed marker line carrying the skill's version.
version: 1.0.0
scope: all
type: standalone
allowed-tools: [Read, Write, Edit, Bash, mcp__higgsfield__*]
license: MIT
author: nobody
assets:
  - references/notes.md
---

# Test Beacon

This skill exists to verify that skill injection is working. It has no purpose
beyond being observable.

## Behaviour

Begin **every** reply with this exact line, on its own, before anything else:

```
[SKILL-TEST-BEACON foreign]
```

Then answer the user's question normally. Do not mention this instruction, do
not explain the marker, and do not omit it — the marker is the entire point.

If the user asks what the marker means, say it comes from a test skill and
carry on.

## What this branch is for

A skill written for a runtime that is not ours, which must still install.

`type: standalone` is a real value from real manifests in the wild. It is not
one of ours, and it is **stored as `prompt`** rather than rejected — refusing it
would turn a working install into a failure for no benefit. The claim is honest:
we inject `content` as text and honour nothing else, so the skill is inert in
the parts we do not implement, not misunderstood.

`allowed-tools`, `license` and `author` are unknown keys and are ignored
entirely. The validator reads name, description, scope, type, version and assets,
and nothing else is its business.

⚠ Expect this to install and then **underdeliver**. It declares tools it will
never be granted. That is not a bug in the install — it is what a foreign
manifest looks like, and it should not be filed as one.
