"""Copy file to device."""

from typing import Any

from nornir.core.task import Result, Task
from nornir_pyntc.connections import CONNECTION_NAME


def pyntc_verify_file(
    task: Task,
    checksum: str,
    filename: str,
    hashing_algorithm: str = "md5",
    **kwargs: Any,
) -> Result:
    """Check if file exists on device and the checksum matches the provided value.

    Args:
        task (Task): Nornir Task object.
        checksum (str): Expected checksum of the file.
        filename (str): Name of the file.
        hashing_algorithm (str): Hashing algorithm to use for checksum verification (default: "md5").
        kwargs (Any): Additional keyword args.

    Returns:
        Result object with:
            * (bool): True if file exists and checksum matches, False otherwise.
    """
    pyntc_connection = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = pyntc_connection.verify_file(
        filename, checksum, hashing_algorithm, **kwargs
    )
    return Result(host=task.host, result=result, changed=False)
