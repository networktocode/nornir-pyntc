from unittest.mock import MagicMock

import pytest
from nornir.core.task import Result, Task

from nornir_pyntc.tasks.pyntc_save import pyntc_save


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


def test_pyntc_save_success(mock_task):
    mock_connection = MagicMock()
    mock_connection.save.return_value = True
    mock_task.host.get_connection.return_value = mock_connection

    result = pyntc_save(mock_task)
    assert isinstance(result, Result)
    assert result.result is True
    assert result.changed is True


def test_pyntc_save_failure(mock_task):
    mock_connection = MagicMock()
    mock_connection.save.return_value = False
    mock_task.host.get_connection.return_value = mock_connection

    result = pyntc_save(mock_task)
    assert isinstance(result, Result)
    assert result.result is False
    assert result.changed is False


def test_pyntc_save_with_kwargs(mock_task):
    mock_connection = MagicMock()
    mock_connection.save.return_value = "saved"
    mock_task.host.get_connection.return_value = mock_connection

    result = pyntc_save(mock_task, foo="bar")
    mock_connection.save.assert_called_with(foo="bar")
    assert result.result == "saved"
    assert result.changed is True
