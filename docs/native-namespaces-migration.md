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
| imio.helpers | 1.3.18 | `get_distribution()` in `__init__.py`, `xhtml.py`, `patches.py` | **None released**: 1.3.19 and `master` still call it. Fixed on a `plone62` branch by a colleague, checked out through `sources.cfg` in `prod.cfg` but not yet in `dev.cfg` ([see below](#imiohelpers)) |
| collective.fingerpointing | 1.8.3 | `get_distribution()` in `subscribers/__init__.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| collective.privacy | 1.1.0b2 | `get_distribution()` in `storage.py`, `browser/consent.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| collective.timedevents | 1.1 | `get_distribution()` in `__init__.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| collective.exportimport | 1.15 | `get_distribution()` / `DistributionNotFound` in `export_content.py`, `export_other.py`, `import_other.py`, `serializer.py` | Fixed on a `plone62` branch, checked out through `sources.cfg` ([see below](#fixes-for-the-third-party-blockers)). PR to open upstream |
| imio.smartweb.core | checkout | `resource_filename()` in `browser/anysurfer.py` | Fixed on the `plone62` branch, checked out through `sources.cfg` ([group 1](#imiosmartwebcommon-core-locales-policy)) |
| eea.facetednavigation | 16.5 | `get_distribution()` in `subtypes/subtyper.py` | Bumped to 16.5 (still old-style, but no more `pkg_resources` calls) |
| collective.taxonomy | 3.1.7 | `DistributionNotFound` in `behavior.py` | Bumped to 4.0.0 ([3a](#3a-native-release-already-available-bump-the-pin)) |
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
- `imio` and `pas`: no recipe lives in these namespaces, so old-style
  checkouts there don't break buildout. imio.smartweb.core and
  pas.plugins.kimug are migrated anyway (see
  [below](#imiosmartwebcommon-core-locales-policy) and
  [below](#paspluginskimug)).

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
| [2. iMio, eggs](#2-eggs-written-by-imio) | 10 | Check out, migrate, release (8 migrated, not released: all but imio.omnia.tinymce and collective.faceted.map) |
| [3a. Third-party, native release available](#3a-native-release-already-available-bump-the-pin) | 6 | Bumped (2026-11-16), checks pending |
| [3b. Third-party, still old-style](#3b-still-old-style-upstream-contribute-or-wait) | 19 | Contribute upstream or wait (collective.anysurfer, collective.autopublishing, collective.complexrecordsproxy and collective.timedevents migrated on `plone62`, not released) |
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
| imio.smartweb.common | `plone62` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | `@search-filters` fix for plone.restapi 10; own buildout moved to Plone 6.2.3 (see below) | [x] (not released) |
| imio.smartweb.core | `plone62` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | `pkg_resources` in `browser/anysurfer.py`; `LockInfoViewlet` import; `sitemap.xml.gz` pagination; own buildout moved to Plone 6.2.3 (see below) | [x] (not released) |
| imio.smartweb.locales | `plone62` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | Own buildout (releaser, i18ndude) moved to Plone 6.2.3 | [x] (not released) |
| imio.smartweb.policy | `plone62` | `src/imio/__init__.py`, `src/imio/smartweb/__init__.py` | Own buildout moved to Plone 6.2.3 and buildout.smartweb `plone62` | [x] (not released) |
| pas.plugins.kimug | `main` | `src/pas/__init__.py`, `src/pas/plugins/__init__.py` | Configured with plone.meta 2.12.0, metadata moved to `pyproject.toml`. Plone 6.1 and 6.2 only, needs pas.plugins.oidc >= 2.1.0 (see below). Released as 2.0.0 (PR #34) | [x] (released 2.0.0) |
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

The imio.smartweb.common `plone62` branch (2026-11-16) also fixes two
Plone 6.2 breakages, and moves its own buildout to Plone 6.2.3:

- `@search-filters` always returned an empty result: since plone.restapi 10,
  the catalog query adapter drops `metadata_fields` from the query.
  `rest/search_filters.py` now pops `metadata_fields` before `_parse_query`.
- `test_iframe_transform` uses closed `<iframe>` tags: with libxml2 2.14
  (HTML5 parsing), the content of an unclosed `<iframe>` is text, as in
  browsers.
- `base.cfg` extends Plone 6.2.3 and buildout.smartweb's `plone62`
  `versions.cfg` / `sources.cfg`, and adds imio.helpers,
  collective.behavior.talcondition and collective.privacy to `auto-checkout`.
  Its `[versions]` also restores Plone 6.2.3 pins that buildout.smartweb used
  to override (plone.restapi, z3c.form, protobuf, collective.taxonomy,
  eea.facetednavigation…). buildout.smartweb now pins Plone 6.2.3, so these
  overrides can go.
- `setup.py` classifiers: Plone 6.2 added next to 6.1. 6.1 still works only
  with `horse-with-no-namespace` installed, as for the other migrated
  packages.

The imio.smartweb.core `plone62` branch (2026-11-16) also fixes two other
Plone 6.2 breakages, and moves its own buildout to Plone 6.2.3:

- `contents/sections/views.py` imports `LockInfoViewlet` from
  `plone.app.layout.viewlets.locking` instead of `plone.locking.browser.info`.
- `sitemap.xml.gz`: plone.app.layout 6 paginates the sitemap (without a
  `page` parameter, the view returns an index of pages).
  `CustomSiteMapView` now overrides `_objects` instead of `objects`, so the
  smartweb items (authentic sources included) are counted in the index and
  split across `?page=N`. New test in `tests/test_sitemap.py`.
- `base.cfg` extends Plone 6.2.3 and buildout.smartweb's `plone62`
  `versions.cfg` / `sources.cfg`, and adds the third-party blockers
  (imio.helpers, collective.privacy, collective.fingerpointing,
  collective.exportimport, collective.timedevents,
  collective.behavior.talcondition) to `auto-checkout`.
- `setup.py` classifiers: Plone 6.1 replaced by 6.2. Plone 6.0 is still
  listed: drop it before the release, since native namespaces and the
  imports above need Plone 6.2.

Each one gets its own `plone62` branch ([step 0](#0-work-on-a-plone62-branch)).
Release the four together and pin the new versions in one commit.

### pas.plugins.kimug

Namespaces `pas`, `pas.plugins`. Migrated on the `plone62` branch
(2026-11-16), merged into `main` (PR #34) and released as **2.0.0** the same
day. `sources.cfg` checks out `main` again and `versions.cfg` pins 2.0.0. It
follows collective.preventactions rather than the `setup.py` recipe above:

- plone.meta 2.12.0 did the work: `switch-to-pep420` deleted
  `src/pas/__init__.py` and `src/pas/plugins/__init__.py`, then
  `setup-to-pyproject` moved the metadata to `pyproject.toml`. `setup.py` is now
  only `setup()`, and setuptools finds the native namespace packages by itself,
  so there is no `find_namespace_packages`.
- No other `pkg_resources` use.
- The `pas.plugins` namespace is shared with pas.plugins.oidc, native since
  2.1.0. kimug now requires `pas.plugins.oidc>=2.1.0` (`versions.cfg` already
  pins 2.1.0) and supports Plone 6.1 and 6.2 only, like oidc 2.1.0.
- The package is tested with pytest and tox, not buildout: the plone.meta test
  matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13, and `make install`
  builds a uv development environment on Plone 6.2.3.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe).
- Released as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2 only)
  and pinned in `versions.cfg` (was `1.9.5`). It is still in the
  `auto-checkout` of `dev.cfg` and `prod.cfg`. Other iMio applications on
  Plone 6.0 must stay on 1.9.x.

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
| imio.helpers | 1.3.18 | 1.3.19 | `imio/__init__.py`. Migrated on `plone62` by a colleague (see [below](#imiohelpers)) | [x] (not released) |
| imio.pyutils | 1.2.2 | 1.2.2 | None: native on Python 3 only, still compatible with Python 2.7. Migrated on `plone62` (see [below](#imiopyutils)) | [x] (not released) |
| imio.prometheus | 1.0.1 | 1.0.1 | `imio/__init__.py`. Migrated on `plone62` (see [below](#imioprometheus)) | [x] (not released) |
| imio.gdpr | 1.2.3 | 1.2.3 | `imio/__init__.py`. Migrated on `plone62` (see [below](#imiogdpr)) | [x] (not released) |
| imio.omnia.core | 1.2 | 1.3 | `imio/__init__.py`, `imio/omnia/__init__.py`. Migrated on `plone62` (see [below](#imioomniacore)) | [x] (not released) |
| imio.omnia.tinymce | 1.0 | 1.0 | `imio/__init__.py`, `imio/omnia/__init__.py` | [ ] |
| collective.behavior.talcondition | 1.1.3 | 1.1.3 | `collective/__init__.py`, `collective/behavior/__init__.py`. Migrated on `plone62` by a colleague (see [below](#collectivebehaviortalcondition)) | [x] (not released) |
| collective.autoscaling | 1.2 | 1.2 | `collective/__init__.py`. Migrated on `plone62` (see [below](#collectiveautoscaling)) | [x] (not released) |
| collective.faceted.map | 1.0.0 | 1.0.0 | `collective/__init__.py`, `collective/faceted/__init__.py` | [ ] |
| iaweb.privacy | 1.0a2 | 1.0a2 | `iaweb/__init__.py`. Migrated on `plone62` (see [below](#iawebprivacy)) | [x] (not released) |

Notes:

- **imio.helpers** and **imio.pyutils** are used by many other iMio
  applications (not only SmartWeb). imio.pyutils keeps Python 2.7 support, but
  imio.helpers' `plone62` branch drops Python 2 and Plone before 6.2, so those
  applications must stay on imio.helpers 1.3.x (see [below](#imiohelpers)).
- **imio.helpers** blocks Plone 6.2.3 until its `plone62` branch is released:
  every release (up to 1.3.19) and `master` still call `pkg_resources`.
- **imio.omnia.core** and **imio.omnia.tinymce** share the `imio.omnia`
  namespace: imio.omnia.core is migrated, imio.omnia.tinymce isn't yet.
  Release them together: the old-style `imio/omnia/__init__.py` of
  imio.omnia.tinymce needs `pkg_resources`.
- Packages under `collective` (talcondition, autoscaling, faceted.map) live in
  the `collective` GitHub organisation or are released by iMio: open a PR in
  the repository listed in the egg's metadata.

### imio.helpers

Namespace `imio`. Migrated by a colleague on the `plone62` branch
(2026-11-16, `4b8ec68`), which `sources.cfg` checks out and `prod.cfg` adds to
`auto-checkout`. It follows [the recipe](#the-migration-recipe) and keeps its
`setup.py` and buildout:

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/imio/__init__.py` is gone. `python_requires=">=3.10"`, classifiers
  updated (Plone 6.2, Python 3.10 to 3.13).
- The `pkg_resources` calls that blocked Plone 6.2.3 are replaced with
  `importlib.metadata.distribution()` / `PackageNotFoundError`: `ftw.labels` in
  `__init__.py`, `collective.solr` in `patches.py`, `collective.ckeditor` in
  `xhtml.py`.
- **Breaking: drops Python 2.7 and Plone 4.3** (CI matrix and classifiers),
  without a Python 2 fallback like imio.pyutils. `six`, `future`,
  `pathlib2` and the Python 2 extras are still there: they can go in a later
  cleanup.
- Tested with buildout: new `test-6.2.cfg` (buildout.plonetest
  `test-6.2.x.cfg`) and `requirements-6.2.txt` (Plone `6.2-latest`
  constraints). The GitHub Actions matrix is Plone 6.2 on Python 3.13, and it
  passes. `test-6.2.cfg` checks out collective.behavior.talcondition's
  `plone62` branch, a test dependency.
- The branch is 2 commits behind `master`: 1.3.19 was released from `master`
  the same day, without the migration. `CHANGES.rst` on `plone62` still adds
  the entry under 1.3.19: merge `master` into `plone62` and move the entry.
- No PR opened yet.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.3.18 egg, which still stops `bin/instance fg` on Plone 6.2.3.
- Release it as **2.0.0**, not 1.3.20 (breaking: native namespace, Python
  3.10+ and Plone 6.2 only), then pin it in `versions.cfg` (currently
  `1.3.18`). `master` still releases 1.3.x for the other iMio applications:
  agree with its maintainers on a 1.3.x maintenance branch before merging
  `plone62` into `master`.

### imio.pyutils

Namespace `imio`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `dev.cfg` and `prod.cfg` add to `auto-checkout`.
Unlike the other packages, it **keeps Python 2.7 support**: many other iMio
applications still run on Python 2, and PEP 420 doesn't exist there. So
`setup.py` picks the namespace style from the Python version that builds it:

```python
if sys.version_info[0] < 3:
    from setuptools import find_packages

    namespace_kwargs = {
        "packages": find_packages(exclude=["ez_setup"]),
        "namespace_packages": ["imio"],
    }
else:
    from setuptools import find_namespace_packages

    namespace_kwargs = {"packages": find_namespace_packages(include=["imio.*"])}

setup(
    ...,
    **namespace_kwargs  # last, without a trailing comma (Python 2 syntax)
)
```

- `imio/__init__.py` stays in the source tree, for Python 2. On Python 3,
  `imio` isn't listed as a package, so the wheel ships only `imio/pyutils/`
  and no namespace file.
- `MANIFEST.in` includes `imio/__init__.py`. Without it, the sdist built on
  Python 3 would lack that file, and installing it on Python 2 would fail.
- The release wheel is `py3-none-any` (the universal wheel option was already
  removed in 1.2.1). Python 2 installs from the sdist and gets the old-style
  namespace, as before.
- When the source tree is on `sys.path` on Python 3 (develop egg,
  `pip install -e .`), the leftover `imio/__init__.py` extends `__path__`
  (horse-with-no-namespace, or its `pkgutil` fallback), so the other `imio.*`
  packages are still found.
- Checked: the Python 3 wheel imports next to another native `imio` portion
  without horse-with-no-namespace; the sdist installs on Python 2.7 with the
  old `nspkg.pth`; the 22 tests pass on Python 2.7 and 3.12 (editable install,
  as in CI); buildout.smartweb no longer lists it as old-style, and
  `bin/zopepy` imports it with the `imio.smartweb.*` packages.
- No other `pkg_resources` use. No breaking change, so release it as
  **1.3.0** (minor bump), then pin it in `versions.cfg` (currently `1.2.2`).

### imio.prometheus

Namespace `imio`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. It follows
pas.plugins.kimug rather than the `setup.py` recipe above:

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`, so there is no `find_namespace_packages`.
- `pkg_resources` was only used by the `update_locale` script
  (`locales/update.py`), which isn't imported at runtime, so it didn't block
  Plone 6.2.3. It now uses the pathlib version of pas.plugins.kimug.
  `INonInstallable` is imported from `plone.base`.
- Drops the dependencies the code never imported (z3c.jbot,
  plone.app.dexterity, plone.restapi) and the unused robot acceptance layer.
- The package is tested with tox and zope.testrunner, not buildout: the
  plone.meta test matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13,
  and `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`).
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.0.1 egg.
- Release it as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2
  only), then pin it in `versions.cfg` (currently `1.0.1`). Other iMio
  applications on Python 2 or Plone 4.3 to 6.0 must stay on 1.0.x.

### imio.gdpr

Namespace `imio`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. Unlike
imio.prometheus, it follows [the recipe](#the-migration-recipe) and keeps its
`setup.py` and buildout:

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/imio/__init__.py` is gone. `python_requires='>=3.10'`, classifiers
  updated (Plone 6.2, Python 3.10 to 3.13).
- No `pkg_resources` use beyond the namespace declaration, so it didn't block
  Plone 6.2.3.
- `views.py` compares `content.language` instead of calling `Language()`.
  The test layer is based on `PLONE_APP_CONTENTTYPES_FIXTURE` directly.
- Code formatted with black and isort, flake8 warnings fixed.
- Tested with buildout: new `plone62.cfg` and `requirements-6.2.txt`, and a
  GitHub Actions workflow (`IMIO/gha-workflows` `package-full-test`, Python
  3.12 and 3.13) replaces Travis.
- `six` and the `HAS_PLONE_5_AND_MORE` check are still there: they can go in
  a later cleanup.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.2.3 egg.
- `CHANGES.rst` announces **1.2.4**, but the change is breaking (native
  namespace, Python 3.10+ and Plone 6.2 only): release it as **2.0.0**, then
  pin it in `versions.cfg` (currently `1.2.3`). Other iMio applications on
  Python 2 or older Plone must stay on 1.2.x.

### imio.omnia.core

Namespaces `imio`, `imio.omnia`. Migrated on the `plone62` branch
(2026-11-16, `ff59325`), which `sources.cfg` checks out and `prod.cfg` adds
to `auto-checkout`. It follows [the recipe](#the-migration-recipe) and keeps
its `setup.py` and buildout:

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/imio/__init__.py` and `src/imio/omnia/__init__.py` are gone.
  `python_requires='>=3.12'`, Plone 6.2 classifier added.
- `locales/update.py` uses `importlib.resources.files` instead of
  `pkg_resources.resource_filename`.
- The missing `imio.helpers` dependency is declared.
- Code formatted with black. `test_sync_env_to_registry_ignores_vocabulary_fields`
  fixed (the database isn't opened when no env var is synced).
- Tested with buildout: new `test_plone62.cfg` and `requirements-6.2.txt`, and
  a GitHub Actions workflow (`IMIO/gha-workflows` `package-full-test`, Python
  3.12 and 3.13). The unused `[remotes]` and `[sources]` parts of `base.cfg`
  are gone.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.2 egg.
- `CHANGES.rst` announces **1.4**, but the change is breaking (native
  namespace, Plone 6.1 and 6.2, Python 3.12+): release it as **2.0.0**, together
  with imio.omnia.tinymce (shared `imio.omnia` namespace), then pin it in
  `versions.cfg` (currently `1.2`).

### collective.behavior.talcondition

Namespaces `collective`, `collective.behavior`. Migrated by a colleague on the
`plone62` branch (2026-11-16, `81b5782`), which `sources.cfg` checks out and
`prod.cfg` adds to `auto-checkout`. In SmartWeb, it is a dependency of
collective.messagesviewlet (used by imio.smartweb.core's `rest/messages.py`),
and a test dependency of imio.helpers. It follows
[the recipe](#the-migration-recipe) and keeps its `setup.py` and buildout:

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/collective/__init__.py` and `src/collective/behavior/__init__.py` are
  gone. `python_requires='>=3.10'`, the universal wheel option is removed, and
  the classifiers are updated (Plone 6.2, Python 3.10 to 3.13).
- No `pkg_resources` use beyond the namespace declarations, so it didn't block
  Plone 6.2.3. `utils.py`: `raise(e)` becomes `raise e`.
- **Breaking: drops Python 2.7 and 3.7, and Plone 4.3 to 6.1** (CI matrix and
  classifiers).
- Tested with buildout: new `test-6.2.cfg` and `requirements-6.2.txt`. The
  GitHub Actions matrix is Plone 6.2 on Python 3.13, and it passes.
- Up to date with `master`. No PR opened yet.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.1.3 egg.
- `CHANGES.rst` announces **1.1.4**, but the change is breaking: release it as
  **2.0.0**, then pin it in `versions.cfg` (currently `1.1.3`). The repository
  belongs to the `collective` organisation: open a PR there. Other iMio
  applications on Python 2 or Plone 4.3 to 6.1 must stay on 1.1.x.

### collective.autoscaling

Namespace `collective`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. It follows
pas.plugins.kimug rather than the `setup.py` recipe above:

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`, so there is no `find_namespace_packages`.
  The buildout configuration (`base.cfg`, `plone-5.2.x.cfg`,
  `plone-6.0.x.cfg`, their requirements files) is gone, and the README,
  CHANGES, CONTRIBUTORS and LICENSE are now in Markdown.
- No other `pkg_resources` use. The Python 2 branches (`cStringIO`) are gone.
  `IPloneSiteRoot`, `INonInstallable` and `get_installer` are imported from
  `plone.base`, and the test layers use `plone.testing.zope`.
- `configure.zcml` now includes the CMFCore permissions its views use: the
  package failed to load when it was included before Plone
  (`zcml_package_includes`). Through autoinclude, as in buildout.smartweb, it
  always loaded after Plone, which hid the problem.
- The package is tested with tox and zope.testrunner, not buildout: the
  plone.meta test matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13,
  robot scenarios included (Selenium, headless Chrome), and `make install`
  builds a uv development environment on Plone 6.2.3 (`mx.ini`,
  `instance.yaml`).
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.2 egg.
- Release it as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2
  only), then pin it in `versions.cfg` (currently `1.2`). The repository
  belongs to the `collective` organisation: open a PR there. Other iMio
  applications on Plone 4.3 to 6.0 must stay on 1.x.

### iaweb.privacy

Namespace `iaweb`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. It follows
collective.autoscaling:

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`, so there is no `find_namespace_packages`.
  The Plone 4.3 buildout, Travis, GitLab CI and the Python 2.7 GitHub workflow
  are gone, and the README, CHANGES, CONTRIBUTORS and LICENSE are now in
  Markdown. The broken `update_locale` console script (its module never
  existed) is gone too.
- No other `pkg_resources` use. `INonInstallable` is imported from
  `plone.base`. The setup tests used `portal_quickinstaller`, so they couldn't
  run on any Plone since 5.2: they now use `get_installer`. The unused robot
  acceptance layer is gone.
- Depends on collective.privacy, whose 1.1.0b2 release blocks Plone 6.2.3
  (see [blockers](#blockers-for-plone-623)). Until it is released, the
  package's `mx.ini` and tox (`test_deps_additional` in `.meta.toml`) install
  its `plone62` branch from GitHub. Replace both with a version pin once it is
  out.
- `configure.zcml` now includes the CMFCore permissions that collective.privacy
  uses (`cmf.ManagePortal`), as in collective.autoscaling: the package failed
  to load when it was included before Plone (`zcml_package_includes`). In
  buildout.smartweb, imio.smartweb.common includes it after Plone.
- `rules/all.zcml` included a nonexistent `medial.zcml`, so it failed to
  load. Now fixed. Nothing in SmartWeb includes `all.zcml`.
- The package is tested with tox and zope.testrunner, not buildout: the
  plone.meta test matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13,
  and `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`).
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads the
  1.0a2 egg.
- Release it as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2
  only), then pin it in `versions.cfg` (currently `1.0a2`). Other iMio
  applications on Plone 4.3 to 6.0 must stay on 1.0a2.

## 3. Third-party eggs

### 3a. Native release already available: bump the pin

These packages are pinned in `versions.cfg`, and their latest release on PyPI
uses native namespaces. Bump the pin, then run buildout, start the instance and
test the feature that uses the package. Most are major version bumps, so read
their changelog first.

All six were bumped on 2026-11-16 (`12dde8e`). The checks in the Notes column
are still to do.

| Package | Pinned | Native release | Notes | Done |
|---|---|---|---|---|
| collective.taxonomy | 3.1.7 | 4.0.0 (2026-10-20) | Bumped 2026-11-16. Major bump: check the taxonomy pages and widgets | [x] |
| plone.app.imagecropping | 3.0.3 | 4.0.0 (2026-10-30) | Bumped 2026-11-16 (only breaking change: Plone 6.2 only). Check the cropping editor | [x] |
| plone.formwidget.recaptcha | 2.3.0 | 4.0.0 (2026-11-10) | Bumped 2026-11-16. Major bump: check the forms that use the captcha | [x] |
| plone.patternslib | 9.10.3.1 | 9.11.1 (2026-09-19) | Bumped 2026-11-16. Minor bump: check the front-end JavaScript | [x] |
| zope.minmax | 3.0 | 4.0 (2025-09-12) | Bumped 2026-11-16. Major bump | [x] |
| zope.session | 5.1 | 6.0 (2025-09-12) | Bumped 2026-11-16. Major bump | [x] |

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
| collective.anysurfer | 1.4.7 | 1.4.7 (2022) | Migrated on `plone62` (see [below](#collectiveanysurfer)) | [x] (not released) |
| collective.autopublishing | 1.1b1 | 1.1b1 (2022) | Migrated on `plone62` (see [below](#collectiveautopublishing)) | [x] (not released) |
| collective.complexrecordsproxy | 1.1 | 1.1 (2022) | Migrated on `plone62` (see [below](#collectivecomplexrecordsproxy)) | [x] (not released) |
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
| collective.timedevents | 1.1 | 1.1 (2021) | Blocked Plone 6.2.3: fixed on a `plone62` branch, checked out through `auto-checkout` in `dev.cfg` and `prod.cfg`. PR to open | [x] (not released) |
| collective.z3cform.select2 | 3.0.0b6 | 3.0.0b9 (2023) | Namespaces `collective`, `collective.z3cform` | [ ] |
| eea.facetednavigation | 16.5 | 16.5 (2026-10) | Active: check the default branch (`develop`) first. Pinned to 16.5 for Plone 6.2.3: it no longer calls `pkg_resources` | [x] |
| plone.gallery | 1.1.6 | 1.1.6 (2023) | | [ ] |
| hurry.filesize | 0.9 | 0.9 (2009) | Unmaintained (last release 2009): find which package requires it | [ ] |

### collective.anysurfer

Namespace `collective`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. It follows
collective.autoscaling:

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`. The buildout configuration (Plone 4.3 and
  5.2), Travis, `bootstrap.py` and the hand-written GitHub workflow are gone,
  and the README, CHANGES, CONTRIBUTORS and LICENSE are now in Markdown.
- No other `pkg_resources` use. The Python 2 and Plone 4 code is gone: `six`,
  the `HAS_PLONE_5` / `HAS_PLONE_6` flags (they called `plone.api` at import
  time), the Plone 4 `search.js` and the overrides of templates that no longer
  exist. `INonInstallable`, `IPloneSiteRoot` and `safe_text` are imported from
  `plone.base`.
- The tests couldn't run on any current stack (`unittest2` on Python 3.10+,
  `portal_quickinstaller` on Plone 5.2+): they now use `unittest`,
  `plone.testing.zope` and `get_installer`. They check French titles, so tox
  compiles the `.mo` files (`zope_i18n_compile_mo_files`), as the buildout
  test runner did.
- What imio.smartweb.core uses doesn't change: `interfaces.ILayerSpecific`,
  `layout.LayoutPolicy` and the `default` profile (still `0004`, no upgrade
  step).
- The jbot override of the search page and the breadcrumb viewlet template
  still use the Plone 5 markup (no Bootstrap 5 classes). They render on Plone
  6.2, but check them on a SmartWeb site.
- The package is tested with tox and zope.testrunner, not buildout: the
  plone.meta test matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13,
  and `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`). Checked by hand on a Plone 6.2.3 classic site:
  page titles (views, search, 404), accessibility page, control panel.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  the branch isn't pushed yet, so `buildout -c prod.cfg` fails until it is,
  and it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads
  the 1.4.7 egg.
- Release it as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2
  only), then pin it in `versions.cfg` (currently `1.4.7`). The repository
  belongs to the `collective` organisation: open a PR there. Other
  applications on Plone 4.3 to 6.0 must stay on 1.4.x.

### collective.autopublishing

Namespace `collective`. Migrated on the `plone62` branch (2026-11-16), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. It follows
collective.anysurfer:

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`. The package moved from the repository
  root to a `src/` layout, which plone.meta's tox expects. The buildout
  configuration (Plone 5.2 and 6.0), the hand-written GitHub workflow,
  `setup.cfg`, `.coveragerc` and `.gitattributes` are gone, and the README,
  CHANGES, CONTRIBUTORS and LICENSE are now in Markdown.
- No other `pkg_resources` use. The views are registered for
  `IPloneSiteRoot` from `plone.base`, and the behavior registration lost its
  `for` (no effect without a factory, plone.behavior warned at startup).
- The test layer imported `plone.app.contenttypes.testing`, which needs
  plone.app.robotframework: it now loads the plone.app.contenttypes ZCML and
  sets `simple_publication_workflow` on top of `PLONE_FIXTURE`. New tests
  render the control panel and the report view. The doctest no longer imports
  `interlude`.
- The report view (`@@autopublish-report`) used the `eva.content` i18n
  domain and had no i18n markup: it is now translatable, with French
  translations.
- Depends on collective.timedevents, whose 1.1 release blocks Plone 6.2.3
  (see [blockers](#blockers-for-plone-623)). Until it is released, the
  package's `mx.ini` and tox (`test_deps_additional` in `.meta.toml`) install
  its `plone62` branch from GitHub. Replace both with a version pin once it is
  out. collective.complexrecordsproxy 1.1 is still old-style, but its wheel
  imports next to the native portions without horse-with-no-namespace (its
  `nspkg.pth`, no `pkg_resources` call). Its `plone62` branch is native
  (see [below](#collectivecomplexrecordsproxy)).
- The package is tested with tox and zope.testrunner, not buildout: the
  plone.meta test matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13,
  and `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`). Checked on a Plone 6.2.3 classic site:
  installation, control panel, report view and `@@tick_hourly`.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  the branch isn't pushed yet, so `buildout -c prod.cfg` fails until it is,
  and it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads
  the 1.1b1 egg.
- Release it as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2
  only), after a collective.timedevents release without `pkg_resources`
  (a PyPI release can't depend on a git branch), then pin it in
  `versions.cfg` (currently `1.1b1`). The repository belongs to the
  `collective` organisation: open a PR there. Other applications on Plone 5.2
  or 6.0 must stay on 1.1b1.

### collective.complexrecordsproxy

Namespace `collective`. Migrated on the `plone62` branch (2026-11-17), which
`sources.cfg` checks out and `prod.cfg` adds to `auto-checkout`. It follows
collective.autopublishing, which is its only user in SmartWeb:

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`. The package moved from the repository
  root to a `src/` layout. The README, CHANGES and LICENSE are now in
  Markdown, the licenses moved from `docs/` to the root, and a
  `CONTRIBUTORS.md` lists the authors. There was no buildout, Travis or CI
  to remove.
- No other `pkg_resources` use. The code doesn't change, apart from the
  import order and `__all__` in `__init__.py`. It is a library, not an
  add-on (no ZCML, no profile), and depends on plone.registry and
  zope.schema only.
- The package had no tests: new unit tests on a plain plone.registry
  `Registry` (no Plone layer) cover scalar, `Object` and tuple of `Object`
  fields. collective.autopublishing's tests also pass on Plone 6.2.3 with
  this branch instead of the 1.1 egg.
- Two behaviors found while writing the tests, unchanged (1.1 has them too):
  a tuple of more than 10 items is read back in the wrong order (items are
  stored as `r0`, `r1`… and read in string order, `r10` before `r2`), and a
  tuple field is read back as a mapping values view, which can't be indexed.
  collective.autopublishing only iterates over it.
- The package is tested with tox and zope.testrunner, not buildout: the
  plone.meta test matrix covers Plone 6.2.3 and 6.1 on Python 3.10 to 3.13,
  and `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`). Plone isn't a dependency of the package: the
  Makefile adds Products.CMFPlone and plone.app.contenttypes for the
  instance. Checked on a Plone 6.2.3 classic site: settings written and read
  back through the site's `portal_registry`.
- Not yet checked from buildout.smartweb (steps 5.1 and 5.2 of the recipe):
  the branch isn't pushed yet, so `buildout -c prod.cfg` fails until it is,
  and it isn't in `dev.cfg`'s `auto-checkout`, so `bin/instance` still loads
  the 1.1 egg.
- Release it as **2.0.0** (breaking: native namespace, Plone 6.1 and 6.2
  only), then pin it in `versions.cfg` (currently `1.1`). The repository
  belongs to the `collective` organisation: open a PR there. Other
  applications on Plone 4.3 to 6.0 or Python 2.7 must stay on 1.1.

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
