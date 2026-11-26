# Native namespace migration: package details

What changed in each package, and what to know before reviewing or releasing
it. Status and next steps are in the
[migration overview](native-namespaces-migration.md#status), which links here.

Each section starts with the same facts: namespace, repository and branch,
[variant of the recipe](native-namespaces-migration.md#the-migration-recipe),
which buildout.smartweb config checks it out, and which release older stacks
must stay on.

## collective.anysurfer

**Namespace** `collective` · **Repository**
[collective/collective.anysurfer](https://github.com/collective/collective.anysurfer),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 4.3 to 6.0) stay on 1.4.x

Migrated 2026-11-16, following collective.autoscaling. Merged into `master`
([#9](https://github.com/collective/collective.anysurfer/pull/9)) and released
as **2.0.0** on 2026-11-18: `versions.cfg` pins it, and no config checks it out
any more. `sources.cfg` still names its `plone62` branch, deleted after the
merge: switch it to `master`.

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
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13. Checked by hand
  on a Plone 6.2.3 classic site: page titles (views, search, 404),
  accessibility page, control panel.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## collective.autopublishing

**Namespace** `collective` · **Repository**
[collective/collective.autopublishing](https://github.com/collective/collective.autopublishing),
branch `master` (`plone62` merged by
[#12](https://github.com/collective/collective.autopublishing/pull/12),
2026-11-20) · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 5.2, 6.0) stay on 1.1b1

Migrated 2026-11-16, following collective.anysurfer. Released as **2.0.0** on
2026-11-24: `versions.cfg` pins it, and no config checks it out any more
(`sources.cfg` points to `master`).

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
- **Depends on collective.timedevents 2.0.0**: its 1.1 release blocks Plone
  6.2.3, so `pyproject.toml` requires `>=2.0.0`. Since that release,
  `mx.ini` and tox (`test_deps_additional` in `.meta.toml`) no longer install
  its branch from GitHub.
- Also depends on collective.complexrecordsproxy, released as 2.0.0 and
  pinned. `pyproject.toml` doesn't require `>=2.0.0`: the 1.1 release is
  old-style, but its wheel imports next to the native portions without
  horse-with-no-namespace (its `nspkg.pth`, no `pkg_resources` call).
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13. Checked on a
  Plone 6.2.3 classic site: installation, control panel, report view and
  `@@tick_hourly`.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## collective.autoscaling

**Namespace** `collective` · **Repository**
[collective/collective.autoscaling](https://github.com/collective/collective.autoscaling),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 4.3 to 6.0) stay on 1.x

Migrated on `plone62` on 2026-11-16, following pas.plugins.kimug, merged into
`master` ([#9](https://github.com/collective/collective.autoscaling/pull/9))
and released as **2.0.0** on 2026-11-18. `versions.cfg` pins 2.0.0, and no
config checks it out any more (`sources.cfg` points to `master` again).

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`. The buildout configuration (`base.cfg`,
  `plone-5.2.x.cfg`, `plone-6.0.x.cfg`, their requirements files) is gone, and
  the README, CHANGES, CONTRIBUTORS and LICENSE are now in Markdown.
- No other `pkg_resources` use. The Python 2 branches (`cStringIO`) are gone.
  `IPloneSiteRoot`, `INonInstallable` and `get_installer` are imported from
  `plone.base`, and the test layers use `plone.testing.zope`.
- `configure.zcml` now includes the CMFCore permissions its views use: the
  package failed to load when it was included before Plone
  (`zcml_package_includes`). Through autoinclude, as in buildout.smartweb, it
  always loaded after Plone, which hid the problem.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13, robot scenarios
  included (Selenium, headless Chrome).
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## collective.behavior.talcondition

**Namespaces** `collective`, `collective.behavior` · **Repository**
[collective/collective.behavior.talcondition](https://github.com/collective/collective.behavior.talcondition),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Python 2, Plone 4.3 to 6.1) stay on 1.1.x

Migrated by a colleague on 2026-11-16 (`81b5782`), then modernized like
collective.autopublishing on 2026-11-20, before the release. In SmartWeb, it
is a dependency of collective.messagesviewlet (used by imio.smartweb.core's
`rest/messages.py`), and a test dependency of imio.helpers. Merged into
`master` ([#17](https://github.com/collective/collective.behavior.talcondition/pull/17))
and released as **2.0.0** on 2026-11-20: `versions.cfg` pins it, and no
config checks it out any more (`sources.cfg` points to `master`).

- No more `namespace_packages`, and `src/collective/__init__.py` and
  `src/collective/behavior/__init__.py` are gone. No `pkg_resources` use
  beyond the namespace declarations. `utils.py`: `raise(e)` becomes
  `raise e`.
- plone.meta 2.12.0 configures it, and `setup-to-pyproject` moved the
  metadata to `pyproject.toml`. `setup.py` is now only `setup()`. The
  z3c.autoinclude entry point became a `plone.autoinclude.plugin` one, and
  the license is SPDX `GPL-2.0-only`. The README, CHANGES, CONTRIBUTORS and
  LICENSE are now in Markdown.
- Gone: the buildout configuration (`base.cfg`, `gha.cfg`, `test-4.3.cfg` to
  `test-6.2.cfg`, their requirements files), the hand-written GitHub workflow,
  `.coveragerc`, `.isort.cfg` and the empty robot test setup.
- **Breaking: drops Python before 3.10, Plone before 6.2, and the Archetypes
  code**: the schema extender (`extender.py`, `utils.applyExtender`) and the
  `PLONE_VERSION` constant. SmartWeb only imports `ITALCondition`, so it isn't
  affected.
- `get_installer` comes from `plone.base`, the test layer helpers from
  `plone.testing.zope`, and `logger.warn` became `logger.warning`.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14. `make install` builds a uv development
  environment on Plone 6.2.3, from collective.autopublishing's Makefile.
- `CHANGES.rst` announced 1.1.4, but the change is breaking: released as
  2.0.0.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.
- imio.helpers' `test-6.2.cfg` still checks out the `plone62` branch (now
  deleted) from GitHub: replace it by the 2.0.0 release there.

## collective.complexrecordsproxy

**Namespace** `collective` · **Repository**
[collective/collective.complexrecordsproxy](https://github.com/collective/collective.complexrecordsproxy),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 4.3 to 6.0, Python 2.7) stay on 1.1

Migrated 2026-11-17, following collective.autopublishing, which is its only
user in SmartWeb. Merged into `master`
([#3](https://github.com/collective/collective.complexrecordsproxy/pull/3))
and released as **2.0.0** on 2026-11-23: `versions.cfg` pins it, and no
config checks it out any more (`sources.cfg` points to `master`).

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
- **Two existing bugs**, found while writing the tests and left unchanged (1.1
  has them too): a tuple of more than 10 items is read back in the wrong order
  (items are stored as `r0`, `r1`… and read in string order, `r10` before
  `r2`), and a tuple field is read back as a mapping values view, which can't
  be indexed. collective.autopublishing only iterates over it.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 and 6.1 on Python 3.10 to 3.13. Plone isn't a dependency of the
  package: the Makefile adds Products.CMFPlone and plone.app.contenttypes for
  the instance. Checked on a Plone 6.2.3 classic site: settings written and
  read back through the site's `portal_registry`.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## collective.exportimport

**Namespace** `collective` · **Repository**
[collective/collective.exportimport](https://github.com/collective/collective.exportimport),
branch `plone62`, draft PR
[#287](https://github.com/collective/collective.exportimport/pull/287) ·
**Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** `base.cfg` · **Older stacks** (Plone 6.0 or older) stay on
1.x

🚧 Every release calls `get_distribution()` / `DistributionNotFound` in
`export_content.py`, `export_other.py`, `import_other.py` and `serializer.py`.

Migrated 2026-11-16, then modernized like collective.messagesviewlet
(2026-11-17).

- **One PR.** The `importlib-metadata` branch (`importlib.metadata` with the
  [Python 2.7 fallback](native-namespaces-migration.md#variant-keep-python-2))
  kept Python 2 for the sites exportimport exports from. Its PR
  [#286](https://github.com/collective/collective.exportimport/pull/286) is
  closed. `plone62`, the full modernization below, is
  [#287](https://github.com/collective/collective.exportimport/pull/287) into
  `main` (2.0.0), a draft until plone.restapi 10.3.1 is out (see below).
  Exporting from Python 2 sites stays on 1.x.
- `src/collective/__init__.py` is gone. `__init__.py` imports `get_version`
  and `PackageNotFoundError` from `importlib.metadata` only (the
  `pkg_resources` fallback for Python 2.7 is gone), and the
  `update_locale` script (`locales/update.py`) finds the package folder with
  `importlib.resources.files()` instead of
  `pkg_resources.resource_filename()`.
- plone.meta 2.12.0 configures it (tox, GitHub Actions test matrix,
  pre-commit, dependabot), and `setup-to-pyproject` moved the metadata to
  `pyproject.toml`. `setup.py` is now only `setup()`. The z3c.autoinclude
  entry point became a `plone.autoinclude.plugin` one. Before running
  `setup-to-pyproject`, the `sys.version_info` branch (Python 2 pins),
  `packages` and `package_dir` were removed from `setup.py`, and
  `install_requires` written inline.
- **Breaking: Plone 6.1 on Python 3.10 to 3.13, Plone 6.2 on Python 3.10 to
  3.14** (version `2.0.0.dev0`). 3.14 is set up like collective.anysurfer:
  in the Plone 6.2 `test_matrix` of `.meta.toml`, the `py314-plone62` tox env,
  the CI job (3.14 and 3.10 for Plone 6.2) and the classifier. The README explains that exporting from Plone 4.3 to 6.0 or
  Python 2 needs 1.x in the old site, and that 2.x imports the result (same
  json format).
- `six` is dropped. pyupgrade rewrote most uses (`six.moves.urllib`,
  `six.text_type`, the `if six.PY2:` imports), and the remaining `six.PY2` /
  `six.PY3` branches were removed by hand. The other lint autofixes (isort,
  black, zpretty) and the flake8 and codespell findings are applied: bare
  `except:` became `except Exception:`, an unused `BlocksJSONFieldSerializer`
  import is gone, typos fixed. The JSON samples in the `import_*.pt`
  templates get `i18n:ignore`, and one untranslated sentence in
  `import_content.pt` gets `i18n:translate` (not yet in the `.pot`). The Plone
  4 and 5 code paths (Archetypes, LinguaPlone, `Products.CMFPlone.interfaces`
  imports) are kept: they are guarded and are what exportimport exports from.
- The dependencies the code imports are declared (checked by
  z3c.dependencychecker): Zope, Products.CMFPlone, plone.app.contenttypes,
  python-dateutil… The guarded imports (Archetypes, ATContentTypes,
  LinguaPlone, plone.app.multilingual, plone.app.discussion,
  collective.relationhelpers, z3c.relationfield…) are in
  `dependencies_ignores`. The test extra needs `plone.app.contenttypes[test]`:
  `plone.app.contenttypes.testing` imports plone.app.robotframework.
- Gone: the buildout configuration (`base.cfg`, `buildout.cfg`,
  `test-*.x.cfg`), `requirements*.txt`, `setup.cfg`, `DEVELOP.rst`, the Sphinx
  stub (`docs/conf.py`, `docs/index.rst`; the README images stay in `docs/`)
  and the hand-written GitHub workflow (Plone 4.3 to 6.0 with Python 2.7
  docker images). There was no Travis.
- exportimport has no GenericSetup profile, so `scripts/create_site.py` only
  creates the site: the `@@export_*` and `@@import_*` views work as soon as the
  package is loaded. Checked: `make install` then `make create-site` build the
  environment and create the site.
- `hurry.filesize` is dropped: the large file and image log messages use
  `plone.base.utils.human_readable_size` (`2.0 KB` instead of `2K`).
  `plone.base` is declared instead.
- Tests (zope.testrunner through tox): Plone 6.1 on Python 3.10, 52 tests
  pass. Plone 6.2.3 on Python 3.12 and 3.14, 4 fail (`test_import_contenttree`,
  `test_import_imports_but_ignores_constrains`, `test_import_workflow_history`,
  `test_reset_dates`), with the 1.x code too: the plone.restapi bug below.
  With plone.restapi at the #2094 merge commit, the 52 tests pass on both.
- **plone.restapi bug: image and file import broken on Plone 6.2.3.**
  plone.restapi 10.2.1 (pinned by Plone 6.2.3, still in 10.3.0):
  `NamedFieldDeserializer` reads `request.form[value["part"]]` whenever the
  request is `multipart/form-data`, even if the value carries inline `data`.
  The `@@import_content` form always posts multipart, so every image and file
  is dropped (`KeyError: 'part'`, "Didn't add Image"). This affects any
  content import on the Plone 6.2 stack. Fixed in plone.restapi by
  [#2094](https://github.com/plone/plone.restapi/pull/2094) (only use the
  multipart branch when `"part" in value`), merged 2026-11-18, first
  released in 10.3.1 (not out yet). Then pin it in `versions.cfg`, and get
  the tox Plone 6.2 envs on it (newer Plone 6.2 constraints, or an override
  in `.meta.toml`) before marking #287 ready.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker. `versions.cfg` still pins 1.16, as for the
  other checked-out packages.

## collective.faceted.map

**Namespaces** `collective`, `collective.faceted` · **Repository**
[affinitic/collective.faceted.map](https://github.com/affinitic/collective.faceted.map),
branch `master` (`plone62` merged by
[#3](https://github.com/affinitic/collective.faceted.map/pull/3),
2026-11-24) · **Variant**
[setup.py](native-namespaces-migration.md#the-migration-recipe) · **Checked
out by** none (`affinitic` remote in `sources.cfg`) · **Older stacks**
(Python 2, Plone before 6.2) stay on 1.0.x

Migrated 2026-11-17 (`c5c4b5a`). Released as **2.0.0** on 2026-11-24:
`versions.cfg` pins it, and no config checks it out any more (`sources.cfg`
points to `master`).

- No more `namespace_packages`, and `src/collective/__init__.py` and
  `src/collective/faceted/__init__.py` are gone. `setup.py` no longer lists
  the packages: setuptools finds them in the `src/` layout (`5eccc51`).
  `python_requires='>=3.10'`, classifiers updated (Plone 6.2, Python 3.10 to
  3.14).
- `locales/update.py` uses `importlib.resources` instead of
  `pkg_resources`.
- `test_map_view` fixed for Plone 6: it renders the map view through
  `@@faceted_query` on a faceted folder (the `getFolderContents` skin script
  is gone), and the test layer loads eea.facetednavigation. `not_skip`
  removed from the isort configuration.
- Tested with buildout: new `plone6.2.x.cfg` and `requirements6.2.x.txt`. The
  GitHub Actions matrix is Plone 6.2 on Python 3.12 and 3.13; Travis CI is
  gone.
- **Breaking: drops Python before 3.10 and Plone before 6.2** (classifiers),
  hence 2.0.0.
- Its map viewlet triggers `leaflet.refresh` after each search, which only
  the iMio plone.formwidget.geolocation bundle handles
  ([details](plone-formwidget-geolocation.md)).
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## collective.fingerpointing

**Namespace** `collective` · **Repository**
[collective/collective.fingerpointing](https://github.com/collective/collective.fingerpointing),
branch `master` (upstream) · **Checked out by** none · **Older stacks** stay
on 1.8.x

1.8.3 calls `get_distribution()` in `subscribers/__init__.py`: fixed in 2.0.0.

Migrated upstream: `master` (2.0.0.dev0) is Plone 6.2 only, Python 3.10+ and
native, merged on 2026-11-16 ([#110](https://github.com/collective/collective.fingerpointing/pull/110)).
Our `importlib-metadata` PR (#111) was closed in favor of it. Released as
**2.0.0** on 2026-11-19: `versions.cfg` pins it, and no config checks it out
any more (removed from `sources.cfg`).

- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## collective.geotransform

**Namespace** `collective` · **Repository**
[collective/collective.geotransform](https://github.com/collective/collective.geotransform),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 6.0) stay on 3.0

Migrated 2026-11-17, like collective.complexrecordsproxy. In SmartWeb,
imio.smartweb.policy requires it and includes its ZCML. Merged into `master`
([#25](https://github.com/collective/collective.geotransform/pull/25)) and
released as **4.0.0** on 2026-11-20: `versions.cfg` pins it, and no config
checks it out any more (`sources.cfg` points to `master`).

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`,
  written by hand (`setup-to-pyproject` can't parse the `long_description`
  concatenation). `setup.py` is now only `setup()`. The package moved from
  the repository root to a `src/` layout. The README, CHANGES
  (`docs/HISTORY.txt`), CONTRIBUTORS and LICENSE are now in Markdown, at the
  root. The z3c.autoinclude entry point became a `plone.autoinclude.plugin`
  one, and the license is SPDX `GPL-2.0-or-later` (the license text says "or
  any later version").
- Gone: Travis, the Plone 6.0 buildout configuration (`base.cfg`,
  `buildout.cfg`, `plone-6.0.x.cfg`, `code-analysis.cfg`, `versions.cfg`,
  `requirements*.txt`) and the hand-written GitHub workflow.
- No other `pkg_resources` use. `six` is dropped, and `safe_text`,
  `IFilterSchema` and `IBundleRegistry` come from `plone.base`. In
  `registry.xml`, the two bundle records keep their values, so existing sites
  need no upgrade step. The robot layer uses `WSGI_SERVER_FIXTURE` from
  `plone.testing.zope`. The dependencies the code imports are declared
  (checked by z3c.dependencychecker), and lxml too: the transform asks
  BeautifulSoup for its lxml parser.
- **Breaking: Plone 6.1 and 6.2 only, Python 3.10 to 3.14 (3.13 on Plone
  6.1).** Release 4.0.0: 3.0 is the Plone 6.0 release (`CHANGES` announced
  3.0.1).
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13. Run locally:
  Plone 6.2.3 on Python 3.13 and Plone 6.1 on Python 3.10 (8 tests each),
  plus lint, dependencies, circular and release-check. The robot scenario (Selenium,
  headless Chrome) passes unchanged. It checks in the browser that
  `geoMailDecoder.js` decodes the links, so the jQuery-based decoder still
  works in the Plone 6.2 classic UI. robotsuite writes its reports to
  `robot/`, which is ignored through `.meta.toml`.
- `make install` builds a uv development environment on Plone 6.2.3 (`mx.ini`,
  `instance.yaml` with `zcml_package_includes`), and the instance starts with
  the package loaded. There is no create-site script: activate it in the
  Add-ons control panel. `make release` runs zest.releaser through uvx, as in
  collective.complexrecordsproxy, so zest.releaser isn't a dependency.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it as
  old-style, `bin/zopepy` imports it from the `src/` checkout, and the wheel
  has no namespace marker.

## collective.instancebehavior

**Namespace** `collective` · **Repository**
[collective/collective.instancebehavior](https://github.com/collective/collective.instancebehavior),
branch `plone62`, pinned at `2aef9eb` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** `base.cfg` · **Older stacks** (Plone 6.1 and older,
Python 2.7) stay on 0.5

Migrated 2026-11-17, like collective.geotransform. In SmartWeb,
imio.smartweb.core requires it and includes its ZCML: its instance behaviors
form calls `enable_behaviors` / `disable_behaviors` to add collective.taxonomy
behaviors to a single page or procedure.

Its upstream PR, [#7](https://github.com/collective/collective.instancebehavior/pull/7)
(opened 2026-11-18), is the whole branch. It is still open, with no review
(2026-11-26). Until it is merged and released, `sources.cfg` checks out the
head of `plone62`, `2aef9eb`, with a fixed `rev` (2026-11-24, `c9c00af`).

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`,
  written by hand (`setup-to-pyproject` can't parse the `long_description`
  built by `read_file()`). `setup.py` is now only `setup()`. The package was
  already in a `src/` layout. The README, CHANGES, CONTRIBUTORS and LICENSE
  are now in Markdown. The z3c.autoinclude entry point became a
  `plone.autoinclude.plugin` one, and the license is SPDX `GPL-2.0-only` (the
  README says GPLv2). pyroma requires an author email: Robert Niederreiter's,
  from the git history.
- **License mismatch, left as is**: `LICENSE.md` (formerly `LICENSE.rst`) has
  held a BSD 3-clause text since the initial packaging in 2013, while the
  README, the metadata and `LICENSE.GPL` say GPLv2. Ask upstream which one
  applies before releasing.
- Gone: the Plone 5.2 buildout (`buildout.cfg`, `requirements.txt`),
  `setup.cfg` and `DEVELOP.rst`. There was no Travis file or CI to remove.
- No other `pkg_resources` use. The code doesn't change apart from the lint
  autofixes (`super()`, imports) and the docstring examples, which flake8
  checked as doctests. `transaction`, which the helpers import, is now
  declared.
- **Version 0.6, not 2.0.0**: 0.6 was never released (`master` already said
  0.6.dev0, with "Drop Python 2 support"), so the breaking changes join it.
- **Two existing behaviours, left unchanged** (in `master` too):
  `enable_behaviors` and `disable_behaviors` commit the transaction
  themselves (added in 2024 so the modification timestamp changes before
  reindexing), and they call `reindexObject(idxs=("object_provides"))`, a
  string instead of a tuple: CMFCore's indexing queue drops it, so every
  index is reindexed instead of `object_provides` only.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13. The only test
  asserted `1 == 1`: five functional tests now cover `enable_behaviors`,
  `disable_behaviors`, `instance_behaviors_of` and the behavior assignable,
  with a test behavior and Dexterity type. Run locally: the whole matrix,
  plus lint, coverage, dependencies, circular and release-check.
- `make install` builds a uv development environment on Plone 6.2.3 (the
  Makefile of collective.complexrecordsproxy: Plone isn't a dependency, so
  it adds Products.CMFPlone and plone.app.contenttypes), and the instance
  starts with the package's ZCML (`zcml_package_includes`). `make release`
  runs zest.releaser through uvx, so zest.releaser isn't a dependency.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it as
  old-style, `bin/zopepy` imports it from the `src/` checkout, and the wheel
  has no namespace marker. `versions.cfg` still pins 0.5, as for the other
  checked-out packages. imio.smartweb.core's own tests
  (`test_instance_behaviors.py`) haven't been run against the branch.

## collective.js.jqueryui

**Namespaces** `collective`, `collective.js` · **Repository**
[collective/collective.js.jqueryui](https://github.com/collective/collective.js.jqueryui),
branch `master` (upstream) · **Checked out by** none · **Older stacks** stay
on 2.2.x

Migrated upstream: `master` (3.0.0.dev0) is Plone 6.2 only, Python 3.10+ and
native, merged on 2026-11-17
([#57](https://github.com/collective/collective.js.jqueryui/pull/57)). No
`pkg_resources` use. [#58](https://github.com/collective/collective.js.jqueryui/pull/58),
merged the same day, fixes the plugin resource ids of the aggregated
JavaScript: until then, jQuery UI was never loaded. Check what uses it on a
SmartWeb site. Released as **3.0.0** on 2026-11-19: `versions.cfg` pins it,
and no config checks it out any more (removed from `sources.cfg`).

## collective.messagesviewlet

**Namespace** `collective` · **Repository**
[collective/collective.messagesviewlet](https://github.com/collective/collective.messagesviewlet),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 4.3 to 6.0) stay on 1.0b5

Migrated 2026-11-16, then modernized like pas.plugins.kimug (2026-11-17). Its
`Makefile` and uv environment are the template for the later packages. Merged
into `master`
([#24](https://github.com/collective/collective.messagesviewlet/pull/24)) and
released as **2.0.0** on 2026-11-18: `versions.cfg` pins it, and no config
checks it out any more. `sources.cfg` still names its `plone62` branch,
deleted after the merge: switch it to `master`.

- `src/collective/__init__.py` is gone, and the Python 2 branches in
  `__init__.py` (the last `pkg_resources` reference) too.
- plone.meta 2.12.0 configures it (tox, GitHub Actions test matrix,
  pre-commit), and `setup-to-pyproject` moved the metadata to
  `pyproject.toml`. `setup.py` is now only `setup()`. The z3c.autoinclude
  entry point became a `plone.autoinclude.plugin` one.
- **Breaking: Plone 6.1 and 6.2 only, Python 3.10 to 3.14 (3.13 on Plone
  6.1).** The plone.meta test matrix covers Plone 6.2.3 on Python 3.10 to
  3.14, and 6.1 on 3.10 to 3.13 (22 tests). The Plone 5.2 job had been
  failing since 2026-10-22 anyway: setuptools 75.3 builds
  plone.app.robotframework 1.5.6 as `plone_app_robotframework`, which
  zc.buildout 3.4 can't find.
- Gone: Travis, the buildout configuration (`base.cfg`, `plone-*.x.cfg`,
  `versions*.cfg`, `requirements*.txt`, `code-analysis.cfg`), `.coveragerc`, the
  hand-written GitHub workflow, and the Selenium robot tests (with the
  acceptance layer and their test dependencies): they need
  `plone/app/robotframework/selenium.robot`, which plone.app.robotframework 3
  (pinned by Plone 6.2.3) no longer ships, and the old CI never ran them.
- `make install` builds a uv development environment on Plone 6.2.3 (`mx.ini`,
  `instance.yaml`, `scripts/create_site.py`), from kimug's Makefile without the
  Keycloak targets. `make i18n` runs `locales/update.sh`.
- `IPloneSiteRoot` and `INonInstallable` come from `plone.base`, `six` is
  dropped, and the dependencies the code imports are declared (checked by
  z3c.dependencychecker). `plone.formwidget.datetime` is only imported on
  Plone 4, and is ignored by the checker. The other Plone 4 and 5 code paths
  (`HAS_PLONE_5_AND_MORE`, the `plone4`/`plone5` profiles) are still there.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it as
  old-style, `bin/zopepy` imports it from the checkout with the
  `plone.autoinclude` entry point, and the wheel has no namespace marker.
- Release 2.0.0, not 1.0b6.

## collective.pivot

**Namespace** `collective` · **Repository**
[IMIO/collective.pivot](https://github.com/IMIO/collective.pivot), branch
`main` · **Variant**
[setup.py](native-namespaces-migration.md#the-migration-recipe) · **Checked
out by** none · **Older stacks** (Python 2, Plone 4.3 to 6.1) stay on 1.0b2

Migrated on `plone62`, merged into `main`
([#4](https://github.com/IMIO/collective.pivot/pull/4)) and released as
**2.0.0** on 2026-11-19. `versions.cfg` pins 2.0.0, and no config checks it
out any more (`sources.cfg` points to `main` again).

- Standard recipe, then `git rm src/collective/__init__.py`.
- `locales/update.py` uses `str(files(domain))` instead of
  `pkg_resources.resource_filename(domain, "")`.
- **Breaking: Python 3.10+ and Plone 6.2 only**, hence 2.0.0. Plone 5.2,
  6.0, Python 2 and 3.8–3.9 are dropped, with their CI jobs, `.travis.yml`,
  `ci.cfg` and the 4.3/5.2/6.0 buildout and requirements files. CI tests
  Python 3.10 to 3.14 on Plone 6.2 (`test_plone6.2.cfg`,
  `requirements_plone-6.2.x.txt`).
- The Plone 4/5 code paths are gone (`HAS_PLONE_5_AND_MORE`, the `plone4`
  and `plone5` profiles, the zcml conditions): the `plone6` profile became
  `profiles/default`. The profile id and version are unchanged, so no
  upgrade step is needed.

## collective.preventactions

**Namespace** `collective` · **Repository**
[collective/collective.preventactions](https://github.com/collective/collective.preventactions),
branch `plone6` (upstream) · **Checked out by** none

Migrated upstream on `plone6` (native namespace, `bootstrap.py` gone), merged
into `master` on 2026-11-12
([#2](https://github.com/collective/collective.preventactions/pull/2)) and
released as **0.4.0**, which `versions.cfg` pins. No config checks it out
any more, but `sources.cfg` still names `plone6`: switch it to `master`.
Delete the stale `src/collective/__pycache__` and `collective_*-nspkg.pth`
files ([step 5](native-namespaces-migration.md#5-clean-up-and-check)).

## collective.privacy

**Namespace** `collective` · **Repository**
[collective/collective.privacy](https://github.com/collective/collective.privacy),
branch `master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Python 2, Plone 4.3 to 6.0) stay on 1.1.0b2

1.1.0b2 calls `get_distribution()` in `storage.py` and `browser/consent.py`:
fixed in 2.0.0.

Fixed and migrated 2026-11-16, then modernized like collective.messagesviewlet
(2026-11-17). Merged into `master`
([#22](https://github.com/collective/collective.privacy/pull/22)) and released
as **2.0.0** on 2026-11-19: `versions.cfg` pins it, and no config checks it
out any more (`sources.cfg` points to `master`).

- Its first commit (`bb46b06`, `importlib.metadata` with the [Python 2.7
  fallback](native-namespaces-migration.md#variant-keep-python-2)) still works
  as a standalone upstream PR, if the maintainers want to keep Python 2.
- `src/collective/__init__.py` is gone. `storage.py` uses
  `email.utils.formatdate`, and `browser/consent.py` no longer looks up
  `plone.directives.form` at all (it was the Plone 4 fallback), so the last
  `pkg_resources` reference is gone.
- plone.meta 2.12.0 configures it (tox, GitHub Actions test matrix,
  pre-commit), and the metadata moved to `pyproject.toml`, written by hand
  (`setup.py` is now only `setup()`). The z3c.autoinclude entry point became a
  `plone.autoinclude.plugin` one, and the license is SPDX `GPL-2.0-only`.
  Version 2.0.0.dev0.
- **Breaking: Plone 6.2 only, Python 3.10 to 3.14, without
  `horse-with-no-namespace`** (2026-11-19: Plone 6.1 dropped from the tox and
  GitHub Actions matrix and the classifiers, Python 3.14 added).
- Gone: Travis, GitLab CI, the buildout configuration (`base.cfg`,
  `buildout.cfg`, `travis.cfg`, `plone-4.3.x.cfg` to `plone-5.2.x.cfg`,
  `versions.cfg`, `requirements.txt`), `setup.cfg`, `.coveragerc`,
  `DEVELOP.rst`, `bobtemplate.cfg`, and the Selenium robot tests (with the
  acceptance layer): they need `plone/app/robotframework/selenium.robot`,
  which plone.app.robotframework 3 no longer ships. **They were the only
  tests of the JavaScript consent banner**, which is now untested: check it by
  hand on a SmartWeb site.
- `INonInstallable`, `safe_text` and `get_installer` come from `plone.base`,
  `six` is dropped, and the jbot overrides of the Plone 4 skin templates
  (`Products.CMFPlone.skins.*`) are gone. The override of the Plone 6
  `sendto_template.pt` is kept: it is still Plone 6.2.3's template plus the
  privacy notice. The dependencies the code imports are declared (checked by
  z3c.dependencychecker), including plone.app.upgrade (`upgrades.py`).
- Tests: 6 of the 7 tests failed on Plone 6.2.3. The setup tests used the
  `portal_quickinstaller` API (`isProductInstalled`, `uninstallProducts`),
  and the cookie test expected the old cookie keys (`max_age`, Zope now
  returns `Max-Age`). They are fixed, and new tests render `@@consent` and
  `@@consent-json` (9 tests). They pass on Plone 6.2.3 with Python 3.14 and
  3.10, with lint and dependency checks. Neither tox environment installs
  `horse-with-no-namespace` or has a `pkg_resources` module.
- Codespell fixed `separeted` in a ZCML field description, which is also a
  msgid: the `.pot` and `.po` files follow.
- `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`, `scripts/create_site.py`), from
  collective.messagesviewlet's Makefile. `make i18n` runs `locales/update.sh`.
- Checked from buildout.smartweb: `bin/zopepy` imports it from the `src/`
  checkout (2.0.0.dev0) with the `plone.autoinclude` entry point, `collective`
  is a native namespace (not in horse-with-no-namespace's list), and the
  wheel has no namespace marker.
- iaweb.privacy's `mx.ini` and tox still install the `plone62` branch (now
  deleted) from GitHub: replace it by the 2.0.0 release there.

## collective.solr

**Namespace** `collective` · **Repository**
[collective/collective.solr](https://github.com/collective/collective.solr),
branch `pep-420-native-namespace` (upstream) · **Checked out by** `base.cfg`
· **Older stacks** stay on 10.x (Plone 6.0 and 6.1)

Migrated upstream on `pep-420-native-namespace` (11.0.0.dev0: Plone 6.2 only,
Python 3.10+, native), approved on 2026-11-17 (two reviews) but not merged yet
([#408](https://github.com/collective/collective.solr/pull/408)). No
`pkg_resources` use. This upstream branch replaces the IMIO fork in
`sources.cfg`: the fork entry pointed to a `main` branch that doesn't exist,
and it was never checked out.

- **Two major versions** from the pinned 9.4.0. 10.0.0 drops Python 3.9,
  Plone 5.2 and Solr 9.0 and 9.1 (dev runs Solr 9.6.1: check the production
  version), and reimplements Solr faceting for Classic UI. 11.0.0 removes the
  old Archetypes code. Test search, faceted navigation and indexing on a
  SmartWeb site.
- imio.helpers patches `SolrIndexProcessor.index` (`patches.py`): the method
  is still there on the branch.
- Once #408 is merged and 11.0.0 released, drop the checkout and pin it.

## collective.themefragments

**Namespace** `collective` · **Repository**
[collective/collective.themefragments](https://github.com/collective/collective.themefragments),
branch `master` (`plone62` merged by
[#20](https://github.com/collective/collective.themefragments/pull/20),
2026-11-20) · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 4.3 to 6.0, Python 2.7) stay on 2.12

Migrated 2026-11-17. In SmartWeb, imio.smartweb.policy requires it, includes
its ZCML and allows `requests` in RestrictedPython for the fragment modules.
The fragment tile isn't loaded: plone.tiles isn't installed.

The upstream maintainer approved the PR, no longer uses the package and
suggested that iMio take it over. Released as **3.0.0** on 2026-11-24:
`versions.cfg` pins it, and no config checks it out any more (`sources.cfg`
points to `master`).

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`,
  written by hand (`setup-to-pyproject` can't parse the `long_description`
  concatenation). `setup.py` is now only `setup()`. The package was already
  in a `src/` layout. The z3c.autoinclude entry point became a
  `plone.autoinclude.plugin` one. The README and CHANGES are now in Markdown,
  and a `CONTRIBUTORS.md` lists the git authors.
- **License**: `setup.py` only said "GPL", and there was no license file.
  The metadata says SPDX `GPL-2.0-only` and `LICENSE.md` / `LICENSE.GPL` were
  added, like plone.app.theming, which the fragments come from. Upstream
  approved it with the PR.
- Gone: Travis (Plone 4.3 to 5.2, Python 2.7 to 3.7), the buildout
  configurations based on buildout.plonetest, and `bootstrap.py`.
- No other `pkg_resources` use. The Python 2 and Plone 4 code is gone: `six`
  (which was never declared), the Python 2 encoding of the fragment name in
  the tile forms (the unreleased 2.13.1 fix, dropped from the changelog), the
  plone.app.widgets fallbacks and the `IThemingPolicy` import guard.
  `safe_text` comes from `plone.base`.
- **plone.app.widgets is no longer a dependency**: it was deprecated (removed
  in Plone 7), and collective.themefragments was the only package that pulled
  it into buildout.smartweb (`bin/instance` no longer lists it). The tile
  field permission checker is now registered for `IFieldPermissionChecker`
  from plone.app.z3cform, the interface the plone.app.widgets alias pointed
  to: without plone.app.widgets, it wasn't registered at all.
- The tile stays optional (its ZCML is only loaded when plone.tiles is
  installed): what it imports is now declared in a `tiles` extra.
  z3c.dependencychecker 3.0 doesn't count extras for missing imports, so
  `.meta.toml` ignores these packages, with a comment.
- `configure.zcml` includes the CMFCore permissions (the tile uses
  `cmf.ModifyPortalContent`), and the tests use `plone.testing.zope`.
- **Version 3.0.0, not 2.0.0**: 2.12 is already a 2.x release.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13 (11 functional
  tests of the traversal views, which already passed on 6.2.3 before the
  changes). Run locally: the whole matrix, plus lint, coverage, dependencies,
  circular and release-check. **Not covered by the tests**: the fragment tile
  (no tile tests, 31% coverage of `tiles.py`) and the theme cache, which only
  runs with debug mode off (the tests force it on).
- `make install` builds a uv development environment on Plone 6.2.3 (the
  Makefile of collective.complexrecordsproxy: the package doesn't depend on
  Products.CMFPlone, so it adds it and plone.app.contenttypes), and the
  instance starts with the package's ZCML (`zcml_package_includes`).
  `make release` runs zest.releaser through uvx, so zest.releaser isn't a
  dependency.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` doesn't list it as
  old-style, `bin/zopepy` imports it from the `src/` checkout, and the wheel
  has no namespace marker.

## collective.timedevents

**Namespace** `collective` · **Repository**
[collective/collective.timedevents](https://github.com/collective/collective.timedevents),
branch `master` (`plone62` merged by
[#13](https://github.com/collective/collective.timedevents/pull/13),
2026-11-18) · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Python 2, Plone 4.3 to 6.0) stay on 1.1

1.1 calls `get_distribution()` in `__init__.py`: fixed in 2.0.0.

Migrated 2026-11-16, then modernized like collective.messagesviewlet
(2026-11-17). Its upstream PR is the whole branch. Released as **2.0.0** on
2026-11-18: `versions.cfg` pins it, and no config checks it out any more.

- `collective/__init__.py` is gone, and `__init__.py` reads its version with
  `importlib.metadata` only (the `pkg_resources` fallback for Python 2.7 is
  gone too).
- plone.meta 2.12.0 configures it (tox, GitHub Actions test matrix,
  pre-commit), and the metadata moved to `pyproject.toml`. `setup.py` is now
  only `setup()`. The package moved from the repository root to a `src/`
  layout, which plone.meta's tox expects, and `docs/HISTORY.txt` became
  `CHANGES.rst`. The z3c.autoinclude entry point became a
  `plone.autoinclude.plugin` one, and the license is now SPDX
  `GPL-2.0-only` (was `GPL`). `setup-to-pyproject` can't parse the
  `long_description` concatenation, and always commits: the `[project]`
  section was written by hand.
- **Breaking: Plone 6.1 and 6.2 only, Python 3.10 to 3.14 (3.13 on Plone
  6.1).** The plone.meta test matrix covers Plone 6.2.3 on Python 3.10 to
  3.14, and 6.1 on 3.10 to 3.13 (6 tests, unchanged).
- Gone: Travis (README badge), the buildout configuration (`buildout.cfg`,
  `plone-4.3.x.cfg`, `plone-5.1.x.cfg`, `plone-5.2.x.cfg`,
  `requirements.txt`), `.coveragerc`, and the hand-written GitHub workflow
  (Python 2.7 to 3.8, Plone 4.3 to 5.2).
- plone.protect is now a declared dependency, imported without the
  `HAS_PROTECT` fallback. `configure.zcml` always includes the CMFCore
  permissions (`have plone-41` condition dropped). The dependencies the code
  imports are declared (checked by z3c.dependencychecker).
- `make install` builds a uv development environment on Plone 6.2.3
  (`mx.ini`, `instance.yaml`, `scripts/create_site.py`), from
  collective.messagesviewlet's Makefile without the i18n target (the package
  has no locales).
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it as
  old-style, `bin/zopepy` imports it from the `src/` checkout (2.0.0.dev0)
  with the `plone.autoinclude` entry point, and the wheel has no namespace
  marker.
- collective.autopublishing requires the 2.0.0 release (`>=2.0.0`).
- The README still documents the Zope 2 `<clock-server>`, which WSGI Zope
  no longer has: on Plone 6 the views are called by cron (or any HTTP
  client) with a Manager account.

## collective.upgrade

**Namespace** `collective` · **Repository**
[collective/collective.upgrade](https://github.com/collective/collective.upgrade),
branch `master` (upstream; `combined-prs` merged by
[#20](https://github.com/collective/collective.upgrade/pull/20), 2026-11-20) ·
**Checked out by** none · **Older stacks**: Plone 6.1 on 2.0.0, older ones on
1.7

Migrated upstream on `plone61` (native namespace, `bootstrap.py` gone), and
released from that branch as **2.0.0** on 2026-11-24, for Plone 6.1. `master`
(Plone 6.2 only, Python 3.10 to 3.14) was released the same day as **3.0.0**:
`versions.cfg` pins it, and no config checks it out any more (`sources.cfg`
points to `master`). Upstream
PRs [#17](https://github.com/collective/collective.upgrade/pull/17) (`plone61`
into `master`),
[#18](https://github.com/collective/collective.upgrade/pull/18) (PEP 420
native namespace, into `master`) and
[#19](https://github.com/collective/collective.upgrade/pull/19) (Plone 6.2
support, into `plone61`) are closed: their work is combined in
[#20](https://github.com/collective/collective.upgrade/pull/20)
(`combined-prs` into `master`, merged 2026-11-20, released as 3.0.0). The
3.0.0 release on PyPI has no 3.0.0 section in its changelog. `master`'s
`CHANGES.rst` got one after the release (`4116306`), but the `news/`
fragments of #18 and #19 are still there: delete them, or towncrier adds
them again to 3.0.1.

## collective.z3cform.select2

**Namespaces** `collective`, `collective.z3cform` · **Repository**
[collective/collective.z3cform.select2](https://github.com/collective/collective.z3cform.select2),
branch `master` (upstream) · **Checked out by** none · **Older stacks** stay
on 3.0.0b9

Migrated upstream: `master` (4.0.0b1.dev0) is Plone 6.2 only, Python 3.10+ and
native, merged on 2026-11-17
([#15](https://github.com/collective/collective.z3cform.select2/pull/15)). No
`pkg_resources` use. `master` also carries unreleased changes made since
3.0.0b9: Plone 6.1 support, without Plone 4 and 5
([#14](https://github.com/collective/collective.z3cform.select2/pull/14)).
Check the select2 widgets on a SmartWeb site. Released as **4.0.0** (not
4.0.0b1) on 2026-11-19: `versions.cfg` pins it, and no config checks it out
any more (removed from `sources.cfg`).

## eea.facetednavigation

**Namespace** `eea` · **Repository**
[collective/eea.facetednavigation](https://github.com/collective/eea.facetednavigation),
branch `main` (`plone62` merged by
[#65](https://github.com/collective/eea.facetednavigation/pull/65),
2026-11-20) · **Variant** [plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** `base.cfg` · **Older stacks** (Plone 5.2 and 6.0) stay
on 16.x

EEA archived [eea/eea.facetednavigation](https://github.com/eea/eea.facetednavigation):
collective's repository is now the main one, and released 16.5. 16.5 already
dropped its `get_distribution()` call (`subtypes/subtyper.py`), which blocked
Plone 6.2.3, so only the namespace was left. Migrated, then modernized like
pas.plugins.kimug, on 2026-11-17. Merged into `main` on 2026-11-20, not
released yet (`main` says 17.0.0.dev0): `base.cfg` checks out `main`, and
`versions.cfg` still pins 16.5.

- `eea/__init__.py` is gone, and the package moved to a `src/` layout. The
  webpack, sass, eslint and prettier paths (`package.json`,
  `webpack.config.js`, `resources/*`, `.eslintignore`) follow it.
- The metadata moved to `pyproject.toml` by hand (`setup.py` concatenates
  `long_description`): `setup.py` is now only `setup()`, the version is no
  longer read from `version.txt`, and the z3c.autoinclude entry point became a
  `plone.autoinclude.plugin` one. The changelog moved from `docs/HISTORY.txt`
  to `CHANGES.rst`.
- plone.meta 2.12.0 configures it (tox, GitHub Actions test matrix,
  pre-commit). Its format hooks touched about 220 files (pyupgrade, isort,
  black, zpretty).
- **zpretty changes the rendered HTML**: it puts `tal:` attributes on their
  own lines and sorts the attributes, so Chameleon renders `<legend >` and
  `<input class="..." type="...">`. Valid HTML, but the doctests that matched
  `<legend>` and `<input type=` now use ellipses (`docs/unicode.txt`, the
  autocomplete and text `widget.txt`).
- `docs/wrapper.txt` no longer prints `sandbox.getFolderContents` and
  `sandbox.queryCatalog`: Plone 6.1 and 6.2 don't ship these skin scripts.
  The wrapper still provides both.
- codespell: typos fixed in comments, docs and the changelog. The JS and
  template identifiers (`colapse`, `alph`, `oll`, `aLine`) and the
  `filters bellow` msgid are ignored, so existing translations still match.
  Generated bundles, `yarn.lock` and the `.po`/`.pot` files are skipped.
- Dependencies the code imports are declared (checked by
  z3c.dependencychecker). `collective.solr` and `eea.cache` stay optional
  (imported in `try/except ImportError`).
- Gone: Jenkins, `docker-compose.yml`, `zope.conf`, `constraints.txt`,
  `setup.cfg`, `.vscode`, `DEVELOP.md` and the old GitHub workflows (black,
  flake8, zpretty, docker, test). The JS workflows (eslint, prettier) stay.
- `make install` builds a uv development environment on Plone 6.2.3, from
  collective.messagesviewlet's Makefile without the i18n target, plus
  `make resources` (yarn build of `browser/static`). `make create-site`
  installs the add-on, with no pending upgrade.
- The wheel holds the same files as 16.5, except `version.txt` and the `.mo`
  files, which are compiled at release time.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, and `bin/zopepy` imports it from the checkout
  (`src/eea.facetednavigation/src`) with the `plone.autoinclude` entry point.
- Tests: the plone.meta test matrix passed on Plone 6.2.3 and 6.1 with
  Python 3.10 to 3.13 (24 tests), and so did `lint` and `dependencies`.
  Before the merge, `64ed2ec` (2026-11-19) dropped Plone 6.1 and added
  Python 3.14: the matrix is now Plone 6.2.3 only.
- **Breaking: Plone 6.2 only, Python 3.10 to 3.14.** Release 17.0.0.

## iaweb.privacy

**Namespace** `iaweb` · **Repository**
[IMIO/iaweb.privacy](https://github.com/IMIO/iaweb.privacy), branch `master`
· **Variant** [plone.meta](native-namespaces-migration.md#variant-plonemeta) ·
**Checked out by** none · **Older stacks** (Plone 4.3 to 6.0) stay on 1.0a2

Migrated on `plone62` on 2026-11-16, following collective.autoscaling, merged
into `master` ([#2](https://github.com/IMIO/iaweb.privacy/pull/2)) and
released as **2.0.0** on 2026-11-19. `versions.cfg` pins 2.0.0, and no config
checks it out any more (`sources.cfg` points to `master` again).

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`. The Plone 4.3 buildout, Travis, GitLab CI
  and the Python 2.7 GitHub workflow are gone, and the README, CHANGES,
  CONTRIBUTORS and LICENSE are now in Markdown. The broken `update_locale`
  console script (its module never existed) is gone too.
- No other `pkg_resources` use. `INonInstallable` is imported from
  `plone.base`. The setup tests used `portal_quickinstaller`, so they couldn't
  run on any Plone since 5.2: they now use `get_installer`. The unused robot
  acceptance layer is gone.
- **Depends on collective.privacy**, whose 1.1.0b2 release blocks Plone 6.2.3.
  The package's `mx.ini` and tox (`test_deps_additional` in `.meta.toml`)
  install its `plone62` branch from GitHub: replace both with the 2.0.0 pin,
  released on 2026-11-19 (the branch is now deleted). 2.0.0 requires
  collective.privacy without a version, so it was released first.
- `configure.zcml` now includes the CMFCore permissions that collective.privacy
  uses (`cmf.ManagePortal`), as in collective.autoscaling: the package failed
  to load when it was included before Plone (`zcml_package_includes`). In
  buildout.smartweb, imio.smartweb.common includes it after Plone.
- `rules/all.zcml` included a nonexistent `medial.zcml`, so it failed to
  load. Now fixed. Nothing in SmartWeb includes `all.zcml`.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14, and 6.1 on 3.10 to 3.13.
- Checked from buildout.smartweb on the `src/` checkout: `.venv/bin/buildout
  -N` no longer listed it as old-style, `bin/zopepy` imported it, and the
  wheel had no namespace marker.

## imio.gdpr

**Namespace** `imio` · **Repository**
[IMIO/imio.gdpr](https://github.com/IMIO/imio.gdpr), branch `master` ·
**Variant** [setup.py](native-namespaces-migration.md#the-migration-recipe) ·
**Checked out by** none · **Older stacks** (Python 2, older Plone) stay on
1.2.x

Migrated on `plone62` on 2026-11-16, merged into `master`
([#5](https://github.com/IMIO/imio.gdpr/pull/5)) and released as **2.0.0**
on 2026-11-19. `versions.cfg` pins 2.0.0, and no config checks it out any
more (`sources.cfg` points to `master` again).

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/imio/__init__.py` is gone. `python_requires='>=3.10'`, classifiers
  updated (Plone 6.2, Python 3.10 to 3.14).
- No `pkg_resources` use beyond the namespace declaration.
- `views.py` compares `content.language` instead of calling `Language()`.
  The test layer is based on `PLONE_APP_CONTENTTYPES_FIXTURE` directly.
- Code formatted with black and isort, flake8 warnings fixed.
- Tested with buildout: new `plone62.cfg` and `requirements-6.2.txt`, and a
  GitHub Actions workflow (`IMIO/gha-workflows` `package-full-test`, Python
  3.12 to 3.14) replaces Travis.
- `six` and the `HAS_PLONE_5_AND_MORE` check are still there: they can go in
  a later cleanup.
- **Breaking: Python 3.10+ and Plone 6.2 only**, hence 2.0.0. It also
  ships German translations, merged into `master` before the migration.
- Checked from buildout.smartweb on the `src/` checkout: `.venv/bin/buildout
  -N` no longer listed it as old-style, `bin/zopepy` imported it, and the
  wheel had no namespace marker.

## imio.helpers

**Namespace** `imio` · **Repository**
[IMIO/imio.helpers](https://github.com/IMIO/imio.helpers), branch `plone62` ·
**Variant** [setup.py](native-namespaces-migration.md#the-migration-recipe) ·
**Checked out by** `base.cfg` · **Older stacks** (Python 2, Plone
before 6.2) stay on 1.3.x

🚧 Every release up to 1.3.19, and `master`, call `get_distribution()` in
`__init__.py`, `xhtml.py` and `patches.py`.

Migrated by a colleague on 2026-11-16 (`4b8ec68`).

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/imio/__init__.py` is gone. `python_requires=">=3.10"`, classifiers
  updated (Plone 6.2, Python 3.10 to 3.13).
- The `pkg_resources` calls are replaced with
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
  `plone62` branch, a test dependency. That branch is deleted since the
  2.0.0 release: pin 2.0.0 instead.
- 1.3.19 was released from `master` the same day, without the migration.
  `master` was merged into `plone62` (2026-11-18, `7c640c8`), and the
  `CHANGES.rst` entry is now under 1.3.20 (unreleased). `master` moved on
  since: it is 5 commits ahead of `plone62` again
  ([#52](https://github.com/IMIO/imio.helpers/pull/52), DMS-1243, merged
  2026-11-23). Merge it into `plone62` again.
- **Used by many other iMio applications**, not only SmartWeb. Release 2.0.0,
  not 1.3.20. `master` still releases 1.3.x for the other applications: agree
  with its maintainers on a 1.3.x maintenance branch before merging `plone62`
  into `master`.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker. `versions.cfg` still pins 1.3.18, as for the
  other checked-out packages.

## imio.omnia.core

**Namespaces** `imio`, `imio.omnia` · **Repository**
[IMIO/imio.omnia.core](https://github.com/IMIO/imio.omnia.core), branch
`plone62` · **Variant**
[setup.py](native-namespaces-migration.md#the-migration-recipe) · **Checked
out by** `base.cfg`

Migrated 2026-11-16 (`ff59325`). Shares the `imio.omnia` namespace with
imio.omnia.tinymce: release them together, since an old-style
`imio/omnia/__init__.py` left by either one needs `pkg_resources`.

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
- **Breaking: native namespace, Plone 6.1 and 6.2, Python 3.12+.**
  `CHANGES.rst` announces 1.4: release 2.0.0.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker. `versions.cfg` still pins 1.2, as for the
  other checked-out packages.

## imio.omnia.tinymce

**Namespaces** `imio`, `imio.omnia` · **Repository**
[IMIO/imio.omnia.tinymce](https://github.com/IMIO/imio.omnia.tinymce), branch
`plone62` · **Variant**
[setup.py](native-namespaces-migration.md#the-migration-recipe) · **Checked
out by** `base.cfg`

Migrated 2026-11-17 (`52d308d`), like imio.omnia.core: release them together.

- `find_namespace_packages`, no more `namespace_packages`, and
  `src/imio/__init__.py` and `src/imio/omnia/__init__.py` are gone.
  `python_requires='>=3.12'`, Plone 6.2 classifier added.
- `locales/update.py` uses `importlib.resources.files` instead of
  `pkg_resources.resource_filename`.
- Code formatted with black.
- Tested with buildout: new `test_plone62.cfg` and `requirements-6.2.txt`
  (`buildout.cfg` now extends `test_plone62.cfg`), and a GitHub Actions
  workflow (`IMIO/gha-workflows` `package-full-test`, Python 3.12 and 3.13).
- **1.1 was released from `master` on 2026-11-16, without the migration.**
  `master` is merged into `plone62` (2026-11-18, `785d77f`): the branch is no
  longer behind. `CHANGES.rst` now announces 1.2.
- `sources.cfg` checked out `OIA-30-structure-simplify-text` before. Its
  commit `a9c4c86` (replaces make-accessible by simplify-text and
  structure-text) is in neither `master` nor `plone62`: SmartWeb doesn't have
  that feature until the branch is merged.
- **Breaking: native namespace, Plone 6.1 and 6.2, Python 3.12+.** Release
  2.0.0.
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker. `versions.cfg` still pins 1.0, as for the
  other checked-out packages.

## imio.prometheus

**Namespace** `imio` · **Repository**
[IMIO/imio.prometheus](https://github.com/IMIO/imio.prometheus), branch
`master` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Python 2, Plone 4.3 to 6.1) stay on 1.0.x

Migrated 2026-11-16, following pas.plugins.kimug. Merged into `master`
([#2](https://github.com/IMIO/imio.prometheus/pull/2)) and released as
**2.0.0** on 2026-11-20: `versions.cfg` pins it, and no config checks it out
any more (`sources.cfg` points to `master`).

**Removed** on 2026-11-24, with collective.prometheus, the base of its
view: plone.observability serves `@@metrics` on the Zope root, and both
views fought over the single ZODB activity monitor. imio.smartweb.policy
no longer requires it, and `versions.cfg` and `sources.cfg` no longer name
it.

- plone.meta 2.12.0 configures it, and the metadata moved to `pyproject.toml`.
  `setup.py` is now only `setup()`.
- `pkg_resources` was only used by the `update_locale` script
  (`locales/update.py`), which isn't imported at runtime, so it didn't block
  Plone 6.2.3. It now uses the pathlib version of pas.plugins.kimug.
  `INonInstallable` is imported from `plone.base`.
- Drops the dependencies the code never imported (z3c.jbot,
  plone.app.dexterity, plone.restapi) and the unused robot acceptance layer.
- Tested with tox and zope.testrunner: the plone.meta test matrix covers
  Plone 6.2.3 on Python 3.10 to 3.14 (Plone 6.1 was dropped before the
  release), and `make install` builds a uv development environment on Plone
  6.2.3 (`mx.ini`, `instance.yaml`).
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer lists it
  as old-style, `bin/zopepy` imports it from the `src/` checkout, and the
  wheel has no namespace marker.

## imio.pyutils

**Namespace** `imio` · **Repository**
[IMIO/imio.pyutils](https://github.com/IMIO/imio.pyutils), branch `master` ·
**Variant** [keep Python 2](native-namespaces-migration.md#variant-keep-python-2)
· **Checked out by** `base.cfg`

Migrated on `plone62` on 2026-11-16, merged into `master` the same day
([#4](https://github.com/IMIO/imio.pyutils/pull/4)). 1.2.3 was released a few
hours before the merge, so it is still old-style.

Unlike the other packages, it **keeps Python 2.7 support**: many other iMio
applications still run on Python 2, and PEP 420 doesn't exist there. So
`setup.py` picks the namespace style from the Python version that builds it
(see the [variant](native-namespaces-migration.md#variant-keep-python-2)).

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
- No other `pkg_resources` use. **No breaking change**: release 1.3.0 (minor
  bump; `master` says 1.2.4.dev0).
- `versions.cfg` pins 1.2.3 (2026-11-20), as for the other checked-out
  packages. Its `CHANGES.rst` lists the native namespace entry, but the
  release isn't native: the wheel still ships an `nspkg.pth` file and
  `namespace_packages.txt`, and its `setup.py` declares
  `namespace_packages=["imio"]`. Keep the checkout until 1.3.0.

## imio.smartweb.common, .core, .locales, .policy

**Namespaces** `imio`, `imio.smartweb` · **Repositories**
[common](https://github.com/IMIO/imio.smartweb.common),
[core](https://github.com/IMIO/imio.smartweb.core),
[locales](https://github.com/IMIO/imio.smartweb.locales),
[policy](https://github.com/IMIO/imio.smartweb.policy), branch `main` ·
**Variant** [setup.py](native-namespaces-migration.md#the-migration-recipe)
· **Checked out by** `dev.cfg`

All four are released as 2.0.0 (then 2.0.1 for the policy) and pinned in
`versions.cfg` (see below), so the image installs the releases. Same change
in all four:

```diff
-    packages=find_packages("src", exclude=["ez_setup"]),
-    namespace_packages=["imio", "imio.smartweb"],
+    packages=find_namespace_packages("src", exclude=["ez_setup"]),
```

```sh
git rm src/imio/__init__.py src/imio/smartweb/__init__.py
```

**imio.smartweb.core**: `src/imio/smartweb/core/browser/anysurfer.py` used
`pkg_resources`:

```python
from importlib.resources import files

class AccessibilityInfo(BrowserView):
    hide_herobanner = True
    index = ViewPageTemplateFile(
        str(files("Products.CMFPlone") / "browser/templates/accessibility-info.pt")
    )
```

The `plone62` branch (2026-11-16) also fixes two Plone 6.2 breakages:

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
- `setup.py` classifiers: Plone 6.2 only, Python 3.10 to 3.14 (3.14 added to
  the CI matrix too).

It also drops collective.sendinblue from `install_requires`, so that package
(still old-style upstream) doesn't need to be migrated. The Sendinblue
section was removed in 1.4.13, whose upgrade step 1073 uninstalls the
add-on. Before deploying 2.0.0, check that every site has run step 1073 (on an
older site, the step no longer finds the uninstall profile), and that no
site still has a Sendinblue portlet assigned (the uninstall leaves them, as
broken objects).

Merged into `main`
([#102](https://github.com/IMIO/imio.smartweb.core/pull/102)) and released as
**2.0.0** on 2026-11-20 (Python 3.10+, Plone 6.2 only). `versions.cfg` pins
2.0.0 in place of 1.4.66, `prod.cfg` no longer checks it out, and
`sources.cfg` points to `main` again (its `plone62` branch was deleted).
`dev.cfg` still checks it out.

**imio.smartweb.common**: the `plone62` branch (2026-11-16) also fixes two
Plone 6.2 breakages:

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
- `setup.py` classifiers: Plone 6.2 only, Python 3.12+.

Merged into `main`
([#37](https://github.com/IMIO/imio.smartweb.common/pull/37)) and released as
**2.0.0** on 2026-11-19 (it also brings 1.2.65). `versions.cfg` pins 2.0.0,
`prod.cfg` no longer checks it out, and `sources.cfg` points to `main` again.
`dev.cfg` still checks it out. Its `base.cfg` still has the `[versions]`
overrides above ([clean up](native-namespaces-migration.md#clean-up)).

**imio.smartweb.locales**: its own buildout (releaser, i18ndude) moved to
Plone 6.2.3. Merged into `main`
([#4](https://github.com/IMIO/imio.smartweb.locales/pull/4)) and released as
**2.0.0** on 2026-11-19 (Python 3.10+, Plone 6.2 only; it only requires
setuptools). `versions.cfg` pins 2.0.0, `prod.cfg` no longer checks it out,
and `sources.cfg` points to `main` again. `dev.cfg` still checks it out, to
work on translations.

**imio.smartweb.policy**: its own buildout moved to Plone 6.2.3 and
buildout.smartweb `plone62`. Merged into `main`
([#28](https://github.com/IMIO/imio.smartweb.policy/pull/28)) and released as
**2.0.0** on 2026-11-19 (Python 3.10+; it also brings 1.2.24, WEB-4523).
**2.0.1** followed on 2026-11-24: it no longer requires imio.prometheus
([removed](#imioprometheus)). `versions.cfg` pins 2.0.1, `prod.cfg` no longer
checks it out, and `sources.cfg` points to `main` again. `dev.cfg` still
checks it out. The 2.0.1 classifiers still list Plone 6.0 and 6.1, but native
namespaces need Plone 6.2: fix them in the next release.

## pas.plugins.kimug

**Namespaces** `pas`, `pas.plugins` · **Repository**
[IMIO/pas.plugins.kimug](https://github.com/IMIO/pas.plugins.kimug), branch
`main` · **Variant**
[plone.meta](native-namespaces-migration.md#variant-plonemeta) · **Checked
out by** none · **Older stacks** (Plone 6.0) stay on 1.9.x

Migrated on `plone62` on 2026-11-16, merged into `main`
([#34](https://github.com/IMIO/pas.plugins.kimug/pull/34)) and released as
**2.0.0** the same day. `versions.cfg` pins 2.0.0, and no config checks it
out any more (`sources.cfg` points to `main` again). The first package
migrated with plone.meta:

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
- Checked from buildout.smartweb: `.venv/bin/buildout -N` no longer develops
  it, and `bin/zopepy` imports the pinned 2.0.0 egg, which has no namespace
  marker (no `pas/__init__.py` or `pas/plugins/__init__.py`).

## plone.formwidget.geolocation

**Namespaces** `plone`, `plone.formwidget` · **Repository**
[collective/plone.formwidget.geolocation](https://github.com/collective/plone.formwidget.geolocation),
branch `master` (upstream) · **Checked out by** `base.cfg` (so prod too)

Done by switching from the IMIO fork (branch `fix-geosearch`) to upstream
`master` in `sources.cfg`. Upstream `master` (4.0.0, unreleased) is already
migrated: native namespaces, `src/` layout, Plone 6.2 only. It also fixed
buildout for the `plone` namespace
([blockers](native-namespaces-migration.md#blockers-for-plone-623)).

Why it is still checked out, and why it can't be pinned yet:
[plone.formwidget.geolocation](plone-formwidget-geolocation.md).

- **Lost: the faceted map refresh (WEB-4028).** The fork's bundle was built
  from `affinitic/pat-leaflet@refresh-geojson`, which adds the
  `leaflet.refresh` handler that collective.faceted.map and
  imio.smartweb.core's faceted map trigger after each search. Upstream
  pat-leaflet never merged it
  ([#36](https://github.com/Patternslib/pat-leaflet/pull/36)), so `master`'s
  bundle ignores the event, and the markers probably stay on the first
  results. Found by reading the code, not yet checked in a browser. The
  fork's other commits (pat-leaflet upgrade, and the `default_input_zoom` /
  `default_display_zoom` control panel options) were released upstream in
  3.0.6 and 3.0.7, and are on `master`.
- **Upgrade step**: the fork's profile is 2001, upstream's is 2002. Existing
  sites get one pending upgrade, "Add zoom for input and display", which
  re-imports the registry records of the zoom options. Run it and check that
  the zoom values set in the control panel are kept.
- **Production**: `versions.cfg` still pins 3.0.6, but the checkout in
  `base.cfg` overrides it, so every prod build clones the moving `master`.
  No release has the refresh fix, neither 3.0.x nor a future 4.0.0: until
  pat-leaflet releases it, check out an IMIO `plone62` branch with a rebuilt
  bundle ([recommended path](plone-formwidget-geolocation.md#recommended-path)).
- The old fork checkout must be moved away before mr.developer can clone the
  new URL (`bin/develop co plone.formwidget.geolocation`). Until then, dev
  still runs the old-style fork (3.0.4.dev0), with the fix, while a fresh
  build gets `master`, without it.

## Bumped to a native release

Their latest release on PyPI uses native namespaces: the pin is bumped, and
the feature that uses the package must be tested. Most are major version
bumps, so read their changelog first.

| Package | Was | Now | What to test |
|---|---|---|---|
| collective.geolocationbehavior | 1.7.2 | 2.0.0 (2026-11-12) | Bumped in `62f79d5`. Major bump |
| collective.taxonomy | 3.1.7 | 4.0.0 (2026-10-20) | Bumped 2026-11-16 (`12dde8e`). Major bump: the taxonomy pages and widgets. 3.1.7 also called `pkg_resources` (`DistributionNotFound` in `behavior.py`) |
| plone.app.imagecropping | 3.0.3 | 4.0.0 (2026-10-30) | Bumped 2026-11-16 (only breaking change: Plone 6.2 only). The cropping editor. 3.0.3 also called `get_distribution()` in `__init__.py` |
| plone.formwidget.recaptcha | 2.3.0 | 4.0.0 (2026-11-10) | Bumped 2026-11-16. Major bump: the forms that use the captcha |
| plone.patternslib | 9.10.3.1 | 9.11.1 (2026-09-19) | Bumped 2026-11-16. Minor bump: the front-end JavaScript |
| zope.minmax | 3.0 | 4.0 (2025-09-12) | Bumped 2026-11-16. Major bump |
| zope.session | 5.1 | 6.0 (2025-09-12) | Bumped 2026-11-16. Major bump |

## Still old-style upstream

Their latest release on PyPI still uses old-style namespaces (checked
2026-11-26). None of them calls `pkg_resources` beyond `declare_namespace`, so
none blocks Plone 6.2.3. Their wheels have no namespace `__init__.py`, only an
`nspkg.pth` file, which an egg directory doesn't load: buildout's eggs import
as native portions. `base.cfg` no longer loads horse-with-no-namespace
(2026-11-19, `c4a2538`), but Plone's `requirements.txt` still installs it in
`.venv`. What to do with each one:
[not started](native-namespaces-migration.md#not-started).

| Package | Pinned | Latest on PyPI | Notes |
|---|---|---|---|
| plone.gallery | 1.1.6 | 1.1.6 (2023) | |
| hurry.filesize | 0.9 | 0.9 (2009) | Unmaintained. Only collective.exportimport 1.x requires it, 2.x (`plone62`) drops it: remove the pin once 2.x is pinned |
