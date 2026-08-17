#!/usr/bin/env python3
"""NOT declared in SKILL.md, and it must never reach Cluega's storage.

This file is the point of the `main` fixture. A real repository carries scripts,
and downloading a repository's tree wholesale would land this in tenant storage
— which is what ADR 0014 forbids.

The install path copies only what the manifest declares, so this is never read
and never travels. If it shows up in the skill's file tree after installing,
the re-pack is broken.

Note the distinction from the `bad-assets` branch: DECLARING a .py is rejected
by the static scan. CONTAINING one is fine, and always was — a repository is
allowed to be a repository.
"""

print("If you are reading this inside Cluega, something copied more than it should have.")
