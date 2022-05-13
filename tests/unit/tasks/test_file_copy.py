"""Test reboot."""

from nornir_pyntc.tasks import pyntc_file_copy


def test_pyntc_filecopy_nxos(nornir, monkeypatch):
    from pyntc.devices import NXOSDevice

    def mock_file_copy(cls, src):
        return True

    monkeypatch.setattr(NXOSDevice, "file_copy", mock_file_copy)
    device = nornir.filter(name="router1")
    result = device.run(pyntc_file_copy, src="source")
    assert len(result["router1"]) == 1
    assert result["router1"].result == True
    assert result["router1"].failed == False
    assert result["router1"].changed == False


def test_pyntc_filecopy_ios(nornir, monkeypatch):
    from pyntc.devices import IOSDevice

    def mock_file_copy(cls, src):
        return False

    monkeypatch.setattr(IOSDevice, "file_copy", mock_file_copy)
    device = nornir.filter(name="router2")
    result = device.run(pyntc_file_copy, src="source")
    assert len(result["router2"]) == 1
    assert result["router2"].result == False
    assert result["router2"].failed == False
    assert result["router2"].changed == False
