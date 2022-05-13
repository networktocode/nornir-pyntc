"""Test save."""

from nornir_pyntc.tasks import pyntc_save
from pyntc.devices import IOSDevice, NXOSDevice


def test_pyntc_save_nxos(nr, monkeypatch):
    def mock_save(cls):  # pylint:disable=unused-argument
        return True

    monkeypatch.setattr(NXOSDevice, "save", mock_save)
    device = nr.filter(name="router1")
    result = device.run(pyntc_save)
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_save_ios(nr, monkeypatch):
    def mock_save(cls):  # pylint:disable=unused-argument
        return False

    monkeypatch.setattr(IOSDevice, "save", mock_save)
    device = nr.filter(name="router2")
    result = device.run(pyntc_save)
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False
