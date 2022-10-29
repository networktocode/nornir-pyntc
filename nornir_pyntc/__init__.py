"""Initialize Connection and Tasks."""

try:
    from importlib import metadata  # type: ignore[attr-defined]
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata  # type: ignore[no-redef]

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

__version__ = metadata.version(__name__)

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
