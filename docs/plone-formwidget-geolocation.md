# plone.formwidget.geolocation: pinned to 4.0.0, without the faceted map refresh

Part of the [native namespace migration](native-namespaces-migration.md)
(WEB-4533). What changed in the package:
[package details](native-namespaces-packages.md#ploneformwidgetgeolocation).

Last updated: 2026-11-27.

## Context

On branch `plone62`, `versions.cfg` pins `plone.formwidget.geolocation = 4.0.0`,
released on PyPI on 2026-11-27 (sdist only, no wheel). No config checks it out
any more: `base.cfg` no longer lists it in `auto-checkout`, and `sources.cfg`
no longer names it. Dev, CI and prod builds now all install the same egg.

4.0.0 is collective `master` released: PEP 420 native namespaces, a src
layout, imports from `plone.base` instead of `Products.CMFPlone`, Plone 6.2
only. Apart from that, it only adds translations and lint fixes: its bundle is
still built from pat-leaflet 2.2.0, like 3.0.7's.

## History

| When | Commit | What |
|---|---|---|
| 2023-02 | `a86fa19` | Checked out from the iMio fork, "waiting for a fixed community release" |
| 2023-10 | `b74633c` | Back to a released version (3.0.5, then 3.0.6) |
| 2023-12 | `13c4edd` (WEB-4028) | iMio fork `fix-geosearch` restored: "We must wait for Patternslib/pat-leaflet#36" |
| 2026-11-16 | `9c53097` (WEB-4533) | Switched to collective `master`, "waiting to version 4.0.0" |
| 2026-11-27 | WEB-4533 | 4.0.0 pinned, no longer checked out |

**The WEB-4028 fix, still missing upstream:** the iMio fork `fix-geosearch`
is 3.0.6 plus a JS bundle built from `affinitic/pat-leaflet@refresh-geojson`
(fork commit `b4512ef`). That pat-leaflet branch adds a `leaflet.refresh`
event handler, which re-draws the markers from new GeoJSON. Two things use it:

- `collective.faceted.map/.../browser/mapviewlet.pt:14,17`
- `imio.smartweb.core/.../browser/faceted/map.pt:72`

Each time a faceted search runs, they trigger `leaflet.refresh`.
`collective.faceted.map` has no pat-leaflet of its own: the pattern comes from
the `plone-formwidget-geolocation` bundle, which is enabled on every page.
**Upstream pat-leaflet has never had this handler**:
[#36](https://github.com/Patternslib/pat-leaflet/pull/36) has been open since
2023-02 (no activity since 2023-12), and the latest release, 2.2.2, does not
include it.

## Findings

1. **4.0.0 drops the WEB-4028 fix.** Its `package.json` pins pat-leaflet
   2.2.0, and no file of the 4.0.0 sdist mentions `leaflet.refresh`, while
   the fork's bundle does (`static/chunks/209.*.min.js`). So
   `leaflet.refresh` does nothing, and the faceted map markers probably stay
   on the first result set after a filter changes. Found by reading the code
   (2026-11-27); not checked in a browser yet.
2. **Dev and prod now match.** Before the pin, an existing
   `src/plone.formwidget.geolocation` checkout kept the iMio fork (3.0.4.dev0,
   with the fix), because mr.developer does not change the remote of an
   existing checkout, while a fresh build cloned collective `master`. Now
   every build uses the 4.0.0 egg. The old `src/` checkout is no longer
   developed and can be deleted.
3. **Builds are reproducible again.** Prod no longer clones the moving
   `master`.

## Recommended path

1. **Check the regression** (step 2 of [Verification](#verification)).
2. **Upstream first** (Zen 2). Rebase the 9-line `leaflet.refresh` patch from
   [#36](https://github.com/Patternslib/pat-leaflet/pull/36) onto pat-leaflet
   2.2.2 and get it merged and released. Then ask the collective maintainers
   (erral, Mikel Larreategi) for a plone.formwidget.geolocation release with
   its bundle rebuilt against that pat-leaflet, and bump the pin.
3. **Optional, outside this repo:** move the refresh logic into
   `collective.faceted.map`, so SmartWeb no longer depends on a pat-leaflet
   patch.

## Verification

1. **What is installed:** `grep geolocation bin/instance` shows
   `~/.buildout/eggs/.../plone.formwidget.geolocation-4.0.0-...egg`, not
   `src/`. In `bin/zopepy`, check `plone.formwidget.geolocation.__file__` and
   `importlib.metadata.version("plone.formwidget.geolocation")`.
2. **Regression:** `make start`, open a faceted map page (directory or events
   with the map), change a filter, and check whether the markers follow the
   results. In the browser console,
   `$('#faceted-map-container').trigger('leaflet.refresh', …)` should redraw
   the markers.
3. **Upgrade step:** on an existing site, run the pending "Add zoom for input
   and display" upgrade step (profile 2001 → 2002), and check that the zoom
   values set in the control panel are kept.
4. **Prod image:** `make test` builds it from the pins.
