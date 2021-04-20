#!/usr/bin/make
all: buildout

IMAGE_NAME="docker-staging.imio.be/smartweb/mutual:latest"

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

eggs:  ## Copy eggs from docker image to speed up docker build
	-docker run --entrypoint='' $(IMAGE_NAME) tar -c -C /plone eggs | tar x
	mkdir -p eggs

docker-image: eggs  ## Build docker image
	mkdir -p eggs
	docker build --pull -t smartweb/mutual:latest .

lint:
	pre-commit run --all
