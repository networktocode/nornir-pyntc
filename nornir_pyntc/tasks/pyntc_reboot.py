"""Reboot device."""
from requests.exceptions import ConnectionError, ReadTimeout  # pylint: disable=redefined-builtin

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_reboot(task: Task, wait_for_reload: bool = False) -> Result:
    """Reboot device. Reload the controller or controller pair.

    Args:
        wait_for_reload (bool): Whether pyntc should wait for device to come back online before returning.

    Returns:
        Result object with:
            * (bool) - True if successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    try:
        result = pyntc_connection.reboot(wait_for_reload=wait_for_reload)
        if result:
            return Result(host=task.host, result=result, changed=True, failed=False)
        return Result(host=task.host, result=result, changed=False, failed=False)
    except (ConnectionError, ReadTimeout):
        return Result(host=task.host, result="Connection Closed. Reboot In Progress.", changed=True, failed=False)
