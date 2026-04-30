from zope.annotation.interfaces import IAnnotations
import transaction

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
        print(f"[{i}/{total_brains}] REMOVED   {brain.getPath()} — {entries} entries, ~{size_kb} KB")
    else:
        print(f"[{i}/{total_brains}] ok        {brain.getPath()}")

transaction.commit()

print("\n=== Summary ===")
print(f"Sections scanned       : {total_brains}")
print(f"Annotations removed    : {len(cleaned)}")
print(f"Total space freed      : ~{sum(s for _, _, s in cleaned)} KB")
if cleaned:
    print("\nDetails:")
    for path, entries, size_kb in cleaned:
        print(f"  {path} ({entries} entries, ~{size_kb} KB)")
