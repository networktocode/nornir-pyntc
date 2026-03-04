"""Copy file to device, using the device's copy command."""

from typing import Any

from nornir.core.task import Result, Task
from pyntc.utils.models import FileCopyModel
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_remote_file_copy(task: Task, src: FileCopyModel, **kwargs: Any) -> Result:
    """Execute the file copy command on a remote device using the device's native copy command.

    Args:
        src (FileCopyModel): Source of file.
        kwargs (Any): Additional keyword args.

    Returns:
        Result object with:
            * (bool): True if save is successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.remote_file_copy(src=src, **kwargs)
    if result:
        return Result(host=task.host, result=result, changed=True)
    return Result(host=task.host, result=result, changed=False)
