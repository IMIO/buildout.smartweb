# CI/CD Workflows

This repository uses GitHub Actions to build, publish, and deploy the SmartWeb Docker image across three environments: **dev**, **staging**, and **production**.

All workflows run on self-hosted runners labelled `gha-runners-smartweb` and rely on three external tools:

- **Harbor** — Docker image registry
- **Rundeck** — deployment orchestration
- **Mattermost** — notifications

---

## Overview

```mermaid
flowchart TD
    A[push to dev branch] -->|dev.yml| B[Build image :dev]
    B --> C[Push to Harbor]
    C --> D[Deploy to dev via Rundeck]

    E[push to main branch] -->|staging.yml| F[Build image :staging]
    F --> G[Push to Harbor]
    G --> H[Deploy to staging via Rundeck]

    P[push to plone62 branch] -->|staging-plone62.yml| Q[Build image :plone62]
    Q --> R[Push to Harbor]
    R --> S[Update k8s staging tag via ArgoCD repo]

    I[push a git tag] -->|prod.yml| J{quick release?\ntag ends with -quick}
    J -- No --> K[Schedule deploy\nnext day at 3:00 AM]
    J -- Yes --> L[Deploy immediately]

    style K fill:#f5a623,color:#000
    style L fill:#7ed321,color:#000

    note1[" ⚠️ Commits from zest.releaser\n'Preparing release' and\n'Back to development:'\nare skipped by dev.yml and staging.yml"]
    style note1 fill:#fffbe6,stroke:#d4b300,color:#333
```

---

## Making a release

### Prerequisites

- You are on the `main` branch with a clean working tree.
- `CHANGES.rst` has an entry for the version you are about to release.

### Version numbering (semver)

Versions follow `MAJOR.MINOR.PATCH`:

| Bump | When to use |
|------|-------------|
| `PATCH` (e.g. `1.5.28` → `1.5.29`) | Bug fixes, small improvements |
| `MINOR` (e.g. `1.5.x` → `1.6.0`) | New features, backwards-compatible changes |
| `MAJOR` (e.g. `1.x.x` → `2.0.0`) | Breaking changes |

### Running the release

```bash
make release
```

`zest.releaser` will interactively propose the next version. Confirm or adjust it. It will then automatically:

1. Set the release date in `CHANGES.rst`
2. Update the version pin in `versions.cfg`
3. Commit with message `"Preparing release X.Y.Z"` ← *skipped by CI*
4. Create git tag `X.Y.Z`
5. Commit with message `"Back to development: X.Y.(Z+1)"` ← *skipped by CI*

The two automatic commits are intentionally excluded from the CI builds (see the `if:` condition in `dev.yml` and `staging.yml`) to avoid spurious deployments.

### Standard release vs quick release

```mermaid
flowchart LR
    A[make release\ncreates tag X.Y.Z] --> B[prod.yml triggers]
    B --> C{tag ends with -quick?}

    C -- No\ntag: 1.5.29 --> D["Rundeck schedules deploy\nnext day at 3:00 AM 🌙"]
    C -- Yes\ntag: 1.5.29-quick --> E["Rundeck deploys\nimmediately ⚡"]

    style D fill:#f5a623,color:#000
    style E fill:#7ed321,color:#000
```

**Standard release** (`make release` → tag `X.Y.Z`): production is updated overnight, during low-traffic hours.

**Quick release** (`make release` → tag `X.Y.Z-quick`): use this only for **urgent hotfixes** that cannot wait until the next morning. Production is deployed right away.

---

## dev.yml — Publish and deploy dev image

**Trigger:** push to the `dev` branch (tags excluded), or manual via `workflow_dispatch`.

**Skip condition:** the job is skipped if the commit message contains `"Preparing release"` or `"Back to development:"` — these are the two automatic commits created by `zest.releaser` during a release cycle.

**Jobs:**

```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Harbor
    participant Mattermost
    participant Rundeck

    GH->>Harbor: Build & push :dev and :dev-{run_number}
    Harbor-->>Mattermost: Notify build result
    GH->>Rundeck: Trigger deploy job (RUNDECK_DEPLOY_DEV_JOB_ID)
    Rundeck-->>Mattermost: Notify deploy result
```

| Step | Action used |
|------|-------------|
| Build & push image | `IMIO/gha/build-push-notify@v6` |
| Deploy via Rundeck | `IMIO/gha/rundeck-notify@v6` |

**Image tags produced:**
- `:dev`
- `:dev-{run_number}`

---

## staging.yml — Publish and deploy staging image

**Trigger:** push to the `main` branch (tags excluded). No `workflow_dispatch`.

**Skip condition:** same as `dev.yml` — zest.releaser commits are ignored.

**Jobs:**

