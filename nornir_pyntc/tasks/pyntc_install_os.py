"""Installs the prescribed Network OS."""

from typing import Any

from nornir.core.task import Result, Task
from requests.exceptions import (  # pylint: disable=redefined-builtin
    ConnectionError,
    ReadTimeout,
)
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_install_os(
    task: Task,
    image_name: str,
    **kwargs: Any,
) -> Result:
    """Installs the prescribed Network OS, which must be present before issuing this command.

    Args:
        image_name (str): Name of the IOS image to boot into
        kwargs (Any): Additional keyword args.

    Raises:
        OSInstallError: Unable to install OS Error type

    Returns:
        bool: False if no install is needed, true if the install completes successfully
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    try:
        result = pyntc_connection.install_os(image_name, **kwargs)
        return Result(host=task.host, result=result)
    except (ConnectionError, ReadTimeout):
        return Result(host=task.host, result="Connection Closed. Install In Progress.", failed=False)
    except Exception as err:  # pylint: disable=broad-except
        return Result(host=task.host, result=err, failed=True)
