from unittest.mock import MagicMock

import pytest

from nornir_pyntc.tasks.pyntc_file_copy import pyntc_file_copy


class DummyHost:
    def __init__(self):
        self.name = "dummy_host"

    def get_connection(self, connection_name, config):
        return self.connection


class DummyTask:
    def __init__(self, result_value):
        self.host = DummyHost()
        self.nornir = MagicMock()
        self.host.connection = MagicMock()
        self.host.connection.file_copy = MagicMock(return_value=result_value)


@pytest.mark.parametrize(
    "result_value,expected_changed",
    [
        (True, True),
        (False, False),
        (None, False),
    ],
)
def test_pyntc_file_copy_result(result_value, expected_changed):
    task = DummyTask(result_value)
    res = pyntc_file_copy(task, src="testfile.txt")
    assert res.result == result_value
    assert res.changed == expected_changed
    assert res.host.name == "dummy_host"


def test_pyntc_file_copy_passes_kwargs():
    task = DummyTask(True)
    pyntc_file_copy(task, src="testfile.txt", foo="bar")
    task.host.connection.file_copy.assert_called_with(src="testfile.txt", foo="bar")
