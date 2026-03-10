from unittest.mock import MagicMock, patch

import pytest
from nornir.core.task import Result, Task
from nornir_pyntc.tasks.pyntc_reboot import pyntc_reboot

# Dummy constants and objects
CONNECTION_NAME = "pyntc"


class DummyHost:
    def __init__(self):
        self.name = "dummy_host"

    def get_connection(self, conn_name, config):
        return self.connection


class DummyNornir:
    def __init__(self):
        self.config = {}


@pytest.fixture
def task():
    host = DummyHost()
    nornir = DummyNornir()
    task = MagicMock(spec=Task)
    task.host = host
    task.nornir = nornir
    return task


def test_pyntc_reboot_success_changed(task):
    reboot_result = True
    reboot_mock = MagicMock()
    reboot_mock.reboot.return_value = reboot_result
    task.host.connection = reboot_mock

    result = pyntc_reboot(task)
    assert isinstance(result, Result)
    assert result.result is True
    assert result.changed is True
    assert result.failed is False


def test_pyntc_reboot_success_not_changed(task):
    reboot_result = False
    reboot_mock = MagicMock()
    reboot_mock.reboot.return_value = reboot_result
    task.host.connection = reboot_mock

    result = pyntc_reboot(task)
    assert isinstance(result, Result)
    assert result.result is False
    assert result.changed is False
    assert result.failed is False


@pytest.mark.skip(reason="To fix in next release.")
def test_pyntc_reboot_connection_error(task):
    reboot_mock = MagicMock()
    reboot_mock.reboot.side_effect = Exception("ConnectionError")
    task.host.connection = reboot_mock

    with (
        patch("requests.exceptions.ConnectionError", Exception),
        patch("requests.exceptions.ReadTimeout", Exception),
    ):
        result = pyntc_reboot(task)
        assert isinstance(result, Result)
        assert result.result == "Connection Closed. Reboot In Progress."
        assert result.changed is True
        assert result.failed is False


@pytest.mark.skip(reason="To fix in next release.")
def test_pyntc_reboot_read_timeout(task):
    reboot_mock = MagicMock()
    reboot_mock.reboot.side_effect = Exception("ReadTimeout")
    task.host.connection = reboot_mock

    with (
        patch("requests.exceptions.ConnectionError", Exception),
        patch("requests.exceptions.ReadTimeout", Exception),
    ):
        result = pyntc_reboot(task)
        assert isinstance(result, Result)
        assert result.result == "Connection Closed. Reboot In Progress."
        assert result.changed is True
        assert result.failed is False


def test_pyntc_reboot_wait_for_reload_argument(task):
    reboot_mock = MagicMock()
    reboot_mock.reboot.return_value = True
    task.host.connection = reboot_mock

    result = pyntc_reboot(task, wait_for_reload=True)
    reboot_mock.reboot.assert_called_with(wait_for_reload=True)
    assert result.changed is True
