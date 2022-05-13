"""Test save."""

from nornir_pyntc.tasks import pyntc_save


def test_pyntc_save_nxos(nornir, monkeypatch):
    from pyntc.devices import NXOSDevice

    def mock_save(cls):
        return True

    monkeypatch.setattr(NXOSDevice, "save", mock_save)
    device = nornir.filter(name="router1")
    result = device.run(pyntc_save)
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_save_ios(nornir, monkeypatch):
    from pyntc.devices import IOSDevice

    def mock_save(cls):
        return False

    monkeypatch.setattr(IOSDevice, "save", mock_save)
    device = nornir.filter(name="router2")
    result = device.run(pyntc_save)
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False
