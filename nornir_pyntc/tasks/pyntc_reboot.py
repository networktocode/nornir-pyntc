"""Reboot device."""
from nornir.core.task import Result, Task
from requests.exceptions import (  # pylint: disable=redefined-builtin
    ConnectionError,
    ReadTimeout,
)
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_reboot(task: Task, timer: int = 0) -> Result:
    """Reboot device. Reload the controller or controller pair.

    Args:
        timer (int): The time to wait before reloading.

    Raises:
        ReloadTimeoutError: When the device is still unreachable after the timeout period.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    try:
        result = pyntc_connection.reboot(timer=timer)
        return Result(host=task.host, result=result)
    except (ConnectionError, ReadTimeout):
        return Result(host=task.host, result="Connection Closed. Reboot In Progress.", failed=False)
    except Exception as err:  # pylint: disable=broad-except
        return Result(host=task.host, result=err, failed=True)
