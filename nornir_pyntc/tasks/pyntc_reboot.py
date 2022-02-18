"""Reboot device."""

# TODO: Fix currently fails with "ValueError: signal only works in main thread of the main interpreter'".  Signal is used by reboot method.

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_reboot(task: Task, timer: int = 0) -> Result:
    """Reboot device. Reload the controller or controller pair.

    Args:
        timer (int): The time to wait before reloading.

    Raises:
        ReloadTimeoutError: When the device is still unreachable after the timeout period.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.reboot(timer=timer)
    return Result(host=task.host, result=result)