# -*- coding: utf-8 -*-
from compose.cli.main import project_from_options
from compose.cli.main import TopLevelCommand
from docker import APIClient
from docker.models.containers import Container
from os import path
from pytest import FixtureRequest

import docker
import pytest
import requests
import time

options = {
    "--no-deps": False,
    "--always-recreate-deps": False,
    "--abort-on-container-exit": False,
    "SERVICE": "",
    "--remove-orphans": True,
    "--detach": True,
    "--no-recreate": False,
    "--force-recreate": True,
    "--build": True,
    "--no-build": False,
    "--no-color": False,
    "--rmi": "all",
    "--volumes": "",
    "--follow": False,
    "--timestamps": False,
    "--tail": "all",
    "--scale": "",
    # "-p": "../",
}


def get_health(container: Container):
    api_client = APIClient()
    inspect_results = api_client.inspect_container(container.name)
    return inspect_results["State"]["Health"]["Status"]


@pytest.fixture(scope="session")
def docker_compose(request: FixtureRequest):
    project = project_from_options(path.dirname(__file__), options)
    cmd = TopLevelCommand(project)
    cmd.up(options)

    def finalize():
        cmd.down(
            {
                "--rmi": "local",
                "--volumes": True,
                "--remove-orphans": True,
            }
        )

    request.addfinalizer(finalize)


def test_start_instance(docker_compose):
    project = project_from_options(path.dirname(__file__), options)
    cmd = TopLevelCommand(project)
    instance = [serv for serv in cmd.project.services if serv.name == "instance"][0]
    container_name = f"{instance.project}_{instance.name}_1"
    client = docker.from_env()
    container = client.containers.get(container_name)
    is_plone_ready = False
    timeout = time.time() + 30
    while not is_plone_ready:
        time.sleep(1)
        if container not in client.containers.list():
            print("Instance container is down, it must restart")
            break
        bytes_logs = container.logs()
        logs = bytes_logs.decode(encoding="utf-8", errors="strict")
        # print(logs)
        if "Listening at: http://0.0.0.0:8080" in logs:
            is_plone_ready = True
            print("Instance started !")
            continue
        if time.time() > timeout:
            print("Timeout")
            break
    assert is_plone_ready


def test_policy_installed(docker_compose):
    project = project_from_options(path.dirname(__file__), options)
    cmd = TopLevelCommand(project)
    instance = [serv for serv in cmd.project.services if serv.name == "instance"][0]
    container_name = f"{instance.project}_{instance.name}_1"
    client = docker.from_env()
    container = client.containers.get(container_name)
    while get_health(container) != "healthy":
        # print(f"health: {get_health(container)}")
        time.sleep(1)
    # print("Container is healthy")
    # installed_package_id = "plone.restapi"
    installed_package_id = "imio.smartweb.policy"
    package_info = requests.get(
        f"http://portal.localhost/@addons/{installed_package_id}",
        headers={"Accept": "application/json"},
        auth=("admin", "admin"),
    ).json()
    assert package_info.get(
        "is_installed"
    ), f"package {installed_package_id} is not installed"
