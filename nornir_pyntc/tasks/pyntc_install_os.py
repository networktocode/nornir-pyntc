"""Installs the prescribed Network OS."""

from typing import Any

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_install_os(
    task: Task,
    image_name: str,
    # install_mode: bool = False,
    # install_mode_delay_factor: int = 20,
    **vendor_specifics: Any,
) -> Result:
    """Installs the prescribed Network OS, which must be present before issuing this command.

    Args:
        image_name (str): Name of the IOS image to boot into
        install_mode (bool, optional): Uses newer install method on devices. Defaults to False.

    Raises:
        OSInstallError: Unable to install OS Error type

    Returns:
        bool: False if no install is needed, true if the install completes successfully
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    # result = pyntc_connection.install_os(image_name, install_mode, install_mode_delay_factor, **vendor_specifics)
    result = pyntc_connection.install_os(image_name, **vendor_specifics)
    return Result(host=task.host, result=result)
