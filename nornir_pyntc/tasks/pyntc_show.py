"""Send a non-configuration command."""

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_show(task: Task, command: str, raw_text: bool = False) -> Result:
    """Send a non-configuration command.

    Args:
        command (str): The command to send to the device.

    Returns:
        The output of the show command, which could be raw text or structured data.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.show(command, raw_text=raw_text)
    return Result(host=task.host, result=result)
