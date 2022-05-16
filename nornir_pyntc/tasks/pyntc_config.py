"""Send configuration commands."""
from typing import List

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_config(task: Task, commands: List[str]) -> Result:
    """Send configuration command or commands.

    Args:
        command (list): The commands to send to the device.

    Returns:
        Result object with:
            * (list) the config session input and output from sending ``commands``.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.config(command=commands)
    return Result(host=task.host, result=result, changed=True)
