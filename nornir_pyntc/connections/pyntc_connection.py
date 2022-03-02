"""Pyntc Device Connection."""

from typing import Any, Dict, Optional

from nornir.core.configuration import Config
from pyntc import ntc_device

CONNECTION_NAME = "pyntc"

platform_to_pyntc_map = {
    "cisco_ios": "cisco_ios_ssh",
    "cisco_nxos": "cisco_nxos_nxapi",
    "arista_eos": "arista_eos_eapi",
    "juniper_junos": "juniper_junos_netconf",
    "cisco_iosxr": "cisco_xr",
}


class Pyntc:
    """This plugin connects to the device using the Pyntc driver and sets the relevant connection.

    Inventory:
        extras: maps to argument passed to ``ntc_device``.
    """

    def open(  # pylint: disable=too-many-arguments
        self,
        hostname: Optional[str],
        username: Optional[str],
        password: Optional[str],
        port: Optional[int],
        platform: Optional[str],
        extras: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,  # pylint: disable=unused-argument
    ) -> None:
        """Opens a Connection with Pyntc.

        Args:
            hostname (Optional[str]): hostname or IP.
            username (Optional[str]): username to connect to the device.
            password (Optional[str]): password to connect to the device.
            port (Optional[int]): port to connect to.
            platform (Optional[str]): platform | device type.
            extras (Optional[Dict[str, Any]], optional): Extras for inventory item. Defaults to None.
            configuration (Optional[Config], optional): Additional configuration items. Defaults to None.
        """
        parameters = {
            "host": hostname,
            "username": username,
            "password": password,
            "port": port,
        }
        if platform is not None:
            platform = platform_to_pyntc_map.get(platform, platform)
            parameters["device_type"] = platform
        extras = extras or {}
        parameters.update(extras)
        if not parameters["port"]:
            parameters["port"] = 22
        #conn_args = {**parameters, **kwargs}
        connection = ntc_device(**parameters)
        self.connection = connection  # pylint: disable=attribute-defined-outside-init

    def close(self) -> None:
        """Close the Pyntc connection."""
        self.connection.close()
