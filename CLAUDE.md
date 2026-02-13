# buildout.smartweb

Plone 6.1.3 buildout for iMio SmartWeb — a CMS platform for Belgian local authorities. Uses `uv` for Python environment management and `mr.developer` for source checkouts.

## Development commands

```
make install          # Create venv, install deps via uv, run buildout
make start            # Start Zope instance in foreground (also starts Solr)
make lint             # Run pre-commit hooks on all files (uvx pre-commit run --all)
make cleanall         # Remove venv, eggs, bin, parts — full clean rebuild
make upgrade-steps    # Run pending Plone portal upgrade steps
make release          # Full release via zest.releaser
make solr             # Start Solr container (foreground)
make solr-background  # Start Solr container (background)
```

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

Supporting packages: `collective.pivot`, `collective.preventactions`, `collective.upgrade`, `pas.plugins.imio`, `pas.plugins.kimug`, `plone.formwidget.geolocation`

## Testing

Each src/ package has its own test infrastructure. Run tests from within the package:

```
cd src/imio.smartweb.core
bin/test
```

Or use the package's own buildout (e.g. `src/imio.smartweb.core/buildout.cfg`).

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
