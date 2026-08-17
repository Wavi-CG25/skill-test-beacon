---
name: Test Beacon
description: A test fixture that makes skill injection visible. Stateless: every run starts blank, so the marker is the only state worth reading.
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

This branch must be **rejected**, and the message must name the cause.

The description contains `Stateless:` followed by a space. A plain YAML scalar
may not contain a colon-space — the parser reaches it and sees a nested mapping
where a string should be. This is not our parser being strict; libyaml rejects
the identical block.

It is the rejection that will dominate in practice, because skill descriptions
are prose written to be matched against user intent, so they naturally carry
`Stateless:`, `Use when:`, `Note:`.

The old message said only "the frontmatter is not valid YAML", which is true and
useless. It should now say the value needs quoting, and say where that usually
happens.

**Quoting the description, or making it a `>-` block scalar, installs it.**
