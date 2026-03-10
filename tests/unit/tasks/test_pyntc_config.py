from unittest.mock import MagicMock

from nornir_pyntc.tasks.pyntc_config import pyntc_config


class DummyHost:
    def __init__(self):
        self.name = "dummy_host"

    def get_connection(self, connection_name, config):
        return MagicMock(config=MagicMock())


class DummyTask:
    def __init__(self):
        self.host = DummyHost()
        self.nornir = MagicMock()
        self.nornir.config = MagicMock()


def test_pyntc_config_single_command():
    task = DummyTask()
    mock_connection = MagicMock()
    mock_connection.config.return_value = ["command output"]
    task.host.get_connection = MagicMock(return_value=mock_connection)

    commands = ["interface Gig1"]
    result = pyntc_config(task, commands)

    assert result.changed is True
    assert result.result == ["command output"]
    assert result.host == task.host


def test_pyntc_config_multiple_commands():
    task = DummyTask()
    mock_connection = MagicMock()
    mock_connection.config.return_value = ["output1", "output2"]
    task.host.get_connection = MagicMock(return_value=mock_connection)

    commands = ["interface Gig1", "shutdown"]
    result = pyntc_config(task, commands)

    assert result.changed is True
    assert result.result == ["output1", "output2"]
    assert result.host == task.host


def test_pyntc_config_empty_commands():
    task = DummyTask()
    mock_connection = MagicMock()
    mock_connection.config.return_value = []
    task.host.get_connection = MagicMock(return_value=mock_connection)

    commands = []
    result = pyntc_config(task, commands)

    assert result.changed is True
    assert result.result == []
    assert result.host == task.host
