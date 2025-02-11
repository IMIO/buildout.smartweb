#!/usr/bin/make

all: buildout

BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

buildout.cfg:
	ln -fs dev.cfg buildout.cfg

bin/buildout: bin/pip buildout.cfg
	bin/uv pip install -r requirements.txt

buildout: bin/instance

bin/instance: bin/buildout
	bin/buildout

bin/pip:
	python3.12 -m venv .
	bin/pip install uv

run: bin/instance
	bin/instance fg

.PHONY: help				# List parts phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: start				# Start the instance
start: solr-background
	bin/instance fg

.PHONY: cleanall				# Clean development environment
cleanall:
	rm -fr develop-eggs downloads eggs parts .installed.cfg lib lib64 include bin .mr.developer.cfg local/

.PHONY: upgrade-steps			# Run upgrade steps
upgrade-steps:
	bin/instance -O Plone run scripts/run_portal_upgrades.py

.PHONY: docker-image			# Build docker image
docker-image:
	docker build --pull --no-cache -t smartweb/mutual:$(BRANCH)  .

lint:
	pre-commit run --all

test-image: bin/pip
	echo test
	#./bin/pip install pip==21.3.1
	#docker-compose up --no-start postgres # create network
	#docker-compose run --rm -u root solr chmod 777 -R /var/solr/data/plone
	#make local-test-image

local-test-image:
	python3.12 -m venv .
	./bin/pip install -r tests/requirements.txt
	./bin/pytest -s tests

docker-test-image:
	docker build -f Dockerfile.test -t smartweb-test:latest .
	docker run  -v /var/run/docker.sock:/var/run/docker.sock smartweb-test

.PHONY: solr 				# Start solr container (foreground)
solr:
	sudo chmod -R 777 solr
	docker compose up solr

.PHONY: solr-background			# Start solr container (background)
solr-background:
	sudo chmod -R 777 solr
	docker compose up solr -d

.PHONY: solr-cluster			# Start solr cluster
solr-cluster:
	docker compose -f docker-compose-solr-cluster.yml up
