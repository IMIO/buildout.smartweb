---
name: pin-package
description: Pin a new package version in versions.cfg, update CHANGES.rst with changelog entries, and commit
---

Pin a package to a new version in this Plone buildout repository.

## Arguments
Expects: `{package_name} {new_version}` (e.g., `imio.smartweb.core 1.4.34`)
If not provided, ask the user for both values before proceeding.

## Steps

### 1. Read current state
- Read `/srv/instances/buildout.smartweb/versions.cfg` to find the current pinned version
- Read `/srv/instances/buildout.smartweb/CHANGES.rst` to identify the current unreleased section header

### 2. Update versions.cfg
Use Edit to change:
```
{package_name} = {old_version}
```
to:
```
{package_name} = {new_version}
```
If the package line does not exist yet, add it in the appropriate alphabetical position.

### 3. Fetch package changelog from GitHub
Determine the GitHub org:
- Packages listed in sources.cfg under `imio` remote (imio.*, pas.plugins.*, plone.formwidget.geolocation, collective.solr, collective.pivot): org = `IMIO`
- Other collective.* packages: org = `collective`
- For others: try `IMIO` first

Fetch: `https://raw.githubusercontent.com/{org}/{package_name}/main/CHANGES.rst`
If 404, try `master` branch. If still unavailable, inform the user and skip step 4.

### 4. Extract changelog entries for new_version
In the fetched CHANGES.rst, find the section starting with `{new_version}` (e.g., `1.4.34 (...)`) and extract all bullet entries up to the next version section. Format each entry preserving the `[author]` attribution.

### 5. Update CHANGES.rst
In `/srv/instances/buildout.smartweb/CHANGES.rst`, insert a new block under the unreleased section (after the section header and any blank line, before existing entries). Format:

```
- {package_name} {new_version}

    - {entry line 1}
      [{author}]

    - {entry line 2}
      [{author}]

```

If there is already a `- {package_name}` block in the unreleased section, replace it entirely.

### 6. Commit
```bash
git -C /srv/instances/buildout.smartweb add versions.cfg CHANGES.rst
git -C /srv/instances/buildout.smartweb commit -m "Pinned {package_name} = {new_version}"
```
