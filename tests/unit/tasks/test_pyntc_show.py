from unittest.mock import MagicMock

import pytest
from nornir.core.task import Result, Task

from nornir_pyntc.connections import CONNECTION_NAME
from nornir_pyntc.tasks.pyntc_show import pyntc_show


@pytest.fixture
def mock_task():
    mock_host = MagicMock()
    mock_nornir = MagicMock()
    mock_config = MagicMock()
    mock_task = MagicMock(spec=Task)
    mock_task.host = mock_host
    mock_task.nornir = mock_nornir
    mock_task.nornir.config = mock_config
    return mock_task


def test_pyntc_show_with_string_command(mock_task):
    mock_connection = MagicMock()
    mock_connection.show.return_value = "show version output"
    mock_task.host.get_connection.return_value = mock_connection

    command = "show version"
    result = pyntc_show(mock_task, command)

    mock_task.host.get_connection.assert_called_once_with(CONNECTION_NAME, mock_task.nornir.config)
    mock_connection.show.assert_called_once_with(command)
    assert isinstance(result, Result)
    assert result.result == "show version output"
    assert result.changed is False


def test_pyntc_show_with_list_command(mock_task):
    mock_connection = MagicMock()
    mock_connection.show.return_value = ["output1", "output2"]
    mock_task.host.get_connection.return_value = mock_connection

    command = ["show version", "show interfaces"]
    result = pyntc_show(mock_task, command)

    mock_task.host.get_connection.assert_called_once_with(CONNECTION_NAME, mock_task.nornir.config)
    mock_connection.show.assert_called_once_with(command)
    assert isinstance(result, Result)
    assert result.result == ["output1", "output2"]
    assert result.changed is False


def test_pyntc_show_with_kwargs(mock_task):
    mock_connection = MagicMock()
    mock_connection.show.return_value = "filtered output"
    mock_task.host.get_connection.return_value = mock_connection

    command = "show running-config"
    kwargs = {"filter": "hostname"}
    result = pyntc_show(mock_task, command, **kwargs)

    mock_connection.show.assert_called_once_with(command, **kwargs)
    assert result.result == "filtered output"
    assert result.changed is False
