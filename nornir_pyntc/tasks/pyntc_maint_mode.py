"""Enter or exit device maintenance mode."""

from typing import Any

from nornir.core.task import Result, Task

from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_maint_mode(task: Task, **kwargs: Any) -> Result:
    """Enter or exit device maintenance mode.

    Args:
        task (Task): Nornir Task object.
        kwargs (Any): Additional keyword args, including optional vars.

    Returns:
        Result object with:
            (bool): True if state transition is successful.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.maint_mode(**kwargs)
    return Result(host=task.host, result=result, changed=True)
