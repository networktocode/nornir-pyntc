"""Test show_list."""

from nornir_pyntc.tasks import pyntc_show_list
from pyntc.devices import IOSDevice, NXOSDevice


def test_pyntc_show_list_nxos(nr, monkeypatch):
    def mock_show_list(cls, commands):  # pylint:disable=unused-argument
        return ["version 1.1.1", "ip route fake"]

    monkeypatch.setattr(NXOSDevice, "show_list", mock_show_list)
    device = nr.filter(name="router1")
    result = device.run(pyntc_show_list, commands=["show version", "show ip route"])
    assert len(result["router1"]) == 1
    assert result["router1"].result == ["version 1.1.1", "ip route fake"]
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_show_list_ios(nr, monkeypatch):
    def mock_show_list(cls, commands):  # pylint:disable=unused-argument
        return ["version 1.1.1", "ip route fake"]

    monkeypatch.setattr(IOSDevice, "show_list", mock_show_list)
    device = nr.filter(name="router2")
    result = device.run(pyntc_show_list, commands=["show version", "show ip route"])
    assert len(result["router2"]) == 1
    assert result["router2"].result == ["version 1.1.1", "ip route fake"]
    assert result["router2"].failed is False
    assert result["router2"].changed is False
