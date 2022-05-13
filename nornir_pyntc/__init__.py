"""Initialize Connection and Tasks."""

__version__ = "1.0.0"

from nornir_pyntc.connections import CONNECTION_NAME, Pyntc
from nornir_pyntc.tasks import (
    pyntc_config,
    pyntc_file_copy,
    pyntc_install_os,
    pyntc_reboot,
    pyntc_save,
    pyntc_show,
    pyntc_show_list,
)

__all__ = (
    "Pyntc",
    "CONNECTION_NAME",
    "pyntc_show",
    "pyntc_show_list",
    "pyntc_config",
    "pyntc_file_copy",
    "pyntc_install_os",
    "pyntc_reboot",
    "pyntc_save",
)
