# plone.formwidget.geolocation: why it is checked out, and can it be pinned?

Part of the [native namespace migration](native-namespaces-migration.md)
(WEB-4533). What changed in the package:
[package details](native-namespaces-packages.md#ploneformwidgetgeolocation).

Last updated: 2026-11-18.

## Context

On branch `plone62`, `plone.formwidget.geolocation` is the only package in the
`auto-checkout` of `base.cfg`. Because of that, **prod also uses it**:
`prod.cfg` extends `base.cfg`, so every prod image gets a fresh git clone.
`sources.cfg` points it at collective `master`, a moving branch. The
`plone.formwidget.geolocation = 3.0.6` pin in `versions.cfg` is ignored while
the package is checked out.

## Why it is checked out

| When | Commit | What |
|---|---|---|
| 2023-02 | `a86fa19` | Checked out from the iMio fork, "waiting for a fixed community release" |
| 2023-10 | `b74633c` | Back to a released version (3.0.5, then 3.0.6) |
| 2023-12 | `13c4edd` (WEB-4028) | iMio fork `fix-geosearch` restored: "We must wait for Patternslib/pat-leaflet#36" |
| 2026-11-16 | `9c53097` (WEB-4533) | Switched to collective `master`, "waiting to version 4.0.0" |

**The original reason (WEB-4028), still unresolved:** the iMio fork
`fix-geosearch` is 3.0.6 plus a JS bundle built from
`affinitic/pat-leaflet@refresh-geojson` (fork commit `b4512ef`). That
pat-leaflet branch adds a `leaflet.refresh` event handler, which re-draws the
markers from new GeoJSON. Two things use it:

- `collective.faceted.map/.../browser/mapviewlet.pt:14,17`
- `imio.smartweb.core/.../browser/faceted/map.pt:72`

Each time a faceted search runs, they trigger `leaflet.refresh`.
`collective.faceted.map` has no pat-leaflet of its own: the pattern comes from
the `plone-formwidget-geolocation` bundle, which is enabled on every page.
**Upstream pat-leaflet has never had this handler**:
[#36](https://github.com/Patternslib/pat-leaflet/pull/36) has been open since
2023-02, and the latest release, 2.2.2, does not include it.

**The new reason (WEB-4533, Plone 6.2):** collective `master` is the
unreleased 4.0.0. It moves to PEP 420 native namespaces and a src layout,
imports from `plone.base` instead of `Products.CMFPlone`, and requires Plone
6.2. Apart from that, it only adds translations and lint fixes: its compiled
JS in `static/` is the same as 3.0.7's.

## Findings

1. **Switching to collective `master` dropped the WEB-4028 fix.** The `master`
   bundle uses the released pat-leaflet, so `leaflet.refresh` does nothing.
   The faceted map markers probably stay on the first result set after a
   filter changes. I found this by reading the code; I have not run it yet.
2. **Local dev hides it.** `src/plone.formwidget.geolocation` is still the
   iMio fork on `fix-geosearch` (3.0.4.dev0). mr.developer does not change the
   remote of an existing checkout. So dev runs the patched bundle, while a
   fresh prod or CI build gets collective `master`.
3. **No release to pin to.** The latest version on PyPI is 3.0.7
   (2024-08-28); 4.0.0 is not released.
4. **Tracking the moving `master` in prod builds is not reproducible.** Any
   upstream merge goes straight into the next prod image.

## Answer: can it safely be pinned?

**No, not yet.**

- Pinning 3.0.6 or 3.0.7 loses the `leaflet.refresh` fix. It also keeps the
  old namespace packages (`pkg_resources`) that WEB-4533 is removing (they
  would only load thanks to the `horse-with-no-namespace` shim).
- 4.0.0 does not exist on PyPI. Once released, it would still lack the
  refresh fix.

## Recommended path

1. **Check the regression** (step 1 of [Verification](#verification)).
2. **Upstream first** (Zen 2). Rebase the 9-line `leaflet.refresh` patch from
   [#36](https://github.com/Patternslib/pat-leaflet/pull/36) onto pat-leaflet
   2.2.2 and get it merged and released. Then ask the collective maintainers
   (erral, Mikel Larreategi) to release plone.formwidget.geolocation 4.0.0,
   with its bundle rebuilt against that pat-leaflet.
3. **Until then, make the checkout reproducible:**
   - Create an iMio fork branch `plone62` = collective `master` + the bundle
     rebuilt with the patched pat-leaflet (`package.json` → patched
     pat-leaflet, `yarn build`, commit `static/`).
   - Point `sources.cfg` at `${remotes:imio}`, `branch=plone62`,
     `rev=<sha>`.
   - Keep the checkout in `base.cfg`. A private egg on
     `eggs.imio.be/find-links` is another option, but it is more work.
4. **When the release exists:** remove the package from the `auto-checkout`
   in `base.cfg` and from `sources.cfg`, and set
   `plone.formwidget.geolocation = 4.0.0` in `versions.cfg`. Bumping the pin
   needs no CHANGES.rst entry, but removing the fork does (with
   WEB-4028/WEB-4533).
5. **Optional, outside this repo:** move the refresh logic into
   `collective.faceted.map`, so SmartWeb no longer depends on a pat-leaflet
   patch.

## Files to change (steps 3 and 4)

- `base.cfg`: `auto-checkout` block
- `sources.cfg`: the `plone.formwidget.geolocation` line
- `versions.cfg`: the `plone.formwidget.geolocation` pin
- `CHANGES.rst`

## Verification

1. **Regression:** re-clone the package from collective `master`, or run
   `bin/develop rb -f plone.formwidget.geolocation` after fixing the remote,
   then `make start`. Open a faceted map page (directory or events with the
   map), change a filter, and check that the markers follow the results. In
   the browser console, `$('#faceted-map-container').trigger('leaflet.refresh', …)`
   should redraw the markers. Compare with the iMio fork checkout.
2. **After the change:** run `make test`, which builds the prod image from a
   fresh checkout, then repeat step 1 against the image.
3. **Check what was actually installed:** in `bin/instance debug`, check
   `plone.formwidget.geolocation.__file__` and its version.