```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Harbor
    participant Mattermost
    participant Rundeck

    GH->>Harbor: Build & push :staging and :staging-{run_number}
    Harbor-->>Mattermost: Notify build result
    GH->>Rundeck: Trigger deploy job (RUNDECK_DEPLOY_STAGING_JOB_ID)
    Rundeck-->>Mattermost: Notify deploy result
```

| Step | Action used |
|------|-------------|
| Build & push image | `IMIO/gha/build-push-notify@v6` |
| Deploy via Rundeck | `IMIO/gha/rundeck-notify@v6` |

**Image tags produced:**
- `:staging`
- `:staging-{run_number}`

---

## staging-plone62.yml — Publish and deploy plone62 staging image

**Trigger:** push to the `plone62` branch (tags excluded), or manual via `workflow_dispatch`.

**Skip condition:** same as `dev.yml` — zest.releaser commits are ignored.

Builds the Plone 6.2 image and deploys it to the Kubernetes staging: `IMIO/gha/k8s-update-tag` writes the commit's short SHA into `staging/common/values.yaml` of the ArgoCD repository, and ArgoCD rolls it out. Its tags never touch `:staging`, so `prod.yml` keeps promoting the `main` image. While this workflow exists, the `deploy-on-k8s` job of `staging.yml` is commented out; delete this workflow once `plone62` is merged into `main`.

| Step | Action used |
|------|-------------|
| Build & push image | `IMIO/gha/build-push-notify@v7` |
| Image and filesystem scans | `IMIO/gha/trivy-scan-notify@v7` |
| Update k8s staging tag | `IMIO/gha/k8s-update-tag@v5` |

**Image tags produced:**
- `:plone62`
- `:plone62-{run_number}`
- `:{short_sha}`

---

## tests.yml — Test the image

**Trigger:** pull request, or manual via `workflow_dispatch`. It does not gate `dev.yml` and `staging.yml` yet: on Plone 6.1.5, `collective.z3cform.datagridfield` 3.0.5 leaves a pending upgrade step on every fresh site, so `test_no_pending_upgrades` fails. Once Plone 6.2 (datagridfield 4.0.3) is merged, `build-push` will need this job, so a failing image never gets the `:dev` or `:staging` tag.

It calls the reusable workflow `IMIO/gha-workflows/.github/workflows/plone-image-test.yml`, which builds the image from `tests/docker-compose.test.yml`, boots it and runs the generic checks of `IMIO/gha/plone-image-test-notify` plus `tests/test_smartweb.py`. Locally: `make test`.

---

## prod.yml — Promote staging to production

**Trigger:** any git tag push, or manual via `workflow_dispatch`.

This workflow does **not** rebuild the image. It promotes the already-validated `:staging` image to production by re-tagging it. The heavy lifting is delegated to a shared reusable workflow:
`IMIO/gha-workflows/.github/workflows/promote-staging-to-production.yml@v1`

**Quick release flag:** if the tag ends with `-quick` (e.g. `1.5.29-quick`), `quick_release` is set to `true` and the deployment happens immediately. Otherwise, Rundeck schedules it for the next day at 3:00 AM.

---

## Secrets and variables reference

### Repository secrets

| Secret | Used by | Purpose |
|--------|---------|---------|
| `HARBOR_URL` | all | Harbor registry base URL |
| `SMARTWEB_HARBOR_USERNAME` | all | Harbor login |
| `SMARTWEB_HARBOR_PASSWORD` | all | Harbor password |
| `SMARTWEB_MATTERMOST_WEBHOOK_URL` | all | Mattermost notification webhook |
| `RUNDECK_URL` | all | Rundeck instance URL |
| `SMARTWEB_RUNDECK_TOKEN` | all | Rundeck API token |
| `RUNDECK_DEPLOY_DEV_JOB_ID` | dev.yml | Rundeck job ID for dev deployment |
| `RUNDECK_DEPLOY_STAGING_JOB_ID` | staging.yml, testharden.yml | Rundeck job ID for staging deployment |
| `SMARTWEB_ARGOCD_TOKEN_NAME` | staging-plone62.yml | ArgoCD repository token name |
| `SMARTWEB_ARGOCD_ACCESS_TOKEN` | staging-plone62.yml | ArgoCD repository access token |
| `SMARTWEB_ARGOCD_REPO_URL` | staging-plone62.yml | ArgoCD repository URL |

### Repository variables

| Variable | Used by | Purpose |
|----------|---------|---------|
| `IMAGE_NAME` | prod.yml | Docker image name (`web/smartweb/mutual`) |
| `IMAGE_TAG_STAGING` | prod.yml | Source tag to promote from staging |
| `IMAGE_TAG_PRODUCTION` | prod.yml | Target tag for production |
| `RUNDECK_JOB_ID` | prod.yml | Rundeck job ID for production deployment |
