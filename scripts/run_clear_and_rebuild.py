# -*- coding: utf-8 -*-

from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Testing import makerequest
from z3c.relationfield.event import updateRelations
from z3c.relationfield.interfaces import IHasRelations
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.component.hooks import setSite
from zope.globalrequest import setRequest

import logging

logger = logging.getLogger("clear_and_rebuild")


def get_site(zopeapp=None):
    zopeapp = makerequest.makerequest(app)  # noqa
    zopeapp.REQUEST["PARENTS"] = [app]  # noqa
    setRequest(zopeapp.REQUEST)
    # newSecurityManager(None, user)
    user = app.acl_users.getUser("admin")  # noqa
    newSecurityManager(None, user.__of__(app.acl_users))  # noqa
    portal = None
    for oid in app.objectIds():  # noqa
        obj = app[oid]  # noqa
        if IPloneSiteRoot.providedBy(obj):
            portal = obj
    if not portal:
        raise ("Do not find portal")
    setSite(portal)
    return portal


def reindex_relations(portal):
    """Clear the relation catalog to fix issues with interfaces that don't exist anymore."""
    rcatalog = getUtility(ICatalog)
    rcatalog.clear()
    catalog = portal.portal_catalog
    brains = catalog.searchResults(object_provides=IHasRelations.__identifier__)
    for brain in brains:
        try:
            obj = brain.getObject()
            logger.warn(f"reindex_relations : {obj.getPhysicalPath()}")
            updateRelations(obj, None)
        except:
            logger.warn(f"reindex_relations Exception: {obj.getPhysicalPath()}")


def clear_and_rebuild(portal):
    catalog = portal.portal_catalog
    catalog.clearFindAndRebuild()
    reindex_relations(portal)


if __name__ == "__main__":
    portal = get_site(app)  # noqa
    clear_and_rebuild(portal)
