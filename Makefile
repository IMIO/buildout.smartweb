#!/usr/bin/make
all: buildout

BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
#BRANCH := $(shell git for-each-ref --format='%(objectname) %(refname:short)' refs/heads | awk "/^$$(git rev-parse HEAD)/ {print \$$2}")

buildout.cfg:
	ln -fs dev.cfg buildout.cfg

bin/buildout: bin/pip buildout.cfg
	bin/pip install -I -r requirements.txt

buildout: bin/instance

bin/instance: bin/buildout
	bin/buildout

bin/pip:
	python3 -m venv .

run: bin/instance
	bin/instance fg

cleanall:
	rm -fr develop-eggs downloads eggs parts .installed.cfg lib lib64 include bin .mr.developer.cfg local/

upgrade-steps:
	bin/instance -O plone run scripts/run_portal_upgrades.py

docker-image:
	docker build --pull --no-cache -t smartweb/mutual:$(BRANCH)  .

lint:
	pre-commit run --all

test-image: bin/pip
	bin/pip install -r tests/requirements.txt
	bin/pytest -s tests

.PHONY: solr
solr:
	docker-compose -f docker-compose-solr.yml up
