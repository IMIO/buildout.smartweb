# buildout.smartweb

This repository contains the Buildout configuration for **SmartWeb**, a Plone 6-based website solution tailored for local authorities (pouvoirs locaux). It serves as the reference setup used to deploy and maintain Smartweb instances in a consistent and scalable way.

## Overview

Smartweb provides a flexible and robust content management platform built on Plone 6, designed specifically to meet the needs of Belgian Walloon local authorities.

This `buildout.smartweb` project includes everything required to install, configure, and run a complete Smartweb environment.

- **Demo site**: [https://demo-smartweb.imio.be/](https://demo-smartweb.imio.be/)
- **User documentation (French only)**: [https://docs.imio.be/iasmartweb/smartweb_v6/index.html](https://docs.imio.be/iasmartweb/smartweb_v6/index.html)


## Usage

### 1. Setup development environment

```bash
make
```

### 2. Launch instance

```bash
make start
```

## Goals

- Provide a repeatable, consistent deployment for Smartweb
- Maintain clear separation between core, extensions, and instance-specific configuration

## Contributing

Feel free to open issues or submit pull requests if you find bugs or want to improve the setup.


## Maintainers

- iMio