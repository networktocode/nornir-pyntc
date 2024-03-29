"""Initialize Connection and Tasks."""
from importlib import metadata
from nornir_pyntc.connections import CONNECTION_NAME, Pyntc
from nornir_pyntc.tasks import pyntc_config, pyntc_file_copy, pyntc_install_os, pyntc_reboot, pyntc_save, pyntc_show

__version__ = metadata.version(__name__)

__all__ = (
    "Pyntc",
    "CONNECTION_NAME",
    "pyntc_show",
    "pyntc_config",
    "pyntc_file_copy",
    "pyntc_install_os",
    "pyntc_reboot",
    "pyntc_save",
)
