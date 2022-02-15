from typing import Any, Dict, Optional

from nornir.core.configuration import Config

from pyntc import ntc_device

CONNECTION_NAME = "pyntc"

napalm_to_pyntc_map = {
    "ios": "cisco_ios_ssh",
    "nxos": "cisco_nxos_nxapi",
    "eos": "arista_eos_eapi",
    "junos": "juniper_junos_netconf",
    "iosxr": "cisco_xr",
}

class Pyntc:
    """
    This plugin connects to the device using the Pyntc driver and sets the
    relevant connection.
    Inventory:
        extras: maps to argument passed to ``ntc_device``.
    """

    def open(
        self,
        hostname: Optional[str],
        username: Optional[str],
        password: Optional[str],
        port: Optional[int],
        platform: Optional[str],
        extras: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,
    ) -> None:
        parameters = {
            "host": hostname,
            "username": username,
            "password": password,
            "port": port,
        }

        if platform is not None:
            platform = napalm_to_pyntc_map.get(platform, platform)
            parameters["device_type"] = platform

        extras = extras or {}
        parameters.update(extras)
        connection = ntc_device(platform, **parameters)
        self.connection = connection

    def close(self) -> None:
        self.connection.close()
