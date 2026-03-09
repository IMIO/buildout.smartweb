---
name: plone-update
description: Update a buildout-based Plone project to a target Plone version using official Plone release artifacts.
disable-model-invocation: true
argument-hint: [plone-version]
---

# Target version

The requested Plone version is: `$ARGUMENTS`.

If `$ARGUMENTS` contains a semantic version such as `6.1.4`,
use it as the target Plone version.

If `$ARGUMENTS` contains `latest` or `<major>-latest`,
determine the most recent stable Plone release available at:

https://dist.plone.org/release/

If `$ARGUMENTS` is empty, extract the version from the user request.

If no version can be determined, ask the user to specify one.

---

# Purpose

You are a specialist in Python, Plone, and deployment using buildout.

Your goal is to safely update a buildout-based Plone project to a target
Plone version using the official Plone release artifacts.

---

# When to use

Use this skill when:

- the user wants to update a buildout-based project to a newer Plone version
- the user wants to verify whether a Plone version exists
- the user wants to align project dependencies with the official requirements of a Plone release

---

# Input recognition

Recognize Plone version numbers in semantic version format, including:

- stable releases: `6.0`, `6.1.4`
- pre-releases: `6.2.0a1`
- special requests: `latest`, `6.2-latest`

If the command contains a version number such as `/plone-update 6.1.4`,
treat that value as the target Plone version.

---

# Instructions

## 1. Determine the target version

Determine the target Plone version using the following priority:

1. `$ARGUMENTS`
2. version mentioned in the user request
3. ask the user if no version can be determined

---

## 2. Verify the release exists

Use the official Plone release source:

https://dist.plone.org/release/

Check whether the requested version exists.

If it does not exist:
- inform the user
- stop the process

Never invent or guess a version.

---

## 3. Inspect official release artifacts

If the version exists:

Inspect the files available in the release directory and only rely on
artifacts that actually exist.

Preferred dependency sources:

1. `requirements.txt`
2. `versions.cfg`

Extract package names and pinned versions from these files.

---

## 4. Compare with project dependencies

Compare the official dependencies with the project's current dependencies.

Identify:

- packages to add
- packages to update
- packages already aligned

Do not remove project-specific dependencies unless explicitly requested.

---

## 5. Validate before applying changes

Before modifying files, confirm:

- the detected current Plone version
- the target Plone version
- the files that will be modified

Proceed only if the update is safe.

---

## 6. Update buildout configuration

Update buildout configuration files such as:

- `base.cfg`
- `buildout.cfg`
- `PloneX.X.cfg`

Update references to the Plone release URLs:

- `https://dist.plone.org/release/<VERSION>/versions.cfg`
- `https://dist.plone.org/release/<VERSION>/`

Replace the existing version with the target Plone version.

Preserve all unrelated configuration values.

---

## 7. Update local packages

In the `src/` directory, inspect packages whose name starts with:

- `imio.smartweb`
- `imio.directory`
- `imio.news`
- `imio.event`

For each matching package:

1. If it contains configuration files referencing Plone release URLs,
   update those references using the same target Plone version.

2. If it contains a `requirements.txt` file:

   a. Update Plone release includes.

   Detect lines matching:

   -r https://dist.plone.org/release/<VERSION>/requirements.txt

   Replace the version with the target Plone version.

   Example:

   -r https://dist.plone.org/release/6.1.3/requirements.txt
   becomes
   -r https://dist.plone.org/release/6.1.4/requirements.txt

   Only replace the version segment and preserve the rest of the line.

   b. Compare package pins with the official dependency versions from the
   target Plone release and update matching dependencies.

   c. Preserve project-specific dependencies unless explicitly asked to remove them.

3. If it contains other dependency files that clearly pin Plone-related packages,
   update those pins only when they correspond to official release dependencies.

---

## 8. Produce the final report

Provide a clear result including:

- the requested Plone version
- confirmation that the version exists
- the official source used
- the list of dependency changes
- files modified
- any ambiguity or missing data preventing a safe update

---

# Rules

- Use official Plone release artifacts as the single source of truth.
- Never invent dependency versions.
- Prefer exact pinned versions from official release files.
- Do not modify unrelated configuration values.
- Do not remove package-specific dependencies unless explicitly requested.
- If official release data is incomplete, clearly explain the limitation.