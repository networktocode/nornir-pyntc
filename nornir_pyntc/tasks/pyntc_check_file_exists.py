"""Copy file to device."""

from typing import Any

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_check_file_exists(task: Task, filename: str, **kwargs: Any) -> Result:
    """Check if file exists on device.

    Args:
        task (Task): Nornir Task object.
        filename (str): Name of the file.
        kwargs (Any): Additional keyword args.

    Returns:
        Result object with:
            * (bool): True if file exists, False otherwise.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.check_file_exists(filename, **kwargs)
    return Result(host=task.host, result=result, changed=False)
