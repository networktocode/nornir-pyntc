"""Test show."""

from nornir_pyntc.tasks import pyntc_show


def test_pyntc_show_nxos(nornir, monkeypatch):
    from pyntc.devices import NXOSDevice

    def mock_show(cls, command):
        return "version 1.1.1"

    monkeypatch.setattr(NXOSDevice, "show", mock_show)
    device = nornir.filter(name="router1")
    result = device.run(pyntc_show, command="show version")
    assert len(result["router1"]) == 1
    assert result["router1"].result == "version 1.1.1"
    assert result["router1"].failed == False
    assert result["router1"].changed == False


def test_pyntc_show_ios(nornir, monkeypatch):
    from pyntc.devices import IOSDevice

    def mock_show(cls, command):
        return "version 1.1.1"

    monkeypatch.setattr(IOSDevice, "show", mock_show)
    device = nornir.filter(name="router2")
    result = device.run(pyntc_show, command="show version")
    assert len(result["router2"]) == 1
    assert result["router2"].result == "version 1.1.1"
    assert result["router2"].failed == False
    assert result["router2"].changed == False
