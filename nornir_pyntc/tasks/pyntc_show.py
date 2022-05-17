"""Send a non-configuration command."""
from typing import Any

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_show(task: Task, command: str, **kwargs: Any) -> Result:
    """Send a non-configuration command.

    Args:
        command (str): The command to send to the device.
        kwargs (Any): Additional keyword args to send.

    Returns:
        Result object with:
            * (str) - The output of the show command, which could be raw text or structured data.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.show(command, **kwargs)
    return Result(host=task.host, result=result, changed=False)
