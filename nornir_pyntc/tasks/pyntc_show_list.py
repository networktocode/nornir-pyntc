"""Send non-configuration commands."""
from typing import Any, List

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_show_list(task: Task, commands: List[str], **kwargs: Any) -> Result:
    """Send non-configuration commands.

    Args:
        commands (list): The command to send to the device.
        kwargs (Any): Additional keyword args to send.

    Returns:
        Result object with:
            * (list) - The output of the show commands, which could be raw text or structured data.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.show_list(commands=commands, **kwargs)
    return Result(host=task.host, result=result, changed=False)
