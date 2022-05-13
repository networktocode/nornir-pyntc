"""Test reboot."""

from nornir_pyntc.tasks import pyntc_config


def test_pyntc_config_nxos(nornir, monkeypatch):
    from pyntc.devices import NXOSDevice

    def mock_config(cls, command):
        return "hostname router1"

    monkeypatch.setattr(NXOSDevice, "config", mock_config)
    device = nornir.filter(name="router1")
    result = device.run(pyntc_config, commands="hostname router1")
    assert len(result["router1"]) == 1
    assert result["router1"].result == "hostname router1"
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_config_ios(nornir, monkeypatch):
    from pyntc.devices import IOSDevice

    def mock_config(cls, command):
        return ["hostname router2", "ntp server 1.1.1.1"]

    monkeypatch.setattr(IOSDevice, "config", mock_config)
    device = nornir.filter(name="router2")
    result = device.run(pyntc_config, commands=["hostname router2", "ntp server 1.1.1.1"])
    assert len(result["router2"]) == 1
    assert result["router2"].result == ["hostname router2", "ntp server 1.1.1.1"]
    assert result["router2"].failed is False
    assert result["router2"].changed is False
