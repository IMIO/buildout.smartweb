# buildout.smartweb

Plone 6.1.3 buildout for iMio SmartWeb — a CMS platform for Belgian local authorities. Uses `uv` for Python environment management and `mr.developer` for source checkouts.

## Development commands

```
make install          # Create venv, install deps via uv, run buildout
make start            # Start Zope instance in foreground (also starts Solr) — serves the built prod React bundle, no VITE_DEV_URL needed
make dev              # Same as make start, plus a Vite dev server (webcomponents/) for React HMR
make build            # Build the webcomponents production bundle (npm run build)
make test             # Build the prod image, boot it with Postgres/Solr/memcached and run the smoke tests
make lint             # Run pre-commit hooks on all files (uvx pre-commit run --all)
make cleanall         # Remove venv, eggs, bin, parts — full clean rebuild
make upgrade-steps    # Run pending Plone portal upgrade steps
make release          # Full release via zest.releaser
make solr             # Start Solr container (foreground)
make solr-background  # Start Solr container (background)
```

`make dev` sets `VITE_DEV_URL` only for that process, launching `bin/instance fg` and `npm run watch`
(in `src/imio.smartweb.core/src/imio/smartweb/core/webcomponents`) together so both stop on Ctrl-C. Use it
when iterating on the React webcomponents; use plain `make start` otherwise.

## Buildout config layering

- `base.cfg` — Plone version pins (6.1.3), core eggs, instance recipe
- `dev.cfg` — Development profile (symlinked as `buildout.cfg`): debug-mode on, Solr on localhost:8983, all src/ packages auto-checked-out
- `prod.cfg` — Production: RelStorage/PostgreSQL, memcache, no picked versions
- `sources.cfg` — mr.developer git source definitions (IMIO and collective GitHub repos)
- `versions.cfg` — Local version pins (overrides Plone's upstream pins)

## Source packages (src/)

Checked out via mr.developer. The core SmartWeb packages:

- **imio.smartweb.core** — Content types, views, behaviors, upgrade steps
- **imio.smartweb.common** — Shared utilities across SmartWeb products
- **imio.smartweb.policy** — Site policy (GenericSetup profiles, dependencies)
- **imio.smartweb.locales** — i18n translations

Supporting packages: `collective.pivot`, `collective.preventactions`, `collective.upgrade`, `pas.plugins.kimug`, `plone.formwidget.geolocation`

## Testing

Each src/ package has its own test infrastructure. Run tests from within the package:

```
cd src/imio.smartweb.core
bin/test
```

Or use the package's own buildout (e.g. `src/imio.smartweb.core/buildout.cfg`).

### Image smoke tests

`make test` checks the stack as a whole after a pin or source change: it builds the production image
(`prod.cfg`), starts it with `tests/docker-compose.test.yml` (throwaway Postgres, memcached, Solr; random
host ports, nothing mounted from `var/`), lets `collective.big.bang` create the site, then runs:

- the generic Plone checks from IMIO/gha `plone-image-test-notify` (health probes, add-ons installed with no
  pending upgrade, site root and its JS/CSS, control panels, no error in the instance log);
- `tests/test_smartweb.py` (SmartWeb content types, search).

Log records that are known noise go in `tests/log_allowlist.txt`. Building needs `docker login harbor.imio.be`
(private base image). To work on the generic checks, point `PLONE_IMAGE_TEST` at a local clone of IMIO/gha:
`make test PLONE_IMAGE_TEST=/path/to/gha/plone-image-test-notify`.

CI runs the same tests on pull requests (`tests.yml`).

## Pre-commit hooks

Configured in `.pre-commit-config.yaml`. Runs automatically on commit and via `make lint`:

- check-json, check-merge-conflict, check-symlinks, check-yaml
- yesqa (remove unnecessary `# noqa` comments)
- yamllint (relaxed mode)
- gitlint (commit message linting)
- hadolint (Dockerfile linting via Docker)

## Version pinning

All version pins go in `versions.cfg`. The SmartWeb package versions at the top are the release-managed pins. When pinning a new dependency, add it to `versions.cfg` — never rely on picked versions in dev (prod disallows them).

## Key conventions

- Default admin credentials in dev: `admin:admin`
- Solr runs via Docker Compose on `localhost:8983`
- Source repos are on GitHub under the IMIO and collective organizations
- Releases are managed with `zest.releaser` (`make release`)
