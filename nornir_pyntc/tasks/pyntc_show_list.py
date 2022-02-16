"""Send non-configuration commands."""

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_show_list(task: Task, commands: str, raw_text: bool = False) -> Result:
    """Send non-configuration commands.

    Args:
        commands (str): The command to send to the device.

    Returns:
        The output of the show commands, which could be raw text or structured data.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.show_list(commands, raw_text=raw_text)
    return Result(host=task.host, result=result)
