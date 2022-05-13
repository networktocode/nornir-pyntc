"""Test Connection."""

from pyntc.devices import IOSDevice


def test_connection_core_setup(nr, monkeypatch):
    """Test simple connection."""

    def mock_open(cls, confirm_active=False):  # pylint:disable=unused-argument
        pass

    monkeypatch.setattr(IOSDevice, "open", mock_open)
    nxos_conn = nr.inventory.hosts["router1"].get_connection("pyntc", nr.config)
    assert nxos_conn.host == "192.168.1.1"
    assert nxos_conn.transport == "http"
    assert nxos_conn.username == "ntc"
    assert nxos_conn.password == "ntc123"
    ios_conn = nr.inventory.hosts["router2"].get_connection("pyntc", nr.config)
    assert ios_conn.host == "192.168.1.2"
    assert ios_conn.port == 22
    assert ios_conn.username == "ntc"
    assert ios_conn.password == "ntc123"
