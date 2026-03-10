from unittest.mock import MagicMock

from nornir.core.task import Result
from requests.exceptions import ConnectionError, ReadTimeout

from nornir_pyntc.tasks.pyntc_install_os import pyntc_install_os


class DummyHost:
    def __init__(self):
        self.name = "dummy"

    def get_connection(self, conn_name, config):
        return self.connection


class DummyTask:
    def __init__(self, connection):
        self.host = DummyHost()
        self.host.connection = connection
        self.nornir = MagicMock()
        self.nornir.config = MagicMock()


def test_install_os_successful_install():
    connection = MagicMock()
    connection.install_os.return_value = True
    task = DummyTask(connection)
    result = pyntc_install_os(task, "test-image")
    assert isinstance(result, Result)
    assert result.changed is True
    assert result.failed is False
    assert result.result is True


def test_install_os_no_install_needed():
    connection = MagicMock()
    connection.install_os.return_value = False
    task = DummyTask(connection)
    result = pyntc_install_os(task, "test-image")
    assert isinstance(result, Result)
    assert result.changed is False
    assert result.failed is False
    assert result.result is False


def test_install_os_connection_error():
    connection = MagicMock()
    connection.install_os.side_effect = ConnectionError()
    task = DummyTask(connection)
    result = pyntc_install_os(task, "test-image")
    assert isinstance(result, Result)
    assert result.changed is True
    assert result.failed is False
    assert result.result == "Connection Closed. Install In Progress."


def test_install_os_read_timeout():
    connection = MagicMock()
    connection.install_os.side_effect = ReadTimeout()
    task = DummyTask(connection)
    result = pyntc_install_os(task, "test-image")
    assert isinstance(result, Result)
    assert result.changed is True
    assert result.failed is False
    assert result.result == "Connection Closed. Install In Progress."
