"""Test show_list."""

from pyntc.devices import IOSDevice, NXOSDevice
from pyntc.errors import CommandError

from nornir_pyntc.tasks import pyntc_show_list


def test_pyntc_show_list_nxos(nornir_conn, monkeypatch):
    def mock_show_list(cls, commands):  # pylint:disable=unused-argument
        return ["version 1.1.1", "ip route fake"]

    monkeypatch.setattr(NXOSDevice, "show_list", mock_show_list)
    device = nornir_conn.filter(name="router1")
    result = device.run(pyntc_show_list, commands=["show version", "show ip route"])
    assert len(result["router1"]) == 1
    assert result["router1"].result == ["version 1.1.1", "ip route fake"]
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_show_list_ios(nornir_conn, monkeypatch):
    def mock_show_list(cls, commands):  # pylint:disable=unused-argument
        return ["version 1.1.1", "ip route fake"]

    monkeypatch.setattr(IOSDevice, "show_list", mock_show_list)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_show_list, commands=["show version", "show ip route"])
    assert len(result["router2"]) == 1
    assert result["router2"].result == ["version 1.1.1", "ip route fake"]
    assert result["router2"].failed is False
    assert result["router2"].changed is False


def test_pyntc_show_list_exception(nornir_conn, monkeypatch):
    def mock_show_list(cls, commands):  # pylint:disable=unused-argument
        raise CommandError(message="invalid command", command="show xversion")

    monkeypatch.setattr(IOSDevice, "show_list", mock_show_list)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_show_list, commands=["show xversion", "show ip interface brief"])
    assert len(result["router2"]) == 1
    assert isinstance(result["router2"].exception, CommandError)
    assert result["router2"].failed is True
    assert result["router2"].changed is False
