"""Save a device's running configuration."""
from typing import Any

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_save(task: Task, **kwargs: Any) -> Result:
    """Save a device's running configuration.

    kwargs: Additional keyword args.

    Returns:
        Result object with:
            * bool: True if save is successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.save(**kwargs)
    if result:
        return Result(host=task.host, result=result, changed=True)
    return Result(host=task.host, result=result, changed=False)
