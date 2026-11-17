"""SmartWeb checks, run by `make test` after the generic image checks.

The fixtures (`site_url`, `admin`) come from the pytest plugin of
IMIO/gha plone-image-test-notify.
"""

import pytest
import uuid

TIMEOUT = 60
HTML = {"Accept": "text/html"}


def create(admin, container_url, portal_type, title, **fields):
    response = admin.post(
        container_url,
        json={"@type": portal_type, "title": title, **fields},
        timeout=TIMEOUT,
    )
    assert response.status_code == 201, response.text
    return response.json()["@id"]


@pytest.mark.parametrize(
    "portal_type",
    [
        "imio.smartweb.Folder",
        "imio.smartweb.Page",
        "imio.smartweb.PortalPage",
        "imio.smartweb.Procedure",
    ],
)
def test_create_and_render(admin, site_url, portal_type):
    url = create(admin, site_url, portal_type, f"Test {portal_type}")
    response = admin.get(url, headers=HTML, timeout=TIMEOUT)
    assert response.status_code == 200


def test_page_renders_its_sections(admin, site_url):
    page = create(admin, site_url, "imio.smartweb.Page", "Test page with a section")
    text = f"section-{uuid.uuid4().hex}"
    create(
        admin,
        page,
        "imio.smartweb.SectionText",
        "Test section",
        text={"data": f"<p>{text}</p>", "content-type": "text/html"},
    )
    response = admin.get(page, headers=HTML, timeout=TIMEOUT)
    assert response.status_code == 200
    assert text in response.text


def test_search_finds_new_content(admin, site_url):
    title = f"search-{uuid.uuid4().hex}"
    create(admin, site_url, "imio.smartweb.Page", title)
    response = admin.get(
        f"{site_url}/@search", params={"SearchableText": title}, timeout=TIMEOUT
    )
    response.raise_for_status()
    assert [item["title"] for item in response.json()["items"]] == [title]
