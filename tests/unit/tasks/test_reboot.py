"""Test reboot."""

from nornir_pyntc.tasks import pyntc_reboot
from pyntc.devices import IOSDevice, NXOSDevice


def test_pyntc_reboot_nxos(nr, monkeypatch):
    def mock_reboot(cls, timer):  # pylint:disable=unused-argument
        return True

    monkeypatch.setattr(NXOSDevice, "reboot", mock_reboot)
    device = nr.filter(name="router1")
    result = device.run(pyntc_reboot)
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_reboot_ios(nr, monkeypatch):
    def mock_reboot(cls, timer):  # pylint:disable=unused-argument
        return False

    monkeypatch.setattr(IOSDevice, "reboot", mock_reboot)
    device = nr.filter(name="router2")
    result = device.run(pyntc_reboot)
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False
