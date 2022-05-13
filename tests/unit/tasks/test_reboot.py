"""Test reboot."""

from nornir_pyntc.tasks import pyntc_reboot


def test_pyntc_reboot_nxos(nornir, monkeypatch):
    from pyntc.devices import NXOSDevice

    def mock_reboot(cls, timer):
        return True

    monkeypatch.setattr(NXOSDevice, "reboot", mock_reboot)
    device = nornir.filter(name="router1")
    result = device.run(pyntc_reboot)
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_reboot_ios(nornir, monkeypatch):
    from pyntc.devices import IOSDevice

    def mock_reboot(cls, timer):
        return False

    monkeypatch.setattr(IOSDevice, "reboot", mock_reboot)
    device = nornir.filter(name="router2")
    result = device.run(pyntc_reboot)
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False
