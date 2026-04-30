import logging
import sys
import transaction
from zope.annotation.interfaces import IAnnotations

logger = logging.getLogger("clean_jsons_annotations")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
logger.addHandler(handler)

SECTION_TYPES = [
    "imio.smartweb.SectionContact",
    "imio.smartweb.SectionEvents",
    "imio.smartweb.SectionNews",
    "imio.smartweb.SectionTimestampedPublications",
]

brains = app.Plone.portal_catalog(portal_type=SECTION_TYPES)
total_brains = len(brains)
cleaned = []

for i, brain in enumerate(brains, 1):
    obj = brain.getObject()
    ann = IAnnotations(obj)
    if "JSONS" in ann:
        entries = len(ann["JSONS"])
        size_kb = sum(len(str(item)) for item in ann["JSONS"]) // 1024
        del ann["JSONS"]
        cleaned.append((brain.getPath(), entries, size_kb))
        logger.info(f"[{i}/{total_brains}] REMOVED   {brain.getPath()} — {entries} entries, ~{size_kb} KB")
    else:
        logger.info(f"[{i}/{total_brains}] ok        {brain.getPath()}")

transaction.commit()

logger.info("=== Summary ===")
logger.info(f"Sections scanned       : {total_brains}")
logger.info(f"Annotations removed    : {len(cleaned)}")
logger.info(f"Total space freed      : ~{sum(s for _, _, s in cleaned)} KB")
for path, entries, size_kb in cleaned:
    logger.info(f"  {path} ({entries} entries, ~{size_kb} KB)")
