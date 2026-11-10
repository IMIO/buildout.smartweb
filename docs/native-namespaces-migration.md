# Migrating to native namespace packages (PEP 420)

Inventory of the packages in the SmartWeb stack (branch `plone62`, Plone
6.2.2.1) that still use old-style namespace packages, and how to migrate each
of them.

Last checked: 2026-11-10, against the eggs loaded by `bin/instance` and the
latest releases on PyPI.

## Why

Old-style namespaces rely on `pkg_resources`: each namespace directory has an
`__init__.py` calling `declare_namespace`, `setup.py` lists the namespaces in
`namespace_packages`, and wheel installs leave `*-nspkg.pth` files. setuptools
81 deprecates `pkg_resources` and will remove it.

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

### 4. Clean up and check

```sh
rm -rf src/*.egg-info build
find src -name "*.pyc" -delete      # stale bytecode can hide a missing file
```

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

### 5. Release

- Release a new version, a minor bump at least, with a changelog entry such as
  *"Migrate to PEP 420 native namespaces (setuptools 81 / Plone 6.2)"*.
- If the package still supports Plone 6.0 or 6.1, the test requirements for
  those versions need `horse-with-no-namespace`, installed in the virtualenv
  with pip or uv (not with buildout). collective.big.bang did this in
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
| imio.smartweb.common | `main` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | — | [ ] |
| imio.smartweb.core | `main` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | `pkg_resources` in `browser/anysurfer.py` | [ ] |
| imio.smartweb.locales | `main` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | — | [ ] |
| imio.smartweb.policy | `main` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | — | [ ] |
| pas.plugins.kimug | `main` | `src/pas/__init__.py`, `src/pas/plugins/__init__.py` | — | [ ] |
| plone.formwidget.geolocation | `fix-geosearch` | `plone/__init__.py`, `plone/formwidget/__init__.py` | No `src/` layout (see below) | [ ] |
| collective.pivot | `main` | `src/collective/__init__.py` | `pkg_resources` in `locales/update.py` | [ ] |
| collective.messagesviewlet | `master` | `src/collective/__init__.py` | Python 2 branch in `__init__.py` | [ ] |
| collective.preventactions | `plone6` | `src/collective/__init__.py` | — | [ ] |
| collective.upgrade | `plone61` | `src/collective/__init__.py` | Delete `bootstrap.py` | [ ] |

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

### plone.formwidget.geolocation (IMIO fork)

Namespaces `plone`, `plone.formwidget`. This package has **no `src/`
directory**: the code lives in `plone/` at the root of the repository. Without
a filter, `find_namespace_packages()` would also turn `docs/`, `resources/` and
any other directory into packages, so restrict it:

```diff
-from setuptools import find_packages
+from setuptools import find_namespace_packages
 ...
-    packages=find_packages(),
-    namespace_packages=["plone", "plone.formwidget"],
+    packages=find_namespace_packages(include=["plone.*"]),
```

```sh
git rm plone/__init__.py plone/formwidget/__init__.py
```

Check the wheel content carefully: it must contain only
`plone/formwidget/geolocation/...`. The classifiers stop at Python 3.10 and
Plone 6.0, so update them. The fork is on branch `fix-geosearch` and pinned at
3.0.6 in `versions.cfg` (PyPI has 3.0.7): decide whether to migrate the fork or
contribute to `collective/plone.formwidget.geolocation`.

### collective.pivot

Namespace `collective`.

```sh
git rm src/collective/__init__.py
```

`src/collective/pivot/locales/update.py` (a developer script for i18n) uses
`pkg_resources.resource_filename(domain, "")`. Replace it with:

```python
from importlib.resources import files
os.chdir(str(files(domain)))
```

The classifiers stop at Python 3.9 and Plone 6.0, so update them.

### collective.messagesviewlet

Namespace `collective`. `setup.py` uses single quotes:

```diff
-    packages=find_packages('src', exclude=['ez_setup']),
-    namespace_packages=['collective'],
+    packages=find_namespace_packages('src', exclude=['ez_setup']),
```

```sh
git rm src/collective/__init__.py
```

`src/collective/messagesviewlet/__init__.py` imports `pkg_resources` only in
its `if six.PY2:` branch. That branch never runs, but drop it along with `six`
to remove the last `pkg_resources` reference. This is a `collective` repo, so
open a PR there.

### collective.preventactions

