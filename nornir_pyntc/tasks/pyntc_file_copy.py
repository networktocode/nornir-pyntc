"""Copy file to device."""

from typing import Optional

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_file_copy(task: Task, src: str, dest: Optional[str] = None, file_system: Optional[str] = None, **kwargs) -> Result:
    """Copy file to device.

    Args:
        src (str): Source of file.
        dest (str, optional): Destination name for file. Defaults to None.
        file_system (str, optional): File system to copy file to. Defaults to None.

    Returns:
        bool: True if save is successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.file_copy(src=src, dest=dest, file_system=file_system, **kwargs)
    return Result(host=task.host, result=result)
