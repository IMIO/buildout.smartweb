# -*- coding: utf-8 -*-
"""
You can start this script with a "instance run" like :
    bin/instance -O Plone run scripts/migrate_to_keycloak.py

"""
from plone import api
from zope.component import queryMultiAdapter
from zope.globalrequest import getRequest

import argparse
import logging
import sys
import transaction


logger = logging.getLogger("migrate_to_keycloak.py")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s", "%Y-%m-%d %H:%M:%S"
)
ch.setFormatter(formatter)
logger.addHandler(ch)

parser = argparse.ArgumentParser(description="Run a script")
parser.add_argument("-c")  # use to bin/instance run script.py


def migrate():
    with api.env.adopt_user(username="admin"):
        portal = api.portal.get()
        view = queryMultiAdapter((portal, getRequest()), name="keycloak_migration")
        users = view.get_keycloak_users()
        view.migrate_plone_user_id_to_keycloak_user_id(api.user.get_users(), users)

        transaction.commit()
        logger.info(users)


if __name__ == "__main__":
    args = parser.parse_args()
    migrate()
