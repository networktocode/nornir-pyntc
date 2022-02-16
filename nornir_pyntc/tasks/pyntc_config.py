"""Send configuration command or commands."""

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_config(task: Task, commands: list) -> Result:
    """Send a configuration command or commands. config_list is being DEPRECATED in pyntc config can take str or list.

    Args:
        command (list): The commands to send to the device.

    Returns:
        list: When ``command`` is a list, the config session input and output from sending ``command``.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.config(command=commands)
    return Result(host=task.host, result=result)
