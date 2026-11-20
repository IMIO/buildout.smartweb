# Migrating to native namespace packages (PEP 420)

Tracks the move of the SmartWeb stack (branch `plone62`, Plone 6.2.3) away
from old-style namespace packages: where each package stands, what's left to
do, and how to migrate one. What changed in each package, and its gotchas:
[package details](native-namespaces-packages.md).

Last updated: 2026-11-20.

## Status

**26 pinned** (19 migrated, 7 bumped) · **7 merged**, not released · **4 PRs
open** · **4 branches pushed**, no PR yet · **3 not started** (none of them
blocks Plone 6.2.3)

✅ done · ⬜ to do · ➖ not applicable · 🚧 its pinned release calls
`pkg_resources` and fails on Plone 6.2.3 ([blockers](#blockers-for-plone-623)) ·
⚠️ its native branch drops an iMio fix
([details](plone-formwidget-geolocation.md))

| Package | Branch | Checked | PR | Merged | Released | Pinned |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| [collective.anysurfer](native-namespaces-packages.md#collectiveanysurfer) | ✅ | ✅ | [#9](https://github.com/collective/collective.anysurfer/pull/9) | ✅ | ✅ | ✅ |
| [collective.autopublishing](native-namespaces-packages.md#collectiveautopublishing) | ✅ | ✅ | [#12](https://github.com/collective/collective.autopublishing/pull/12) | ✅ | ⬜ | ⬜ |
| [collective.autoscaling](native-namespaces-packages.md#collectiveautoscaling) | ✅ | ✅ | [#9](https://github.com/collective/collective.autoscaling/pull/9) | ✅ | ✅ | ✅ |
| [collective.behavior.talcondition](native-namespaces-packages.md#collectivebehaviortalcondition) | ✅ | ✅ | [#17](https://github.com/collective/collective.behavior.talcondition/pull/17) | ✅ | 2.0.0 | ✅ |
| [collective.complexrecordsproxy](native-namespaces-packages.md#collectivecomplexrecordsproxy) | ✅ | ✅ | [#3](https://github.com/collective/collective.complexrecordsproxy/pull/3) | ✅ | ⬜ | ⬜ |
| [collective.exportimport](native-namespaces-packages.md#collectiveexportimport) 🚧 | ✅ | ✅ | [#287](https://github.com/collective/collective.exportimport/pull/287) | ⬜ | ⬜ | ⬜ |
| [collective.faceted.map](native-namespaces-packages.md#collectivefacetedmap) | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| [collective.fingerpointing](native-namespaces-packages.md#collectivefingerpointing) | ✅ | ✅ | [#110](https://github.com/collective/collective.fingerpointing/pull/110) | ✅ | ✅ | ✅ |
| [collective.geolocationbehavior](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 2.0.0 | ✅ |
| [collective.geotransform](native-namespaces-packages.md#collectivegeotransform) | ✅ | ✅ | [#25](https://github.com/collective/collective.geotransform/pull/25) | ✅ | 4.0.0 | ✅ |
| [collective.instancebehavior](native-namespaces-packages.md#collectiveinstancebehavior) | ✅ | ✅ | [#7](https://github.com/collective/collective.instancebehavior/pull/7) | ⬜ | ⬜ | ⬜ |
| [collective.js.jqueryui](native-namespaces-packages.md#collectivejsjqueryui) | ✅ | ✅ | [#57](https://github.com/collective/collective.js.jqueryui/pull/57) | ✅ | ✅ | ✅ |
| [collective.messagesviewlet](native-namespaces-packages.md#collectivemessagesviewlet) | ✅ | ✅ | [#24](https://github.com/collective/collective.messagesviewlet/pull/24) | ✅ | 2.0.0 | ✅ |
| [collective.pivot](native-namespaces-packages.md#collectivepivot) | ✅ | ✅ | [#4](https://github.com/IMIO/collective.pivot/pull/4) | ✅ | 2.0.0 | ✅ |
| [collective.preventactions](native-namespaces-packages.md#collectivepreventactions) | ✅ | ✅ | [#2](https://github.com/collective/collective.preventactions/pull/2) | ✅ | 0.4.0 | ✅ |
| [collective.privacy](native-namespaces-packages.md#collectiveprivacy) | ✅ | ✅ | [#22](https://github.com/collective/collective.privacy/pull/22) | ✅ | 2.0.0 | ✅ |
| [collective.prometheus](native-namespaces-packages.md#still-old-style-upstream) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| [collective.solr](native-namespaces-packages.md#collectivesolr) | ✅ | ✅ | [#408](https://github.com/collective/collective.solr/pull/408) | ⬜ | ⬜ | ⬜ |
| [collective.taxonomy](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 4.0.0 | ✅ |
| [collective.themefragments](native-namespaces-packages.md#collectivethemefragments) | ✅ | ✅ | [#20](https://github.com/collective/collective.themefragments/pull/20) | ✅ | ⬜ | ⬜ |
| [collective.timedevents](native-namespaces-packages.md#collectivetimedevents) | ✅ | ✅ | [#13](https://github.com/collective/collective.timedevents/pull/13) | ✅ | ✅ | ✅ |
| [collective.upgrade](native-namespaces-packages.md#collectiveupgrade) | ✅ | ✅ | [#20](https://github.com/collective/collective.upgrade/pull/20) | ✅ | ⬜ | ⬜ |
| [collective.z3cform.select2](native-namespaces-packages.md#collectivez3cformselect2) | ✅ | ✅ | [#15](https://github.com/collective/collective.z3cform.select2/pull/15) | ✅ | ✅ | ✅ |
| [eea.facetednavigation](native-namespaces-packages.md#eeafacetednavigation) | ✅ | ✅ | [#65](https://github.com/collective/eea.facetednavigation/pull/65) | ✅ | ⬜ | ⬜ |
| [hurry.filesize](native-namespaces-packages.md#still-old-style-upstream) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| [iaweb.privacy](native-namespaces-packages.md#iawebprivacy) | ✅ | ✅ | [#2](https://github.com/IMIO/iaweb.privacy/pull/2) | ✅ | 2.0.0 | ✅ |
| [imio.gdpr](native-namespaces-packages.md#imiogdpr) | ✅ | ✅ | [#5](https://github.com/IMIO/imio.gdpr/pull/5) | ✅ | 2.0.0 | ✅ |
| [imio.helpers](native-namespaces-packages.md#imiohelpers) 🚧 | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.omnia.core](native-namespaces-packages.md#imioomniacore) | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.omnia.tinymce](native-namespaces-packages.md#imioomniatinymce) | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| [imio.prometheus](native-namespaces-packages.md#imioprometheus) | ✅ | ✅ | [#2](https://github.com/IMIO/imio.prometheus/pull/2) | ⬜ | ⬜ | ⬜ |
| [imio.pyutils](native-namespaces-packages.md#imiopyutils) | ✅ | ✅ | [#4](https://github.com/IMIO/imio.pyutils/pull/4) | ✅ | ⬜ | ⬜ |
| [imio.smartweb.common](native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | ✅ | ✅ | [#37](https://github.com/IMIO/imio.smartweb.common/pull/37) | ✅ | 2.0.0 | ✅ |
| [imio.smartweb.core](native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | ✅ | ✅ | [#102](https://github.com/IMIO/imio.smartweb.core/pull/102) | ✅ | 2.0.0 | ✅ |
| [imio.smartweb.locales](native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | ✅ | ✅ | [#4](https://github.com/IMIO/imio.smartweb.locales/pull/4) | ✅ | 2.0.0 | ✅ |
| [imio.smartweb.policy](native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy) | ✅ | ✅ | [#28](https://github.com/IMIO/imio.smartweb.policy/pull/28) | ✅ | 2.0.0 | ✅ |
| [pas.plugins.kimug](native-namespaces-packages.md#paspluginskimug) | ✅ | ✅ | [#34](https://github.com/IMIO/pas.plugins.kimug/pull/34) | ✅ | 2.0.0 | ✅ |
| [plone.app.imagecropping](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 4.0.0 | ✅ |
| [plone.formwidget.geolocation](native-namespaces-packages.md#ploneformwidgetgeolocation) ⚠️ | ✅ | ⬜ | ➖ | ✅ | ⬜ | ⬜ |
| [plone.formwidget.recaptcha](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 4.0.0 | ✅ |
| [plone.gallery](native-namespaces-packages.md#still-old-style-upstream) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| [plone.patternslib](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 9.11.1 | ✅ |
| [zope.minmax](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 4.0 | ✅ |
| [zope.session](native-namespaces-packages.md#bumped-to-a-native-release) | ➖ | ⬜ | ➖ | ➖ | 6.0 | ✅ |

Columns:

- **Branch**: a native branch is pushed (ours or upstream's). `local`:
  committed, not pushed yet. ➖: nothing to migrate, a native release
  already exists.
- **Checked**: buildout.smartweb loads the branch ([step 5](#5-clean-up-and-check)):
  `.venv/bin/buildout -N` no longer lists it as old-style, and `bin/zopepy`
  imports it from the checkout (or, once released and pinned, from the egg).
  `bin/instance fg` serves with every checkout loaded (2026-11-17). For a
  bumped package: the feature that uses it is tested on a SmartWeb site.
- **PR**: link to the pull request that merges the branch. ⬜: none opened
  yet. ➖: done upstream, without us.
- **Released**: the native version on PyPI. **Pinned**: `versions.cfg` pins it.

Plone and Zope core packages aren't listed: Plone 6.2.3 pins native releases
of plone.app.content, plone.autoform, plone.restapi and Paste. PasteDeploy
3.1.0 is still old-style, and comes with Plone's pins: nothing to do.

collective.sendinblue isn't listed either: imio.smartweb.core no longer
depends on it, so it doesn't need to be migrated
([details](native-namespaces-packages.md#imiosmartwebcommon-core-locales-policy)).

## What's left

### Update the branches

- [x] imio.helpers: `master` (1.3.19) merged into `plone62` (2026-11-18,
  `7c640c8`), the `CHANGES.rst` entry is now under 1.3.20 (unreleased).
- [x] imio.omnia.tinymce: `master` (1.1) merged into `plone62` (2026-11-18,
  `785d77f`). Commit `a9c4c86` (simplify-text and structure-text) is still in
  neither.
- [ ] plone.formwidget.geolocation: create an IMIO `plone62` branch
  (collective `master` plus the bundle rebuilt with the patched pat-leaflet),
  point `sources.cfg` at it with a fixed `rev`, then re-clone `src/`, which
  is still the old-style `fix-geosearch` fork
  ([details](plone-formwidget-geolocation.md#recommended-path)).

### Open pull requests

Rows with ⬜ in the PR column, and open questions on existing PRs:

- [ ] imio.omnia.core, imio.omnia.tinymce (IMIO)
- [ ] imio.helpers, once its maintainers agree on a 1.3.x maintenance branch
  for the other iMio applications
- [ ] collective.faceted.map (affinitic)
- [ ] collective.instancebehavior
  ([#7](https://github.com/collective/collective.instancebehavior/pull/7)):
  ask upstream which license applies
  ([details](native-namespaces-packages.md#collectiveinstancebehavior))

### Release

When the Plone 6.2 stack goes to production ([step 6](#6-release)). A PyPI
release can't depend on a git branch, so the order matters:

- [x] collective.timedevents 2.0.0 is released: collective.autopublishing's
  `master` requires it, and its `mx.ini` and tox no longer install the
  branch.
- [ ] Replace the collective.privacy branch in iaweb.privacy's `mx.ini` and
  tox by the 2.0.0 release.
- [ ] Replace the collective.behavior.talcondition `plone62` branch (now
  deleted) in imio.helpers' `test-6.2.cfg` by the 2.0.0 release.
- [ ] imio.omnia.core and imio.omnia.tinymce together (shared `imio.omnia`
  namespace).
- [x] imio.smartweb.common, .core, .locales and .policy: 2.0.0 released and
  pinned (core on 2026-11-20).
- [ ] imio.pyutils as 1.3.0 (not breaking; `master` says 1.2.4.dev0).
  collective.instancebehavior as 0.6 (never released, 0.5 is the latest).
  collective.themefragments as 3.0.0 (2.12, from 2019, is the latest; asked
  upstream on [#20](https://github.com/collective/collective.themefragments/pull/20)).
  Every other package as 2.0.0.
- [ ] Ask upstream for collective.solr 11.0.0 once
  [#408](https://github.com/collective/collective.solr/pull/408) is merged.
- [ ] Ask upstream for plone.formwidget.geolocation 4.0.0 once pat-leaflet
  has released the `leaflet.refresh` handler, with its bundle rebuilt against
  it ([details](plone-formwidget-geolocation.md#recommended-path)).

### Check by hand on a SmartWeb site

- [ ] collective.taxonomy 4.0.0: taxonomy pages and widgets.
- [ ] plone.app.imagecropping 4.0.0: the cropping editor.
- [ ] plone.formwidget.recaptcha 4.0.0: the forms that use the captcha.
- [ ] plone.patternslib 9.11.1: the front-end JavaScript.
- [ ] collective.geolocationbehavior 2.0.0, zope.minmax 4.0, zope.session 6.0:
  major bumps.
- [ ] plone.formwidget.geolocation: run the "Add zoom for input and display"
  upgrade step, and check that the zoom values are kept. On a faceted map
  (directory or events), change a filter and check that the markers follow
  the results ([details](plone-formwidget-geolocation.md#verification)).
- [ ] collective.privacy: the JavaScript consent banner (its only tests are
  gone).
- [ ] collective.anysurfer: the search page and the breadcrumb (Plone 5
  markup).
- [ ] collective.solr 11.0.0.dev0 (two major versions from 9.4.0): search,
  faceted navigation and indexing. Check the production Solr version too
  ([details](native-namespaces-packages.md#collectivesolr)).
- [ ] collective.z3cform.select2 4.0.0: the select2 widgets.
- [ ] collective.instancebehavior: imio.smartweb.core's instance behaviors
  form (enable then disable a taxonomy on a page).
- [ ] eea.facetednavigation 17.0.0.dev0: the faceted views, their widgets and
  the faceted edit form (zpretty reformatted every template, and the JS
  bundles moved under `src/`).
- [ ] collective.js.jqueryui 3.0.0: whatever uses jQuery UI, which the bundle never
  loaded before
  [#58](https://github.com/collective/collective.js.jqueryui/pull/58).
- [ ] collective.themefragments: the theme fragments and their Python
  modules, with debug mode off (the theme cache, which the tests don't
  cover).

### Fix upstream

- [ ] plone.restapi 10.2.1 drops every image and file imported by
  collective.exportimport (and any multipart content import) on Plone 6.2.3.
  Fixed by [#2094](https://github.com/plone/plone.restapi/pull/2094), merged
  2026-11-18, first released in 10.3.1 (not out yet). Once it is out, pin
  `plone.restapi` in `versions.cfg` (Plone 6.2.3 pins 10.2.1) and mark
  collective.exportimport
  [#287](https://github.com/collective/collective.exportimport/pull/287) ready
  for review ([details](native-namespaces-packages.md#collectiveexportimport)).
- [ ] pat-leaflet: rebase the `leaflet.refresh` handler of
  [#36](https://github.com/Patternslib/pat-leaflet/pull/36) onto 2.2.2, and
  get it merged and released. The faceted maps need it
  ([details](plone-formwidget-geolocation.md#recommended-path)).

### Not started

- [ ] The 3 [still old-style](native-namespaces-packages.md#still-old-style-upstream)
  third-party packages. For each one, in order of preference:
  1. Check the repository's main branch: the migration may already be merged
     and only waiting for a release. Ask the maintainers for a release.
  2. Open a PR applying [the recipe](#the-migration-recipe).
  3. If the package is unmaintained and we still need it, fork it under IMIO.
  4. If we no longer need it, remove it.

### Clean up

- [ ] imio.smartweb.common's own `base.cfg`: drop the `[versions]` that restore
  Plone 6.2.3 pins, buildout.smartweb pins 6.2.3 now.
- [ ] collective.preventactions: `sources.cfg` still names its old `plone6`
  branch, switch it to `master`. Like pas.plugins.kimug, it is released and
  pinned, and no config checks it out any more.
- [x] collective.sendinblue: `versions.cfg` no longer pins it, and
  imio.smartweb.core 2.0.0 no longer requires it.
- [ ] Drop the `hurry.filesize` pin from `versions.cfg` once
  collective.exportimport 2.x is pinned: only exportimport 1.x requires it.
- [ ] Once the last old-style package is gone, remove `horse-with-no-namespace`
  from `base.cfg` (`eggs` and `initialization`). Plone's `requirements.txt`
  still installs it.

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
error. [Step 3](#3-remove-other-pkg_resources-uses) of the recipe is
therefore mandatory before moving to 6.2.3.

Watch out: with the stub in place, `import pkg_resources` succeeds, so a
`try: import pkg_resources / except ImportError` guard does not catch it.
Only the failing attribute access does.

Mixing both styles works today only because of `horse-with-no-namespace`,
installed by Plone's `requirements.txt` and imported in
`[instance] initialization` (`base.cfg`). Once every package is native, that
workaround can go.

### Blockers for Plone 6.2.3

Found by running the imio.smartweb.common tests and starting buildout.smartweb
on Plone 6.2.3 (2026-11-16), and scanning the eggs that `bin/test` and
`bin/instance` load.

**At import time.** The 🚧 packages call `pkg_resources` beyond
`declare_namespace` in every release: their fixed branch stays checked out
until it is released. Each package's details say which call it was.
eea.facetednavigation 16.5, collective.taxonomy 4.0.0 and
plone.app.imagecropping 4.0.0 had the same problem, solved by bumping them.
Babel, Paste, pytz and grpcio-tools also mention `pkg_resources`, but only as
a guarded fallback that isn't reached on Python 3.12.

**While running buildout.** buildout.smartweb stopped on 6.2.3 (zc.buildout
6.0.2) while loading its recipes, with `ModuleNotFoundError: No module named
'plone.recipe'` (or `'collective.recipe'`). The cause: each old-style package
checked out in `src/` leaves a `<package>-<version>-nspkg.pth` file in the
develop-eggs directory (`~/.buildout/develop-eggs`, shared by all your
buildouts through `~/.buildout/default.cfg`). zc.buildout 6 loads these files,
and they make the namespace module (`plone`, `collective`…) look only in the
`src/` checkouts, so recipe eggs in the same namespace can't be found.
`horse-with-no-namespace` doesn't fix this.

- `plone`: fixed by switching plone.formwidget.geolocation to upstream
  `master`, which is native.
- `collective`: fixed by migrating the `collective.*` checkouts, which broke
  `collective.recipe.omelette`, `collective.recipe.vscode`, etc. An old-style
  `collective.*` checkout breaks buildout again: migrate it before checking it
  out.
- `imio` and `pas`: no recipe lives in these namespaces, so old-style
  checkouts there don't break buildout.

Since 2026-11-16, buildout.smartweb's buildout passes on Plone 6.2.3.

## The migration recipe

This is what
[collective.big.bang `bfe22ca`](https://github.com/collective/collective.big.bang/commit/bfe22ca)
did. It applies to any package with a `setup.py`. Two variants follow:
[plone.meta](#variant-plonemeta), which also modernizes the package, and
[keep Python 2](#variant-keep-python-2).

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
   (`git push -u origin plone62`) and open the PR.

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

Then, from `buildout.smartweb`, with the package in `auto-checkout` in
`dev.cfg`:

1. Run `.venv/bin/buildout -N`. The package must no longer be listed in the
   *"old style namespace packages"* warning.
2. Check that `bin/zopepy -c "import <package>"` imports it from `src/`, then
   run `bin/instance fg` and wait for `Serving on http://0.0.0.0:8080` with no
   traceback.
3. Run the package's own tests (`bin/test`, `make test` or `tox` in the
   package).
4. Check that the build contains no namespace marker:

   ```sh
   uvx --from build pyproject-build --wheel --outdir dist .
   unzip -l dist/*.whl | grep -E "nspkg.pth|namespace_packages.txt|^.* (imio|collective|pas|plone)/__init__.py$"
   ```

   This should print nothing.

Then tick **Checked** in the [status table](#status).

### 6. Release

When the Plone 6.2 stack goes to production:

- Merge the package's `plone62` branch into `main`, and set `branch=main` again
  in `sources.cfg`.
- Release a new version with a changelog entry such as *"Migrate to PEP 420
  native namespaces (setuptools 81 / Plone 6.2)"*. Dropping Python 2 or a
  Plone version is breaking: release **2.0.0**, even if `CHANGES.rst` announces
  a patch release. Applications on the older stacks then stay on the 1.x
  releases (each package's details say which).
- If the package also keeps test requirements for Plone 6.0 or 6.1 (whose
  `requirements.txt` don't include it), add `horse-with-no-namespace` to them,
  installed in the virtualenv with pip or uv (not with buildout).
  collective.big.bang did this in
  [`8ec39db`](https://github.com/collective/collective.big.bang/commit/8ec39db).
- Pin the new version in `buildout.smartweb/versions.cfg`, and remove the
  package from `auto-checkout`.

### Variant: plone.meta

Most packages migrated after pas.plugins.kimug went further: plone.meta
configures them (tox, GitHub Actions, pre-commit) and their metadata moves to
`pyproject.toml`, so `setup.py` is only `setup()` and setuptools finds the
namespace packages by itself (no `find_namespace_packages`). The package then
supports Plone 6.1 and 6.2 only, on Python 3.10 to 3.13, and is released as
2.0.0.

1. Remove `packages` and `package_dir` from `setup.py`, any
   `sys.version_info` branch, and write `install_requires` inline:
   `setup-to-pyproject` can't parse them. It can't parse a `long_description`
   concatenation either, and it always commits: in that case, write the
   `[project]` section by hand.
2. Run plone.meta 2.12.0 in a clone named after the package, whose `origin`
   is the GitHub URL: it takes the package name from the folder name, and
   only writes the GitHub workflows for a GitHub remote. `switch-to-pep420`
   deletes the namespace `__init__.py` files, `setup-to-pyproject` moves the
   metadata.
3. A package at the repository root moves to a `src/` layout, which
   plone.meta's tox expects.
4. The z3c.autoinclude entry point becomes a `plone.autoinclude.plugin` one.
5. If the package uses CMFCore permissions (`cmf.ManagePortal`…), its
   `configure.zcml` includes `Products.CMFCore` (`permissions.zcml`).
   Otherwise it fails to load when included before Plone
   (`zcml_package_includes`). Autoinclude, as in buildout.smartweb, always
   loads it after Plone and hides the problem.
6. Robot tests that need `plone/app/robotframework/selenium.robot` fail:
   plone.app.robotframework 3 (pinned by Plone 6.2.3) no longer ships it.
7. Declare the dependencies the code imports (tox runs
   z3c.dependencychecker). `IPloneSiteRoot`, `INonInstallable`,
   `get_installer` and `safe_text` come from `plone.base`.
8. For a development environment, copy collective.messagesviewlet's
   `Makefile`, `mx.ini`, `instance.yaml` and `scripts/create_site.py`:
   `make install` builds a uv environment on Plone 6.2.3.
9. If a dependency is only fixed on an unreleased branch, install that branch
   from GitHub in `mx.ini` and tox (`test_deps_additional` in `.meta.toml`)
   until it is released.
10. Run `tox -e format` until it passes: it stops at the first hook that
    changes a file. zpretty puts `tal:` attributes on their own lines and
    sorts the attributes, so the rendered HTML changes (`<legend >`,
    `<input class="..." type="...">`): doctests that compare markup need
    ellipses.

### Variant: keep Python 2

PEP 420 doesn't exist on Python 2. imio.pyutils, used by many iMio
applications still on Python 2, picks the namespace style from the Python
version that builds it:

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

Keep `imio/__init__.py`, and include it in `MANIFEST.in` (see
[imio.pyutils](native-namespaces-packages.md#imiopyutils)).

For an upstream PR that only removes the `pkg_resources` calls and must keep
Python 2, use a fallback:

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

then `get_version("x")` / `except PackageNotFoundError`. The namespace
migration then goes in a separate commit, or a separate branch, that drops
Python 2.

### Rules

- **Keep `horse-with-no-namespace` until the last package is migrated.** A
  native `imio` namespace and old-style `imio.*` eggs only coexist through it.
- **Migrate packages that share a namespace together** (the four
  `imio.smartweb.*`, the two `imio.omnia.*`), so the namespace never has two
  styles in your own code.

## How the inventory was built

Last full scan: 2026-11-10, against the eggs loaded by `bin/instance` and the
latest releases on PyPI.

- `src/` packages: buildout's warning (*"Some development packages are using
  old style namespace packages"*) and `namespace_packages.txt` in each
  `.egg-info`.
- Eggs: a `*-nspkg.pth` or `namespace_packages.txt` file in the eggs listed in
  `bin/instance`.
- PyPI: the latest wheel (or sdist) of each package, checked for the same
  markers and for `declare_namespace`.
- Out of scope: prod-only eggs (`RelStorage`, `pylibmc`, `psycopg2`), which
  don't use namespaces.