Namespace `collective`. Standard recipe, then `git rm src/collective/__init__.py`.
The checkout is on branch `plone6`, and PyPI's last release is 0.3.0 (2019):
make the migration on that branch and release from it, or contribute to the
`collective` repo.

### collective.upgrade

Namespace `collective`. Standard recipe, then `git rm src/collective/__init__.py`.
Also delete `bootstrap.py`, an old zc.buildout bootstrap script full of
`pkg_resources` calls that modern buildout no longer uses. Remove it from
`flake8-exclude` in `buildout.cfg` too. The checkout is on branch `plone61`.

## 2. Eggs written by iMio

Classified by the author or repository in the egg metadata. None of them has a
native release on PyPI yet.

To migrate one: add it to `sources.cfg` and `auto-checkout` in `dev.cfg`,
apply [the recipe](#the-migration-recipe), release, and remove it from
`auto-checkout`. The files listed are relative to the package's source
directory (usually `src/`), so check the actual layout first.

| Package | Pinned | Latest on PyPI | Files to delete | Done |
|---|---|---|---|---|
| imio.helpers | 1.3.11 | 1.3.18 | `imio/__init__.py` | [ ] |
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
| collective.taxonomy | 3.1.7 | 4.0.0 (2026-10-20) | Major bump: check the taxonomy pages and widgets | [ ] |
| plone.app.imagecropping | 3.0.3 | 4.0.0 (2026-10-30) | Major bump: check the cropping editor | [ ] |
| plone.formwidget.recaptcha | 2.3.0 | 4.0.0 (2026-11-10) | Major bump, released today: let it settle before pinning | [ ] |
| plone.patternslib | 9.10.3.1 | 9.11.1 (2026-09-19) | Minor bump: check the front-end JavaScript | [ ] |
| zope.minmax | 3.0 | 4.0 (2025-09-12) | Major bump | [ ] |
| zope.session | 5.1 | 6.0 (2025-09-12) | Major bump | [ ] |

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
| collective.exportimport | 1.15 | 1.16 (2026-02) | Active: check the main branch first | [ ] |
| collective.fingerpointing | 1.8.3 | 1.8.3 (2022) | | [ ] |
| collective.geolocationbehavior | 1.7.2 | 1.7.2 (2021) | | [ ] |
| collective.geotransform | 3.0 | 3.0 (2023) | | [ ] |
| collective.instancebehavior | 0.5 | 0.5 (2021) | | [ ] |
| collective.js.jqueryui | 2.2.0 | 2.2.0 (2023) | Namespaces `collective`, `collective.js` | [ ] |
| collective.privacy | 1.1.0b2 | 1.1.0b2 (2022) | | [ ] |
| collective.prometheus | 1.6.1 | 1.6.1 (2022) | `plone.observability` now provides metrics: check whether it is still needed | [ ] |
| collective.sendinblue | 2.0.4 | 2.0.4 (2025) | | [ ] |
| collective.solr | 9.4.0 | 10.1.1 (2026-03) | Active: check the main branch first | [ ] |
| collective.themefragments | 2.12 | 2.12 (2019) | Last release 2019 | [ ] |
| collective.timedevents | 1.1 | 1.1 (2021) | | [ ] |
| collective.z3cform.select2 | 3.0.0b6 | 3.0.0b9 (2023) | Namespaces `collective`, `collective.z3cform` | [ ] |
| eea.facetednavigation | 16.4 | 16.5 (2026-10) | Active: check the main branch first | [ ] |
| plone.gallery | 1.1.6 | 1.1.6 (2023) | | [ ] |
| hurry.filesize | 0.9 | 0.9 (2009) | Unmaintained (last release 2009): find which package requires it | [ ] |

## 4. Plone and Zope core: nothing to do

These come from the Plone and Zope pins. Plone and Zope release them, so they
will become native through future Plone releases.

| Package | Version | Where it comes from |
|---|---|---|
| plone.app.content | 4.2.1 | `requirements.txt` (Plone security advisory 2026-10-22) |
| plone.autoform | 2.0.5 | `requirements.txt` (Plone security advisory 2026-08-31) |
| plone.restapi | 9.15.7 | `requirements.txt` (Plone security advisory 2026-08-31) |
| PasteDeploy | 3.1.0 | Plone `requirements.txt` |
| Paste | 3.10.1 | Zope pins (3.11.0, native, is on PyPI) |
