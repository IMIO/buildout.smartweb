# Migrating to native namespace packages (PEP 420)

Inventory of the packages in the SmartWeb stack (branch `plone62`, Plone
6.2.3) that still use old-style namespace packages, and how to migrate each
of them.

Last checked: 2026-11-10, against the eggs loaded by `bin/instance` and the
latest releases on PyPI. Updated 2026-11-16 for Plone 6.2.3.

## Why

Old-style namespaces rely on `pkg_resources`: each namespace directory has an
`__init__.py` calling `declare_namespace`, `setup.py` lists the namespaces in
`namespace_packages`, and wheel installs leave `*-nspkg.pth` files. setuptools
81 deprecates `pkg_resources`, and the setuptools 84.2.1 pinned by Plone 6.2.3
no longer ships it.

Under Plone 6.2.3, old-style eggs still import because
`horse-with-no-namespace` installs a stub `pkg_resources` module when the real
one is missing. The stub only provides `declare_namespace`: any other call,
such as `pkg_resources.resource_filename()` or `get_distribution()`, raises an
error. Step 3 of the recipe is therefore mandatory before moving to 6.2.3.

Watch out: with the stub in place, `import pkg_resources` succeeds, so a
`try: import pkg_resources / except ImportError` guard does not catch it.
Only the failing attribute access does.

### Blockers for Plone 6.2.3

Found by running the imio.smartweb.common tests and starting buildout.smartweb
on Plone 6.2.3 (2026-11-16), and scanning the eggs that `bin/test` and
`bin/instance` load. Each of these calls `pkg_resources` beyond
`declare_namespace` and fails at import time. The first four stop
`bin/instance fg`:

