from unittest.mock import MagicMock

import pytest
from nornir.core.task import Result, Task

from nornir_pyntc.tasks.pyntc_check_file_exists import pyntc_check_file_exists


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


def test_file_exists_returns_true(mock_task):
    mock_connection = MagicMock()
    mock_connection.check_file_exists.return_value = True
    mock_task.host.get_connection.return_value = mock_connection

    result = pyntc_check_file_exists(mock_task, "test.txt")
    assert isinstance(result, Result)
    assert result.result is True
    assert result.changed is False
    mock_connection.check_file_exists.assert_called_once_with("test.txt")


def test_file_exists_returns_false(mock_task):
    mock_connection = MagicMock()
    mock_connection.check_file_exists.return_value = False
    mock_task.host.get_connection.return_value = mock_connection

    result = pyntc_check_file_exists(mock_task, "missing.txt")
    assert isinstance(result, Result)
    assert result.result is False
    assert result.changed is False
    mock_connection.check_file_exists.assert_called_once_with("missing.txt")


def test_file_exists_with_kwargs(mock_task):
    mock_connection = MagicMock()
    mock_connection.check_file_exists.return_value = True
    mock_task.host.get_connection.return_value = mock_connection

    result = pyntc_check_file_exists(mock_task, "file.txt", foo="bar")
    assert result.result is True
    mock_connection.check_file_exists.assert_called_once_with("file.txt", foo="bar")
