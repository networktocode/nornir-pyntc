"""Copy file to device."""
from typing import Any

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_file_copy(task: Task, src: str, **kwargs: Any) -> Result:
    """Copy file to device.

    Args:
        src (str): Source of file.
        kwargs (Any): Additional keyword args.

    Returns:
        Result object with:
            * (bool): True if save is successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.file_copy(src=src, **kwargs)
    if result:
        return Result(host=task.host, result=result, changed=True)
    return Result(host=task.host, result=result, changed=False)
