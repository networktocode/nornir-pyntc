"""Save a device's running configuration."""

from typing import Optional

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_save(task: Task, filename: Optional[str] = None) -> Result:
    """Save a device's running configuration.

    Args:
        filename (str): The filename on the remote device.
            If none is supplied, the implementing class should
            save to the "startup configuration".

    Returns:
        bool: True if save is successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.save(filename=filename)
    return Result(host=task.host, result=result)
