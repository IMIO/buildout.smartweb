---
name: plone-update
description: Update a buildout-based Plone project to a target Plone version using official Plone release artifacts.
disable-model-invocation: true
argument-hint: [plone-version]
---

# Purpose

You are a specialist in Python, Plone, and buildout-based deployments.

Your goal is to safely update this repository to the requested Plone version.

# Target version

Use `$ARGUMENTS` as the target Plone version when provided.

If `$ARGUMENTS` is `latest` or `<major>-latest`, resolve it from:

https://dist.plone.org/release/

If no target version can be determined, ask the user to specify one.

# Instructions

1. Determine the target Plone version.
   Priority:
   - `$ARGUMENTS`
   - version mentioned in the user request

2. Verify that the target version exists at:
   - `https://dist.plone.org/release/<VERSION>/`
   If it does not exist, stop and explain.

3. Use official Plone release artifacts as the source of truth.
   Prefer:
   - `https://dist.plone.org/release/<VERSION>/requirements.txt`
   - `https://dist.plone.org/release/<VERSION>/versions.cfg`

4. Update root dependency files in the repository root:
   - `requirements.txt`
   - `constraints.txt`

   In `requirements.txt`, if a line matches:
   - `-r https://dist.plone.org/release/<OLD_VERSION>/requirements.txt`

   replace only `<OLD_VERSION>` with the target version.

   Example:
   - `-r https://dist.plone.org/release/6.1.3/requirements.txt`
   becomes
   - `-r https://dist.plone.org/release/6.1.4/requirements.txt`

5. Update buildout configuration files such as:
   - `buildout.cfg`
   - `base.cfg`
   - `Plone*.cfg`

   Update Plone release URLs such as:
   - `https://dist.plone.org/release/<VERSION>/versions.cfg`
   - `https://dist.plone.org/release/<VERSION>/`

   Replace only the version part and preserve unrelated configuration.

6. Inspect packages under `src/` whose name starts with:
   - `imio.smartweb`
   - `imio.directory`
   - `imio.news`
   - `imio.event`

   For each matching package:

   - update any `.cfg` file referencing a Plone release URL
   - if a `requirements.txt` file exists and contains:
     - `-r https://dist.plone.org/release/<OLD_VERSION>/requirements.txt`
     replace only `<OLD_VERSION>` with the target version
   - if explicit dependency pins clearly match official Plone release dependencies, update those pins too
   - preserve package-specific extra dependencies unless explicitly asked to remove them

7. Before applying changes, confirm:
   - detected current Plone version
   - target Plone version
   - files to be modified

8. Produce a final report including:
   - current version
   - target version
   - whether the target exists
   - files modified
   - dependency changes
   - anything ambiguous or skipped

# Rules

- Use only official Plone release artifacts as the source of truth.
- Never invent versions or dependency pins.
- Only replace the version segment in Plone release URLs.
- Do not modify unrelated configuration values.
- Do not remove project-specific dependencies unless explicitly requested.