"""Testing Fixtures Setup."""

import os

import pytest
from nornir import InitNornir
from nornir.core.state import GlobalState

global_data = GlobalState(dry_run=True)


@pytest.fixture(scope="session", autouse=True)
def nr(request):  # pylint:disable=unused-argument
    """Initializes nornir."""
    dir_path = os.path.dirname(os.path.realpath(__file__))

    nornir = InitNornir(
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": f"{dir_path}/inventory_data/hosts.yaml",
            },
        },
        dry_run=True,
    )
    nornir.data = global_data
    return nornir


@pytest.fixture(scope="function", autouse=True)
def reset_data():
    """Reset Data."""
    global_data.dry_run = True
    global_data.reset_failed_hosts()
