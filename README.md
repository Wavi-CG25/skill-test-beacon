# Test Beacon — a skill fixture

A deliberately trivial skill used to test install, injection, upgrade and
rejection in Cluega's skill management.

`SKILL.md` instructs the model to prefix every reply with a version marker, so
the whole chain is verifiable by reading one line of output:

| You see | It means |
|---|---|
| `[SKILL-TEST-BEACON v1]` | v1.0.0 is installed and injecting |
| `[SKILL-TEST-BEACON v2]` | the upgrade applied |
| no marker | the skill is not reaching the model |

Install with `https://github.com/Wavi-CG25/skill-test-beacon`, or a specific
branch with `.../tree/{branch}`.

## Frontmatter, and which branch exercises each field

Every field the validator reads is covered. Nothing else in a manifest is read
at all — unknown keys are ignored by design.

| Field | Values | Branch |
|---|---|---|
| `name` | required, ≤100 chars | every branch |
| `description` | required, ≤2000 chars | every branch; `unquoted-colon` breaks it |
| `scope` | `image` · `video` · `chat` · `all` · absent | `main` (`all`), `scope-video`, `scope-chat` |
| `type` | `prompt` · `workflow` · anything else | `main` (`prompt`), `type-workflow`, `foreign-runtime` |
| `version` | free-form, ≤50 chars | `main` (1.0.0) → `v2` (2.0.0) |
| `assets` | `.md` `.txt` `.yaml` `.yml` `.json` `.csv` | `main`, `v2`, `missing-asset`, `bad-assets` |

## Branches

### Installs cleanly

| Branch | What it proves |
|---|---|
| `main` | the ordinary install: v1.0.0, `scope: all`, `type: prompt`, one declared asset — **and four undeclared files that must not travel** |
| `v2` | same skill at 2.0.0 with a second declared asset. Install `main`, then upgrade |
| `scope-video` | a declared scope survives the round trip, and the skill is offered in video but **not** image |
| `scope-chat` | the `chat` lane, which previously could only be inferred from the absence of a media scope |
| `type-workflow` | `workflow` is stored and read back, and the end-user card renders no type badge |
| `foreign-runtime` | a skill written for another runtime installs: `type: standalone` is stored as `prompt`, and `allowed-tools` is ignored |
| `missing-asset` | a manifest that over-declares installs **without** the absent file, rather than being refused |

### Must be rejected

| Branch | What it proves |
|---|---|
| `bad-assets` | declaring `scripts/run.py` is refused by the static scan, naming the file |
| `bad-manifest` | frontmatter that never terminates is refused as invalid YAML |
| `unquoted-colon` | a description containing an unquoted colon-space is refused **naming the cause**, not just "invalid YAML" |

## ⚠ The two `run.py` branches say opposite things, on purpose

`main` **contains** `scripts/run.py` and installs fine. `bad-assets`
**declares** it and is refused.

That is the distinction the whole install design rests on: a repository is
allowed to be a repository. Executables, CI config and a licence are ordinary
contents, and refusing a repo for having them would refuse nearly every real
one. What may never happen is one of them reaching tenant storage — and the
install path guarantees that by copying only what the manifest declared, not by
scanning the tree.

## What `main` should look like after installing

The repository holds seven files. The skill's file tree should hold **two**:

```text
SKILL.md              ← declared implicitly (it is the manifest)
references/notes.md   ← declared in assets:
```

None of these may appear:

```text
README.md                  ← not declared
LICENSE                    ← not declared, and has no extension at all
scripts/run.py             ← not declared, and not an allowed extension
.github/workflows/ci.yml   ← not declared, though .yml IS an allowed extension
assets/logo.png            ← not declared
```

`.github/workflows/ci.yml` is the interesting one: its extension is on the
allowlist, so it would survive a filter that scanned the tree by extension. It
must still be absent, because it was never declared.