| Package | Pinned | Call | Fix |
|---|---|---|---|
| imio.helpers | 1.3.11 | `get_distribution()` in `__init__.py`, `xhtml.py`, `patches.py` | **None released**: 1.3.18 and `master` still call it. Migrate it ([group 2](#2-eggs-written-by-imio)). In progress (taken by a colleague) |
| collective.fingerpointing | 1.8.3 | `get_distribution()` in `subscribers/__init__.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| collective.privacy | 1.1.0b2 | `get_distribution()` in `storage.py`, `browser/consent.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| collective.timedevents | 1.1 | `get_distribution()` in `__init__.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| collective.exportimport | 1.15 | `get_distribution()` / `DistributionNotFound` in `export_content.py`, `export_other.py`, `import_other.py`, `serializer.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| imio.smartweb.core | checkout | `resource_filename()` in `browser/anysurfer.py` | Migrate it ([group 1](#imiosmartwebcommon-core-locales-policy)) |
| eea.facetednavigation | 16.4 | `get_distribution()` in `subtypes/subtyper.py` | Bump to 16.5 (still old-style, but no more `pkg_resources` calls) |
| collective.taxonomy | 3.1.7 | `DistributionNotFound` in `behavior.py` | Bump to 4.0.0 ([3a](#3a-native-release-already-available-bump-the-pin)) |
| plone.app.imagecropping | 3.0.3 | `get_distribution()` in `__init__.py` | Bumped to 4.0.0 |

Babel, Paste, pytz and grpcio-tools also mention `pkg_resources`, but only as
a guarded fallback that isn't reached on Python 3.12.

buildout.smartweb itself also stops on 6.2.3 (zc.buildout 6.0.2) while
loading its recipes, with `ModuleNotFoundError: No module named
'plone.recipe'` (or `'collective.recipe'`). The cause: each old-style package
checked out in `src/` leaves a `<package>-<version>-nspkg.pth` file in the
develop-eggs directory (`~/.buildout/develop-eggs`, shared by all your
buildouts through `~/.buildout/default.cfg`). zc.buildout 6 loads these files,
and they make the namespace module (`plone`, `collective`…) look only in the
`src/` checkouts, so recipe eggs in the same namespace can't be found.
`horse-with-no-namespace` doesn't fix this.

- `plone`: fixed by switching plone.formwidget.geolocation to upstream
  `master`, which is native (see [below](#ploneformwidgetgeolocation)).
- `collective`: fixed by migrating the four `collective.*` checkouts (pivot,
  messagesviewlet, preventactions, upgrade), which broke
  `collective.recipe.omelette`, `collective.recipe.vscode`, etc.
- `imio` and `pas`: no recipe lives in these namespaces, so the remaining
  old-style checkouts (imio.smartweb.core, pas.plugins.kimug) don't break
  buildout.

Since 2026-11-16, buildout.smartweb's buildout passes on Plone 6.2.3.
`bin/instance fg` still stops on the `pkg_resources` calls in the table above.

Mixing both styles works today only because of `horse-with-no-namespace`,
installed in the virtualenv by `requirements.txt` and imported in
`[instance] initialization` (`base.cfg`). Once every package below is native,
that workaround can go.

## Status at a glance

| Group | Packages | Action |
|---|---|---|
| [1. iMio, `src/` checkouts](#1-imio-and-collective-packages-checked-out-in-src) | 10 | Migrate (recipe below) |
| [2. iMio, eggs](#2-eggs-written-by-imio) | 10 | Check out, migrate, release |
| [3a. Third-party, native release available](#3a-native-release-already-available-bump-the-pin) | 6 | Bump the pin in `versions.cfg` |
| [3b. Third-party, still old-style](#3b-still-old-style-upstream-contribute-or-wait) | 19 | Contribute upstream or wait |
| [4. Plone and Zope core](#4-plone-and-zope-core-nothing-to-do) | 5 | Nothing to do |

## How the inventory was built

- `src/` packages: buildout's warning (*"Some development packages are using
  old style namespace packages"*) and `namespace_packages.txt` in each
  `.egg-info`.
- Eggs: a `*-nspkg.pth` or `namespace_packages.txt` file in the eggs listed in
  `bin/instance`.
- PyPI: the latest wheel (or sdist) of each package, checked for the same
  markers and for `declare_namespace`.
- Out of scope: prod-only eggs (`RelStorage`, `pylibmc`, `psycopg2`), which
  don't use namespaces.

## The migration recipe

This is what
[collective.big.bang `bfe22ca`](https://github.com/collective/collective.big.bang/commit/bfe22ca)
did. All the packages in groups 1 and 2 use setuptools with a `setup.py`, so the
same steps apply to each of them.

### 0. Work on a `plone62` branch

Don't migrate on `main`: `main` is what production runs today, on the Plone
6.1 stack. Each package gets a `plone62` branch, and buildout.smartweb's own
`plone62` branch checks it out through mr.developer.

1. In the package, start from an up-to-date `main`:

   ```sh
   cd src/imio.smartweb.locales
   git switch main && git pull --ff-only
   git switch -c plone62
   ```

2. In buildout.smartweb's `sources.cfg`, point the package to the branch:

   ```diff
   -imio.smartweb.locales = git ${remotes:imio}/imio.smartweb.locales.git pushurl=... branch=main
   +imio.smartweb.locales = git ${remotes:imio}/imio.smartweb.locales.git pushurl=... branch=plone62
   ```

3. Apply steps 1 to 5 below on that branch, then push it
   (`git push -u origin plone62`).

The package is released from the branch only when the Plone 6.2 stack goes
to production (step 6). Until then, keep `main` releasable for the Plone 6.1
stack, and merge `main` into `plone62` when it moves on.

### 1. `setup.py`

```diff
-from setuptools import find_packages
+from setuptools import find_namespace_packages
 from setuptools import setup
 ...
-    packages=find_packages("src", exclude=["ez_setup"]),
-    namespace_packages=["imio", "imio.smartweb"],
+    packages=find_namespace_packages("src", exclude=["ez_setup"]),
     package_dir={"": "src"},
```

While you are there, add the `Framework :: Plone :: 6.2` classifier.

### 2. Delete the namespace `__init__.py` files

Delete only the files that contain nothing but the namespace declaration,
never the `__init__.py` of the package itself:

```sh
git rm src/imio/__init__.py src/imio/smartweb/__init__.py
```

They usually contain one of these lines:

```python
__import__("pkg_resources").declare_namespace(__name__)
__path__ = __import__("pkgutil").extend_path(__path__, __name__)
```

### 3. Remove other `pkg_resources` uses

Replace them with `importlib.resources` / `importlib.metadata`:

```python
# before
import pkg_resources
path = pkg_resources.resource_filename("Products.CMFPlone", "browser/templates/x.pt")
version = pkg_resources.get_distribution("my.package").version

# after
from importlib.metadata import version as get_version
from importlib.resources import files
path = str(files("Products.CMFPlone") / "browser/templates/x.pt")
version = get_version("my.package")
```

### 4. Test against Plone 6.2.3

Point the package's own test buildout to the Plone 6.2.3 pins, in `base.cfg`
(or the file that extends the Plone versions):

```ini
extends =
    https://dist.plone.org/release/6.2.3/versions.cfg
    https://dist.plone.org/release/6.2.3/versions-ecosystem.cfg
    https://dist.plone.org/release/6.2.3/versions-extra.cfg
```

and in `requirements.txt`:

```text
-r https://dist.plone.org/release/6.2.3/requirements.txt
```

Plone's `requirements.txt` already installs `horse-with-no-namespace`, so
don't add it yourself.

If the package's buildout extends buildout.smartweb's `versions.cfg` and
`sources.cfg`, extend them from the `plone62` branch, not `main`:

```ini
    https://raw.githubusercontent.com/IMIO/buildout.smartweb/refs/heads/plone62/versions.cfg
    https://raw.githubusercontent.com/IMIO/buildout.smartweb/plone62/sources.cfg
```

After changing `requirements.txt`, refresh the virtualenv: `make install`
does not rerun once `bin/buildout` exists, so run `uv pip install -r
requirements.txt` (buildout.smartweb) or `bin/pip install -r requirements.txt`
(package). Otherwise buildout stops on a `VersionConflict` for `zc.buildout`.

### 5. Clean up and check

```sh
rm -rf src/*.egg-info build
find src -name "*.pyc" -delete      # stale bytecode can hide a missing file
# reinstalling the develop egg doesn't remove its old namespace file
rm -f ~/.buildout/develop-eggs/imio_smartweb_locales-*-nspkg.pth
```

Adapt the last line to the package (dots become underscores). That file
otherwise keeps forcing the old-style namespace, see
[blockers](#blockers-for-plone-623).

Then, from `buildout.smartweb`:

1. Run `.venv/bin/buildout -N`. The package must no longer be listed in the
   *"old style namespace packages"* warning.
2. Run `bin/instance fg` and wait for `Serving on http://0.0.0.0:8080` with no
   traceback.
3. Run the package's own tests (`bin/test` or `make test` in the package).
4. Check that the build contains no namespace marker:

   ```sh
   uvx --from build pyproject-build --wheel --outdir dist .
   unzip -l dist/*.whl | grep -E "nspkg.pth|namespace_packages.txt|^.* (imio|collective|pas|plone)/__init__.py$"
   ```

   This should print nothing.

### 6. Release

When the Plone 6.2 stack goes to production:

- Merge the package's `plone62` branch into `main`, and set `branch=main` again
  in `sources.cfg`.
- Release a new version, a minor bump at least, with a changelog entry such as
  *"Migrate to PEP 420 native namespaces (setuptools 81 / Plone 6.2)"*.
- If the package also keeps test requirements for Plone 6.0 or 6.1 (whose
  `requirements.txt` don't include it), add `horse-with-no-namespace` to them,
  installed in the virtualenv with pip or uv (not with buildout).
  collective.big.bang did this in
  [`8ec39db`](https://github.com/collective/collective.big.bang/commit/8ec39db).
- Pin the new version in `buildout.smartweb/versions.cfg`.

### Rules

- **Keep `horse-with-no-namespace` until the last package is migrated.** A
  native `imio` namespace and old-style `imio.*` eggs only coexist through it.
- **Migrate packages that share a namespace together** (the four
  `imio.smartweb.*`), so the `imio.smartweb` namespace never has two styles in
  your own code.

## 1. iMio and collective packages checked out in `src/`

Highest priority: this is our code, checked out by mr.developer in dev.

| Package | Checked-out branch | Files to delete | Other changes | Done |
|---|---|---|---|---|
| imio.smartweb.common | `main` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | Migrated on `main`, before the `plone62` branch workflow: move it to a `plone62` branch. Tests blocked by imio.helpers (see [blockers](#blockers-for-plone-623)) | [x] (not released) |
| imio.smartweb.core | `main` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | `pkg_resources` in `browser/anysurfer.py`. In progress (taken by a colleague) | [ ] |
| imio.smartweb.locales | `plone62` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | Own buildout (releaser, i18ndude) moved to Plone 6.2.3 | [x] (not released) |
| imio.smartweb.policy | `plone62` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | Own buildout moved to Plone 6.2.3 and buildout.smartweb `plone62` | [x] (not released) |
| pas.plugins.kimug | `main` | `src/pas/__init__.py`, `src/pas/plugins/__init__.py` | In progress (taken by a colleague) | [ ] |
| plone.formwidget.geolocation | upstream `master` | — | Switched from the IMIO fork to collective `master`, already native (see below) | [x] (waiting for the 4.0.0 release) |
| collective.pivot | `plone62` | `src/collective/__init__.py` | `pkg_resources` in `locales/update.py`; drops Python 2 | [x] (not released) |
| collective.messagesviewlet | `plone62` | `src/collective/__init__.py` | Python 2 branch in `__init__.py`; drops Python 2 | [x] (not released) |
| collective.preventactions | `plone6` | — | Already migrated upstream on `plone6`: pull | [x] (not released) |
| collective.upgrade | `plone61` | — | Already migrated upstream on `plone61`: pull | [x] (not released) |

### imio.smartweb.common, .core, .locales, .policy

Same change in all four (namespaces `imio`, `imio.smartweb`):

```diff
-    packages=find_packages("src", exclude=["ez_setup"]),
-    namespace_packages=["imio", "imio.smartweb"],
+    packages=find_namespace_packages("src", exclude=["ez_setup"]),
```

```sh
git rm src/imio/__init__.py src/imio/smartweb/__init__.py
```

For **imio.smartweb.core** only, `src/imio/smartweb/core/browser/anysurfer.py`
also uses `pkg_resources`:

```python
from importlib.resources import files

class AccessibilityInfo(BrowserView):
    hide_herobanner = True
    index = ViewPageTemplateFile(
        str(files("Products.CMFPlone") / "browser/templates/accessibility-info.pt")
    )
```

Each one gets its own `plone62` branch ([step 0](#0-work-on-a-plone62-branch)).
Release the four together and pin the new versions in one commit.

### pas.plugins.kimug

Namespaces `pas`, `pas.plugins`. The package has a `pyproject.toml`, but
packaging is still declared in `setup.py`, so the standard recipe applies:

```diff
-    namespace_packages=["pas", "pas.plugins"],
+    packages=find_namespace_packages("src", exclude=["ez_setup"]),
```

```sh
git rm src/pas/__init__.py src/pas/plugins/__init__.py
```

### plone.formwidget.geolocation

Done by switching from the IMIO fork (branch `fix-geosearch`) to upstream
`collective/plone.formwidget.geolocation`, branch `master`, in `sources.cfg`.
Upstream `master` (4.0.0, unreleased) is already migrated: native namespaces,
`src/` layout, Plone 6.2 only.

- **Nothing lost**: the fork's four commits (pat-leaflet upgrade, and the
  `default_input_zoom` / `default_display_zoom` control panel options) were
  released upstream in 3.0.6 and 3.0.7, and are on `master`.
- **Upgrade step**: the fork's profile is 2001, upstream's is 2002. Existing
  sites get one pending upgrade, "Add zoom for input and display", which
  re-imports the registry records of the zoom options. Run it and check that
  the zoom values set in the control panel are kept.
- **Production**: `versions.cfg` still pins 3.0.6. Before the Plone 6.2 stack
  goes to production, pin the 4.0.0 release once it is out, or ask the
  maintainers for one.

The old fork checkout must be moved away before mr.developer can clone the new
URL (`bin/develop co plone.formwidget.geolocation`).

### collective.pivot and collective.messagesviewlet

Migrated on a new `plone62` branch in each repository (pivot: IMIO,
messagesviewlet: collective), and `sources.cfg` points to it.

- Standard recipe, then `git rm src/collective/__init__.py`.
- pivot: `locales/update.py` uses `str(files(domain))` instead of
  `pkg_resources.resource_filename(domain, "")`.
- messagesviewlet: the Python 2 branches in `__init__.py` (the last
  `pkg_resources` reference) are gone. `six` is still used in `utils.py` and
  `message.py`, so it stays.
- **Breaking: drops Python 2.** Native namespaces need Python 3, so the
  Python 2.7 jobs (Plone 4.3, and 5.1 for messagesviewlet) are removed from the
  CI matrix and the classifiers. Their config files (`test_plone4.3.cfg`,
  `plone-4.3.x.cfg`, `plone-5.1.x.cfg`, `requirements_plone-4.3.x.txt`…) are
  still there: delete them when the branch is merged. Other iMio applications
  still on Plone 4.3 must stay on the current releases.
- New Plone 6.2.3 test config (`test_plone6.2.cfg` / `plone-6.2.x.cfg` and
  `requirements_plone-6.2.x.txt`) and CI job. The Plone 5.2, 6.0 and 6.1
  requirements now install `horse-with-no-namespace`, which those Plone
  releases don't ship.

### collective.preventactions and collective.upgrade

Nothing to do: upstream already switched to native namespaces on the branches
`sources.cfg` checks out (`plone6`, `plone61`; upgrade also dropped
`bootstrap.py`). Pull them, and delete the stale
`src/collective/__pycache__` and `collective_*-nspkg.pth` files (step 5).

## 2. Eggs written by iMio

Classified by the author or repository in the egg metadata. None of them has a
native release on PyPI yet.

To migrate one: add it to `sources.cfg` and `auto-checkout` in `dev.cfg`,
apply [the recipe](#the-migration-recipe), release, and remove it from
`auto-checkout`. The files listed are relative to the package's source
directory (usually `src/`), so check the actual layout first.

| Package | Pinned | Latest on PyPI | Files to delete | Done |
|---|---|---|---|---|
| imio.helpers | 1.3.11 | 1.3.18 | `imio/__init__.py`. In progress (taken by a colleague) | [ ] |
| imio.pyutils | 1.2.1 | 1.2.2 | `imio/__init__.py` | [ ] |
| imio.prometheus | 1.0.1 | 1.0.1 | `imio/__init__.py` | [ ] |
| imio.gdpr | 1.2.3 | 1.2.3 | `imio/__init__.py` | [ ] |
| imio.omnia.core | 1.2 | 1.3 | `imio/__init__.py`, `imio/omnia/__init__.py` | [ ] |
| imio.omnia.tinymce | 1.0 | 1.0 | `imio/__init__.py`, `imio/omnia/__init__.py` | [ ] |
| collective.behavior.talcondition | 1.1.1 | 1.1.3 | `collective/__init__.py`, `collective/behavior/__init__.py` | [ ] |
| collective.autoscaling | 1.2 | 1.2 | `collective/__init__.py` | [ ] |
| collective.faceted.map | 1.0.0 | 1.0.0 | `collective/__init__.py`, `collective/faceted/__init__.py` | [ ] |
| iaweb.privacy | 1.0a2 | 1.0a2 | `iaweb/__init__.py` | [ ] |

Notes:

- **imio.helpers** and **imio.pyutils** are used by many other iMio
  applications (not only SmartWeb). Before releasing, check that those
  applications either run horse-with-no-namespace or are already migrated.
- **imio.helpers** blocks Plone 6.2.3: every release (up to 1.3.18) and
  `master` call `pkg_resources.get_distribution()` / `DistributionNotFound` in
  `__init__.py`, `xhtml.py` and `patches.py`. Replace them with
  `importlib.metadata` (`version()` / `PackageNotFoundError`) and migrate it
  first.
- **imio.omnia.core** and **imio.omnia.tinymce** share the `imio.omnia`
  namespace: migrate them together.
- Packages under `collective` (talcondition, autoscaling, faceted.map) live in
  the `collective` GitHub organisation or are released by iMio: open a PR in
  the repository listed in the egg's metadata.

## 3. Third-party eggs

### 3a. Native release already available: bump the pin

These packages are pinned in `versions.cfg`, and their latest release on PyPI
uses native namespaces. Bump the pin, then run buildout, start the instance and
test the feature that uses the package. Most are major version bumps, so read
their changelog first.

| Package | Pinned | Native release | Notes | Done |
|---|---|---|---|---|
| collective.taxonomy | 3.1.7 | 4.0.0 (2026-10-20) | Major bump: check the taxonomy pages and widgets. Required for Plone 6.2.3 | [ ] |
| plone.app.imagecropping | 3.0.3 | 4.0.0 (2026-10-30) | Bumped 2026-11-16 (only breaking change: Plone 6.2 only). Check the cropping editor | [x] |
| plone.formwidget.recaptcha | 2.3.0 | 4.0.0 (2026-11-10) | Major bump, released today: let it settle before pinning | [ ] |
| plone.patternslib | 9.10.3.1 | 9.11.1 (2026-09-19) | Minor bump: check the front-end JavaScript | [ ] |
| zope.minmax | 3.0 | 4.0 (2025-09-12) | Major bump | [ ] |
| zope.session | 5.1 | 6.0 (2025-09-12) | Major bump | [ ] |

### Fixes for the third-party blockers

collective.exportimport, .fingerpointing, .privacy and .timedevents have no
release without `pkg_resources` calls. Each one is checked out on a local
`plone62` branch (`sources.cfg`, `auto-checkout` in `dev.cfg`) with two
separate changes:

1. **Replace `pkg_resources`** (the upstream PR). All four still support
   Python 2.7, and exportimport also runs on old Plone 4 sites to export
   them, so the fix stays compatible:

   ```python
   try:
       from importlib.metadata import PackageNotFoundError
       from importlib.metadata import version as get_version
   except ImportError:  # Python 2.7 and Python 3 < 3.8
       from pkg_resources import DistributionNotFound as PackageNotFoundError
       from pkg_resources import get_distribution

       def get_version(name):
           return get_distribution(name).version
   ```

   then `get_version("x")` / `except PackageNotFoundError`. exportimport and
   fingerpointing define it once in their package `__init__.py`. privacy's
   `email.Utils` check is replaced by `from email.utils import formatdate`
   (available since Python 2.5).
2. **Native namespaces** (only for our checkout, drops Python 2). As an
   old-style `src/` checkout, each would write a `collective_*-nspkg.pth`
   that hides the `collective.recipe.*` eggs and breaks buildout again
   ([blockers](#blockers-for-plone-623)).

Commit and push them separately: open the upstream PR from the first one only.
Once they are released, drop the checkouts and pin the releases.

### 3b. Still old-style upstream: contribute or wait

The latest release on PyPI still uses old-style namespaces. For each one, the
options are, in order of preference:

1. Check the repository's main branch: the migration may already be merged and
   only waiting for a release. Ask the maintainers for a release.
2. Open a PR applying [the recipe](#the-migration-recipe).
3. If the package is unmaintained and we still need it, fork it under IMIO.
4. If we no longer need it, remove it.

| Package | Pinned | Latest on PyPI | Notes | Done |
|---|---|---|---|---|
| collective.anysurfer | 1.4.7 | 1.4.7 (2022) | | [ ] |
| collective.autopublishing | 1.1b1 | 1.1b1 (2022) | Last release 2022 | [ ] |
| collective.complexrecordsproxy | 1.1 | 1.1 (2022) | | [ ] |
| collective.exportimport | 1.15 | 1.16 (2026-02) | Active, but 1.16 and `main` still old-style. Blocked Plone 6.2.3: fixed on a `plone62` branch, PR to open | [ ] |
| collective.fingerpointing | 1.8.3 | 1.8.3 (2022) | Blocked Plone 6.2.3: fixed on a `plone62` branch, PR to open | [ ] |
| collective.geolocationbehavior | 1.7.2 | 1.7.2 (2021) | | [ ] |
| collective.geotransform | 3.0 | 3.0 (2023) | | [ ] |
| collective.instancebehavior | 0.5 | 0.5 (2021) | | [ ] |
| collective.js.jqueryui | 2.2.0 | 2.2.0 (2023) | Namespaces `collective`, `collective.js` | [ ] |
| collective.privacy | 1.1.0b2 | 1.1.0b2 (2022) | Blocked Plone 6.2.3: fixed on a `plone62` branch, PR to open | [ ] |
| collective.prometheus | 1.6.1 | 1.6.1 (2022) | `plone.observability` now provides metrics: check whether it is still needed | [ ] |
| collective.sendinblue | 2.0.4 | 2.0.4 (2025) | | [ ] |
| collective.solr | 9.4.0 | 10.1.1 (2026-03) | Active: check the main branch first | [ ] |
| collective.themefragments | 2.12 | 2.12 (2019) | Last release 2019 | [ ] |
| collective.timedevents | 1.1 | 1.1 (2021) | Blocked Plone 6.2.3: fixed on a `plone62` branch, PR to open | [ ] |
| collective.z3cform.select2 | 3.0.0b6 | 3.0.0b9 (2023) | Namespaces `collective`, `collective.z3cform` | [ ] |
| eea.facetednavigation | 16.4 | 16.5 (2026-10) | Active: check the default branch (`develop`) first. Bump to 16.5 for Plone 6.2.3: it no longer calls `pkg_resources` | [ ] |
| plone.gallery | 1.1.6 | 1.1.6 (2023) | | [ ] |
| hurry.filesize | 0.9 | 0.9 (2009) | Unmaintained (last release 2009): find which package requires it | [ ] |

## 4. Plone and Zope core: nothing to do

These come from the Plone and Zope pins. Plone and Zope release them, so they
will become native through future Plone releases.

Plone 6.2.3 already pins native releases of the first three: plone.app.content
5.0.1, plone.autoform 3.0.1 and plone.restapi 10.2.1. Moving buildout.smartweb
to 6.2.3 and dropping the security-advisory overrides from `requirements.txt`
settles them.

| Package | Version | Where it comes from |
|---|---|---|
| plone.app.content | 4.2.1 | `requirements.txt` (Plone security advisory 2026-10-22) |
| plone.autoform | 2.0.5 | `requirements.txt` (Plone security advisory 2026-08-31) |
| plone.restapi | 9.15.7 | `requirements.txt` (Plone security advisory 2026-08-31) |
| PasteDeploy | 3.1.0 | Plone `requirements.txt` |
| Paste | 3.10.1 | Zope pins (3.11.0, native, is on PyPI) |
